# rps
rock paper scissor game .it is a ai based game build in python .
This code represents a simple implementation of the Rock, Paper, Scissors game in Python. 
It begins by creating a list, `t`, containing the possible plays: Rock, Paper, and Scissors. 
The computer's play is then randomly selected from this list. 
The code enters a game loop where the user is prompted to input their play choice. 
The program compares the user's choice with the computer's play, and the outcome is determined based on the game rules. 
If the user and computer play the same move, it results in a tie. 
Otherwise, the code checks various scenarios, such as Rock being covered by Paper or Paper being cut by Scissors. 
In case of an invalid play input, the program prompts the user to check their spelling. 
After each round, the player variable is reset to False, and the computer's play is randomized for the next round. 
The game loop continues until the user decides to exit. Overall, the code provides a basic interactive experience of the Rock, Paper, Scissors game with simple logic and input validation.
This code is a simple implementation of the classic Rock, Paper, Scissors game in Python. Let's break down the code step by step:

1. **List of Play Options:**
   ```python
   t = ["Rock", "Paper", "Scissor"]
   ```
   - Creates a list `t` containing the possible plays in the game: Rock, Paper, and Scissors.

2. **Computer's Random Play:**
   ```python
   computer = t[randint(0, 2)]
   ```
   - Uses the `randint` function from the `random` module to randomly select a play for the computer from the list `t`.

3. **Game Loop:**
   ```python
   player = False
   while player == False:
       # ...
   ```
   - Initiates a game loop where the user is prompted to input their play until a valid input is received.

4. **User Input:**
   ```python
   player = input("Rock, Paper, Scissor?:")
   ```
   - Takes user input for their play choice.

5. **Game Logic:**
   ```python
   if player == computer:
       print("Tie!")
   elif player == "Rock":
       # Check and print the outcome based on player's choice and computer's play
   elif player == "Paper":
       # Check and print the outcome based on player's choice and computer's play
   elif player == "Scissor":
       # Check and print the outcome based on player's choice and computer's play
   else:
       print("That's not a valid play. Check your spelling.")
   ```

   - Compares the user's play with the computer's play to determine the winner or declare a tie. It also checks for invalid inputs and prompts the user to check their spelling.

6. **Reset for the Next Round:**
   ```python
   player = False
   computer = t[randint(0, 2)]
   ```
   - Resets the `player` variable to `False` and randomly selects a new play for the computer to prepare for the next round of the game.

The code demonstrates a simple interactive Rock, Paper, Scissors game where the user plays against a computer with random play choices. The outcome of each round is displayed based on the game rules, and the game continues until the user decides to exit.
