# coding=utf-8

class DownloaderMiddlerware(object):
    def process_request(self, request):
        logger.info("Downloader middlerware is processing request.")
        return request

    def process_response(self, response):
        logger.info("Downloader middleware is processing response.")
        return response
