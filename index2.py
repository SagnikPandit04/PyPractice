apple = 'it has vitamin A'
orange = 'it has citric acid'
banana = 'it has vitamin b'
question = input('What is your favourite fruit?\n ')
if question == 'apple':
    print(apple)
elif question == 'orange':
    print(orange)
elif question == 'banana':
    print(banana)
else:
    print('you do not have favourite fruit')