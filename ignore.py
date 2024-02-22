# number1 = int(input('put the 1st number:\n '))
# number2 = int(input('put the second number:\n '))
# operation = input('What operation do you want to do:\n ')
# if operation == 'add' and '+':
#      print(number1 + number2)
# elif operation == 'subtract' and '-':
#     print(number1 - number2)
# elif operation == 'multiplication' and '+':
#     print(number1*number2)
# elif operation == 'division' and '/':
#     print(number1 / number2)
# else:
#     print('want to do nothing!')  
def main(k, art):
    student_in_program = [i+1 for i, art in enumerate(art) if art == 1]
    student_in_maths = [i+1 for i, art in enumerate(art) if art == 2]
    sports = [i+1 for i, art in enumerate(art) if art == 3]
    if min_teams == 0:
        print(0)
    else:
        print(min_teams)
        for i in range(min_teams):
            team = [student_in_program[i], student_in_maths[i], sports[i]]
            print(team)