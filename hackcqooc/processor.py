# -*- coding: utf-8 -*-

import json
from typing import List

import requests


class Processor:
    @staticmethod
    def process_course_data(course_res: requests.Response) -> dict:
        res_course_data = json.loads(course_res.text)
        course_data = dict()
        course_data["meta"] = res_course_data["meta"]
        course_data["data"] = []
        for course in res_course_data["data"]:
            course_data["data"].append(
                {
                    "courseId": course["courseId"],
                    "ownerId": course["ownerId"],
                    "title": course["course"]["title"],
                }
            )
        return course_data

    @staticmethod
    def process_lessons_data(
        username: str,
        lessons_res_meta: dict,
        lessons_res_data: List,
        lessons_status_res_data: List,
    ) -> dict:
        lessons_data = {"meta": lessons_res_meta, "data": []}
        for lesson in lessons_res_data:
            lessons_data["data"].append(
                {
                    "title": lesson["title"],
                    "sectionId": lesson["id"],
                    "category": lesson["category"],
                    "chapterId": lesson["chapterId"],
                    "courseId": lesson["courseId"],
                    "ownerId": lesson["ownerId"],
                    "parentId": lesson["parentId"],
                    "id": lesson["id"],
                    "username": username,
                }
            )
        # add status
        lesson_status = [i["sectionId"] for i in lessons_status_res_data]
        for lesson in lessons_data["data"]:
            lesson["status"] = 1 if lesson["sectionId"] in lesson_status else 0
        # sort by sectionId
        lessons_data["data"] = sorted(
            lessons_data["data"], key=lambda x: x["sectionId"]
        )
        return lessons_data

    @staticmethod
    def process_section_data(section_data: dict, mcs_id: str) -> dict:
        post_data = dict()
        post_data["action"] = 0
        post_data["category"] = 2
        post_data["chapterId"] = section_data["chapterId"]
        post_data["courseId"] = section_data["courseId"]
        post_data["ownerId"] = int(section_data["ownerId"])
        post_data["parentId"] = mcs_id
        post_data["sectionId"] = section_data["sectionId"]
        post_data["username"] = section_data["username"]
        return post_data
    
    @staticmethod
    def process_captcha_data(captcha: str, key: str) -> dict:
        captcha_post_data = dict()
        captcha_post_data["captcha"] = captcha
        captcha_post_data["key"] = key
        return captcha_post_data
    @staticmethod
    def process_againlogin_data(signType: str, username: str) -> dict:
        captcha_againlogin_data = dict()
        captcha_againlogin_data["signType"] = signType
        captcha_againlogin_data["username"] = username
        return captcha_againlogin_data
