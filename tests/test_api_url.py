# -*- coding: utf-8 -*-

from hackcqooc.api_url import ApiUrl

import time


def get_ts():
    return int(time.time() * 1000)


xsid = "xsid"
sid = "123"
username = "username"
login_hash = "hash"
nonce = "nonce"
cn = "cn"
course_id = "course_id"
owner_id = "231"
section_id = "section_id"
start = 0
limit = 200


def test_id_api():
    api_url = ApiUrl()
    assert api_url.id_api(xsid) == (
        "http://www.cqooc.com/user/session" + f"?xsid={xsid}&ts={get_ts()}"
    )


def test_info_api():
    api_url = ApiUrl()
    assert api_url.info_api() == (
        "http://www.cqooc.com/account/session/api/profile/get"
        + f"?ts={get_ts()}"
    )


def test_nonce_api():
    api_url = ApiUrl()
    assert api_url.get_nonce_api() == (
        "http://www.cqooc.com/user/login" + f"?ts={get_ts()}"
    )


def test_login_api():
    api_url = ApiUrl()
    assert api_url.login_api(username, login_hash, nonce, cn) == (
        "http://www.cqooc.com/user/login"
        + f"?username={username}&password={login_hash}"
        + f"&nonce={nonce}&cnonce={cn}"
    )


def test_course_api():
    api_url = ApiUrl()
    assert api_url.course_api(sid, limit) == (
        "http://www.cqooc.com/json/mcs?sortby=id&reverse=true&del=2"
        + f"&courseType=2&ownerId={sid}&limit={limit}"
        + f"&ts={get_ts()}"
    )


def test_lessons_api():
    api_url = ApiUrl()
    assert api_url.lessons_api(course_id, start, limit) == (
        "http://www.cqooc.com/json/mooc/lessons"
        + f"?limit={limit}&start={start}&sortby=selfId&reverse=false"
        + f"&courseId={course_id}&ts={get_ts()}"
    )


def test_lessons_status_api():
    api_url = ApiUrl()
    assert api_url.lessons_status_api(course_id, username, start, limit) == (
        "http://www.cqooc.com/json/learnLogs"
        + f"?limit={limit}&start={start}&courseId={course_id}&select=sectionId"
        + f"&username={username}&ts={get_ts()}"
    )


def test_mcs_id_api():
    api_url = ApiUrl()
    assert api_url.mcs_id_api(owner_id, course_id) == (
        "http://www.cqooc.com/json/mcs"
        + f"?ownerId={owner_id}&courseId={course_id}"
        + f"&ts={get_ts()}"
    )


def test_learn_log_api():
    api_url = ApiUrl()
    assert api_url.learn_log_api(section_id, username) == (
        "http://www.cqooc.com/json/learnLogs"
        + f"?sectionId={section_id}&username={username}"
        + f"&ts={get_ts()}"
    )


def test_skip_section_api():
    api_url = ApiUrl()
    assert (
        api_url.skip_section_api() == "http://www.cqooc.com/learnLog/api/add"
    )


def test_exam_papers_api():
    api_url = ApiUrl()
    assert api_url.exam_papers_api(course_id, start, limit) == (
        "http://www.cqooc.com/json/exam/papers"
        + f"?limit={limit}&start={start}&courseId={course_id}"
        f"&ts={get_ts()}"
    )


def test_exams_api():
    api_url = ApiUrl()
    assert api_url.exams_api(course_id, start, limit) == (
        "http://www.cqooc.com/json/exams"
        + f"?limit={limit}&start={start}&courseId={course_id}"
        f"&ts={get_ts()}"
    )


def test_tasks_api():
    api_url = ApiUrl()
    assert api_url.tasks_api(course_id, start, limit) == (
        "http://www.cqooc.com/json/tasks"
        + f"?limit={limit}&start={start}&courseId={course_id}"
        + f"&ts={get_ts()}"
    )


def test_chapters_api():
    api_url = ApiUrl()
    assert api_url.chapters_api(course_id, start, limit) == (
        "http://www.cqooc.com/json/chapters"
        + f"?limit={limit}&start={start}&courseId={course_id}"
        + f"&ts={get_ts()}"
    )
