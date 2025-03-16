# Task Tracker Project

## Overview

The Task Tracker Project is a simple yet effective task management application that allows users to:

- Add tasks
- Update task descriptions
- Delete tasks
- Change task statuses
- List tasks and filter them based on various criteria

The application is designed for easy management of daily tasks and ensures that task details are saved persistently in a JSON file.

## Features

✅ **Add Task**: Add new tasks with descriptions and given status or default status as 'todo'.

✅ **Update Task**: Modify the description of an existing task.

✅ **Delete Task**: Remove a task by its ID.
 
✅ **Change Task Status**: Update the status of a task (e.g., 'todo', 'in progress', 'done').

✅ **List Tasks**: Display all tasks with their details.

✅ **Filter Tasks**: Filter tasks by status, description, or timestamps.

## Installation

**Step 1**: Clone the repository

```sh
git clone <repository_link>
cd task-tracker
```

**Step 2**: Install dependencies

```sh
pip install -r requirements.txt
```

**Step 3**: Run the application

```sh
python task.py
```

## Usage

### Add a Task

Upon running the application, you will see the following menu:

```
Task Manager
1. Add Task
2. Update Task
3. Delete Task
4. Change Task Status
5. List Tasks
6. Get Task by ID
7. Get Tasks by Status
8. Get Tasks by Description
9. Get Tasks by Created At
10. Get Tasks by Updated At
11. Exit
```

Simply follow the prompts to perform the desired actions.

## Testing

To run the test cases, make sure you have pytest installed. If not, you can install it by running:

```sh
pip install pytest
```
Then, run the following command to execute the test cases:

```sh
pytest test_task.py
```

## File Structure

├── task.py            # Main application file  
├── test_task.py       # Test cases for the application  
├── task.json          # JSON file storing task data  
├── requirements.txt   # Project dependencies  
├── README.md          # Project documentation

## Requirements

Python 3.8+

Pytest (for testing) 

Reference : https://roadmap.sh/projects/task-tracker 
