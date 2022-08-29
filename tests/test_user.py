# -*- coding: utf-8 -*-
from hackcqooc.user import User

xsid = "ASD121AS1"
cookie = "xsid=ASD121AS1"
sid = "121324"
username = "122132421"
pwd = "123456"
name = "asad"
course_data = dict(course="test")
lessons_data = dict(lesson="test")


def test_init():
    user = User(username, pwd)
    assert user.get_username() == username
    assert user.get_pwd() == pwd


def test_get_and_set_username():
    user = User(username, pwd)
    user.set_username(username)
    assert user.get_username() == username


def test_get_and_set_pwd():
    user = User(username, pwd)
    user.set_pwd(pwd)
    assert user.get_pwd() == pwd


def test_get_and_set_xsid():
    user = User(username, pwd)
    user.set_xsid(xsid)
    assert user.get_xsid() == xsid


def test_get_and_set_id():
    user = User(username, pwd)
    user.set_id(sid)
    assert user.get_id() == sid


def test_get_and_set_name():
    user = User(username, pwd)
    user.set_name(name)
    assert user.get_name() == name


def test_get_and_set_course_data():
    user = User(username, pwd)
    user.set_course_data(course_data)
    assert user.get_course_data() == course_data


def test_get_and_set_lesson_data():
    user = User(username, pwd)
    user.set_lessons_data(lessons_data)
    assert user.get_lessons_data() == lessons_data


def test_get_and_set_mcs_id():
    user = User(username, pwd)
    user.set_mcs_id(sid)
    assert user.get_mcs_id() == sid


def test_get_cookie():
    user = User(cookie=cookie)
    assert user.get_cookie() == cookie


def test_get_info():
    user = User(username, pwd)
    user.set_xsid(xsid)
    user.set_id(sid)
    user.set_name(name)
    user.set_course_data(course_data)
    user.set_lessons_data(lessons_data)
    info = user.get_info()
    assert info["xsid"] == xsid
    assert info["id"] == sid
    assert info["username"] == username
    assert info["pwd"] == pwd
    assert info["name"] == name
    assert info["course_data"] == course_data
    assert info["lessons_data"] == lessons_data
