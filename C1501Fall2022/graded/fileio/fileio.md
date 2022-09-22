# File Input and Output

## Introduction
This is a **timed live exercise**. You have 50 minutes to complete **one of** the following exercises and **one of** the short answer questions. Your instructor will tell you which to complete for your section.

Each exercise deals with data contained in a specific file. All of these files are formatted with **one number per line**.

To save time during this exercise, you may assume:
- The file exists and can be loaded (no need to implement `try/except`)
- The file contains one number per line, with no empty lines 
- All numbers are the same datatype (`int` or `float` depending on the file)
- Filenames may be hard-coded

## Exercises
1. The file `speeds.txt` contains a list of vehicle speeds measured on a road with a speed limit of 80 km/hr. Write a Python script to read `speeds.txt` and display the **total number** of vehicles **exceeding the speed limit**.

2. The file `hikes.txt` contains a list of hike distances completed over the course of a year. Write a Python script to read `hikes.txt` and display the **average** hike distance.

3. The file `hikes.txt` contains a list of hike distances completed over the course of a year. Write a Python script to read `hikes.txt` and display the **maximum** hike distance.

4. The file `student-sections.txt` contains a list of section numbers for students registered in first year programming. Write a Python script to read `student-sections.txt` and display the **number of students in section 5**.

5. The file `grades.txt` contains a list of percentage grades for a course. Write a Python script to read `grades.txt` and display the **number of students** passing the class with a grade of 50 or above.

6. The file `grades.txt` contains a list of percentage points for a course. Write a Python script to read `grades.txt` and display the **highest grade** in the class.

## Short answer questions
1. One of your simplifying assumptions is to assume that there are no empty lines in the file. **In your own words** (not code), how would you handle the situation where there **are** empty lines in the file?

2. One of your simplifying assumptions is to assume that there is one number per line. **In your own words** (not code), how would you handle the situation where there are **multiple entries** per line (separated by spaces)?

3. One of your simplifying assumptions is to assume that each line is a **number** of the same type. **In your own words** (not code), how would you handle the situation where there are **mixed** data types of `float` and `int`?

## Grading

| Letter Grade | Description                                                                   |
| ------------ | ----------------------------------------------------------------------------- |
| F            | Nothing submitted, or plagiarism                                              |
| D            | A bare minimum attempt                                                        |
| C            | At least one large error and 2 or more small errors                           |
| B            | An attempt at all components with more than 2 small errors or one large error |
| A            | All components completed with one or two small errors                         |
| A+           | All components completed with no errors                                       |

Examples of **small errors**:
- Poor variable names
- Inappropriate use (or lack of) named constants
- Forgetting to close a file object
- Correct but poorly explained short answer response

Examples of **large errors**
- Syntax or runtime error
- Incorrect calculation
- Using a file reading method that was **not** presented in class
- Incorrect short answer response
- Solving or answering the wrong problem