# coding=utf-8

class SpiderMiddlerware(object):
    def process_request(self, request):
        logger.info("Spider middlerware is processing request.")
        return request

    def process_item(self, item):
        logger.info("Spider middleware is processing item.")
        return item
