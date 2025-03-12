import json
import os
import pytest
from task import ( add_task, update_task, delete_task, change_status, load_task, save_task, get_task, get_task_by_status, 
get_task_by_description, get_task_by_id, get_task_by_created_at, get_task_by_updated_at, list_tasks)

# Test data
test_task_data = {
    'description': 'Test task',
    'status': 'todo'
}

@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Setup: Initialize the task file with an empty list
    print("Setting up test environment")
    if os.path.exists('task.json'):
        os.remove('task.json')
    save_task([])
    yield
    # Teardown: Clean up after tests
    print("Tearing down test environment")
    if os.path.exists('task.json'):
        os.remove('task.json')

# Test functions

def test_add_task():
    tasks = load_task()
    initial_task_count = len(tasks)
    new_task = add_task({'description': 'Test task'})
    tasks = load_task()
    assert len(tasks) == initial_task_count + 1
    assert tasks[-1]['description'] == 'Test task'
    assert tasks[-1]['status'] == 'todo'


def test_update_task(description=None, task_id=None):
    tasks = load_task()
    add_task(test_task_data)
    print("Loaded tasks:", tasks)
    if tasks:
        task_id = tasks[0]['id']
        update_task('Updated task', task_id)
        tasks = load_task()
        assert tasks[0]['description'] == 'Updated task'

def test_update_task_invalid():
    result = update_task('Non-existent task', 9999)
    assert result is None

def test_delete_task():
    add_task(test_task_data)
    tasks = load_task()
    if tasks:
        task_id = tasks[0]['id']
        delete_task(task_id)
        tasks = load_task()
        assert not any(task['id'] == task_id for task in tasks)

def test_delete_task_invalid():
    result = delete_task(9999)
    assert result is None

def test_change_status():
    tasks = load_task()
    print("Loaded tasks:", tasks)
    if tasks:
        task_id = tasks[0]['id']
        change_status('done', task_id)
        tasks = load_task()
        print("Tasks after changing status:", tasks)
        assert tasks[0]['status'] == 'done'

def test_change_status_invalid():
    result = change_status('done', 9999)
    assert result is None

def test_get_task():
    add_task({'description': 'Task to get'})
    tasks = load_task()
    task_id = tasks[0]['id']
    retrieved_task = get_task(task_id)
    assert retrieved_task['id'] == task_id

def test_get_task_invalid():
    result = get_task(9999)
    assert result is None

def test_get_task_by_status():
    add_task({'description': 'Task 1', 'status': 'todo'})
    add_task({'description': 'Task 2', 'status': 'done'})
    result = get_task_by_status('todo')
    print("Tasks with status 'todo':", result)
    assert len(result) == 1
    assert result[0]['status'] == 'todo'

def test_get_task_by_description():
    add_task({'description': 'Unique Description'})
    result = get_task_by_description('Unique Description')
    assert len(result) == 1
    assert result[0]['description'] == 'Unique Description'

def test_get_task_by_id():
    new_task = add_task({'description': 'Find me'})
    result = get_task_by_id(new_task['id'])
    assert result is not None
    assert result['id'] == new_task['id']

def test_get_task_by_created_at():
    new_task = add_task({'description': 'Created Today'})
    created_at = new_task['created_at'].split()[0]  # Extract date part
    result = get_task_by_created_at(created_at)
    assert len(result) > 0

def test_get_task_by_updated_at():
    new_task = add_task({'description': 'Updated Today'})
    task_id = new_task['id']
    update_task('Updated Description', task_id)
    updated_at = load_task()[0]['updated_at'].split()[0]  # Extract date part
    result = get_task_by_updated_at(updated_at)
    assert len(result) > 0

def test_list_tasks():
    add_task({'description': 'List this task'})
    result = list_tasks()
    assert len(result) > 0
def test_load_task():
    print("Running test_load_task")
    tasks = load_task()
    print("Loaded tasks:", tasks)
    assert isinstance(tasks, list)
    for task in tasks:
        assert 'id' in task
        assert 'description' in task
        assert 'status' in task
        assert 'created_at' in task
        assert 'updated_at' in task
    print("Completed test_load_task")

def test_save_task():
    print("Running test_save_task")
    tasks = load_task()
    print("Loaded tasks:", tasks)
    save_task(tasks)
    with open('task.json', 'r') as f:
        saved_tasks = json.load(f)
    print("Saved tasks:", saved_tasks)
    assert tasks == saved_tasks
    print("Completed test_save_task")