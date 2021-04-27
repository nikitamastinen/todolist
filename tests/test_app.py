# pylint: disable=redefined-outer-name
from copy import copy
import pytest
from todo_list.app import app, todo_list
from todo_list.server.todo_list import Task


@pytest.fixture
def client():
    return app.test_client()


def test_wrong_error_codes(client):
    response = client.get('/cat')
    assert response.status_code == 404


def test_correct_error_codes(client):
    response = client.get('/')
    assert response.status_code == 200


def test_adding_new_task(client):
    client.post('/', data={'new_task_name': 'kokoko'})
    assert todo_list.tasks == [Task('incompleted', 'kokoko')]


def test_adding_wrong_data(client):
    copied = copy(todo_list.tasks)
    client.post('/', data={'new_task': 'kokoko'})
    assert todo_list.tasks == copied


def test_completed_tasks(client):
    client.post('/', data={'new_task_name': 'dsas'})
    client.post('/', data={'new_task_name': 'kokoko2'})
    client.post('/', data={'new_task_name': 'kokoko3'})
    client.post('/', data={'index': '0'})
    client.post('/', data={'index': '1'})
    counter = 0
    for i in todo_list.tasks:
        counter += int(i.status == 'completed')
    assert counter == 2


def test_showing_completed_tasks(client):
    client.post('/', data={'status': 'completed'})
    assert todo_list.status == 'completed'
    client.post('/', data={'status': 'incompleted'})
    assert todo_list.status == 'incompleted'
    client.post('/', data={'status': 'all'})
    assert todo_list.status == 'all'
