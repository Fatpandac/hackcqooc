# -*- coding: utf-8 -*-

import time


class ApiUrl:
    __host = "https://www.cqooc.com"

    @staticmethod
    def __get_ts() -> int:
        return int(time.time() * 1000)

    def id_api(self, xsid: str) -> str:
        return (
            f"{self.__host}/user/session"
            + f"?xsid={xsid}&ts={self.__get_ts()}"
        )

    def info_api(self) -> str:
        return (
            f"{self.__host}/account/session/api/profile/get"
            + f"?ts={self.__get_ts()}"
        )

    def get_nonce_api(self):
        return f"{self.__host}/user/login?ts={self.__get_ts()}"

    def login_api(
        self, username: str, login_hash: str, nonce: str, cn: str
    ) -> str:
        return (
            f"{self.__host}/user/login"
            + f"?username={username}&password={login_hash}"
            + f"&nonce={nonce}&cnonce={cn}"
        )

    def course_api(self, sid: str, limit: int) -> str:
        return (
            f"{self.__host}/json/mcs?sortby=id&reverse=true&del=2"
            + f"&courseType=2&ownerId={sid}&limit={limit}"
            + f"&ts={self.__get_ts()}"
        )

    def lessons_api(
        self, course_id: str, start: int = 1, limit: int = 100
    ) -> str:
        return (
            f"{self.__host}/json/mooc/lessons"
            + f"?limit={limit}&start={start}&sortby=selfId&reverse=false"
            + f"&courseId={course_id}&ts={self.__get_ts()}"
        )

    def lessons_status_api(
        self, course_id: str, username: str, start: int = 1, limit: int = 100
    ) -> str:
        return (
            f"{self.__host}/json/learnLogs"
            + f"?limit={limit}&start={start}&courseId={course_id}"
            + f"&select=sectionId&username={username}&ts={self.__get_ts()}"
        )

    def mcs_id_api(self, owner_id: str, course_id: str) -> str:
        return (
            f"{self.__host}/json/mcs"
            + f"?ownerId={owner_id}&courseId={course_id}"
            + f"&ts={self.__get_ts()}"
        )

    def learn_log_api(self, section_id: str, username: str) -> str:
        return (
            f"{self.__host}/json/learnLogs"
            + f"?sectionId={section_id}&username={username}"
            + f"&ts={self.__get_ts()}"
        )

    def exam_papers_api(
        self, course_id: str, start: int = 0, limit: int = 200
    ) -> str:
        return (
            f"{self.__host}/json/exam/papers"
            + f"?limit={limit}&start={start}&courseId={course_id}"
            f"&ts={self.__get_ts()}"
        )

    def exams_api(
        self, course_id: str, start: int = 0, limit: int = 200
    ) -> str:
        return (
            f"{self.__host}/json/exams"
            + f"?limit={limit}&start={start}&courseId={course_id}"
            f"&ts={self.__get_ts()}"
        )

    def tasks_api(
        self, course_id: str, start: int = 0, limit: int = 200
    ) -> str:
        return (
            f"{self.__host}/json/tasks"
            + f"?limit={limit}&start={start}&courseId={course_id}"
            + f"&ts={self.__get_ts()}"
        )

    def chapters_api(
        self, course_id: str, start: int = 0, limit: int = 200
    ) -> str:
        return (
            f"{self.__host}/json/chapters"
            + f"?limit={limit}&start={start}&courseId={course_id}"
            + f"&ts={self.__get_ts()}"
        )

    def skip_section_api(self) -> str:
        return f"{self.__host}/learnLog/api/add"
