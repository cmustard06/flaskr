#!/usr/bin/env python
# __Author__:cmustard

import sqlite3

import pytest
from flaskr.db import get_db


def test_get_close_db(app):
