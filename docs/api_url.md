# Module: api_url

## 概览

api_url是一个用来获取cqooc网站的可用API的类。cqooc的许多api都需要携带一个时间戳参数，所以不能使用静态的API地址，而是需要这个类提供的函数来动态生成地址。每一个core实例都包含一个api_url实例。

需要注意的是，cqooc的许多API采取了防盗链措施，需要添加合适的Referer header。有些API的样例代码包含如何使用Referer的举例，但不同的API可能使用不同的Referer，具体值请参考cqooc网站上的实际请求字段。

- 覆盖模块：api_url.py

- 最后更新时间：July 4th, 2022

- 作者：Fatpandac, Xtao

- 文档作者：RX-105

## 内容

### 构造函数

这个类没有显式定义的构造函数。

### id_api

id_api(self, xsid: str) -> str

#### 功能描述

生成获取id的api。

#### 参数

| 属性 | 类型 | 说明 |
| :-: | :-: | :-: |
|xsid|string|学生ID|

#### API信息

 - 地址：https://www.cqooc.com/user/session?xsid={XSID}&ts={TS}
 - 请求方法：get

```python
# 使用get方法请求该API，并输出返回文本
s = api.id_api('XSID') # api是ApiUrl实例，下同
req.do_get(s).text # req为Request实例，下同
```

返回内容如下：
```json
{
    "id": number，也就是id,
    "username": string，用户名称，通常是登录名,
    "email": string，用户登记的邮件地址,
    "phone": string，电话号码,
    "group": string list，用户组,
    "profile": json
}
```

### info_api

info_api(self) -> str

#### 功能描述

生成获取个人信息的API。

#### 参数

无。

#### API信息

 - 地址：https://www.cqooc.com/account/session/api/profile/get?ts={TS}
 - 请求方法：get

### get_nonce_api

get_nonce_api(self) -> str

#### 功能描述

生成获取nonce的API，这是其他有些API需要用到的参数。

#### 参数

无。

#### API描述

 - 地址：https://www.cqooc.com/user/login?ts={TS}
 - 请求方法：get

##### 样例代码

```python
req.do_get(api.get_nonce_api(),{ 'Referer': 'http://www.cqooc.com/login' }).text
```

##### 返回内容

```json
{
    "nonce":string，nonce内容
}
```

### course_api

course_api(self, sid: str, limit: int) -> str

#### 功能描述

生成获取课程的API。

#### 参数

| 属性 | 类型 | 说明 |
| :-: | :-: | :-: |
|sid|string|其实这应该是ownerId吧|
|limit|int|分页大小|

#### API信息

 - 地址：https://www.cqooc.com/json/mcs?sortby={SORTBY}&reverse={BOOLEAN}&del={DEL}&courseType={COURSE_TYPE}&ownerId={OWNER_ID}&limit={LIMIT}&ts={TS}
 - 请求方法：get

##### 返回内容

由于字段非常多，这里不做详细的内容解释。

```json
{
    "meta": {
        "total": string,
        "start": string,
        "size": string
    },
    "data": [
        {
            "id": string,
            "ownerId": string,
            "name": string,
            "courseId": string,
            "course": {
                "id": string,
                "title": string,
                "coursePicUrl": string,
                "editStatus": string,
                "isQuality": string,
                "courseManager": string,string,
                "courseType": string,
                "openType": string,
                "school": string,
                "userType": string,
                "status": string,
                "isBuild": string,
                "startDate": number,
                "endDate": number,
                "cmbody": {
                    "data": [
                        {
                            "id": string,
                            "title": string
                        },
                        {
                            "id": string,
                            "title": string
                        }
                    ]
                },
                "publishDate": string,
                "allSchool": string,
                "allSchoolId": string,
                "schema": string,
                "certId": string,
                "spocSchool": null,
                "spocSchoolTitle": null,
                "spocPhone": null,
                "endingView": number,
                "scoreRate": number,
                "rateUnit": number
            },
            "title": string,
            "created": number,
            "lastUpdated": number,
            "courseType": string,
            "username": string,
            "userInfo": {
                "username": string,
                "name": string,
                "gender": string,
                "speciality": string,
                "headimgurl": string,
                "email": string,
                "schoolName": string,
                "signNum": number,
                "staytime": number
            },
            "score": number,
            "status": string,
            "progress": string,
            "remarks": null,
            "body": [
                {
                    ...
                }
            ],
            "del": string,
            "pass": string,
            "openType": string,
            "learn": null,
            "classId": string,
            "classInfo": string,
            "classTitle": null,
            "forumNum": number,
            "testScore": number,
            "scoreBody": null,
            "score2": string,
            "chooseTime": number,
            "dropTime": null,
            "type": string,
            "tusername": null,
            "tInfo": null
        }
    ]
}
```

### lessons_api

lessons_api(self, course_id: str, start: int = 1, limit: int = 100) -> str

#### 功能描述

生成获取课程的API。

#### 参数

| 属性 | 类型 | 说明 |
| :-: | :-: | :-: |
|course_id|string|课程ID|
|start|int|起始位置，默认为1|
|limit|int|分页大小，默认值为100|

#### API信息

 - 地址：https://www.cqooc.com/json/mooc/lessons?limit={LIMIT}&start={START}&sortby={SORT_BY}&reverse={REVERSE}&courseId={COURSE_ID}&ts={TS}
 - 请求方法：get

##### 返回内容

```json
{
    "meta": {
        "total": string,
        "start": string,
        "size": string
    },
    "data": [
        {
            "id": string,
            "parentId": string,
            "chapter": {
                "id": string,
                "title": string,
                "status": string
            },
            "courseId": string,
            "category": string,
            "title": string,
            "resId": string,
            "resource": {
                "id": string,
                "title": string,
                "authorName": string,
                "resSort": string,
                "resMediaType": string,
                "resSize": string,
                "viewer": string,
                "oid": string,
                "username": string,
                "status": string,
                "resMediaType_lk_display": string,
                "pages": null,
                "newSourceID": string,
                "duration": string,
                "dimension": string,
                "resourceType_lk_display": string,
                "isVideo": string,
                "newSourceDIR": string
            },
            "testId": null,
            "test": string,
            "forumId": null,
            "forum": {
                "id": string,
                "title": string,
                "status": string,
                "content": string
            },
            "ownerId": string,
            "created": number,
            "lastUpdated": number,
            "owner": string,
            "chapterId": string,
            "selfId": string,
            "isLeader": string,
            "time": number
        }
    ]
}
```

### lessons_status_api

lessons_status_api(self, course_id: str, username: str, start: int = 1, limit: int = 100) -> str

#### 功能描述

生成获取任务状态的API。

#### 参数

| 属性 | 类型 | 说明 |
| :-: | :-: | :-: |
|course_id|string|课程ID|
|username|string|用户名|
|start|int|起始位置，默认为1|
|limit|int|分页大小，默认值为100|

#### API信息

 - 地址：https://www.cqooc.com/json/learnLogs?limit={LIMIT}&start={START}&courseId={COURSE_ID}&select={SECTION_ID}&username={USERNAME}&ts={TIMESTAMP}
 - 请求方法：get

##### 参考代码

```python
print(req.do_get(apiAddr, headers={
                    "Referer": "http://www.cqooc.com/learn/mooc/progress?id=334572045",
                    "host": "www.cqooc.com",
                }).text)
```

##### 返回内容

```json
{
    "meta": {
        "total": string,
        "start": string,
        "size": string
    },
    "data": [
        {
            "sectionId": string
        }
    ]
}
```

### mcs_id_api

mcs_id_api(self, owner_id: str, course_id: str) -> str

#### 功能描述

生成获取mcs_id的API。

#### 参数

| 属性 | 类型 | 说明 |
| :-: | :-: | :-: |
|owner_id|string|拥有该课程的用户ID，切勿和课程发布者ID混淆|
|course_id|string|课程ID|

#### API信息

 - 地址：https://www.cqooc.com/json/mcs?ownerId={OWNER_ID}&courseId={COURSE_ID}&ts={TIMESTAMP}
 - 请求方法：get

##### 参考代码

```python
apiAddr = api.mcs_id_api("0000", "0000")
print(apiAddr)
print(req.do_get(apiAddr, headers={
                    "Referer": "http://www.cqooc.com/my/learn",
                    "host": "www.cqooc.com",
                }).text)
```

##### 返回内容

```json
{
    "meta": {
        "total": string,
        "start": string,
        "size": string
    },
    "data": [
        {
            "id": string,
            "ownerId": string,
            "name": string,
            "courseId": string,
            "course": {
                "id": string,
                "title": string,
                "coursePicUrl": string,
                "editStatus": string,
                "isQuality": string,
                "courseManager": string,string,
                "courseType": string,
                "openType": string,
                "school": string,
                "userType": string,
                "status": string,
                "isBuild": string,
                "startDate": number,
                "endDate": number,
                "cmbody": {
                    "data": [
                        {
                            "id": string,
                            "title": string
                        }
                    ]
                },
                "publishDate": string,
                "allSchool": string,
                "allSchoolId": string,
                "schema": string,
                "certId": string,
                "spocSchool": null,
                "spocSchoolTitle": null,
                "spocPhone": null,
                "endingView": number,
                "scoreRate": number,
                "rateUnit": number
            },
            "title": string,
            "created": number,
            "lastUpdated": number,
            "courseType": string,
            "username": string,
            "userInfo": {
                "username": string,
                "name": string,
                "gender": string,
                "speciality": string,
                "headimgurl": string,
                "email": string,
                "schoolName": string,
                "signNum": number,
                "staytime": number
            },
            "score": number,
            "status": string,
            "progress": string,
            "remarks": null,
            "body": [
                {
                    "q137555": string,
                    "q137556": string
                }
            ],
            "del": string,
            "pass": string,
            "openType": string,
            "learn": null,
            "classId": string,
            "classInfo": string,
            "classTitle": null,
            "forumNum": number,
            "testScore": number,
            "scoreBody": null,
            "score2": string,
            "chooseTime": number,
            "dropTime": null,
            "type": string,
            "tusername": null,
            "tInfo": null
        }
    ]
}
```

### learn_log_api

learn_log_api(self, section_id: str, username: str) -> str

#### 功能描述

生成获取learn_log的api。

#### 参数

| 属性 | 类型 | 说明 |
| :-: | :-: | :-: |
|section_id|string|章节ID|
|username|string|用户名|

### exam_papers_api

exam_papers_api(self, course_id: str, start: int = 0, limit: int = 200) -> str

#### 功能描述

生成获取exam_papers的api。

#### 参数

| 属性 | 类型 | 说明 |
| :-: | :-: | :-: |
|course_id|string|课程ID|

#### API信息

 - 地址：https://www.cqooc.com/json/exam/papers?limit={LIMIT}&start={START}&courseId={COURSE_ID}&ts={TS}
 - 请求方法：get

##### 样例代码

```python
apiAddr = api.exam_papers_api("PARAM")
print(apiAddr)
print(req.do_get(apiAddr, headers={
                    "Referer": "http://www.cqooc.com/my/learn",
                    "host": "www.cqooc.com",
                }).text)
```

##### 返回内容

```json
{
    "meta": {
        "start": "string",
        "total": "string",
        "size": "string"
    },
    "data": [
        {
            "status": number,
            "submitEnd": number,
            "title": "string",
            "courseId": "string",
            "created": number,
            "number": number,
            "content": "string",
            "score": number,
            "parentId": "string",
            "id": number
        },
        ...
    ]
}
```

### exams_api

exams_api(self, course_id: str, start: int = 0, limit: int = 200) -> str

#### 功能描述

生成获取exams的API。

#### 参数

| 属性 | 类型 | 说明 |
| :-: | :-: | :-: |
|course_id|string|课程ID|

#### API信息

 - 地址：https://www.cqooc.com/json/exams?limit={LIMIT}&start={START}&courseId={COURSE_ID}&ts={TS}
 - 请求方法：get

##### 样例代码

```python
apiAddr = api.exams_api("PARAM")
print(apiAddr)
print(req.do_get(apiAddr, headers={
                    "Referer": "http://www.cqooc.com/my/learn",
                    "host": "www.cqooc.com",
                }).text)
```

##### 返回内容

```json
{
    "meta": {
        "total": "string",
        "start": "string",
        "size": "string"
    },
    "data": [
        {
            "id": number,
            "created": number,
            "ownerId": number,
            "title": "string",
            "courseId": "string",
            "parentId": null,
            "status": number,
            "submitEnd": number,
            "number": null,
            "content": "string",
            "score": number,
            "time": number,
            "answerTime": number
        }
    ]
}
```

### tasks_api

tasks_api(self, course_id: str, start: int = 0, limit: int = 200) -> str

#### 功能描述

生成获取任务列表的API。

#### 参数

| 属性 | 类型 | 说明 |
| :-: | :-: | :-: |
|course_id|string|课程ID|

#### API信息

 - 地址：https://www.cqooc.com/json/tasks?limit={LIMIT}&start={START}&courseId={COURSE_ID}&ts={TS}
 - 请求方法：

##### 样例代码

```python
apiAddr = api.tasks_api("PARAM")
print(apiAddr)
print(req.do_get(apiAddr, headers={
                    "Referer": "http://www.cqooc.com/my/learn",
                    "host": "www.cqooc.com",
                }).text)
```

##### 返回内容

```json
{
    "meta": {
        "start": "string",
        "total": "string",
        "size": "string"
    },
    "data": [
        {
            "courseId": "string",
            "pubClass": "string",
            "markDesc": "string",
            "id": "string",
            "markNum": "string",
            "isJudged": number,
            "lastUpdated": number,
            "noReview": number,
            "title": "string",
            "comments": null,
            "content": "HTMLstring",
            "score": number,
            "attachment": "string",
            "unitId": "string",
            "pubClassTitle": "string",
            "status": "string",
            "publishDate": number,
            "isMark": "string",
            "isPublish": number,
            "chapter": {
                "status": "string",
                "pubClass": "string",
                "id": "string",
                "title": "string"
            },
            "judgeEnd": number,
            "name": "string",
            "submitEnd": number,
            "created": number,
            "gradeId": null,
            "selfId": null
        }
    ]
}

```

### chapters_api

chapters_api(self, course_id: str, start: int = 0, limit: int = 200) -> str

#### 功能描述

生成获取章节内容的API。

#### 参数

| 属性 | 类型 | 说明 |
| :-: | :-: | :-: |
|course_id|string|课程ID|

#### API信息

 - 地址：https://www.cqooc.com/json/chapters?limit={LIMIT}&start={START}&courseId={COURSE_ID}&ts={TS}
 - 请求方法：get

##### 样例代码

```python
apiAddr = api.chapters_api("PARAM")
print(apiAddr)
print(req.do_get(apiAddr, headers={
                    "Referer": "http://www.cqooc.com/learn/mooc/progress?id=PARAM",
                    "host": "www.cqooc.com",
                }).text)
```

##### 返回内容

```json
{
    "meta": {
        "start": "string",
        "total": "string",
        "size": "string"
    },
    "data": [
        {
            "teachDesign": null,
            "importPointFileId": null,
            "courseId": "string",
            "pubClass": "string",
            "studyTime": null,
            "course": {
                "school": "string",
                "title": "string",
                "publishDate": "string",
                "spocPhone": null,
                "id": "string",
                "cmbody": {
                    "data": [
                        {
                            "id": "string",
                            "title": "string"
                        }
                    ]
                }
            },
            "skill": null,
            "isElective": number,
            "id": "string",
            "knowledge": null,
            "title": "string",
            "parentId": null,
            "atWeek": null,
            "pubClassTitle": "string",
            "originId": null,
            "status": "string",
            "permitChild": "string",
            "unitOwnType": null,
            "studyWeek": null,
            "isBuild": null,
            "lastUpdated": number,
            "courseType": "string",
            "level": "string",
            "desc": null,
            "chapter": null,
            "evaluateWay": null,
            "created": number,
            "selfId": number,
            "bookInfo": null,
            "teachTeachers": null,
            "time": number,
            "isPublish": number,
            "isLeader": "string"
        }
    ]
}

```

### skip_section_api

skip_section_api(self) -> str

#### 功能描述

获取跳过任务的API。

#### 参数

无。但是需要注意的是，参数实际上实在Referer字段中指定的。

#### API信息

 - 地址：https://www.cqooc.com/learnLog/api/add
 - 请求方法：get
