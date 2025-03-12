import datetime
import json
import os
import time
from datetime import datetime

task_file = 'task.json'

# Load task from file if it exists.
def load_task():
    if os.path.exists(task_file):
        with open(task_file, 'r') as f:
            try:
                data = json.load(f)
                if not isinstance(data, list):
                    return []
                return data
            except json.JSONDecodeError:
                return []
    return []


# Save task to file.
def save_task(tasks):
    with open(task_file, 'w') as f:
        json.dump(tasks, f, indent=4)

# Add a task.
def add_task(task):
    tasks = load_task()
    task['id'] = len(tasks) + 1
    task['description'] = task.get('description', 'No description')
    task['status'] = task.get('status', 'todo')
    
    current_time = time.time()
    formatted_time = datetime.fromtimestamp(current_time).strftime('%m/%d/%Y %H:%M:%S')
    
    task['created_at'] = formatted_time
    task['updated_at'] = formatted_time
    tasks.append(task)
    save_task(tasks)
    print(f"Task added: {task}")
    return task

# Update a task based on the task ID. User can update description, status
def update_task(description=None, task_id=None):
    tasks = load_task()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = description
            
            current_time = time.time()
            formatted_time = datetime.fromtimestamp(current_time).strftime('%m/%d/%Y %H:%M:%S')
            task['updated_at'] = formatted_time
            save_task(tasks)
            print(f"Task updated: {task}")
            return task
    print(f"Task with ID {task_id} not found.")
    return None

# Delete a task based on the task ID.
def delete_task(task_id):
    tasks = load_task()
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            save_task(tasks)
            print(f"Task with ID {task_id} deleted.")
            return task
    print(f"Task with ID {task_id} not found.")
    return None

def change_status(status=None, task_id=None):
    tasks = load_task()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status

            current_time = time.time()
            formatted_time = datetime.fromtimestamp(current_time).strftime('%m/%d/%Y %H:%M:%S')
            task['updated_at'] = formatted_time
            save_task(tasks)
            print(f"Task status changed: {task}")
            return task
    print(f"Task with ID {task_id} not found.")
    return None

def mark_in_progress(task_id=None):
    return change_status('in progress', task_id)

def mark_done(task_id=None):
    return change_status('done', task_id)

def mark_todo(task_id=None):
    return change_status('todo', task_id)

def list_tasks():
    tasks = load_task()
    if not tasks:
        print("No tasks found.")
        return []
    for task in tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")
    return tasks

def get_task(task_id=None):
    tasks = load_task()
    for task in tasks:
        if task['id'] == task_id:
            print(f"Task found: {task}")
            return task
    print(f"Task with ID {task_id} not found.")
    return None

def get_task_by_status(status=None):
    tasks = load_task()
    filtered_tasks = [task for task in tasks if task['status'] == status]
    if not filtered_tasks:
        print(f"No tasks found with status {status}.")
        return []
    for task in filtered_tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")
    return filtered_tasks

def get_task_by_description(description=None):
    tasks = load_task()
    filtered_tasks = [task for task in tasks if task['description'] == description]
    if not filtered_tasks:
        print(f"No tasks found with description {description}.")
        return []
    for task in filtered_tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")
    return filtered_tasks

def get_task_by_id(task_id=None):
    tasks = load_task()
    for task in tasks:
        if task['id'] == task_id:
            print(f"Task found: {task}")
            return task
    print(f"Task with ID {task_id} not found.")
    return None

def get_task_by_created_at(created_at=None):
    tasks = load_task()
    try:
        created_at_datetime = datetime.strptime(created_at, '%m/%d/%Y')
    except ValueError:
        print(f"Invalid date format. Please use MM/DD/YYYY format.")
        return []
    formatted_created_at = created_at_datetime.strftime('%m/%d/%Y')
    filtered_tasks = [task for task in tasks if task['created_at'][:10] == formatted_created_at]
    if not filtered_tasks:
        print(f"No tasks found with created_at {created_at}.")
        return []
    for task in filtered_tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")
    return filtered_tasks

def get_task_by_updated_at(updated_at=None):
    tasks = load_task()
    try:
        updated_at_datetime = datetime.strptime(updated_at, '%m/%d/%Y')
    except ValueError:
        print(f"Invalid date format. Please use MM/DD/YYYY format.")
        return []
    formatted_updated_at = updated_at_datetime.strftime('%m/%d/%Y')
    filtered_tasks = [task for task in tasks if task['updated_at'][:10] == formatted_updated_at]
    if not filtered_tasks:
        print(f"No tasks found with updated_at {updated_at}.")
        return []
    for task in filtered_tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")
    return filtered_tasks

def main():
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. Change Task Status")
        print("5. List Tasks")
        print("6. Get Task by ID")
        print("7. Get Tasks by Status")
        print("8. Get Tasks by Description")
        print("9. Get Tasks by Created At")
        print("10. Get Tasks by Updated At")
        print("11. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            description = input("Enter task description: ")
            status = input("Enter task status (todo, in progress, done): ")
            if not status:
                status = 'todo'
            task = {'description': description, 'status': status}
            add_task(task)
        elif choice == '2':
            while True:
                try:
                    task_id = int(input("Enter task ID to update: "))
                    break  # Exit loop if conversion is successful
                except ValueError:
                    print("Invalid input. Please enter a valid task ID (numeric value).")
            description = input("Enter new task description: ")
            update_task(description, task_id)
        elif choice == '3':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == '4':
            status = input("Enter new status (todo, in progress, done): ")
            task_id = int(input("Enter task ID to change status: "))
            change_status(status, task_id)
        elif choice == '5':
            list_tasks()
        elif choice == '6':
            task_id = int(input("Enter task ID to get: "))
            get_task(task_id)
        elif choice == '7':
            status = input("Enter status to filter tasks: ")
            get_task_by_status(status)
        elif choice == '8':
            description = input("Enter description to filter tasks: ")
            get_task_by_description(description)
        elif choice == '9':
            created_at = (input("Enter created_at timestamp to filter tasks: "))
            get_task_by_created_at(created_at)
        elif choice == '10':
            updated_at = (input("Enter updated_at timestamp to filter tasks: "))
            get_task_by_updated_at(updated_at)
        elif choice == '11':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()