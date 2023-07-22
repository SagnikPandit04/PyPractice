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
elif question == 'pineapple':
    print('pineapple is ok but you need to choose between apple or orange or banana')
else:
    print('if you do not want to choose it is ok')
