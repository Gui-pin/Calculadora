operation = input('''Plase type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
\n''')

number_1 = int(input('\nEnter your first number: '))
number_2 = int(input('\nEnter your second number: '))

if operation == '+':
    print('\n{} + {} = {}'.format(number_1, number_2, number_1+number_2))
elif operation == '-':
    print('\n{} - {} = {}'.format(number_1, number_2, number_1-number_2))
elif operation == '*':
    print('\n{} * {} = {}'.format(number_1, number_2, number_1*number_2))
elif operation == '/':
    print('\n{} / {} = {}'.format(number_1, number_2, number_1/number_2))
else:
    print('You have not typed a valid operator, please run the program again.')
