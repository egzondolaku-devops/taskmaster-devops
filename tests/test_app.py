import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

def test_get_tasks():
    with app.test_client() as client:
        response = client.get('/tasks')
        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data, list)

def test_post_task():
    with app.test_client() as client:
        new_task = {
            "title": "Test Task",
            "description": "This is a test task"
        }
        response = client.post('/tasks', json=new_task)
        assert response.status_code == 201
        data = response.get_json()
        assert data['title'] == new_task['title']
        assert data['description'] == new_task['description']
        assert data['completed'] is False
        assert data['due_date'] == ""

def test_put_task():
    with app.test_client() as client:
        new_task = {
            "title": "Test update",
            "description": "This is a test update",
        }
        post_response = client.post('/tasks', json=new_task)
        task_id = post_response.get_json()['id']
        updated_task = {
            "title": "Updated Task",
            "description": "This task has been updated",
            "completed": True,
            "due_date": "2025-12-02"
        }
        put_response = client.put(f'/tasks/{task_id}', json=updated_task)
        assert put_response.status_code == 200
        data = put_response.get_json()
        assert data['title'] == updated_task['title']
        assert data['description'] == updated_task['description']
        assert data['completed'] is True
        assert data['due_date'] == updated_task['due_date']

def test_delete_task():
    with app.test_client() as client:
        new_task = {
            "title": "Task to be deleted",
            "description": "This task will be deleted"
        }
        post_response = client.post('/tasks', json=new_task)
        task_id = post_response.get_json()['id']
        delete_response = client.delete(f'/tasks/{task_id}')
        assert delete_response.status_code == 200
        data = delete_response.get_json()
        assert data['message'] == "Task deleted"