# Module: test

## 概览

test模块是一个使用js2py生成的模块，其中包含了一些cqooc网站中使用到的JavaScript加密函数。由于这些函数不能轻易转写为Python版本，所以使用了js2py来进行转换，这也导致了这个模块的调用方式和平常存在区别，其代码也无法提供阅读。

这个模块和其他的模块略有差异。test对外暴露的仅有test变量，你需要通过这个变量来调用js2py转写的JavaScript函数。

## 内容

### cnonce

#### 功能描述

生成cnonce值。cnonce在cqooc中有时会作为参数来使用。

#### 参数

无。

#### 参考代码

```python
from hackcqooc.test import test

test.cnonce()
>>>'3BC581F7ACB3E16D'
```

---

### getEncodePwd

#### 功能描述

生成经过编码处理的密码。

#### 参数

|参数名称|类型|说明|
| :-: | :-: | - |
|param1（暂定，实际上没有参数名）|string|待编码处理的文本|

#### 参考代码

```python
# 下面代码来自core.py，函数__login_by_pwd
data = nonce_res.json()
cn = test.cnonce()
login_hash = test.getEncodePwd(
    data["nonce"] + test.getEncodePwd(self.__user.get_pwd()) + cn
)
```
