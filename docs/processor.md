# Module: processor

## 概览

这个模块包含了一些处理cqooc请求返回内容的函数。cqooc的返回内容较多，包含一些当前环境下不使用的数据，可以使用这里的函数进行处理。

## 内容

### process_course_data

```py
@staticmethod
def process_course_data(course_res: requests.Response) -> dict
```

#### 功能描述

`process_course_data`是一个静态函数，接收一个名为`course_res`的`requests.Response`包含有关课程数据的信息的HTTP响应。函数从HTTP响应中提取一些字段，并依次添加到一个字典类型的对象并返回。

#### 参数

|参数名称|类型|说明|
| :-: | :-: | :-: |
|course_res|requests.Response|使用requests进行HTTP请求得到的返回对象，包含课程内容|

#### 返回内容

字典内的字段如下：

|参数名称|类型|说明|
| :-: | :-: | :-: |
|meta|dict|这部分内容和原本响应内容的meta部分相同|
|data|list[dict]|字典列表，每个字典包含一个课程数据|

课程数据字典字段如下：

|参数名称|类型|说明|
| :-: | :-: | :-: |
|courseId|string|课程ID|
|ownerId|string|课程拥有者ID|
|title|string|课程标题|

---

### process_lessons_data

```py
@staticmethod
def process_lessons_data(username: str,lessons_res_meta: dict,
lessons_res_data: List,lessons_status_res_data: List,) -> dict
```

#### 功能描述

和前面类似，这个函数是用于处理课时数据的函数。处理完成的数据以字典的形式返回。

#### 参数

|参数名称|类型|说明|
| :-: | :-: | :-: |
|username|string||
|lesson_res_meta|dict||
|lesson_res__data|list||
|lesson_status_res_data|list||

#### 返回内容

字典内的字段如下：

|参数名称|类型|说明|
| :-: | :-: | :-: |
|meta|dict|这部分内容和原本响应内容的meta部分相同|
|data|list[dict]|字典列表，每个字典包含一个课时数据|

---

### process_section_data

```py
@staticmethod
def process_section_data(section_data: dict, mcs_id: str) -> dict
```

#### 功能描述

和前面类似，这个函数是用于处理章节数据的函数。处理完成的数据以字典的形式返回。

#### 参数

|参数名称|类型|说明|
| :-: | :-: | :-: |
|section_data|dict||
|mcs_id|string||

#### 返回内容

字典内的字段如下：

|参数名称|类型|说明|
| :-: | :-: | :-: |
|action|int||
|category|int||
|chapterId|string||
|courseId|string||
|ownerId|int||
|parentId|string||
|sectionId|string||
|username|string||
