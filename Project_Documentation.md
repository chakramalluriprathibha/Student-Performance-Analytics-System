# Project Documentation

## 1. Project Title
**Student Performance Analytics System**

## 2. Student Details
- Student Name: C.M. Prathibha
- Project Area: Python with AI
- Tools: Python, NumPy, Pandas, CSV

## 3. Objective
Create a simple program to analyse student academic performance and attendance. It calculates totals and averages, assigns grades and pass/fail results, identifies the highest and lowest averages, calculates the class average, compares subjects, and displays the top three students.

## 4. Technologies Used
- **Python:** functions, loops, conditions, and program flow.
- **NumPy:** totals, means, minimums, and maximums.
- **Pandas:** reading CSV data, organising records in a DataFrame, filtering, sorting, and displaying tables.
- **CSV:** storing the student dataset.

## 5. Dataset Description
The dataset contains 20 student records. Each record includes Student ID, Name, Department, marks in Python, Mathematics, Physics, English, and Data Structures, plus attendance percentage. Marks and attendance are on a 0–100 scale.

## 6. Implementation
1. Load `students.csv` into a Pandas DataFrame.
2. Check required columns and validate numeric marks and attendance.
3. Use NumPy to calculate each student's total and average.
4. Use conditions to determine pass/fail and grade.
5. Use loops to analyse subjects and list failed or low-attendance students.
6. Calculate overall class statistics using NumPy.
7. Sort students by average to display the top three performers.

## 7. Grading and Result Rules
A student passes only if every subject mark is at least 40. If any subject mark is below 40, the student fails and receives grade F. For passing students, grades are assigned by average: A+ for 90 and above, A for 80–89.99, B for 70–79.99, C for 60–69.99, and D below 60.

## 8. Key Features
- Displays dataset overview and departments.
- Calculates total marks and average marks.
- Assigns grades and pass/fail results.
- Displays highest average, lowest average, class average, pass count, fail count, and pass percentage.
- Shows failed students.
- Analyses subject-wise average, highest, and lowest marks.
- Identifies the best-performing subject.
- Displays the top three students.
- Analyses average attendance and lists students with attendance below 75%.
- Checks required columns, missing values, and out-of-range marks/attendance.

## 9. Output
The program prints the dataset overview, student result table, overall performance analysis, subject-wise analysis, top three students, and attendance analysis in the terminal. A sample run is included in `sample_output.txt`.

## 10. Final Outcome
The project demonstrates how Python, NumPy, and Pandas can work together to analyse a student dataset and produce a readable performance report.

## 11. Challenges and Learning
This project provides practice in reading CSV data, using DataFrames, performing numerical calculations, writing reusable functions, using loops and conditions, validating data, sorting records, and interpreting results.

## 12. GitHub Repository Link
Add your own GitHub repository URL here after creating the repository and uploading the project files.


## Screenshots
After running `main.py`, save screenshots of the student results and analysis output in a folder named `screenshots` in this project. Add the screenshots folder to your GitHub repository.
