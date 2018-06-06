#!/usr/bin/env python
# __Author__:cmustard

import sqlite3
import click

from flask import current_app,g
from flask.cli import with_appcontext


def init_db():
	db = get_db()
	with current_app.open_resource('schema.sql') as f:
		db.executescript(f.read().decode('utf-8'))


def get_db():
	if 'db' not in g:
		g.db = sqlite3.connect(
			current_app.config['DATABASE'],
			detect_types=sqlite3.PARSE_DECLTYPES
		)
		g.db.row_factory = sqlite3.Row # 返回像字典一样的行
		
	return g.db

def close_db(e=None):
	db = g.pop('db',None)
	if db is not None:
		db.close()


@click.command('init-db')
@with_appcontext
def init_db_command():
	"""清除已经存在的数据，创建新表"""
	init_db()
	click.echo("Initalized the database.")
	
def init_app(app):
	# 告诉Flask，在返回响应后就调用该函数
	app.teardown_appcontext(close_db)
	app.cli.add_command(init_db_command)