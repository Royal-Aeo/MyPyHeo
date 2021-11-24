#importing things
import time

#Collecting data from user(input)

   #for first number
firstnum = float(input("Enter first number\n"))

   #for second number
secondnum = float(input("Enter second number\n"))

   #for operator
operaor = input("Enter operator, options:- +,-,*,/ or plus,minus,multiply,divide\n")

#calculating all

   #for plus
if operaor == "+" or operaor == "plus":
    print(firstnum + secondnum)

   #for minus
elif operaor == "-" or operaor == "minus":
    print(firstnum - secondnum)

   #for divide
elif operaor == "/" or operaor == "divide":
    print(firstnum / secondnum)

   #for multiply
elif operaor == "*" or operaor == "multiply":
    print(firstnum * secondnum)

   #if any of the condision is not same then:-
   
    #in this type of case usually problem present in data that giver by user(user give data in wrong way)
else:
    print("Any thing went wrong")

#wait, Let user see the output
time.sleep(15)
