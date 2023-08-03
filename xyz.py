def main():
    number1 = int(input('put the 1st number:\n '))
    number2 = int(input('put the second number:\n '))
    operation = input('What operation do you want to do:\n ')
    if operation == 'add':
        print(number1 + number2)
    elif operation == 'subtract':
        print(number1 - number2)
    elif operation == 'multiplication':
        print(number1*number2)
    elif operation == 'division':
        print(number1 / number2)
    else:
        print('want to do nothing!')  


        main() 

