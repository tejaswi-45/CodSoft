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
Invalid Input Handling:

If the user enters an invalid choice that doesn't match any key in the operations dictionary, an "Invalid input" message is displayed.
Function Call:

Finally, the calculator function is called to start the calculator program.
