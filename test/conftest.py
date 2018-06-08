#!/usr/bin/env python
# __Author__:cmustard

import os
import tempfile

import pytest
from flaskr import create_app
from flaskr.db import get_db,init_db

# 测试数据库
with open(os.path.join(os.path.dirname(__file__,'data.sql'),'rb')) as f:
	_data_sql = f.read().decode("utf-8")
	
@pytest.fixture
def app():
	db_fd,db_path = tempfile.mkdtemp() # 创建和返回一个独一无二的临时文件，返回的值为文件对象和路径
	print(db_fd,db_path)
	app = create_app({
		'TESTING':True, # 告诉flask这个app是testing模式
		'DATABASE':db_path,
	})
	
	with app.app_context():
		init_db()
		get_db().executescript(_data_sql)
	yield app
	os.close(db_fd)
	os.unlink(db_path)
	

@pytest.fixture
def client(app):
	"""在没有运行服务器的情况下去请求应用"""
	return app.test_client()

@pytest.fixture
def runner(app):
	return app.test_cli_runner()


	
	