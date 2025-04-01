import json
import os

TASK_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    return {"To Do": [], "In Progress": [], "Done": []}

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task):
    tasks = load_tasks()
    tasks["To Do"].append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added to To Do list.")

def view_tasks():
    tasks = load_tasks()
    for category, task_list in tasks.items():
        print(f"\n{category}:")
        for i, task in enumerate(task_list, 1):
            print(f"  {i}. {task}")

def update_task_status(task_name, new_status):
    tasks = load_tasks()
    for category in tasks:
        if task_name in tasks[category]:
            tasks[category].remove(task_name)
            tasks[new_status].append(task_name)
            save_tasks(tasks)
            print(f"Task '{task_name}' moved to {new_status}.")
            return
    print("Task not found.")

def delete_task(task_name):
    tasks = load_tasks()
    for category in tasks:
        if task_name in tasks[category]:
            tasks[category].remove(task_name)
            save_tasks(tasks)
            print(f"Task '{task_name}' deleted.")
            return
    print("Task not found.")

def main():
    while True:
        print("\nTask Tracker")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task Status")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task = input("Enter task to update: ")
            status = input("Enter new status (To Do, In Progress, Done): ")
            if status in ["To Do", "In Progress", "Done"]:
                update_task_status(task, status)
            else:
                print("Invalid status.")
        elif choice == "4":
            task = input("Enter task to delete: ")
            delete_task(task)
        elif choice == "5":
            print("Exiting Task Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
