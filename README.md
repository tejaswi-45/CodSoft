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
