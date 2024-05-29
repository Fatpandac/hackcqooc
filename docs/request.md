# Module: request

## 概述

request模块定义了Request类，其是对 [Requests](https://pypi.org/project/requests/) 的二次封装，其中提供了一些和网络请求相关的函数。

## 内容

### 构造函数

```py
def __init__(self) -> None
```

#### 功能描述

设置部分HTTP请求参数，包括UA和proxies。

#### 参数

无。

### setters & getters

Request类定义了下列属性。

|属性名称|类型|说明|
| :-: | :-: | :-: |
|headers|dict|对应HTTP请求头。除了setter和getter，还有del_headers函数。|
|proxies|dict|对应HTTP参数代理配置|

 - setter：传入一个key和value，写入参数字典。

 - getter：返回这个字典。

 - del：给定key，删除字典中这个属性的值。

---

### do_get

```py
def do_get(self, url: str, headers: dict = None, proxies: dict = None) -> requests.Response
```

#### 功能描述

使用requests库，基于当前设定的和参数传入的headers和proxies，对指定url使用get方法发起HTTP请求，取得请求响应并返回。

#### 参数

|属性名称|类型|说明|
| :-: | :-: | :-: |
|url|string|请求的地址|
|headers|dict|默认为None|
|proxies|dict|默认为None|

#### 返回内容

返回内容为requests.Response，即requests库请求响应对象。

---

### do_post

```py
def do_post(self,url: str,data: [dict, str] = None,json: dict = None,headers: dict = None,proxies: dict = None,) -> requests.Response
```

#### 功能描述

使用requests库，基于当前设定的和参数传入的headers和proxies与请求参数（即data和json），对指定url使用post方法发起HTTP请求，取得请求响应并返回。

#### 参数

|属性名称|类型|说明|
| :-: | :-: | :-: |
|url|string|请求的地址|
|data|list[dict, string]|默认为None|
|json|dict|默认为None|
|headers|dict|默认为None|
|proxies|dict|默认为None|

#### 返回内容

返回内容为requests.Response，即requests库请求响应对象。
