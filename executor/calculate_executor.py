from executor.abstract_executor import *


class CalculateExecutor(AbstractExecutor):

    def execute(self, args):
        print("got args:", str(args))
        return
