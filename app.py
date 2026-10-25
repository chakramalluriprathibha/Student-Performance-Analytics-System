
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Student Performance Analytics", layout="wide")

st.title("Student Performance Analytics System")
st.write("Analyze student marks, grades, results, and attendance.")

subjects = ["Python", "Mathematics", "Physics", "English", "Data_Structures"]

@st.cache_data
def load_students():
    return pd.read_csv("students.csv")

try:
    data = load_students()
except FileNotFoundError:
    st.error("students.csv was not found. Please add it to the project repository.")
    st.stop()

required = ["Student_ID", "Name", "Department", "Attendance"] + subjects
missing = [col for col in required if col not in data.columns]

if missing:
    st.error("Missing required columns: " + ", ".join(missing))
    st.stop()

for col in subjects + ["Attendance"]:
    data[col] = pd.to_numeric(data[col], errors="coerce")

if data[subjects + ["Attendance"]].isnull().any().any():
    st.error("The dataset contains missing or non-numeric marks or attendance.")
    st.stop()

if ((data[subjects] < 0) | (data[subjects] > 100)).any().any():
    st.error("Subject marks must be between 0 and 100.")
    st.stop()

if ((data["Attendance"] < 0) | (data["Attendance"] > 100)).any().any():
    st.error("Attendance must be between 0 and 100.")
    st.stop()

data["Total"] = data[subjects].sum(axis=1)
data["Average"] = data[subjects].mean(axis=1).round(2)

data["Result"] = np.where((data[subjects] >= 40).all(axis=1), "Pass", "Fail")

def get_grade(row):
    if row["Result"] == "Fail":
        return "F"
    if row["Average"] >= 90:
        return "A+"
    if row["Average"] >= 80:
        return "A"
    if row["Average"] >= 70:
        return "B"
    if row["Average"] >= 60:
        return "C"
    return "D"

data["Grade"] = data.apply(get_grade, axis=1)

passed = int((data["Result"] == "Pass").sum())
failed = int((data["Result"] == "Fail").sum())

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Students", len(data))
c2.metric("Class Average", round(data["Average"].mean(), 2))
c3.metric("Students Passed", passed)
c4.metric("Students Failed", failed)

st.subheader("Student Results")
st.dataframe(
    data[["Student_ID", "Name", "Department"] + subjects +
         ["Total", "Average", "Grade", "Result", "Attendance"]],
    use_container_width=True,
    hide_index=True
)

st.subheader("Subject-wise Analysis")
subject_summary = pd.DataFrame({
    "Subject": subjects,
    "Average": [round(data[s].mean(), 2) for s in subjects],
    "Highest": [data[s].max() for s in subjects],
    "Lowest": [data[s].min() for s in subjects]
})
st.dataframe(subject_summary, use_container_width=True, hide_index=True)

best_subject = subject_summary.loc[subject_summary["Average"].idxmax(), "Subject"]
st.success(f"Best-performing subject: {best_subject}")

st.subheader("Top Three Students")
st.dataframe(
    data.sort_values("Average", ascending=False).head(3)[
        ["Name", "Department", "Total", "Average", "Grade"]
    ],
    use_container_width=True,
    hide_index=True
)

st.subheader("Attendance Analysis")
st.metric("Average Attendance", f"{data['Attendance'].mean():.2f}%")
st.dataframe(
    data.loc[data["Attendance"] < 75, ["Name", "Department", "Attendance"]],
    use_container_width=True,
    hide_index=True
)