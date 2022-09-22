# Indexing and Lists
<!-- Combination of Java 1501, 1631, and some new stuff -->

## Introduction
This tutorial is intended to familiarize you with the `list` datatype and methods. In small groups, working on the whiteboard, work through the following exercises. You can check your answers using the Python interpreter, but try to solve them by hand first.

## List methods, functions, and operators
You may find the following methods or functions useful. For a given list `a_list`:

| Method or function                            | Description                                          |
| --------------------------------------------- | ---------------------------------------------------- |
| `a_list = [element0, element1, ... elementN]` | Initializes the list with any number of elements     |
| `a_list.append(element)`                      | Adds the element to the end of the list              |
| `len(a_list)`                                 | Returns the length of the list                       |
| `a_list.insert(i, element)`                   | Inserts the element between position `i` and `i + 1` |
| `del a_list[i]`                               | Removes the element at position `i`                  |
| `a_list.remove(element)`                      | Removes the first instance of `element`              |

Additionally, there are the following list operators:

| Operator            | Description                                                           |
| ------------------- | --------------------------------------------------------------------- |
| `a_list[i]`         | Accesses the element at position `i` (read or write, but must exist!) |
| `a_list == b_list`  | Evaluates to `True` if both lists contain the exact same elements     |
| `a_list + b_list`   | Concatenates the two lists together                                   |
| `a_list * N`        | Evaluates to a new list with `a_list` elements repeated `N` times     |
| `element in a_list` | Returns `True` if `element` is in the list                            |

## Exercises
1. Design and implement a Python function named `get_courses` that returns a **list of strings** containing student courses. Your function should behave as follows:
   <pre>
   Enter the name of a course to add, or press Enter to finish: <span style="color: green">COMP 1501</span>
   Enter the name of a course to add, or press Enter to finish: <span style="color: green">MATH 1505</span>
   Enter the name of a course to add, or press Enter to finish:
   2 courses added
   </pre>

   > Hints: 
   > - You may use a **loop** or **recursion** to prompt the user, but make sure to think about your exit condition.
   > - The number of courses added will not always be 2 - this should be calculated.

2. Someone has written the following function to remove all courses with a given prefix. However, there's a bug in it. Try to answer the following questions by hand.
    ```python
    def remove_all(courses: list, prefix: str) -> None:
        """Removes all courses matching prefix from the courses list"""
        for i in range(len(courses)):
            if prefix in courses[i]:
                del courses[i]
    ```
    1. Trace the code with the following function calls:
        ```python
        courses = ["COMP 1501", "GNED 1103", "GNED 1401", "MATH 1505"]
        remove_all(courses, "GEOL")
        remove_all(courses, "MATH")
        remove_all(courses, "GNED")
        ```
    2. Does an error occur every time you call the function? If not, under what circumstances does the error occur?
    3. What *kind* of error occurs? The general error types are syntax, runtime, and logic.
    4. How would you approach fixing this function?
    5. What additional test values should you consider to fully ensure the function is working as expected?

## Extra challenge
Assume you have two lists of quiz grades for a class of students, `quiz1` and `quiz2`. Both lists have an equal number of elements.

1. Write a Python function that takes the two lists as input parameters and returns a *third* list name `higher` containing the higher of the two quiz grades for each student.
2. Write another function that takes the `higher` list and returns the maximum grade of the class. Do not use the `max` function.
3. Modify the previous solution so that it returns the *index* position of the maximum grade.