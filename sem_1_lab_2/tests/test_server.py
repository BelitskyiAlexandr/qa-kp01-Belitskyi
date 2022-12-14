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