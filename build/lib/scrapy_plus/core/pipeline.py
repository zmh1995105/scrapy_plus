# encoding=utf-8

class Pipeline(object):
    def process_item(self, item):
        print("管道接收Item，{}".format(item.data))
        return item
