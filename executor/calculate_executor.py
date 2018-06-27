from executor.abstract_executor import *
import json

class CalculateExecutor(AbstractExecutor):

    BAD_OPERATION= "BAD OPERATION"

    def __operation(self,x,y,operation):
        if operation == '/' and  y == '0':
            return CalculateExecutor.BAD_OPERATION

        if operation == '+':
            result = float(x)+float(y)
        if operation == '-':
            result = float(x)-float(y)
        if operation == '*':
            result = float(x)*float(y)
        if operation == '/' and not y == '0' :
            result = float(x)/float(y)
        result = str(result)
        #print("result is: "+result)
        # result is float so it has '.' in it
        splitted = result.split('.')
        right_to_dot= splitted[1]
        if int(right_to_dot) == 0:
            result= splitted[0]
        #print("returning result: " + result)
        return result

    def __concat_numbers(self,x,y):
        '''
        gets two numbers as strings
        :param x: first number, for example 56
        :param y: second number, for exmple 6
        :return: 566
        '''
        if x== '':
            return y
        x=float(x)
        splitted_x=str(x).split('.')
        #got 01 => 1
        if int(splitted_x[0]) == 0 and int(splitted_x[1]) == 0:
            return y
        return str(int(x))+str(int(y))


    def __is_operator(self, input):
        return input in ['+', '-', '/', '*']

    def __is_equal_sign(self, input):
        return input == '='

    def __is_number(self, input):
        return str.isdigit(input)

    def __handle_first_interaction(self,input,restart=False):
        # first interaction with user
        first_number = '0'
        operator = None
        if not restart and self.__is_operator(input) or self.__is_equal_sign(input):
            display = '0'
            if self.__is_operator(input):
                operator = input
        else:
            display = input
            first_number = input
        return {'status':'success','display': display, 'operator': operator, 'first_number': first_number, 'second_number': ''}

    def __handle_interaction(self,input,state):

        #if got bad operation last time, restart calculator
        if state['display'] == CalculateExecutor.BAD_OPERATION:
            if self.__is_number(input):
                return self.__handle_first_interaction(input,restart=True)
            else:
                return state

        #after last time got equal sign. were first number exists and second number doesn't.
        #if input is a number, override the number
        #0
        if (not state['operator'] is None) and (self.__is_equal_sign(state['operator'])) and  not self.__is_operator(input)\
                and not self.__is_equal_sign(input):
            logging.debug('entered to  0\n')
            return self.__handle_first_interaction(input,restart=True)


        # not in a middle of operation & got an operation (it's not first interaction so we assume first_number!=None)
        # 55 and got + => 55+
        #1
        if state['operator'] is None and self.__is_operator(input):
            logging.debug('entered to  1')
            return {'status':'success','display': state['first_number'], 'operator': input, 'first_number': state['first_number'],
                    'second_number': ''}
        # not in a middle of operation & got a number, concat to previous number
        # 55 and got 6 => 556
        # 2
        if state['operator'] is None and not (self.__is_operator(input) or self.__is_equal_sign(input)):
            logging.debug('entered to 2')
            first_number = self.__concat_numbers(state['first_number'] , input)
            return {'status':'success','display': first_number, 'operator': None, 'first_number': first_number, 'second_number': ''}
        # not in a middle of operation & got =
        # 55 and got = => 55
        # 3
        if state['operator'] is None and self.__is_equal_sign(input):
            logging.debug('entered to 3')
            return {'status':'success','display': state['first_number'], 'operator': '=',
                    'first_number': state['first_number'],'second_number': ''}
        # in a middle of operation & got a number
        # 55+ and got 6 => 55+6
        # 4
        if (not state['operator'] is None) and not (self.__is_equal_sign(input) or self.__is_operator(input)):
            logging.debug('entered to 4')
            second_number = self.__concat_numbers(state['second_number'] , input)
            return {'status':'success','display':second_number, 'operator': state['operator'],
                    'first_number': state['first_number'], 'second_number': second_number}
        # in a middle of operation & got an operation & second number is ''
        # 55+ and got - => 55-
        # 5
        if (not (state['operator'] is None)) and self.__is_operator(input) and state['second_number']=='':
            logging.debug('entered to 5')
            return {'status':'success','display': state['first_number'], 'operator': input,
                    'first_number': state['first_number'], 'second_number': state['second_number']}
        # in a middle of operation & got an operation & second number exist
        #55+6 and got - => 61-
        # 6
        if (not (state['operator'] is None)) and self.__is_operator(input) and not state['second_number'] == '':
            logging.debug('entered to 6')
            first_number=self.__operation(state['first_number'],state['second_number'],state['operator'])
            return {'status':'success','display': first_number, 'operator': input,
                    'first_number': first_number, 'second_number': ''}
        # in a middle of operation & got equal sign & second number exist
        #55+6 and got = => 61
        # 7
        if (not (state['operator'] is None)) and self.__is_equal_sign(input) and not state['second_number'] == '':
            logging.debug('entered to 7')
            first_number = self.__operation(state['first_number'], state['second_number'], state['operator'])
            # possible dividing by zero
            return {'status':'success','display': first_number, 'operator': '=',
                    'first_number':first_number, 'second_number': ''}
        # in a middle of operation & got equal sign & second number is ''
        #55+ and got = => 55
        # 8
        if (not (state['operator'] is None)) and self.__is_equal_sign(input) and  state['second_number'] == '':
            logging.debug('entered to 8')
            return {'status':'success','display': state['first_number'], 'operator': '=',
                    'first_number': state['first_number'], 'second_number': ''}



    def execute(self, args):
        input=args['input']


        if not 'calculatorState' in args.keys():
            return self.__handle_first_interaction(input)
        else:
            state = args['calculatorState']
            return self.__handle_interaction(input,state)

        return
