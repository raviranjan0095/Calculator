import math
import logging
logging.basicConfig(level=logging.INFO)


class BasicCalculator():
    
    def __init__(self, first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num
        
    def add(self):
        '''Takes two numbers, Return the sum of these numbers'''
        return self.first_num + self.second_num    
        
    def sub(self):
        '''Takes two numbers, Return the difference of these numbers'''
        return self.first_num - self.second_num
    
    def multiply(self):
        '''Takes two numbers, Return the multiplication of these numbers'''
        return self.first_num * self.second_num
    
    def divide(self):
        '''Takes two numbers, Return the division of these numbers'''
        try:
            return self.first_num / self.second_num
        except Exception as error:
            logging.error(error)
            return error


class ScientifCalculator(BasicCalculator):
    
    def __init__(self, num):
        # self.num = num
        self.num = math.radians(num)  # Convert angle x from degrees to radians
    
    def sin(self):
        '''Takes in a number x, Return the sine of x radians'''
        return math.sin(self.num)
    
    def cos(self):
        '''Takes in a number x, Return the cosine of x radians'''
        return math.cos(self.num)
    
    def tan(self):
        '''Takes in a number x, Return the tangent of x radians'''
        return math.tan(self.num)


while True:
    
    def choose_calculator_type():
        calculator_type = ('1. Basic calculator \n2. Scientific calculator') 
        print(calculator_type)
    choose_calculator_type()
    
    try:
        choice = int(input('Please select calculator type :'))  # Take input from user
    except Exception as error:
        logging.error(error)
                
    if choice == 1:
        try:
            first_num = float(input('Enter First number : '))  # Take input from user
            second_num = float(input('Enter Second number : '))  # Take input from user
        except Exception as error:
            logging.error(error)
        
        obj=BasicCalculator(first_num, second_num)
        
        def choose_operation():
            operations = ('1. Add \n2. Sub \n3. Multiply \n4. Divide') 
            print(operations)
            
        choose_operation()
        
        try:
            choice = int(input('Please select operation : '))  # Take input from user
        except Exception as error:
            logging.error(error)
        
        if choice == 1:
            print("Result: ",obj.add())
        elif choice == 2:
            print("Result: ",obj.sub())
        elif choice == 3:
            print("Result: ",obj.multiply())    
        elif choice == 4:
            print("Result: ",obj.divide())
        else:
            print('Invalid option')
            logging.warning('Invalid option')
            break
            
    elif choice == 2:
        num = float(input('Enter a number : '))  # Take input from user
        obj=ScientifCalculator(num)
        
        def choose_operation():
            operations = ('1. sin \n2. cos \n3. tan') 
            print(operations)
            
        choose_operation()
        
        choice = int(input('Please select operation :'))  # Take input from user
        if choice == 1:
            print("Result: ",obj.sin())
        elif choice == 2:
            print("Result: ",obj.cos())
        elif choice == 3:
            print("Result: ",obj.tan())    
        else:
            print('Invalid option')
            logging.warning('Invalid option')
            break