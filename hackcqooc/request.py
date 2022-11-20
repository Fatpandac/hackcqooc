# -*- coding: utf-8 -*-
import requests
import logging

# logging.basicConfig(
#     level=logging.INFO,
#     filename="hackcqooc.log",
#     filemode="w",
#     format="%(levelname)s:%(asctime)s:%(message)s",
#     datefmt="%Y-%d-%m %H:%M:%S",
# )


class Request:
    def __init__(self):
        self.__headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
            + " AppleWebKit/537.36 (KHTML, like Gecko)"
            + " Chrome/101.0.0.0 Safari/537.36",
        }
        self.__proxies = {
            "http": "",
            "https": "",
        }

    def set_headers(self, name: str, value: str) -> None:
        self.__headers[name] = value

    def del_headers(self, name: str) -> None:
        del self.__headers[name]

    def get_headers(self) -> dict:
        return self.__headers

    def set_proxies(self, name: str, value: str) -> None:
        self.__proxies[name] = value

    def get_proxies(self) -> dict:
        return self.__proxies

    def __process_headers_and_proxies(
        self, headers: dict = None, proxies: dict = None
    ):
        self_headers = self.__headers.copy()
        if headers is not None:
            for key in headers:
                self_headers[key] = headers[key]
        self_proxies = self.__proxies.copy()
        if proxies is not None:
            for key in proxies:
                self_proxies[key] = proxies[key]
        return self_headers, self_proxies

    def do_get(
        self, url: str, headers: dict = None, proxies: dict = None
    ) -> requests.Response:
        headers, proxies = self.__process_headers_and_proxies(headers, proxies)
        res = requests.get(url, headers=headers, proxies=proxies)
        logging.info(f"{url} GET")
        logging.info(f"{res.text}")
        return res

    def do_post(
        self,
        url: str,
        data: [dict, str] = None,
        headers: dict = None,
        proxies: dict = None,
    ) -> requests.Response:
        headers, proxies = self.__process_headers_and_proxies(headers, proxies)
        res = requests.post(url, data=data, headers=headers, proxies=proxies)
        logging.info(f"{url} POST")
        logging.info(f"{res.text}")
        return res
