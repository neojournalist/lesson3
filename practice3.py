number1 = int(input('Enter your number: '))
number2 = int(input('Enter your second number: '))

if number1 == number2:
    print('Your numbers are equal')
    if number1 > number2:
        print('Your first number is bigger')
else:
    print('Your second number is bigger')


function = int(input('Enter your function number: 1. Sum 2. Subtraction 3. Multiplication'))

if function == 1:
    print('Result of function: ', number1 + number2)
elif function == 2:
    print('Result of function: ', number1 - number2)
elif function == 3:
    print('Result of function: ', number1 * number2)
else:
    print('Not defined')

# even or not even
number3 = int(input('Enter your number: '))

if number3 % 2 == 0:
    print('Your number is even')
else:
    print('Your number is not even')