# Import required libraries
import os
import numpy as np
import pandas as pd

# List the subjects
SUBJECTS = ["Python", "Mathematics", "Physics", "English", "Data_Structures"]
PASS_MARK = 40

# Read the student data
def load_data(file_name):
    return pd.read_csv(file_name)

# Calculate total and average marks
def calculate_total_and_average(data):
    marks = data[SUBJECTS].to_numpy()
    data["Total"] = np.sum(marks, axis=1)
    data["Average"] = np.round(np.mean(marks, axis=1), 2)
    return data

# Check pass or fail
def get_result(marks):
    if np.min(marks) >= PASS_MARK:
        return "Pass"
    return "Fail"


# Assign grades to students
def get_grade(average, result):
    if result == "Fail":
        return "F"
    if average >= 90:
        return "A+"
    if average >= 80:
        return "A"
    if average >= 70:
        return "B"
    if average >= 60:
        return "C"
    return "D"

# Add grades and results
def assign_grades_and_results(data):
    results = []
    grades = []
    for i in range(len(data)):
        marks = data.iloc[i][SUBJECTS].to_numpy()
        result = get_result(marks)
        grade = get_grade(data.iloc[i]["Average"], result)
        results.append(result)
        grades.append(grade)
    data["Result"] = results
    data["Grade"] = grades
    return data

# Analyze each subject
def subject_analysis(data):
    rows = []
    for subject in SUBJECTS:
        marks = data[subject].to_numpy()
        rows.append({
            "Subject": subject,
            "Average": round(float(np.mean(marks)), 2),
            "Highest": int(np.max(marks)),
            "Lowest": int(np.min(marks))
        })
    return pd.DataFrame(rows)

# Find the top 3 students
def get_top_students(data):
    return data.sort_values(by="Average", ascending=False).head(3)

# Run the analysis
def main():
    folder = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(folder, "students.csv")

    # Load the dataset
    try:
        data = load_data(file_name)
    except FileNotFoundError:
        print("Could not find students.csv. Keep it in the same folder as main.py.")
        return
    except pd.errors.EmptyDataError:
        print("The dataset file is empty.")
        return

    # Check required columns
    required_columns = [
        "Student_ID", "Name", "Department", "Python", "Mathematics",
        "Physics", "English", "Data_Structures", "Attendance"
    ]
    for column in required_columns:
        if column not in data.columns:
            print("Missing column:", column)
            return
    if data.empty:
        print("The dataset is empty.")
        return

    # Check marks and attendance
    numeric_columns = SUBJECTS + ["Attendance"]
    for column in numeric_columns:
        data[column] = pd.to_numeric(data[column], errors="coerce")
    if data[numeric_columns].isnull().any().any():
        print("Please check the dataset for missing or non-numeric marks/attendance.")
        return
    if ((data[SUBJECTS] < 0) | (data[SUBJECTS] > 100)).any().any():
        print("Subject marks must be between 0 and 100.")
        return
    if ((data["Attendance"] < 0) | (data["Attendance"] > 100)).any():
        print("Attendance must be between 0 and 100.")
        return

    print("=" * 65)
    print("STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 65)
    print("\n1.DATASET OVERVIEW")
    print("Number of students:", len(data))
    print("Number of subjects:", len(SUBJECTS))
    print("Departments:", ", ".join(sorted(data["Department"].astype(str).unique())))
    print("\nDataset information:")
    data.info()

    # Calculate marks and assign grades
    data = calculate_total_and_average(data)
    data = assign_grades_and_results(data)
    print("\n2.STUDENT PERFORMANCE RESULTS")
    # Display student results
    result_columns = ["Student_ID", "Name", "Department"] + SUBJECTS + ["Total", "Average", "Grade", "Result", "Attendance"]
    print(data[result_columns].to_string(index=False))

    # Show overall performance
    average_values = data["Average"].to_numpy()
    best_index = int(np.argmax(average_values))
    worst_index = int(np.argmin(average_values))
    passed = int(np.sum(data["Result"] == "Pass"))
    failed = int(np.sum(data["Result"] == "Fail"))
    pass_percentage = round((passed / len(data)) * 100, 2)
    print("\n3. OVERALL PERFORMANCE ANALYSIS")
    print("Highest average:", data.iloc[best_index]["Name"], "-", data.iloc[best_index]["Average"])
    print("Lowest average:", data.iloc[worst_index]["Name"], "-", data.iloc[worst_index]["Average"])
    print("Class average:", round(float(np.mean(average_values)), 2))
    print("Students passed:", passed)
    print("Students failed:", failed)
    print("Pass percentage:", pass_percentage, "%")

    print("\nStudents who failed:")
    failed_students = data[data["Result"] == "Fail"]
    if failed_students.empty:
        print("No students failed.")
    else:
        for _, student in failed_students.iterrows():
            print("-", student["Name"])

    print("\n4.SUBJECT-WISE PERFORMANCE ANALYSIS")
    # Show subject-wise performance
    subject_table = subject_analysis(data)
    print(subject_table.to_string(index=False))
    best_subject_index = int(np.argmax(subject_table["Average"].to_numpy()))
    print("Best-performing subject:", subject_table.iloc[best_subject_index]["Subject"])

    # Display top 3 students
    print("\n5.TOP PERFORMING STUDENTS")
    for rank, (_, student) in enumerate(get_top_students(data).iterrows(), start=1):
        print(f"Rank {rank}: {student['Name']} | Department: {student['Department']} | Total: {student['Total']} | Average: {student['Average']} | Grade: {student['Grade']}")

    # Analyze student attendance
    print("\n6.ATTENDANCE ANALYSIS")
    print("Average attendance:", round(float(data["Attendance"].mean()), 2), "%")
    low_attendance = data[data["Attendance"] < 75]
    print("Students with attendance below 75%:")
    if low_attendance.empty:
        print("No students have attendance below 75%.")
    else:
        for _, student in low_attendance.iterrows():
            print("-", student["Name"], "-", student["Attendance"], "%")

    print("\n" + "=" * 65)
    print("ANALYSIS COMPLETED SUCCESSFULLY")
    print("=" * 65)

if __name__ == "__main__":
    main()