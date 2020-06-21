def welcome():
    print('''Welcome to Python Calculator''')

#Define our function
def calculate():

    operation = input(''' 
    Please type in the math operation you woul like to complete:
    + for addition
    - for substraction
    * for multiplication
    / for division
    ** for power
    % for modulo
    ''' )




    number_1 = int(input("Enter your first number: "))
    number_2 = int(input("Enter your second number: "))

    #Addition
    if operation == '+':
        print("{} + {} = " .format(number_1, number_2))
        print(number_1 + number_2)

    #Subtraction
    elif operation == '-':
        print('{} - {} = ' .format(number_1, number_2))
        print(number_1 - number_2)

    #Multiplication
    elif operation == '*':
        print('{} * {} = ' .format(number_1, number_2))
        print(number_1 * number_2)

    #Division
    elif operation == '/':
        print('{} / {} = ' .format(number_1, number_2))
        print(number_1 / number_2)

    #Power
    elif operation == '**':
        print('{} ** {} = ' .format(number_1, number_2))
        print(number_1 ** number_2)

    #Modulo
    elif operation == '%':
        print('{} % {} = ' .format(number_1, number_2))
        print(number_1 % number_2)

    else:
        print('You have not typed a valid operator, please run the program again.')

    again()

#Define again() function to ask user if they want to use the claculator again
def again():

    #take input from user
    calc_again = input(''' 
    Do you want to calculate again?
    Please type Y for YES or N for NO.''')

    #If user types Y, run the calculate() function
    if calc_again.upper() == 'Y':
        calculate()

    #If user types N, say good-bye to the user and end the progam
    elif calc_again.upper() == 'N':
        print('See you later.')

    #If user types another key, run the function again 
    else: 
        again()

welcome()
#Call calculate() outside of the function
calculate()