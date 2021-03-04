a = 0
b = 0
while a == 0:
    try:
        a = int(input('Please enter a value for alpha (suggest a = 0):\n'))
    except ValueError:
        print('Please enter an integer number')
while b == 0:
    try:
        b = int(input('Please enter a value for beta (suggest b = -1):\n'))
    except ValueError:
        print('Please enter an integer number')
