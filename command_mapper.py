from executor import calculator_executor


class CommandMapper(object):
    mapper = {
        "calculate": calculator_executor.ClaculateExecutor
    }

    @classmethod
    def execute(cls, executor_name, args):
        return cls.mapper[executor_name].execute(args)
