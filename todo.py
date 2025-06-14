import os

FILE_NAME = "todo.txt"

# Load tasks from the file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []

# Save tasks to the file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("📝 No tasks found.")
    else:
        print("\n--- Your To-Do List ---")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Add a task
def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("✅ Task added.")
    else:
        print("⚠️ Empty task not added.")

# Remove a task
def remove_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter the number of the task to remove: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            save_tasks(tasks)
            print(f"❌ Task '{removed}' removed.")
        else:
            print("❗ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

# Main menu
def main():
    tasks = load_tasks()
    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("👋 Exiting... Stay productive!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
