from executor.abstract_executor import *


class ClaculateExecutor(AbstractExecutor):

    def execute(self, args):
        print("got args:", str(args))
        return
