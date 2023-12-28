## 概览
core是一个公开可用的类，其中包含一些网站操作的函数。创建一个core对象必须提供网站的用户名和密码。

- 覆盖模块：core.py

- 最后更新时间：2023/07/09

- 作者：Fatpandac, Xtao

## 内容

### 构造函数

`__init__(username: str = "", pwd: str = "", cookie: str = None) -> None`

#### 功能描述

创建一个core对象，保存参数中的用户名和密码，也可以使用cookie登录。之后你需要先进行`login()`操作，然后才可以使用对象上的函数。

#### 参数

| 参数名 | 类型 | 说明 |
| :-: | :-: | :-: |
|username|string|用户的用户名。|
|pwd|string|用户的登陆密码。|
|cookie|string|登陆网站之后产生的cookie，其名称为xsid。注意，不同session下产生的xsid不同，你不应当从浏览器的开发者工具中取得xsid进行登录。|

#### 示例代码

```python
from hackcqooc.core import Core
# 使用用户名和密码
core = Core("10611100000000", "password")
# 使用cookie
core = Core(cookie = "XXXXXXXXXXXXXXXX")
```


### login

`login() -> dict`

#### 功能描述

尝试进行登录。为了进行登录过程，core示例中应当保存有可以用于登录的信息。如果出现登录不成功的结果，可能是cqooc的风控策略导致，此时需要在浏览器中先进行一次手动登录。

#### 参数

无。

#### 返回值

返回内容为JSON，其中包含的字段如下。

| 属性 | 类型 | 说明 |
| :-: | :-: | :-: |
|code|number|错误信息。为20时表示登陆成功，为400时表示登陆失败。|
|status|string|状态信息|
|msg|string|错误信息|
|xsid|string|仅限登陆成功后获取，为cookie中xsid的值。|


#### 示例代码

```
core = Core("10611100000000", "iampassword")
core.login()
```

```json
{'status': 'ok', 'code': 200, 'xsid': '000000000000000', 'msg': '登录成功'}
```

### get_user_info

get_user_indo() -> dict

#### 功能描述

获取当前登录用户的用户信息。

#### 参数

无。

#### 返回值

```json
{'xsid': '000000000000000', 'id': 0000000, 'username': '00000000000000000', 'pwd': 'xxx', 'name': 'xxx', 'mcs_id': None, 'course_data': None, 'lessons_data': None, 'code': 200, 'status': 'ok', 'msg': '登录成功'}
```

| 属性 | 类型 | 说明 |
| :-: | :-: | :-: |
|xsid|string |学生ID。|
|id|number||
|username|string|用户名|
|pwd|string|用户密码|
|name|string|真实姓名|
|mcs_id|string||
|course_data|dict||
|lesson_data|dict||
|code|number|状态码|
|status|string|状态信息|
|msg|string|状态信息|

### get_course

get_course() -> dict

#### 描述

获取用户选课内容

#### 参数

无。

#### 返回值

| 属性 | 类型 | 说明 |
| :-: | :-: | :-: |
|meta|dict|meta信息|
|data|dict|课程数据|
|code|number|状态码|
|status|string|状态信息|
|msg|string|状态信息|

课程数据
| 属性 | 类型 | 说明 |
| :-: | :-: | :-: |
|courseId|dict|课程ID|
|ownerId|dict|拥有者ID|
|title|number|标题|

meta信息
| 属性 | 类型 | 说明 |
| :-: | :-: | :-: |
|total|string|总数|
|start|string|起始位|
|size|string|总数|


### get_course_lessons

get_course_lessons(course_id: str) -> dict

#### 描述

获取给定课程ID的课程信息。

#### 参数

| 属性 | 类型 | 说明 |
| :-: | :-: | :-: |
|course_id|string|课程ID|

#### 返回值

| 属性 | 类型 | 说明 |
| :-: | :-: | :-: |
|meta|dict|meta信息|
|data|list|课程数据|
|code|number|状态码|
|status|string|状态信息|
|msg|string|状态信息|

meta信息
| 属性 | 类型 | 说明 |
| :-: | :-: | :-: |
|total|string|总数|
|start|string|起始位|
|size|string|总数|

课程数据
| 属性 | 类型 | 说明 |
| :-: | :-: | :-: |
|title|string|标题|
|sectionId|string|节ID|
|cateory|string|类|
|chapterId|string|章节ID|
|ownerId|string|拥有者ID|
|parentId|string|父级ID|
|id|string|ID|
|username|string|用户名|
|status|string|状态|

### skip_section

skip_section(section_id: str) -> dict

#### 描述

跳过sectionId对应的课程。

#### 参数

| 属性 | 类型 | 说明 |
| :-: | :-: | :-: |
|section_id|string|课程id|

#### 返回值

```json
{'code': 200, 'status': 'ok', 'msg': '跳过课程成功'}
```

| 属性 | 类型 | 说明 |
| :-: | :-: | :-: |
|code|number|状态码|
|status|string|状态信息|
|msg|string|状态信息|

### get_exam_papers_info

get_exam_papers_info(course_id: str, start: int = 0, limit: int = 200) -> dict

#### 描述

获取课程的测验内容。

#### 参数

| 属性 | 类型 | 说明 |
| :-: | :-: | :-: |
|course_id|string|课程ID|
|start|number|起始位，默认值为0|
|limit|number|限制，默认值为200|

#### 返回值

| 属性 | 类型 | 说明 |
| :-: | :-: | :-: |
|meta|dict|meta信息|
|data|dict|测验数据|
|code|number|状态码|
|status|string|状态信息|
|msg|string|状态信息|

测验数据
| 属性 | 类型 | 说明 |
| :-: | :-: | :-: |
|id|number||
|created|number|创建时间|
|ownerId|number|拥有者ID|
|title|string|标题|
|courseId|string|课程ID|
|parentId|string|父级ID|
|status|string|状态|
|submitEnd|number|提交截止时间|
|number|number||
|content|string|内容|
|score|number|分值|

### get_exams_info

get_exams_info(course_id: str, start: int = 0, limit: int = 200) -> dict

#### 描述

获取课程的考试内容。

#### 参数

| 属性 | 类型 | 说明 |
| :-: | :-: | :-: |
|course_id|string|课程ID|
|start|number|起始位，默认值为0|
|limit|number|限制，默认值为200|

#### 返回值

| 属性 | 类型 | 说明 |
| :-: | :-: | :-: |
|meta|dict|meta信息|
|data|dict|测验数据|
|code|number|状态码|
|status|string|状态信息|
|msg|string|状态信息|

测验数据
| 属性 | 类型 | 说明 |
| :-: | :-: | :-: |
|id|number||
|created|number|创建时间|
|ownerId|number|拥有者ID|
|title|string|标题|
|courseId|string|课程ID|
|parentId|string|父级ID|
|status|string|状态|
|submitEnd|number|提交截止时间|
|number|number||
|content|string|内容|
|score|number|分值|
|time|number|时间|
|answerTime|number|完成时间|

### get_tasks_info

get_tasks_info(course_id: str, start: int = 0, limit: int = 200) -> dict\

#### 描述

获取课程的作业列表。

#### 参数

| 属性 | 类型 | 说明 |
| :-: | :-: | :-: |
|course_id|string|课程ID|
|start|number|起始位，默认值为0|
|limit|number|限制，默认值为200|

#### 返回值

| 属性 | 类型 | 说明 |
| :-: | :-: | :-: |
|meta|dict|meta信息|
|data|dict|作业数据|
|code|number|状态码|
|status|string|状态信息|
|msg|string|状态信息|

作业数据
| 属性 | 类型 | 说明 |
| :-: | :-: | :-: |
|id|number||
|title|string|标题|
|unitId|string|单元ID|
|chatper|dict|章节数据|
|courseId|string|课程ID|
|gradeId|unknown|评分ID|
|submitEnd|number|提交截止时间|
|judgeEnd|number|评分截止时间|
|publishDate|number|发布时间|
|score|number|分值|
|content|string|内容|
|isMark|string|是否mark|
|markNum|string|mark数量|
|markDesc|string|mark描述|
|attatchment|string|附件|
|ownerId|number|拥有者ID|
|name|string|姓名|
|created|number|创建时间|
|lastUpdated|number|上次更新时间|
|status|string|状态|
|comments|unknown|评注|
|noReview|number||
|isJudged|number|是否已评判|
|pubClass|string||
|pubClassTitle|string||
|isPublish|number|发布状态|

章节数据
| 属性 | 类型 | 说明 |
| :-: | :-: | :-: |
|id|string||
|title|string|标题|
|status|string|状态|
|pubClass|string||

### get_chapters_info

get_chapters_info(course_id: str, start: int = 0, limit: int = 200) -> dict

#### 描述

获取章节数据信息。

#### 参数

| 属性 | 类型 | 说明 |
| :-: | :-: | :-: |
|course_id|string|课程ID|
|start|number|起始位，默认值为0|
|limit|number|限制，默认值为200|

#### 返回值

| 属性 | 类型 | 说明 |
| :-: | :-: | :-: |
| teachDesign | null |  |
| importPointFileId | null |  |
| courseId | string | 课程ID |
| pubClass | string |  |
| studyTime | null |  |
| course | object | 包含以下子属性 |
| -school | string | 学校 |
| -title | string | 标题 |
| -publishDate | string | 发布时间 |
| -spocPhone | null |  |
| -id | string | id |
| -cmbody | object | 包含以下子属性 |
| --data | array | 包含以下子属性 |
| ---id | string | id |
| ---title | string | 姓名 |
| skill | null |  |
| isElective | number | 是否可选 |
| id | string | id |
| knowledge | null |  |
| title | string | 标题 |
| parentId | null | 父级ID |
| atWeek | null |  |
| pubClassTitle | string |  |
| originId | string | 原始ID |
| status | string | 状态 |
| permitChild | string |  |
| unitOwnType | null |  |
| studyWeek | null | 学习周次 |
| isBuild | string |  |
| lastUpdated | number | 最近更新时间 |
| courseType | string | 课程类型 |
| level | string |  |
| desc | null | 描述 |
| chapter | null | 章节 |
| evaluateWay | null | 测评方式 |
| created | number | 创建时间 |
| selfId | number |  |
| bookInfo | null | 书籍信息 |
| teachTeachers | null | 授课教师 |
| time | number | 时间 |
| isPublish | number | 发布状态 |
| isLeader | string |  |

