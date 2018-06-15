# coding=utf-8

class Request(object):
    def __init__(self, url, headers=None, params=None, data=None, method="GET", callback="parse"):
        self.url = url  # 请求地址
        self.headers = headers  # 请求头
        self.params = params  # 查询字符串
        self.callback = callback  # 回调函数
        self.method = method  # 请求方式
        self.data = data  # 提交的表单数据
