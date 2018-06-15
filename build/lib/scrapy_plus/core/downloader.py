# encoding=utf-8

import requests
import chardet
from ..http.response import Response

class Downloader(object):
    def __init__(self):
        pass

    def get_response(self, request):
        """
        获得Request对象，通过请求方式构建请求，并且返回响应对象
        """
        if request.method.upper() == 'GET':
            response = requests.get(url=request.url, headers=request.headers,
                params=request.parmas)
        elif request.method.upper() == "POST":
            res = request.post(url=request.url, headers=request.headers,
                data=request.data)
        else:
            raise Exception("{}请求方式不支持！".format(request.method))

        encoding = chardet.detect(request.content)["encoding"]
        yield Response(res.url, res.status_code, res.content, encoding, request)
