# -*- coding: utf-8 -*-
class Msg:
    def __init__(self):
        self.__susses = {
            "code": 200,
            "status": "ok",
        }
        self.__fail = {
            "code": 400,
            "status": "fail",
        }

    def processing(self, msg: str, code: int, res: dict = None,cdata:str = None,key:str = None) -> dict:
        if res is None:
            res = {}
        if code == 200:
            res["code"] = self.__susses["code"]
            res["status"] = self.__susses["status"]
            res["msg"] = msg
        else:
            res["code"] = self.__fail["code"]
            res["status"] = self.__fail["status"]
            res["msg"] = msg
            res["data"] = None
            res["cdata"] = cdata
            res["key"] = key

        return res
