#Importing all the files and moules that we need in the project
import pandas as pa
import json as jo
from func.editLineInAno import *
from func.Filter import myFilter
import time as tim

#defined all the functions have to use in code

#nametem
#it will make a json string add to json file
def nametem(name,age,gendre,password):
    stre = f'''
    "{name}":{{
        "Name":"{name}",
        "Age":{age},
        "Gender":"{gendre}",
        "Password":"{password}",
        "AccountType":"Standard"
    }}
}}'''
    return stre

#addUserInJsonConfig
#it will add a json string to json config file
def addUserInJsonConfig(in_which_file,userName,useraAge,userPasword,userGender):
    replcLineInFil("    }","    },",in_which_file)
    delLineLnFil("}",in_which_file)
    addLineInFile(nametem(userName,useraAge,userGender,userPasword),"C:\\Users\\AMRUT\\Coding\\languages\\MyPython\\projsyntax\\LoggingPage\\LoggingPage_Data.json",multi_lines=True)
    
#maked classes have to use in code

# trying to open the it configuration file. if they unable then it will make new one
# and, also making that data as a processible data
try:
    rawJsonUserDate = open("C:\\Users\\AMRUT\\Coding\\languages\\MyPython\\projsyntax\\LoggingPage\\LoggingPage_Data.json","r")
except FileNotFoundError:
    rawJsonUserDate = open("C:\\Users\\AMRUT\\Coding\\languages\\MyPython\\projsyntax\\LoggingPage\\LoggingPage_Data.json","x")
try:
    arrangedJsonUserData = jo.load(rawJsonUserDate)
except:
    addDataToEmpFile = open("C:\\Users\\AMRUT\\Coding\\languages\\MyPython\\projsyntax\\LoggingPage\\LoggingPage_Data.json","w")
    addDataToEmpFile.write("{\n}")

# trying to open log file. if they unable then it will make new one
# and, also making that data as a processible data
try:
    CSVlogFil = pa.read_csv("C:\\Users\\AMRUT\\Coding\\languages\\MyPython\\projsyntax\\LoggingPage\\LoggingPage_Log.csv")
except FileNotFoundError:
    open("C:\\Users\\AMRUT\\Coding\\languages\\MyPython\\projsyntax\\LoggingPage\\LoggingPage_Log.csv","x")
    var = pa.DataFrame({"Date":[None],"Day":[None],"Time":[None],"User":[None],"Activity":[None],"AccountType":[None]})
    var.to_csv("C:\\Users\\AMRUT\\Coding\\languages\\MyPython\\projsyntax\\LoggingPage\\LoggingPage_Log.csv",index=False)
    CSVlogFil = pa.read_csv("C:\\Users\\AMRUT\\Coding\\languages\\MyPython\\projsyntax\\LoggingPage\\LoggingPage_Log.csv")

except pa.errors.EmptyDataError:
    var = pa.DataFrame({"Date":[None],"Day":[None],"Time":[None],"User":[None],"Activity":[None],"AccountType":[None]})
    var.to_csv("C:\\Users\\AMRUT\\Coding\\languages\\MyPython\\projsyntax\\LoggingPage\\LoggingPage_Log.csv",index=False)
    CSVlogFil = pa.read_csv("C:\\Users\\AMRUT\\Coding\\languages\\MyPython\\projsyntax\\LoggingPage\\LoggingPage_Log.csv")

# loop for user interaction
usr_reg = False
# untill user is not regorised the loop is going on
while usr_reg == False:
    #it will set every data that need to describe in log file
    nowtime = list((tim.ctime()).split(" "))
    nowday = nowtime[0]
    nowdate = f"{nowtime[2]} {nowtime[1]} {nowtime[4]}"
    nowtime = nowtime[3]
    username = "Unknown"
    arrangedJsonUserData = jo.load(open("C:\\Users\\AMRUT\\Coding\\languages\\MyPython\\projsyntax\\LoggingPage\\LoggingPage_Data.json","r"))
    log_or_sign = myFilter(input("Please do, login or sign in[login/signin]\n"))
    
    # if user want to login on his/her account then the loop for that case
    if log_or_sign == "login":
        while True:
            takenusername = input("Enter your username\n")
            takenpassword = input("Enter your password\n")

            # if user is regornised then it will save a login history
            if takenusername in arrangedJsonUserData and takenpassword == arrangedJsonUserData[takenusername]["Password"]:
                username = takenusername
                usr_reg = True
                CSVlogFil = CSVlogFil.append({"Date":nowdate,"Day":nowday,"Time":nowtime,"User":username,"Activity":"login into account","AccountType":arrangedJsonUserData[username]["AccountType"]},ignore_index=True)
                CSVlogFil.to_csv("C:\\Users\\AMRUT\\Coding\\languages\\MyPython\\projsyntax\\LoggingPage\\LoggingPage_Log.csv",index=False)
                print(f"Hi {username}")
                break

            # if user is fail to regornise then they can try again or quit
            else:
                print("login information is invalid\nif you dont have any account then you can exit loging page by enter 'n' and can go for sign up\n")
                tryagain = input("Do you want to try again? [y,n]\n")
                if tryagain == 'y' or tryagain == 'yes' or tryagain == 'Y' or tryagain == "Yes" or tryagain == "YES":
                    pass
                elif tryagain == 'n' or tryagain == "no" or tryagain == "N" or tryagain == "No" or tryagain == "NO":
                    print("it's ok!")
                    break
                
                # if user given input not from option
                else:
                    print("Please do not give wrong inputs")
    
    # if the usknown user want to creat his/her account
    elif log_or_sign == 'signin':
        while True:

            # this will take every information about user
            takenusername = input("Enter the username\n")
            takenpassword = input("Enter the password\n")
            takenage = input("User age is\n")
            takensex = input("User gender\n")

            # it print input for verification that can user want to change its his/her details
            print(f"Verify the information is correct or not:-\n >Username: {takenusername}\n >Password:{takenpassword}\n >User Age:{takenage}\n >UserGender:{takensex}\n")
            verify = myFilter(input("Every information is correct?[y/n]?\n"))

            # it every thing is correct
            if verify == "y" or verify == "yes":
                print("Ok...\n")
                addUserInJsonConfig("C:\\Users\\AMRUT\\Coding\\languages\\MyPython\\projsyntax\\LoggingPage\\LoggingPage_Data.json",takenusername,takenage,takenpassword,takensex)
                break

            # if user want to change somthing
            elif verify == "n" or verify == 'no':
                whatWrong = input("whats wrong in here?[username/password/age/gender/i_want_to_fill_details_again]\n")
                if whatWrong == 'username':
                    takenusername = myFilter(input("Enter user name\n"))
                elif whatWrong == 'password':
                    takenpassword = myFilter(input("Enter password\n"))
                elif whatWrong == 'age':
                    takenage = myFilter(input("Enter age\n"))
                elif whatWrong == "gender":
                    takensex = myFilter(input("Enter gender\n"))
                elif whatWrong == 'i_want-to_fill-details_again':
                    takenusername = myFilter(input("Enter user name\n"))
                    takenpassword = myFilter(input("Enter password\n"))
                    takenage = myFilter(input("Enter age\n"))
                    takensex = myFilter(input("Enter gender\n"))
                
                # add all details to users list file
                addUserInJsonConfig("C:\\Users\\AMRUT\\Coding\\languages\\MyPython\\projsyntax\\LoggingPage\\LoggingPage_Data.json",takenusername,takenage,takenpassword,takensex)
                CSVlogFil = CSVlogFil.append({"Date":nowdate,"Day":nowday,"Time":nowtime,"User":username,"Activity":f"New account created {takenusername}","AccountType":arrangedJsonUserData[username]["AccountType"]},ignore_index=True)
                CSVlogFil.to_csv("C:\\Users\\AMRUT\\Coding\\languages\\MyPython\\projsyntax\\LoggingPage\\LoggingPage_Log.csv",index=False)
                print("okay...\n")
                break
    
    # if user given any input not from options
    else:
        print("Please do not give wrong input!\n")
