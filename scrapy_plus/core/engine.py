# coding=utf-8
from ..core.spider import Spider
from ..core.scheduler import Scheduler
from ..core.downloader import Downloader
from ..core.pipeline import Pipeline
from ..middlewares.downloader_middleware import DownloaderMiddleware
from ..middlewares.spider_middleware import SpiderMiddleware
from ..utils.log import logger
from datetime import datetime
from ..http.request import Request
from ..item import Item

class Engine(object):
    def __init__(self):
        self.spider = Spider()
        self.scheduler = Scheduler()
        self.downloader = Downloader()
        self.pipeline = Pipeline()
        self.downloader_mid = DownloaderMiddleware()
        self.spider_mid = SpiderMiddleware()

    def start(self):
        logger.info("Starting enging...")
        start = datetime.utcnow()
        logger.info("Start time: {}".format(start))
        self._start_engine()
        end = datetime.utcnow()
        time = (end - start).total_seconds()
        logger.info("End time: {}, duration: {}".format(end, time))

    def _start_engine(self):
        # 1. 从spider对象获得start_request
        for start_request in self.spider.start_request():
            # 2. 将request对象交给spider_mid对象处理
            start_request = self.downloader_mid.process_request(start_request)
            # 3. 将start_request 交给scheduler 去重，添加到请求队列
            self.scheduler.add_request(request)
        while True:
            # 4. 从scheduler对象中获得request对象
            request = self.scheduler.get_request()
            # 5. 通过downloader对象发送请求，并获得response对象
            response = self.downloader.get_response(request)
            # 6. 将response对象交给downloader_mid进行处理
            response = self.downloader_mid.process_response(response)
            # 7. 通过getattr()获得spider对象的回调函数
            parse_func = getattr(spider, request.callback)  # parse_func 是一个可迭代的生成器
            # 7. 将response交给spider处理，获得item或者request对象
            for item_or_request in parse_func(response):
                # 7.1 如果是request对象，执行下列语句
                if isinstance(item_or_request, Request):
                    # 7.1.1 将request对象交给spider_mid处理
                    request = self.spider_mid.process_request(item_or_request)
                    # 7.1.2 将request对象交给scheduler处理，去重，添加到请求队列
                    self.scheduler.add_request(request)
                # 7.2 如果是item对象，执行下列语句
                elif isinstance(item_or_request, Item):
                    # 7.2.1 将item对象交给spider_mid处理
                    item = self.spider_mid.process_item(item)
                    # 7.2.2 将item对象交给pipeline处理
                    item = self.pipeline.process_item(item)
                del(item)
