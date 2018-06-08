#!/usr/bin/env python
# __Author__:cmustard

from flaskr import create_app

"""
test get request
"""
def test_config():
	assert not create_app().testing
	assert create_app({'TESTING':True}).testing
	
	
def test_hello(client):
	response = client.get('hello')
	assert response.data == b'Hello World'