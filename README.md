# MyPyHeo
This is a repository use to store python small projects.

## Projects already stored in it
___
- [Calculator](MyProjs/Calculator)
- [LoggingPage](MyProjs/Logging_Page/LoggingPage)

## Calculator
___
It is a very basic and beggining level project for a programmer.

### __Versions:__ 

- [Calculator_1.2](MyProjs/Calculator/calculator_1.2_.py)
- [Calculator_3.2](MyProjs/Calculator/calculator_3.20_.py)

### __Tutorial:__
#### __Calculator_1.2:__
it is very easy to use...

first, we have to put a number(any number).
```Python
Enter first number
12 # This is input
```
then, we have to put another number.
```Python
Enter second number
2 # This is another input
```
after this, we got a few option for doing operation in both the number.
```Python
Enter operator, options:- +,-,*,/ or plus,minus,multiply,divide
```
choose any of this operation as your desire, in this case i have choosed "/" (divide). and the output will come(result).
```Python
Enter operator, options:- +,-,*,/ or plus,minus,multiply,divide
/   #This is input
6.0 # This is output
```
Note that, after output is come it will stay till 15 seconds.
now, let's move on next project...
#### __Calculator_3.2:__
it is also easy as calculator_1.2 but there is only a bit difference between calculator 1.2 and 3.2.

well, in this version, first, we have to choose an option from given two options. first option is "calculate", and another option is "findsomeval". both are for some different type of calculations.

when you start the project it will show you output some thing like this.
```Python
CALCULATOR_2.0_
 General instruction
 >>1. You dont have to give input in shortform/expanded form
 >>2. You have to choose and give input according to instruction you gave before giving input
 >>3. if you give input in wrong way the program could be stop running
 >>4. instruction will given in a bracket ()
 >>5. warning is written in square bracket '[]'

What you want to do? (calculate/findsomeval)
```
here a question is asked to you that to choose an option form the bracker.

if you choose _calculate_ then it will ask you to enter another number. and after you entered it will ask you to enter another number.
```Python
calculate # Option i choosed
Enter first number (~Only enter number not alphabet)
36 # input
Enter second number (~Only enter number not alphabet)
2 # input
```
then it will ask you for operator.
```Python
Enter operator, options:- +,-,*,/ or plus,minus,multiply,divide
/    # input
18.0 # output
```
after this, unlike previous one it will ask you for another time.
```Python
warning[if you enter wrong input program will stop]
Do you want to try again? yes/no (~Only enter 'yes' or 'no'}
```
if you choose "yes" by enter "yes" the it will again do that processiger. if you choose "no" by enter "no" the it will stop the program.

Ok, let's talk about _findsomeval_. here if you enter any number you will get its exponent and reminder by the any number.
```Python
Enter the number which you want to know somes value of(Only enter number not alphabets)
```
so, after you enter "findsomeval" it gives output like text given in highlited area above. you have to enter a number. then, it will give you options to choose, you have to choose from the option(basically there are two options are there `%` for reminder and `**` for exponent.)

 after you choose then it will again ask for a number, if you have choosen `%` then enter a number that gonna divided by you previously entered number and gives you reminder, or if you choosen `**` then enter the expontial number for previously entered number.

 after all the output will come. In my case i have entered `**` to know exponent of the number(result is given below).
 ```Python
 Enter the number which you want to know somes value of(Only enter number not alphabets)
12  # This is input
Enter what value you want to know? **,% / exponent,reminder (Only enter that given in options
**  # This iw input
Enter power of number(Only enter number not more)
2   # This is input
144.0 # This is result
 ```
This is all about my project calculator. Let's talk about Logging_Page.

## Logging_Page
___
this is little complicated its first version is so simple but its second one is little complicated.
### __Versions:__
- [LoggingPage](MyProjs/Logging_Page/LoggingPage/loggingpage.py)
- [LoggingPage2](MyProjs/Logging_Page/LoggingPage2/LoggingPage2.py)

### __Tutorial:__
#### __LoggingPage:__
it is also very easy to use.

first we have to give an username, then we have to give password. if the user name and password is correct then it will print some information about user. user username and password is mention in main script. or if you give wrong username or password it will print `Invalid User`.

```Python
Enter your username
amrit # This is input
Enter your password
amritpython #This is input
userdata is present below
, name-Amrit
 Age-14
 Passion-programmer(python)
 class-9
```

#### __LoggingPage2:__
it is some complicated but very cool.

first it will ask for login and signup. if you choose login then it will take you to login section you have to give your username and password(if you have already signup).

if we choose to `login` or `signin`. the we have to give username and password(as shown below).
```Python
Welcome!

Please do, login or register in[(login/signin)/signup/exit]
login # This is input
Enter your username
Amrut # This is input
Enter your password
Amrut10  # This is input
Hi,Amrut
Menu options:-
>.show_my_info
>.update_my_info
>.del_my_account
>.show_my_friends
>.log_out
```
we can choose any option from this there are given in menu.

Or, if we choose `signup` the it ask for some of your information(as shown below).
```Python
Welcome!

Please do, login or register in[(login/signin)/signup/exit]
signup # This is input
Enter the username
Ayush # This is input
Enter the password
Ay10 # This is input
User age is
13 # This is input
User gender
male # This is input
If you have friends then enter space separate name, if not then enter 'no'[list(<names>/no)
no # This is input
What is your hobby?
playing # This is input
Verify the information is correct or not:-
 >Username: Ayush
 >Password:Ay10
 >User Age:13
 >UserGender:male
 >UserHobby:playing
 >User friends:['no']
Every information is correct?[y/n]?
y # This is input
Ok...

okay...
```
after this, it will create your profile in data file.

and if you choose `exit` the it will close this program.