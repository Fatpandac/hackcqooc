# -*- coding: utf-8 -*-

from hackcqooc.request import Request

ua = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
    + " AppleWebKit/537.36 (KHTML, like Gecko)"
    + " Chrome/101.0.0.0 Safari/537.36"
)

proxies = {
    "http": "",
    "https": "",
}

proxiesURI = "http://127.0.0.1:8889"


def test_get_ua():
    request = Request()
    assert request.get_headers()["User-Agent"] == ua


def test_set_cookies():
    request = Request()
    request.set_headers("cookie", "12345678")
    assert request.get_headers()["cookie"] == "12345678"


def test_del_cookie():
    request = Request()
    request.set_headers("cookie", "12345678")
    request.del_headers("cookie")
    assert "cookie" not in request.get_headers()


def test_get_proxies():
    request = Request()
    assert request.get_proxies() == proxies


def test_set_proxies():
    request = Request()
    request.set_proxies("http", proxiesURI)
    assert request.get_proxies()["http"] == proxiesURI
    request.set_proxies("http", "")


def test_do_get():
    request = Request()
    res = request.do_get("https://www.baidu.com", proxies=proxies)
    assert res.status_code == 200
