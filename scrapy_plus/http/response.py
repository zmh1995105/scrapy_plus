# coding=utf-8

class Response(object):

    def __init__(self, url, status_code, headers, body, encoding, request):
        self.url = url
        self.status_code = status_code  # 状态码
        self.headers = headers  # 响应头
        self.body = body  # 响应体
        self.encoding = encoding  # 解码方式
        self.request = request  # 请求对象
