# Student Performance Analytics System

**Student:** C.M.Prathibha  
**Project:** Python with AI — Student Performance Analytics System

## Objective
Analyse student marks and attendance using Python, NumPy, and Pandas. The program calculates totals, averages, grades, pass/fail results, class performance, subject-wise performance, and top performers.

## Technologies Used
- Python
- NumPy
- Pandas
- CSV dataset
- GitHub for version control and submission

## Project files
- `main.py` — Python source code
- `students_data.csv` — dataset containing 20 student records
- `sample_output.txt` — sample output from the program
- `Project_Documentation.md` — project report
- `requirements.txt` — required Python packages

## Dataset
The CSV contains Student ID, Name, Department, marks in Python, Mathematics, Physics, English, and Data Structures, and Attendance. Marks and attendance must be between 0 and 100.

## Grading rules
A student passes only when every subject mark is at least 40. A failed student receives grade `F`. For students who pass: A+ for average 90 or above; A for 80–89.99; B for 70–79.99; C for 60–69.99; D below 60.

## Setup and run
1. Install Python 3 from https://www.python.org/downloads/.
2. Open a terminal in this project folder.
3. Install packages:
   ```bash
   python -m pip install -r requirements.txt
   ```
4. Run the program:
   ```bash
   python main.py
   ```
5. To save fresh output:
   ```bash
   python main.py > sample_output.txt
   ```

If your system uses `python3` instead of `python`, use `python3` in the commands.

## GitHub submission
Create a GitHub repository, upload all project files, and add your repository link to the college Google Form. Follow the assignment PDF for the exact submission instructions.


## Screenshots
After running `main.py`, save screenshots of the student results and analysis output in a folder named `screenshots` in this project. Add the screenshots folder to your GitHub repository.
