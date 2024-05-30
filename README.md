TASK 1

A To-Do List application is a useful project that helps users manage
and organize their tasks efficiently. This project aims to create a
command-line or GUI-based application using Python, allowing

users to create, update, and track their to-do lists


Procedure:
imports:
The script imports necessary modules:
os: To interact with the operating system for file operations.
datetime: To handle dates and times.

d_task(task, due_date, priority): Adds a new task to the to-do list. It takes three parameters: task (the description of the task), due_date (the deadline for the task), and priority (the priority level of the task).
list_tasks(status_filter=None): Lists all tasks in the to-do list. If status_filter is provided, it filters tasks based on the specified status.
update_status(taskad_number, new_status): Updates the status of a task in the to-do list. It takes two parameters: task_number (the index of the task to update) and new_status (the new status for the task).

Main Function (main()):
The main function runs a loop to repeatedly prompt the user for actions until they choose to exit.






It presents a menu of options to the user:
Add a Task
List Tasks
Update Task Status
Exit
Based on the user's choice, it calls the corresponding function.








TASK 2:

Design a simple calculator with basic arithmetic operations.
Prompt the user to input two numbers and an operation choice.

Perform the calculation and display the result.

Function Definitions:

The code begins by defining four functions: add, subtract, multiply, and divide. Each function takes two parameters x and y and performs the corresponding arithmetic operation.
Calculator Function:

The calculator function is defined. This function handles the main logic of the calculator.
Operations Dictionary:

Inside the calculator function, there's a dictionary named operations. This dictionary maps operation choices (keys) to the corresponding function (values). For example, the key '1' maps to the add function, '2' maps to subtract, and so on.
Menu Display:

The calculator displays a menu to the user, listing the available operations: addition, subtraction, multiplication, and division.
User Input:

The user is prompted to enter their choice of operation by selecting a number (1, 2, 3, or 4). They are also asked to input two numbers (num1 and num2) for the calculation.
Operation Execution:

The user's choice is used to access the corresponding function from the operations dictionary. If the choice is valid (exists in the dictionary), the selected function is called with num1 and num2 as arguments. The result of the calculation is stored in the variable result.
Error Handling for Division:

If the user chooses division and the second number (num2) is zero, it will result in division by zero, which is an error. In this case, an error message is displayed, and None is returned as the result.
Result Display:

If the calculation is successful (i.e., no division by zero error), the result is printed to the console.


TASK 3:
A password generator is a useful tool that generates strong and

random passwords for users. This project aims to create a
password generator application using Python, allowing users to

specify the length and complexity of the password.

User Input: Prompt the user to specify the desired length of the

password.

Generate Password: Use a combination of random characters to

generate a password of the specified length.

Display the Password: Print the generated password on the screen.



User Input:

The program prompts the user to specify the desired length of the password using input("Enter the desired length of the password: ").
It also prompts the user to specify the complexity level by inputting either '1' for low complexity, '2' for medium complexity, or '3' for high complexity.

Generate Password Function (generate_password):

This function takes the desired length of the password as an argument.
A variable chars is initialized as an empty string. This variable will hold the characters from which the password will be generated.
Based on the complexity level chosen by the user, different character sets are built.
If the complexity level is '1', the character set includes only lowercase letters, uppercase letters, and digits.
If the complexity level is '2', additional special characters like symbols are included in the character set.
If the complexity level is '3', the character set includes even more special characters.
If the user inputs any other value, the program defaults to medium complexity.
The function then generates a password of the specified length by randomly selecting characters from the character set and concatenating them together.
The generated password is returned.

Main Function (main):

This function serves as the entry point of the program.
It takes no arguments.
It prompts the user to input the desired length of the password.
It calls the generate_password function with the specified length.
It prints the generated password on the screen.
Execution (if __name__ == "__main__":):

This conditional statement ensures that the main function is only executed if the script is run directly, not if it is imported as a module into another script.
When the script is run, it starts the execution by calling the main function.
Invalid Input Handling:

If the user enters an invalid choice that doesn't match any key in the operations dictionary, an "Invalid input" message is displayed.
Function Call:

Finally, the calculator function is called to start the calculator program.




TASK 4:
Rock-Paper-Scissors Game

TASK 4

User Input: Prompt the user to choose rock, paper, or scissors.

Computer Selection: Generate a random choice (rock, paper, or scissors) for

the computer.

Game Logic: Determine the winner based on the user's choice and the

computer's choice.

Rock beats scissors, scissors beat paper, and paper beats rock.
Display Result: Show the user's choice and the computer's choice.

Display the result, whether the user wins, loses, or it's a tie.

Score Tracking (Optional): Keep track of the user's and computer's scores for

multiple rounds.

Play Again: Ask the user if they want to play another round.

User Interface: Design a user-friendly interface with clear instructions and

feedback.

Importing Required Module:
The line imports the random module, which is used to generate random choices for the computer.
Defining the determine_winner Function:
he function takes two arguments: user_choice and computer_choice, representing the choices of the user and computer, respectively.
It compares the choices to determine the winner based on the rules of the game (rock beats scissors, scissors beat paper, and paper beats rock).
If the choices are the same, it returns "It's a tie!". Otherwise, it returns whether the user or the computer wins.

Defining the main Function:

The function serves as the entry point of the program.
It initializes a list choices containing the available choices for the game: rock, paper, and scissors.
It sets up a while loop to allow the user to play the game multiple times until they choose to exit.

User Input and Game Logic:
The program prints a welcome message and prompts the user to choose between rock, paper, or scissors.
It displays the choices along with their corresponding numbers using a for loop and the enumerate function.
It then asks the user to input their choice and stores it as an index in user choice index.

Computer's Choice and Result Display:
If the user's choice is valid, it proceeds to determine the computer's choice using random.choice(choices).
It then displays both the user's and computer's choices and determines the winner using the determine winner function.

Play Again:
After each round, the program asks the user if they want to play again.
If the user responds with anything other than 'yes', the loop breaks, and the program exits with a farewell message.

Execution:
This conditional statement ensures that the main function is executed only if the script is run directly, not if it is imported as a module into another script.
When the script is run, it starts the execution by calling the main function.
