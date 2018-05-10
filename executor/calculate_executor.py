from executor.abstract_executor import *
import json

class CalculateExecutor(AbstractExecutor):

    def __operation(self,x,y,operation):
        if operation == '+':
            return str(int(x)+int(y))
        if operation == '-':
            return str(int(x)-int(y))
        if operation == '*':
            return str(int(x)*int(y))
        if operation == '/' and not y == '0' :
            return str(int(x)/int(y))
        if operation == '/' and  y == '0':
            return "BAD OPERATION"



    def __is_operator(self, input):
        return input in ['+', '-', '/', '*']

    def __is_equal_sign(self, input):
        return input == '='

    def __handle_first_interaction(self,input):
        # first interaction with user
        first_number = '0'
        operator = None
        if self.__is_operator(input) or self.__is_equal_sign(input):
            display = '0'
            if self.__is_operator(input):
                operator = input
        else:
            display = input
            first_number = input
        return {'display': display, 'operator': operator, 'first_number': first_number, 'second_number': ''}

    def __handle_interaction(self,input,state):
        # not in a middle of operation & got an operation (it's not first interaction so we assume first_number!=None)
        # 55 and got + => 55+
        if state['operator'] is None and self.__is_operator(input):
            return {'display': state['first_number'], 'operator': state['operator'], 'first_number': state['first_number'],
                    'second_number': ''}
        # not in a middle of operation & got a number, concat to previous number
        # 55 and got 6 => 556
        if state['operator'] is None and not (self.__is_operator(input) or self.__is_equal_sign(input)):
            first_number = state['first_number'] + input
            return {'display': first_number, 'operator': None, 'first_number': first_number, 'second_number': ''}
        # not in a middle of operation & got =
        # 55 and got = => 55
        if state['operator'] is None and self.__is_equal_sign(input):
            return {'display': state['first_number'], 'operator': None,
                    'first_number': state['first_number'],'second_number': ''}
        # in a middle of operation & got a number
        # 55+ and got 6 => 55+6
        if (not state['operator'] is None) and not (self.__is_equal_sign(input) or self.__is_operator(input)):
            second_number = state['second_number'] + input
            return {'display': state['second_number'], 'operator': state['operator'],
                    'first_number': state['first_number'], 'second_number': state['second_number']}
        # in a middle of operation & got an operation & second number is ''
        # 55+ and got - => 55-
        if (not (state['operator'] is None)) and self.__is_operator(input) and state['second_number']=='':
            return {'display': state['second_number'], 'operator': state['operator'],
                    'first_number': state['first_number'], 'second_number': state['second_number']}
        # in a middle of operation & got an operation & second number exist
        #55+6 and got - => 61-
        if (not (state['operator'] is None)) and self.__is_operator(input) and not state['second_number'] == '':
            first_number=self.__operation(state['first_number'],state['second_number'],state['operation'])
            #possible dividing by zero
            if first_number is "BAD OPERATION":
                return "BAD OPERATION"
            return {'display': first_number, 'operator': state['operator'],
                    'first_number': state['first_number'], 'second_number': ''}
        # in a middle of operation & got equal sign & second number exist
        #55+6 and got = => 61
        if (not (state['operator'] is None)) and self.__is_equal_sign(input) and not state['second_number'] == '':
            first_number = self.__operation(state['first_number'], state['second_number'], state['operation'])
            # possible dividing by zero
            if first_number is "BAD OPERATION":
                return "BAD OPERATION"
            return {'display': first_number, 'operator': None,
                    'first_number': state['first_number'], 'second_number': ''}
        # in a middle of operation & got equal sign & second number is ''
        #55+ and got = => 55
        if (not (state['operator'] is None)) and self.__is_equal_sign(input) and not state['second_number'] == '':
            return {'display': state['first_number'], 'operator': None,
                    'first_number': state['first_number'], 'second_number': ''}


    def execute(self, args):
        print("got args:", str(args))
        state_from_client=json.load(args)
        input=state_from_client['input']
        state=state_from_client['rates']

        if state == {}:
            return self.__handle_first_interaction(input)
        else:
            return self.__handle_interaction(input,state)

        return
