import json
import os

TODO_FILE = "tasks.json"


def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour To‑Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
        print()


def add_task(tasks, task):
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added.")


def remove_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        removed = tasks.pop(task_index)
        save_tasks(tasks)
        print(f"Task '{removed}' removed.")
    else:
        print("Invalid task number.")


def main():
    tasks = load_tasks()

    while True:
        print("\nCommands: list, add, remove, quit")
        command = input("Enter command: ").strip().lower()

        if command == "list":
            display_tasks(tasks)

        elif command == "add":
            task = input("Enter new task: ")
            add_task(tasks, task)

        elif command == "remove":
            display_tasks(tasks)
            try:
                index = int(input("Enter task number to remove: ")) - 1
                remove_task(tasks, index)
            except ValueError:
                print("Please enter a valid number.")

        elif command == "quit":
            print("Exiting To‑Do App.")
            break

        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()
