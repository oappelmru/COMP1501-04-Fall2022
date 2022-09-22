# Recursion

## Instructions
The following exercises will give you practice writing recursive code. Some parts are marked "challenge" and are optional, though recommended to deepen your experience. Manage your time wisely: if you're stuck on the challenge portion of an exercise, move on and finish the required exercises first!

## Exercises
1. Imagine you are creating an online service, and are writing the code that handles creation of user accounts. 
You must write a Python function that prompts the user to choose a password. Your function must check that the password is at least 8 characters long; 
if it isn't, display an error message and re-prompt.
    
    The function should return the final password that meets the criteria. The output after calling your function should look something like this:

    >choose a password: *1234*<br />
    >password must be at least 8 characters<br />
    >choose a password: *Password1234*<br />
    >Password1234<br />
    
    **You must write two versions of your function:**
    
    **a) Iterative.** Use a loop to create the re-prompting behavior
    
    **b) Recursive.** Use recursion to create the re-prompting behavior
    
    <br />
    
2. The "factorial" of an integer is the product of that integer and all the integers less than it. It is denoted with an exclamation mark (!). So,

    n! = n * (n-1) * (n-2) * ... * 2 * 1
    
    Write a **recursive** function that computes the factorial of a given integer. It may help to note that factorial can be *defined* recursively, like this:
    
    n! = n * (n-1)!
    
    Remember to think carefully about what the base case(s) should be!

<br />

3. Iterative procedures can be converted to recursive ones, and vice versa.

    Take the recursive factorial function you wrote in part 2, and convert it to an iterative function. Are there values of *n* that can be handled by one approach but not the other? Can you guess why?
