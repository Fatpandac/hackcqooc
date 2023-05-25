# -*- coding: utf-8 -*-
from hackcqooc.core import Core

import os

# ROOT_PATH = os.path.dirname(os.path.dirname(__file__))

username = os.environ.get("USERS")
password = os.environ.get("PASSWORD")


def test_login_success():
    if (username is None) or (password is None):
        print("!!! 请设置环境变量：USERS 和 PASSWORD !!!")
    core = Core(username, password)
    res = core.login()
    assert res["code"] == 200
    assert res["msg"] == "登录成功"


def test_login_fail():
    username_fail = "test"
    password_fail = "1234567"
    core = Core(username_fail, password_fail)
    res = core.login()
    assert res["code"] == 400
    assert res["msg"] is not None
    assert res["status"] == "fail"


def test_login_by_cookie():
    core_get_cookie = Core(username, password)
    core_get_cookie.login()
    cookie = f'xsid={core_get_cookie.get_user_info().get("xsid")}'
    core = Core(cookie=cookie)
    res = core.login()
    assert res["code"] == 200
    assert res["msg"] == "登录成功"


def test_login_by_cookie_fail():
    cookie_fail = "xsid=fail_cookie"
    core = Core(cookie=cookie_fail)
    res = core.login()
    assert res["code"] == 400
    assert res["msg"] is not None
    assert res["status"] == "fail"


def test_get_info():
    core = Core(username, password)
    res = core.get_user_info()
    assert res["username"] == username
    assert res["pwd"] == password
    assert res["xsid"] is None
    assert res["id"] is None
    assert res["name"] is None


def test_get_course():
    core = Core(username, password)
    core.login()
    res = core.get_course()
    assert res["code"] == 200
    assert res["status"] == "ok"
    assert res["data"] is not None


def test_get_course_lessons():
    core = Core(username, password)
    core.login()
    res = core.get_course_lessons(core.get_course()["data"][0]["courseId"])
    assert res["code"] == 200
    assert res["status"] == "ok"
    assert res["data"] is not None


def test_get_exam_papers_info():
    core = Core(username, password)
    core.login()
    res = core.get_exam_papers_info(core.get_course()["data"][0]["courseId"])
    assert res["code"] == 200
    assert res["status"] == "ok"
    assert res["data"] is not None


def test_get_exams_info():
    core = Core(username, password)
    core.login()
    res = core.get_exams_info(core.get_course()["data"][0]["courseId"])
    assert res["code"] == 200
    assert res["status"] == "ok"
    assert res["data"] is not None


def test_get_tasks_info():
    core = Core(username, password)
    core.login()
    res = core.get_tasks_info(core.get_course()["data"][0]["courseId"])
    assert res["code"] == 200
    assert res["status"] == "ok"
    assert res["data"] is not None


def test_get_chapters_info():
    core = Core(username, password)
    core.login()
    res = core.get_chapters_info(core.get_course()["data"][0]["courseId"])
    assert res["code"] == 200
    assert res["status"] == "ok"
    assert res["data"] is not None


def test_skip_section():
    core = Core(username, password)
    core.login()
    lesson_data = core.get_course_lessons(
        core.get_course()["data"][0]["courseId"]
    )
    res = core.skip_section(lesson_data["data"][0]["sectionId"])
    assert res["code"] == 200
    assert res["status"] == "ok"
