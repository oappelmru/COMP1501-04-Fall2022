---
title: Lab 11
topic: Searching and sorting
---

<!-- Note: this is adapted from W22, where all the labs were camping themed -->

## Introduction
This is a comprehensive lab that incorporates pretty much every topic for the term - great for studying for the final! In this lab, you will be efficiently packing a bag for a camping trip by **sorting** your gear from largest to smallest.

## Part 1: Define a `Gear` class
1. Define a new class named `Gear` in a file named `gear.py`.
2. Define a **parameterized constructor** that takes two input parameters and assigns them to instance variables, one for the gear **name** and one for the **volume**.
3. Define a method called `__str__` that **returns a string** describing the gear name and volume. You may use any (appropriate) language you like.
4. Test to make sure your `Gear` class works by instantiating and printing some gear in a **conditional execution block** (`if __name__ == "__main__"`).

## Part 2: Load your gear
1. Create a **new Python file** in the same folder as `gear.py` and import your `Gear` class.
2. The file `gear.csv` contains a list of items and their volume. In your new file, write a function to read the contents of `gear.csv` and return a list of `Gear` items.
3. In your `main` function, call the previous function and print out the list of `Gear` to make sure it is loading correctly.

## Part 3: Search through your gear to find the largest item
1. In the same file as part 2, define a new function that takes a `list` of `Gear` as a parameter. Give your function a reasonable name that makes it obvious . Your function should return the **index of** the largest `Gear` object in the list.
2. Design an algorithm to search through your list and find the index of the largest item. Hint: You will need a **loop** of some kind with a nested `if` statement.
3. Implement your search algorithm in your function, then test it by calling it from your `main` function. What test values should you use to ensure it's working properly?

## Part 4: Sort your gear
1. In the same file as part 2, define a new function that takes a `list` of `Gear` as a parameter. Give your function a reasonable name that makes it obvious it's for sorting.
2. Implement the **selection sort** algorithm. You may write additional helper functions if you wish.
    ```plaintext
    for each index position in the list:
        find the position of the largest gear in the list from the current index to the end
        swap the current index with the position of the largest
    ```
    > Hint: You already wrote a "find largest" function in part 3!
3. Test your sorting function by calling it from your `main` function, then print the list again to make sure it's sorted.
