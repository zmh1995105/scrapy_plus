# coding=utf-8
from ..http.request import Request
from ..item import Item

class Spider(object):
    start_urls = []

    def start_request(self):
        """
        构建请求对象，返回请求对象列表
        """
        start_requests_list = []
        if start_urls:
            for start_url in start_urls:
                start_requests_list.append(Request(start_url))
        else:
            raise Exception("Start_urls cannot be empty!")
        yield start_requests_list

    def parse(self, response):
        data = response.body
        yield Item(data)
