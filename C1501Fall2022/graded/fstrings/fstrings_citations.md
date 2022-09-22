# f-Strings and Citations

## Introduction
This is a **timed live exercise**. You have 50 minutes to complete the following exercise. You may work with a partner, but you are responsible for understanding and submitting your own work.

## Exercise
1. In the starter code provided, modify the `print` statement so that exactly two decimal places are displayed **with the decimal aligned** for any amount entered below $10,000. We have *not* covered this in class - this is an exercise on looking things up on your own! There are two rules:
   1. Use "f-Strings" (formatted string literals), not the older style Python formatting with `%` or `.format()`
   2. **Cite your source** by including a comment in your code with a link or links to the website(s) that helped you. If you worked with a partner, include their name as well.

    When working, your program should look something like the following:
    ```
    Enter the pre-tax total of your order: 9999
    Before tax: $ 9999.00
    Total:      $10498.95
    ```
    ```
    Enter the pre-tax total of your order: 50
    Before tax: $    50.00
    Total:      $    52.50
    ```

2. In 1-2 sentences and **in your own words**, describe what the curly brackets `{}` in an f-String are used for. If you worked with a partner, make sure that your description is not identical to theirs.

>**Bonus:** Dollar amounts are often printed with a comma between thousands, e.g. "$10,498.95". **Research, implement, and cite** a solution that prints commas.

## Grading

| Letter Grade | Description                                                                 |
| ------------ | --------------------------------------------------------------------------- |
| F            | Nothing submitted, or plagiarism                                            |
| D            | A bare minimum attempt                                                      |
| C            | Two or more errors                                                          |
| B            | An attempt at all components with 2 or more small errors or one large error |
| A            | All components completed with one small error                               |
| A+           | All components completed with no errors                                     |


Examples of **small errors**:
- Poorly written short answer description
- Incomplete short answer description
- Cited source does not match solution

Examples of **large errors**
- Syntax or runtime error
- Use of `.format` or `%` syntax
- Incorrect short answer description
- Incorrect solution