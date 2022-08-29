# -*- coding: utf-8 -*-
from hackcqooc.msg import Msg

susses = {"code": 200, "status": "ok", "msg": "成功"}

fail = {"code": 400, "status": "fail", "msg": "失败"}


def test_process_susses():
    msg = Msg().processing(susses["msg"], susses["code"])
    assert msg["code"] == susses["code"]
    assert msg["status"] == susses["status"]
    assert msg["msg"] == susses["msg"]


def test_process_fail():
    msg = Msg().processing(fail["msg"], fail["code"])
    assert msg["code"] == fail["code"]
    assert msg["status"] == fail["status"]
    assert msg["msg"] == fail["msg"]
