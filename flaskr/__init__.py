#!/usr/bin/env python
# __Author__:cmustard

import os
from flask import Flask
from flaskr import auth,blog


def create_app(test_config=None):
	# 创建和配置一个app
	"""
	# __name__是当前python模块的名字
	instance_relative_config告诉app配置文件与实例文件夹是相对的。
	实例文件夹位于flaskr软件包外部，
	可以保存不应提交给版本控制的本地数据，
	例如配置机密和数据库文件。
	"""
	app = Flask(__name__,instance_relative_config=True)
	app.config.from_mapping(
		SECRET_KEY='dev',
		DATABASE = os.path.join(app.instance_path,"flaskr.sqlite"),
	)
	
	if test_config is None:
		# 加载实例配置文件，如果文件缺失，也不会提示失败 silent=true。
		app.config.from_pyfile('config.py',silent=True)
	else:
		# test_config 如果存在，就加载它
		app.config.from_mapping(test_config)
	# 确保实例文件夹的存在
	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass
	
	# simple page,test page
	@app.route("/hello")
	def hello():
		return "Hello,World!!"
	
	# 初始化数据库
	from . import db
	db.init_app(app)
	
	# 将blueprint注册到app中
	app.register_blueprint(auth.bp)
	app.register_blueprint(blog.bp)
	app.add_url_rule('/',endpoint="index")
	return app

# app = create_app()
# app.run(host="0.0.0.0",port=8000)