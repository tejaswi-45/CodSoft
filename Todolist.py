class TodoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task, status="Pending"):
        self.tasks[task] = status

    def update_task_status(self, task, new_status):
        if task in self.tasks:
            self.tasks[task] = new_status
            print(f"Task '{task}' status updated to '{new_status}'.")
        else:
            print(f"Task '{task}' not found.")

    def view_tasks(self):
        if self.tasks:
            print("To-Do List:")
            for task, status in self.tasks.items():
                print(f"- {task} [{status}]")
        else:
            print("No tasks in the list.")

    def create_task(self):
        task = input("Enter task: ")
        self.add_task(task)
        print(f"Task '{task}' added.")

def main():
    todo_list = TodoList()

    while True:
        print("\n1. Add Task")
        print("2. Update Task Status")
        print("3. View Tasks")
        print("4. Create Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
            print(f"Task '{task}' added.")
        elif choice == "2":
            task = input("Enter task to update: ")
            new_status = input("Enter new status (Pending, In Progress, Completed): ")
            todo_list.update_task_status(task, new_status)
        elif choice == "3":
            todo_list.view_tasks()
        elif choice == "4":
            todo_list.create_task()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
