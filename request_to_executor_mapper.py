from executor import calculate_executor
from executor import not_valid_executor
from collections import defaultdict

class RequestToExecutorMapper(object):


    def __init__(self):

        temp_dict = {
            "/calculate": calculate_executor.CalculateExecutor()
        }
        self.mapper = defaultdict(lambda: not_valid_executor.NotValideExecutor, temp_dict)

    def get_executor(self,executor_name):
        return self.mapper[executor_name]

