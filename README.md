# Student Grade Calculator

A beginner-friendly Python CLI application that calculates students' total marks, average percentage, letter grades, and overall pass/fail results.

## Project Overview

Student Grade Calculator is a simple command-line application built with Python. It allows users to enter a student's name and marks for multiple subjects, then automatically calculates the total marks, average percentage, corresponding letter grade, and final result.

This project demonstrates fundamental Python programming concepts, input validation, exception handling, and automated testing.

## Features

- Accepts a student's name and multiple subjects
- Takes marks for individual subjects
- Validates marks within the range of 0–100
- Calculates total marks and average percentage
- Assigns letter grades from A+ to F
- Determines the overall pass/fail result
- Handles invalid numeric input
- Includes automated unit tests using `unittest`
- Runs directly in the terminal without external dependencies

## Technologies Used

- **Python** — Core programming language
- **unittest** — Automated testing framework
- **Git** — Version control
- **GitHub** — Source code hosting

## Requirements

- Python 3.10 or newer
- Git (optional, for cloning the repository)

No external Python packages are required.

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ahsanhabibabir04/student-grade-calculator.git
```

### 2. Navigate to the Project Directory

```bash
cd student-grade-calculator
```

### 3. Run the Application

```bash
python main.py
```

Follow the on-screen instructions to enter the student's name, subjects, and marks.

### 4. Run Automated Tests

```bash
python -m unittest -v
```

This command runs the available unit tests and displays their results in the terminal.

## Grading Scale

The application uses the following sample grading scale:

| Average Percentage | Letter Grade |
|:---:|:---:|
| 80–100% | A+ |
| 70–79.99% | A |
| 60–69.99% | A- |
| 50–59.99% | B |
| 40–49.99% | C |
| Below 40% | F |

### Pass/Fail Criteria

A student passes only if every subject mark is at least 40. If the student scores below 40 in any subject, the overall result is **Fail**.

**Note:** This is a sample grading scale for educational purposes and does not represent an official national grading policy.

## Project Structure

```text
student-grade-calculator/
├── main.py
├── test_main.py
├── README.md
└── .gitignore
```

## Learning Outcomes

Through this project, I practiced:

- Writing and organizing Python functions
- Using conditional statements and loops
- Handling user input and validating data
- Implementing exception handling
- Performing calculations and assigning grades
- Writing automated tests with Python's `unittest`
- Managing project files using Git and GitHub
- Documenting a software project with Markdown

## Future Improvements

Potential enhancements for future versions include:

- Saving student results to a file
- Generating detailed student report cards
- Supporting multiple students in a single session
- Adding a graphical user interface (GUI)
- Exporting results to CSV

## Author

**M.A. Ahsan Habib Abir**

Aspiring Computer Science and Artificial Intelligence student with an interest in Python programming, machine learning, and software development.

## Repository

GitHub: [Student Grade Calculator](https://github.com/ahsanhabibabir04/student-grade-calculator)

---

If you find this project useful, consider giving the repository a star.
