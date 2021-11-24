#importing 
import time

#data
  #user 1
usr_r = False
username1 = "amrit"
password1 = "amritpython"
  #user 2
username2 = "sudha"
password2 = "sudhapython"
  #user 3
username3 = "arnav"
password3 = "arnavpython"

# take user input
takenusername = str(input("Enter your username\n"))
takenpassword = str(input("Enter your password\n"))

#matching with users data

   #matching with data of user 1
if takenusername == username1 and takenpassword == password1:
    print("userdata is present below\n, name-Amrit\n","Age-14\n","Passion-programmer(python)\n","class-9")
    usr_r = True

   #matching with data of user 2
elif takenusername == username2 and takenpassword == password2:
    print("userdata is present below\n,name-sudha\n","Age-12\n","Passion-unknown\n","class-7")
    usr_r = True

   #matching with data of user 3
elif takenusername == username2 and takenpassword == password3:
    print("userdata is present below\n,name-Arnav\n","Age-12\n","Passion-gamer\n","class-3")
   
    usr_r = True
   #if it is not same with any of the user then it will a user with unregistation(unvalid)
else:
    print("invalid user")

#let user to see output
time.sleep(13)
