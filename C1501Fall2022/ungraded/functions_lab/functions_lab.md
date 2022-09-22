# Functions

## Part 1: Tracing and debugging
You and a friend are developing a journalling app to keep track of your hiking adventures. Your friend started writing the code, so you decide to read what they've got so far to make sure you understand how it works.

1. Open the file named `hiking_journal.py`
2. Trace the code **manually** and write down your predicted output.
3. Run the code. Did it produce what you expected?
4. Try changing the function call to `journal_entry(10.5, "July 12, 2022", "I saw a beautiful lake.")`. What happens?
5. Add an indentation (4 spaces, or tab) before the `main()` statement in the last line of the script. What happens? 
6. Undo your changes so that the file is back to the original.
7. **Without modifying the `journal_entry` function**, change the code so that the journal entry is printed to the screen.

## Part 2: Writing functions
In this exercise, you will use Python's random number generator to implement a simple dice game. The score for each player is calculated by rolling two dice and adding them together, then either adding, subtracting, or ignoring the length of their name. 

1. Open the file `lab04py`. At the very top, you'll see this line:
   
   ```python
   from random import randint
   ```
   This makes the `randint` function available to use in this script.
2. The script contains three **function declarations**:
   - `roll_dice`: uses `randint` to virtually roll two dice and add them together. This function is complete, you don't need to make any changes to it.
   - `play_game`: a void function that takes one **argument**, `name` (a string). This is where you will be implementing the game logic.
   - `main`: a void function that serves as the entry point into the program. This is where you will prompt the user for input and call the `play_game` function.
3. In `main`, replace the `pass` keyword with the following logic:
   
   ```plaintext
   1. Prompt the user to enter the name of player 1
   2. Prompt the user to enter the name of player 2
   3. Pass the name of player 1 to play_game
   4. Pass the name of player 2 to play_game
   ```
   Your input prompts should be formatted so that there is a space between the prompt and the text entered by the user.

4. In `play_game`, implement the game logic as follows:

   ```python
   score = roll_dice() + weight * len(name)
   ```
   where is a random integer equalling -1, 0, or 1.
   > Hint: check out the [Python docs](https://docs.python.org/3/library/random.html#random.randint) for how to use the `randint` function!

5. Finally, print out each player's name and their score as an integer. You may choose to put your print statements in `main`, `play_game`, or a new function, whatever makes the most sense to you.

Your game should look something like the following when run:

<pre class="sample">
Enter the name of player 1: <span style="color: green;">Cali</span>
Enter the name of player 2: <span style="color: green;">Salvador</span>
Cali scores 6!
Salvador scores 11!</pre>

Feel free to get creative with the wording and output formatting, as long as the score is displayed as an integer. You could even add some Unicode symbols for fun, such as:

<pre class="sample">
🎉 Cali scores 6!
🎉 Salvador scores 11!</pre>

### Extra challenge
In tutorial 03, you designed functions to calculate the annual rate of inflation and the area of a triangle. For an extra challenge, try implementing and calling these functions in Python code.