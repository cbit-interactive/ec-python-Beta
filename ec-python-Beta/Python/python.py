choice = input('''
Please select the type of operation you want to perform:
/add for addition
/sub for subtraction
/mult for multiplication
/div for division
/help for help
/inf for program info
/com for Terminus 0.1
''')

while True:
    if choice == '+':
        num_1 = int(input('Enter your first number: '))
        num_2 = int(input('Enter your second number: '))
        print('{} + {} = '.format(num_1, num_2))
        print(num_1 + num_2)
 
    elif choice == '-':
        num_1 = int(input('Enter your first number: '))
        num_2 = int(input('Enter your second number: '))
        print('{} - {} = '.format(num_1, num_2))
        print(num_1 - num_2)
 
    elif choice == '*':
        num_1 = int(input('Enter your first number: '))
        num_2 = int(input('Enter your second number: '))
        print('{} * {} = '.format(num_1, num_2))
        print(num_1 * num_2)
 
    elif choice == '/':
        num_1 = int(input('Enter your first number: '))
        num_2 = int(input('Enter your second number: '))
        print('{} / {} = '.format(num_1, num_2))
        print(num_1 / num_2)
    elif choice == 'help':
        print('Commands: help command inf')
    elif choice == 'inf':
        print('Created using Python. Copyright 2022 IIAB')
        inf_cho = input(" ")
        if inf_cho == 'exit':
            while False:
                exit
 
    else:
        print('Enter a valid operator, please run the program again.')
