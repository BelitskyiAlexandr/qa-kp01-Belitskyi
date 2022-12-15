import requests
import json
from flask import Flask, render_template, request, url_for, redirect

from main import app

flask_app = app


def test_main_page():
    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200


def test_binary_pages():
    with flask_app.test_client() as test_client:
        response = test_client.get('/binaryfile')
        assert response.status_code == 200
        response = test_client.get('/binaryfile_create')
        assert response.status_code == 200

        response = test_client.get('/binaryfile_read/<string:name>')
        assert response.status_code == 302
        response = test_client.get('/binaryfile_del/<string:name>')
        assert response.status_code == 302
        response = test_client.get('/binaryfile_move/<string:name>')
        assert response.status_code == 302

        response = test_client.get('/binaryfile_read')
        assert response.status_code == 404
        response = test_client.get('/binaryfile_del')
        assert response.status_code == 404
        response = test_client.get('/binaryfile_move')
        assert response.status_code == 404


def test_buffer_pages():
    with flask_app.test_client() as test_client:
        response = test_client.get('/bufferfile')
        assert response.status_code == 200
        response = test_client.get('/bufferfile_create')
        assert response.status_code == 200

        response = test_client.get('/bufferfile_read/<string:name>')
        assert response.status_code == 302
        response = test_client.get('/bufferfile_del/<string:name>')
        assert response.status_code == 302
        response = test_client.get('/bufferfile_move/<string:name>')
        assert response.status_code == 302
        response = test_client.get('/bufferfile_add/<string:name>')
        assert response.status_code == 302
        response = test_client.get('/bufferfile_pop/<string:name>')
        assert response.status_code == 302

        response = test_client.get('/bufferfile_read')
        assert response.status_code == 404
        response = test_client.get('/bufferfile_del')
        assert response.status_code == 404
        response = test_client.get('/bufferfile_move')
        assert response.status_code == 404
        response = test_client.get('/bufferfile_add')
        assert response.status_code == 404
        response = test_client.get('/bufferfile_pop')
        assert response.status_code == 404


def test_logtextfile_pages():
    with flask_app.test_client() as test_client:
        response = test_client.get('/logtextfile')
        assert response.status_code == 200
        response = test_client.get('/logtextfile_create')
        assert response.status_code == 200
        response = test_client.get('/logtextfile_del')
        assert response.status_code == 200
        response = test_client.get('/logtextfile_read')
        assert response.status_code == 200

        response = test_client.get('/logtextfile_del/<string:name>')
        assert response.status_code == 404
        response = test_client.get('/logtextfile_read/<string:name>')
        assert response.status_code == 404
        response = test_client.get('/logtextfile_move')
        assert response.status_code == 404


def test_directory_pages():
    with flask_app.test_client() as test_client:
        response = test_client.get('/directory')
        assert response.status_code == 200
        response = test_client.get('/directory_create')
        assert response.status_code == 200

        response = test_client.get('/directory_read/<string:name>')
        assert response.status_code == 302
        response = test_client.get('/directory_del/<string:name>')
        assert response.status_code == 302
        response = test_client.get('/directory_move/<string:name>')
        assert response.status_code == 302

        response = test_client.get('/directory_read')
        assert response.status_code == 404
        response = test_client.get('/directory_del')
        assert response.status_code == 404
        response = test_client.get('/directory_move')
        assert response.status_code == 404


def test_binaryfile_create():
    ENDPOINT = "http://127.0.0.1:5000/binaryfile_create"
    response = requests.get(ENDPOINT)

    #data = response.text
    #print(data)

    payload = {
        "name": "Binn"
    }
    response = requests.post(ENDPOINT, json=payload)
    data = response.text
    print(data)

    name = "Binn"
    check_existance_response = requests.get(f"http://127.0.0.1:5000/binaryfile_read/{name}")
    assert check_existance_response.status_code == 200
    data = check_existance_response.text
    print(data)


def test_binary_delete():
    name = "Binary"
    ENDPOINT = f"http://127.0.0.1:5000/binaryfile_del/{name}"
    response = requests.post(ENDPOINT)

    check_existance_response = requests.get(f"http://127.0.0.1:5000/binaryfile_read/{name}")
    assert check_existance_response.status_code == 200      #redirect
    data = check_existance_response.text
    print(data)


def test_binary_move():
    name = "Binary"
    ENDPOINT = f"http://127.0.0.1:5000/binaryfile_move/{name}"
    payload = {
        "name": "home"
    }
    response = requests.post(ENDPOINT, json=payload)

    check_existance_response = requests.get(f"http://127.0.0.1:5000/binaryfile_read/{name}")
    assert check_existance_response.status_code == 200  # redirect
    data = check_existance_response.text
    print(data)



def test_bufferfile_create():
    ENDPOINT = "http://127.0.0.1:5000/bufferfile_create"
    response = requests.get(ENDPOINT)

    payload = {
        "name": "Buffer"
    }
    response = requests.post(ENDPOINT, json=payload)
    data = response.text
    print(data)

    name = "Buffer"
    check_existance_response = requests.get(f"http://127.0.0.1:5000/bufferfile_read/{name}")
    assert check_existance_response.status_code == 200
    data = check_existance_response.text
    print(data)


def test_buffer_add():
    name = "Buffer"
    ENDPOINT = f"http://127.0.0.1:5000/bufferfile_add/{name}"
    payload = {
        "name": "smth"
    }
    response = requests.post(ENDPOINT, json=payload)

    check_existance_response = requests.get(f"http://127.0.0.1:5000/bufferfile_read/{name}")
    assert check_existance_response.status_code == 200  # redirect
    data = check_existance_response.text
    print(data)


def test_buffer_pop():
    name = "Buffer"
    ENDPOINT = f"http://127.0.0.1:5000/bufferfile_pop/{name}"
    response = requests.post(ENDPOINT)

    check_existance_response = requests.get(f"http://127.0.0.1:5000/bufferfile_read/{name}")
    assert check_existance_response.status_code == 200  # redirect
    data = check_existance_response.text
    print(data)

def test_bufferfile_delete():
    name = "Buffer"
    ENDPOINT = f"http://127.0.0.1:5000/bufferfile_del/{name}"
    response = requests.post(ENDPOINT)

    check_existance_response = requests.get(f"http://127.0.0.1:5000/bufferfile_read/{name}")
    assert check_existance_response.status_code == 200      #redirect
    data = check_existance_response.text
    print(data)


def test_buffer_move():
    name = "Buffer"
    ENDPOINT = f"http://127.0.0.1:5000/bufferfile_move/{name}"
    payload = {
        "name": "home"
    }
    response = requests.post(ENDPOINT, json=payload)

    check_existance_response = requests.get(f"http://127.0.0.1:5000/bufferfile_read/{name}")
    assert check_existance_response.status_code == 200  # redirect
    data = check_existance_response.text
    print(data)


def test_logtextfile_create():
    ENDPOINT = "http://127.0.0.1:5000/logtextfile_create"
    response = requests.get(ENDPOINT)
    assert response.status_code == 200
    data = response.text
    print(data)


def test_logtextfile_delete():
    ENDPOINT = "http://127.0.0.1:5000/logtextfile_del"
    response = requests.get(ENDPOINT)

    assert response.status_code == 200
    data = response.text
    print(data)


def test_logtextfile_move():
    ENDPOINT = "http://127.0.0.1:5000/bufferfile_move"
    response = requests.get(ENDPOINT)
    assert response.status_code == 404


def test_binaryfile_create():
    ENDPOINT = "http://127.0.0.1:5000/directory_create"
    response = requests.get(ENDPOINT)

    payload = {
        "name": "Directory"
    }
    response = requests.post(ENDPOINT, json=payload)
    data = response.text
    print(data)

    name = "Directory"
    check_existance_response = requests.get(f"http://127.0.0.1:5000/directory_read/{name}")
    assert check_existance_response.status_code == 200
    data = check_existance_response.text
    print(data)


def test_directory_delete():
    name = "Directory"
    ENDPOINT = f"http://127.0.0.1:5000/directory_del/{name}"
    response = requests.post(ENDPOINT)

    check_existance_response = requests.get(f"http://127.0.0.1:5000/directory_read/{name}")
    assert check_existance_response.status_code == 200      #redirect
    data = check_existance_response.text
    print(data)


def test_directory_move():
    name = "Directory"
    ENDPOINT = f"http://127.0.0.1:5000/directory_move/{name}"
    payload = {
        "name": "dir1"
    }
    response = requests.post(ENDPOINT, json=payload)

    check_existance_response = requests.get(f"http://127.0.0.1:5000/directory_read/{name}")
    assert check_existance_response.status_code == 200  # redirect
    data = check_existance_response.text
    print(data)


