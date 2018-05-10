from executor.abstract_executor import *


class NotValideExecutor(AbstractExecutor):

    def execute(self, args):
        return UrlErrorResponse
