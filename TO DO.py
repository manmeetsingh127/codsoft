class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a new task to the list"""
        self.tasks.append(task)
        print(f"Task '{task}' added!")

    def view_tasks(self):
        """Display all tasks in the list"""
        print("Your To-Do List:")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def delete_task(self, task_number):
        """Delete a task from the list"""
        try:
            task_number = int(task_number)
            if task_number > 0:
                task = self.tasks.pop(task_number - 1)
                print(f"Task '{task}' deleted!")
            else:
                print("Invalid task number!")
        except (ValueError, IndexError):
            print("Invalid task number!")

    def mark_task_done(self, task_number):
        """Mark a task as done"""
        try:
            task_number = int(task_number)
            if task_number > 0:
                task = self.tasks[task_number - 1]
                self.tasks[task_number - 1] = f"[DONE] {task}"
                print(f"Task '{task}' marked as done!")
            else:
                print("Invalid task number!")
        except (ValueError, IndexError):
            print("Invalid task number!")


def main():
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Mark task done")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter a new task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_number = input("Enter the task number to delete: ")
            todo_list.delete_task(task_number)
        elif choice == "4":
            task_number = input("Enter the task number to mark as done: ")
            todo_list.mark_task_done(task_number)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()