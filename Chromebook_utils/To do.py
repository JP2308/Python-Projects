import os
import json

# File to store tasks
TASK_FILE = "tasks.json"

# Load tasks from the file if it exists, otherwise start with an empty list
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as file:
            return json.load(file)
    return []

# Save tasks to the file
def save_tasks():
    with open(TASK_FILE, 'w') as file:
        json.dump(to_do, file)

# Initialize the task list
to_do = load_tasks()

def main():
    while True:  # Loop to keep asking until the user exits
        question = input("Would you like to add, remove, view, revise, or quit? ").strip().lower()

        if question == "add":
            add_task()
        elif question == "remove":
            remove_task()
        elif question == "view":
            view_tasks()
        elif question == "revise":
            revise_task()
        elif question == "quit":
            print("Exiting...")
            save_tasks()  # Save tasks to the file before quitting
            break  # Stops the loop
        else:
            print("Invalid option. Please enter add, remove, view, or quit.")

# Adds a new task to the list.
def add_task():
    task = input("Enter the task: ")
    to_do.append(task)
    print(f"Added: {task}")

# Removes a task by its index.
def remove_task(): 
    view_tasks()  # Show the current tasks first
    try:
        index = int(input("Enter the number of the task to remove: ")) - 1
        removed_task = to_do.pop(index)
        print(f"Removed: {removed_task}")
    except (IndexError, ValueError):
        print("Invalid input. Please enter a valid task number.")

# Revise a task in the list
def revise_task():
    if not to_do:  # Check if the list is empty first
        print("Yay you aren't busy!")
        return  # Exit the function if the list is empty
    
    view_tasks()
    try:
        task = int(input("Which task needs to be revised? ")) - 1
        new_task = input("What is the revised task? ")
        to_do[task] = new_task  # Directly modify the task in the list
        print("Revision complete")
    except (IndexError, ValueError):
        print("Invalid input. Please enter a valid task number.")

# Displays tasks 
def view_tasks():
    if not to_do:
        print("Yay you aren't busy!")
    else:
        for i, task in enumerate(to_do, 1):
            print(f"{i}. {task}")

# Run the program
main()
