# -*- coding: utf-8 -*-
class User:
    __xsid = None
    __sid = None
    __username = None
    __pwd = None
    __name = None
    __course_data = None
    __lessons_data = None
    __exam_papers_data = None
    __exams_data = None
    __tasks_data = None
    __chapters_data = None
    __mcs_id = None
    __cookie = None
    __captchaToken =None

    def __init__(
        self, username: str = "", pwd: str = "", cookie: str = None
    ) -> None:
        self.__username = username
        self.__pwd = pwd
        self.__cookie = cookie

    def set_xsid(self, xsid: str) -> None:
        self.__xsid = xsid

    def get_xsid(self) -> str:
        return self.__xsid

    def set_id(self, sid: str) -> None:
        self.__sid = sid

    def get_id(self) -> str:
        return self.__sid

    def set_username(self, username: str) -> None:
        self.__username = username

    def get_username(self) -> str:
        return self.__username

    def set_pwd(self, pwd: str) -> None:
        self.__pwd = pwd

    def get_pwd(self) -> str:
        return self.__pwd

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def set_course_data(self, course_data: dict) -> None:
        self.__course_data = course_data

    def get_course_data(self) -> dict:
        return self.__course_data

    def set_lessons_data(self, lessons_data: dict) -> None:
        self.__lessons_data = lessons_data

    def get_lessons_data(self) -> dict:
        return self.__lessons_data

    def set_mcs_id(self, mcs_id: str) -> None:
        self.__mcs_id = mcs_id

    def get_mcs_id(self) -> str:
        return self.__mcs_id

    def set_exam_papers_data(self, exam_papers_data: dict) -> None:
        self.__exam_papers_data = exam_papers_data

    def get_exam_papers_data(self) -> dict:
        return self.__exam_papers_data

    def set_exams_data(self, exams_data: dict) -> None:
        self.__exams_data = exams_data

    def get_exams_data(self) -> dict:
        return self.__exams_data

    def set_tasks_data(self, tasks_data: dict) -> None:
        self.__tasks_data = tasks_data

    def get_tasks_data(self) -> dict:
        return self.__tasks_data

    def set_chapters_data(self, chapters_data: dict) -> None:
        self.__chapters_data = chapters_data

    def get_chapters_data(self) -> dict:
        return self.__chapters_data

    def get_cookie(self) -> str:
        return self.__cookie

    def get_info(self) -> dict:
        return {
            "xsid": self.__xsid,
            "id": self.__sid,
            "username": self.__username,
            "pwd": self.__pwd,
            "name": self.__name,
            "mcs_id": self.__mcs_id,
            "course_data": self.__course_data,
            "lessons_data": self.__lessons_data,
        }
