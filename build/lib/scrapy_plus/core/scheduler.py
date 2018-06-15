# coding=utf-8

# 根据py2和py3版本导入Queue
from six.moves.queue import Queue
from ..utils import logger

class Scheduler(object):
    def __init__():
        self.queue = Queue()
        self._filter_set = set()

    def add_request(self, request):
        """
        请求队列去重，添加请求到队列中
        """
        if request.url in self._filter_set:
            return
        else:
            self.queue.put(request)
            self._filter_set.add(request.url)

    def _filter_request(self, request):
        pass

    def get_request(self):
        try:
            return self.queue.get(False)
        except Exception as e:
            logging.error("The request queue is empty!")
