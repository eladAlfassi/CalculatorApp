import sys
sys.path.insert(0, '/app')
from executor import calculate_executor
from collections import defaultdict

class RequestToExecutorMapper(object):


    def __init__(self):

        temp_dict = {
            "/calculate": calculate_executor.CalculateExecutor()
        }
        self.mapper = defaultdict(None,temp_dict)

    def get_executor(self,executor_name):
        return self.mapper[executor_name]

