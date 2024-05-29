# Module: msg

## 概览

msg类是一个工具库，包含了一些用于处理API返回内容的函数。

## 内容

### 构造函数

`__init__(self)`

### processing

`processing(self, msg: str, code: int, res: dict = None) -> dict`

#### 功能描述

给定返回信息、返回代码和具体数据，将它们处理成统一格式的dict。

#### 参数

| 属性 | 类型 | 说明 |
| :-: | :-: | :-: |
|msg|string|返回信息|
|code|int|返回代码|
|res|dict|具体数据|
