
import logging, sys

class AbstractExecutor(object):

    def __init__(self):
        logging.basicConfig(filename='log.log',filemode='w', level=logging.DEBUG)

    def execute(self, args):
        raise NotImplementedError()



