﻿# actually, system unable to recorgnise user_input
user_input = "yes"
print("CALCULATOR_2.0_\n", "General instruction\n",
      ">>1. You don't have to give input in shortform/expanded form\n",
      ">>2. You have to choose and give input according to instruction you gave before giving input\n",
      ">>3. if you give input in wrong way the program could be stop running\n",
      ">>4. instruction will given in a bracket ()\n",
      ">>5. warning is written in square bracket '[]'\n")
# whenever user is want to calculate numbers it will continue
while user_input != "no":
    # Collecting data from user(input)
    user_want = input("What you want to do? (calculate/findsomeval)\n")
    if user_want == "calculate":
        # for first number
        firstnum = float(input("Enter first number (~Only enter number not alphabet)\n"))

        # for second number
        secondnum = float(input("Enter second number (~Only enter number not alphabet)\n"))

        # for operator
        operaor = input("Enter operator, options:- +,-,*,/ or plus,minus,multiply,divide\n")
        
        # for plus
        if operaor == "+" or operaor == "plus":
            print(firstnum + secondnum)

        # for minus
        elif operaor == "-" or operaor == "minus":
            print(firstnum - secondnum)

        # for divide
        elif operaor == "/" or operaor == "divide":
            print(firstnum / secondnum)

        # for multiply
        elif operaor == "*" or operaor == "multiply" or operaor == "×" or operaor == "X":
            print(firstnum * secondnum)
    elif user_want == "findsomeval":
        num = float(input("Enter the number which you want to know somes value of(Only enter number not alphabets)\n"))
        operaor = input("Enter what value you want to know? **,% / exponent,reminder (Only enter that given in options\n")
        if operaor == "**" or operaor == "exponent":
            pow = float(input("Enter power of number(Only enter number not more)\n"))
            print(num**pow)
        elif operaor == "%" or operaor == "reminder":
            divby = float(input("Enter number which you want to divide by(Only enter number not more)\n"))
            print(num % divby)
    # if any of the condition is not same then:-
   
    # in this type of case usually problem present in data that giver by user(user give data in wrong way)
    else:
        print("Any thing went wrong")

        # It is all ready give a warning to user for they not do any mistake in giving input
    print("warning[if you enter wrong input program will stop]")

    # if user want to calculate any two number again it will continue
    user_input = input("Do you want to try again? yes/no (~Only enter 'yes' or 'no'} \n")
    if user_input != "yes" and user_input != "no":
        user_input = "no"
