# Module: user

## 概述

user模块中定义了User类，这是对cqooc用户的一个简要描述，其中定义了一些cqooc用户的个人信息。

## 内容

### 构造函数

` __init__(self, username: str = "", pwd: str = "", cookie: str = None) -> None `

#### 功能描述

使用给定的用户名、密码、cookie参数构造一个User对象。

#### 参数

|参数名称|类型|说明|
| :-: | :-: | :-: |
|username|string|用户名，默认值为""|
|pwd|string|密码，默认值为""|
|cookie|string|cookie，默认值为None|

---

### setters & getters

User类定义了下列属性。

|属性名称|类型|说明|
| :-: | :-: | :-: |
|xsid|string||
|sid|string|setter和getter函数名分别为set_id和get_id|
|username|string||
|pwd|string||
|name|string||
|course_data|dict||
|lessons_data|dict||
|exam_papers_data|dict||
|exams_data|dict||
|tasks_data|dict||
|chapters_data|dict||
|mcs_id|string||
|cookie|string|cookie只有getter|

---

### get_info

get_info(self) -> dict

#### 功能描述

以dict的形式返回部分User对象属性。

#### 参数

无。

#### 返回内容

返回的dict中包含以下内容。

|属性名称|类型|说明|
| :-: | :-: | :-: |
|xsid|string||
|id|string||
|username|string||
|pwd|string||
|name|string||
|course_data|dict||
|lessons_data|dict||
|mcs_id|string||
