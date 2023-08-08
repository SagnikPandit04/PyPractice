def main():
    number1 = int(input('put the 1st number:\n '))
    number2 = int(input('put the second number:\n '))
    operation = input('What operation do you want to do:\n ')
    if operation == 'add' and '+':
        print(number1 + number2)
    elif operation == 'subtract' and '-':
        print(number1 - number2)
    elif operation == 'multiplication' and '+':
        print(number1*number2)
    elif operation == 'division' and '/':
        print(number1 / number2)
    else:
        print('want to do nothing!')  

#  Here i used all the operators sign to make it more elaborately
# here we cannot use the words and, or
