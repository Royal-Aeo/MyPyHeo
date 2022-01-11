#Importing all the files and moules that we need in the project
import pandas as pa
import json as jo
from func.editLineInAno import *
from func.MyMod import myFilter
import time as tim

#Global varables
LoggingPage_Data__path = "C:\\Users\\aeo_r\\Coding\\languages\\Python\\Git_Repositories\\MyPyHeo\\MyProjs\\Logging_Page\\LoggingPage2\\LoggingPage_Data.json"
LoggingPage_Log__path = "C:\\Users\\aeo_r\\Coding\\languages\\Python\\Git_Repositories\\MyPyHeo\\MyProjs\\Logging_Page\\LoggingPage2\\LoggingPage_Log.csv"

#defined all the functions have to use in code

#json form
def json_form(userName,useraAge,userPasword,userGender,friends,hobby):
    r"it will make a json string from python dict for user"
    dict = {"Name":userName,"Age":useraAge,"Gender":userGender,"Password":userPasword,"Friends":friends,"Hobby":hobby}
    return jo.dumps(dict,indent=4)

#addUserInJsonConfig
def addUserInJsonConfig(in_which_file,userName,useraAge,userPasword,userGender,friends,hobby):
    r"it will add a json string to json config file"
    file = open(in_which_file,"r")
    try:
        file = jo.load(file)
    except jo.decoder.JSONDecodeError:
        file = {}
    file.update({f"{userName}":{"Name":f"{userName}","Age":f"{useraAge}","Gender":f"{userGender}","Password":f"{userPasword}","Friends":friends,"Hobby":f"{hobby}"}})
    filehavetodum = open(in_which_file,"w")
    jo.dump(file,filehavetodum,indent=4)

#change_info
def change_info(username,what_have_to_change,what_should_be_its_val,in_which_json_file):
    r"it help to change user information"
    raw_json_data = open(in_which_json_file,"r")
    json_data = jo.load(raw_json_data)
    json_data[username][what_have_to_change] = what_should_be_its_val
    which_file = open(in_which_json_file,"w")
    jo.dump(json_data,which_file,indent=4)

#Ch_ref_username
def Ch_ref_username(username,new_name,in_which_json_file):
    r"it help to change the reference name of any user"
    raw_json_data = open(in_which_json_file,"r")
    json_data = jo.load(raw_json_data)
    json_data[username]["Name"] = new_name
    json_data[new_name] = json_data.pop(username)
    which_file = open(in_which_json_file,"w")
    jo.dump(json_data,which_file,indent=4)

#del_account_json
def del_account_json(username,which_file):
    r"it help to delete any user account in json file"
    raw_json_data = open(which_file,"r")
    json_data = jo.load(raw_json_data)
    json_data.pop(username)
    which_file1 = open(which_file,"w")
    jo.dump(json_data,which_file1,indent=4)

#append_to_log
def append_to_log(log_file,username,activity):
    r"it will append a log history to log file"
    r"the file should be: xls, csv"
    CSVlogFil = pa.read_csv(log_file)
    CSVlogFil = CSVlogFil.append({"Date":nowTime.nowDate(),"Day":nowTime.nowDay(),"Time":nowTime.nowTime(),"User":username,"Activity":f"{activity}"},ignore_index=True)
    CSVlogFil.to_csv(log_file,index=False)
#nowTime
#it can show current time,day,date,month,year
class nowTime:
    r"it can output you current time,day,date,year"
    @classmethod
    def nowTime(self):
        r"it will output current time"
        nowtime = list((tim.ctime()).split())
        return nowtime[3]
    @classmethod
    def nowDay(self):
        r"it will output current day"
        nowtime = list((tim.ctime()).split())
        return nowtime[0]
    @classmethod
    def nowDate(self):
        r"it will output current date"
        nowtime = list((tim.ctime()).split())
        return f"{nowtime[2]} {nowtime[1]} {nowtime[4]}"
    @classmethod
    def nowMonth():
        r"it wil output current month"
        nowtime = list((tim.ctime()).split())
        return nowtime[1]
    @classmethod
    def nowYear():
        r"it will output current year"
        nowtime = list((tim.ctime()).split())
        return nowtime[4]

# trying to open the it configuration file. if they unable then it will make new one
# and, also making that data as a processible data
try:
    rawJsonUserDate = open(LoggingPage_Data__path,"r")
except FileNotFoundError:
    rawJsonUserDate = open(LoggingPage_Data__path,"x")
try:
    arrangedJsonUserData = jo.load(rawJsonUserDate)
except:
    addDataToEmpFile = open(LoggingPage_Data__path,"w")
    addDataToEmpFile.write("{\n}")
    arrangedJsonUserData = {}

# trying to open log file. if they unable then it will make new one
# and, also making that data as a processible data
try:
    pa.read_csv(LoggingPage_Log__path)

except FileNotFoundError:
    open(LoggingPage_Log__path,"x")
    var = pa.DataFrame({"Date":[None],"Day":[None],"Time":[None],"User":[None],"Activity":[None]})
    var.to_csv(LoggingPage_Log__path,index=False)

except pa.errors.EmptyDataError:
    var = pa.DataFrame({"Date":[None],"Day":[None],"Time":[None],"User":[None],"Activity":[None]})
    var.to_csv(LoggingPage_Log__path,index=False)
    

# loop for user interaction
usr_itract_pross = True
# untill user is not regorised the loop is going on
while usr_itract_pross == True:
    user_regon = False
    #it will set every data that need to describe in log file
    print("Welcome!\n")
    try:
        arrangedJsonUserData = jo.load(open(LoggingPage_Data__path,"r"))
    except:
        pass
    log_or_sign = myFilter(input("Please do, login or register in[(login/signin)/signup/exit]\n"))
    
    # if user want to login on his/her account then the loop for that case
    if log_or_sign == "login" or log_or_sign == "signin":
        while True:
            takenusername = input("Enter your username\n")
            takenpassword = input("Enter your password\n")

            # if user is regornised then it will save a login history
            if takenusername in arrangedJsonUserData and takenpassword == arrangedJsonUserData[takenusername]["Password"]:
                username = takenusername
                append_to_log(LoggingPage_Log__path,username,'Logging into account')
                user_regon = True
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
    elif log_or_sign == 'signup':
        while True:

            # this will take every information about user
            takenusername =    input("Enter the username\n")
            takenpassword =    input("Enter the password\n")
            takenage =         input("User age is\n")
            takensex =         input("User gender\n")
            takenfriends= list(input("If you have friends then enter space separate name, if not then enter 'no'[list(<names>/no)\n").split(" "))
            takenhobby   =     input("What is your hobby?\n")
            # it print input for verification that can user want to change its his/her details
            print(f"Verify the information is correct or not:-\n >Username: {takenusername}\n >Password:{takenpassword}\n >User Age:{takenage}\n >UserGender:{takensex}\n >UserHobby:{takenhobby}\n >User friends:{takenfriends}")
            verify = myFilter(input("Every information is correct?[y/n]?\n"))

            # if every thing is correct
            if verify == "y" or verify == "yes":
                print("Ok...\n")
                addUserInJsonConfig(LoggingPage_Data__path,takenusername,takenage,takenpassword,takensex,takenfriends,takenhobby)
                rawJsonUserDate = open(LoggingPage_Data__path,"r")
                arrangedJsonUserData = jo.load(rawJsonUserDate)
                append_to_log(LoggingPage_Log__path,takenusername,"New account created")
                print("okay...\n")
                break

            # if user want to change somthing
            elif verify == "n" or verify == 'no':
                whatWrong = input("whats wrong in here?[username/password/age/gender/hobby/friends/i_want_to_fill_details_again]\n")
                if whatWrong == 'username':
                    takenusername = input("Enter user name\n")
                elif whatWrong == 'password':
                    takenpassword = input("Enter password\n")
                elif whatWrong == 'age':
                    takenage = input("Enter age\n")
                elif whatWrong == "gender":
                    takensex = input("Enter gender\n")
                elif whatWrong == "hobby":
                    takenhobby = input("Enter hobby\n")
                elif whatWrong == "friends":
                    takenfriends = list(input("If you have friends then enter space separate name, if not then enter 'no'[list(<names>/no)\n").split(" "))
                elif whatWrong == 'i_want-to_fill-details_again':
                    takenusername = input("Enter user name\n")
                    takenpassword = input("Enter password\n")
                    takenage = input("Enter age\n")
                    takensex = input("Enter gender\n")
                    takenfriends = list(input("If you have friends then enter space separate name, if not then enter 'no'[list(<names>/no)\n").split(" "))
                    takenhobby = input("What is your hobby?\n")
                # add all details to users list file
                addUserInJsonConfig(LoggingPage_Data__path,takenusername,takenage,takenpassword,takensex,takenfriends,takenhobby)
                rawJsonUserDate = open(LoggingPage_Data__path,"r")
                arrangedJsonUserData = jo.load(rawJsonUserDate)
                #indicating all process complete!
                print("okay...\n")
                break
    #if they want to exit
    elif log_or_sign == 'exit':
        usr_itract_pross=False

    # if user given any input not from options
    else:
        print("Please do not give wrong input!\n")
    #if user is regornise then...
    if user_regon == True:
        #a var for user is log_on now or log_off
        log_on = True
        while log_on == True:
            #greeding!
            print(f"Hi,{username}")
            usr_itract_pross = True

            #this is menu for user
            while usr_itract_pross == True:
                #load fresh information
                rawJsonUserDate = open(LoggingPage_Data__path,"r")
                arrangedJsonUserData = jo.load(rawJsonUserDate)

                #what user want from menu
                usr_wan = myFilter(input("Menu options:-\n>.show_my_info\n>.update_my_info\n>.del_my_account\n>.show_my_friends\n>.log_out\n"))
                #if they want to see his inforamation
                if usr_wan == "show_my_info":
                    print(f">Your username:- {arrangedJsonUserData[username]['Name']}\n>Your password is:- {arrangedJsonUserData[username]['Password']}\n>Your Age is:- {arrangedJsonUserData[username]['Age']}\n>Your Gender is:- {arrangedJsonUserData[username]['Gender']}\n>Your hobby is:- {arrangedJsonUserData[username]['Hobby']}\n>Your friend list is:- {arrangedJsonUserData[username]['Friends']}\n")
                    tim.sleep(4)
                #if user want to update there information
                elif usr_wan == "update_my_info":
                    while True:
                        whatHaveToCh = myFilter(input("\nWhat have to change?[first_show_me_my_info/username/password/age/gender/hobby/friends/back]\n"))
                        #before updating it thay want to see
                        if whatHaveToCh == "first_show_me_my_info":
                            rawJsonUserDate = open(LoggingPage_Data__path,"r")
                            arrangedJsonUserData = jo.load(rawJsonUserDate)
                            print(f">Your username:- {arrangedJsonUserData[username]['Name']}\n>Your password is:- {arrangedJsonUserData[username]['Password']}\n>Your Age is:- {arrangedJsonUserData[username]['Age']}\n>Your Gender is:- {arrangedJsonUserData[username]['Gender']}\n>Your hobby:- {arrangedJsonUserData[username]['Hobby']}\n>Your friends list is:- {arrangedJsonUserData[username]['Friends']}\n")
                        #want to update username
                        elif whatHaveToCh == "username":
                            newinfo = str(input("Enter new username\n"))
                            Ch_ref_username(username,newinfo,LoggingPage_Data__path)
                            append_to_log(LoggingPage_Log__path,username,f"Username updated to '{newinfo}'")
                            username = newinfo
                            print("\nOk\n")
                            tim.sleep(4)
                            break
                        #want to update password
                        elif whatHaveToCh == "password":
                            newinfo = str(input("Enter new password\n"))
                            change_info(username,"Password",newinfo,LoggingPage_Data__path)
                            append_to_log(LoggingPage_Log__path,username,f"Password updated to '{newinfo}'")
                            print("\nOk\n")
                            tim.sleep(4)
                            break
                        #want to update age
                        elif whatHaveToCh == "age":
                            newinfo = str(input("Enter age\n"))
                            change_info(username,"Age",newinfo,LoggingPage_Data__path)
                            append_to_log(LoggingPage_Log__path,username,f"Age updated to {newinfo}")
                            print("\nOk\n")
                            tim.sleep(4)
                            break
                        #want to update gender
                        elif whatHaveToCh == "gender":
                            newinfo = str(input("Enter gender\n"))
                            change_info(username,"Gender",newinfo,LoggingPage_Data__path)
                            append_to_log(LoggingPage_Log__path,username,f"Gender updated to {newinfo}")
                            print("\nOk\n")
                            tim.sleep(4)
                            break
                        #what to update hobby
                        elif whatHaveToCh == "hobby":
                            newinfo = str(input("Enter hobby\n"))
                            change_info(username,"Hobby",newinfo,LoggingPage_Data__path)
                            append_to_log(LoggingPage_Log__path,username,f"Hobby updated to {newinfo}")
                            print("\nOk\n")
                            tim.sleep(4)
                            break
                        #want to update friends
                        elif whatHaveToCh == "friends":
                            newinfo = list(input("Enter space separated friend names\n").split(" "))
                            change_info(username,'Friends',newinfo,LoggingPage_Data__path)
                            append_to_log(LoggingPage_Log__path,username,f"Friends are updated")
                            print("\nOk\n")
                            tim.sleep(4)
                            break
                        #don't want to update anything.(maybe mood changed)
                        elif whatHaveToCh == "back":
                            break
                        #user given input in wrong way
                        else:
                            print("No scho option! please give input from the given options.\n")
                
                #waht to delete her/his account
                elif usr_wan == "del_my_account":
                    while True:
                        print("Warning:-\n>After you turn off this program you won't be recognised by the program until you have registered by the program\n")
                        var = myFilter(str(input("Are you sure that you want to del account?[y/n]\n")))
                        #if they is conform
                        if var == "y" or var == "yes":
                            del_account_json(username,LoggingPage_Data__path)
                            print("Your account delete successfully!\n")
                            usr_itract_pross = False
                            log_on = False
                            break
                        #if they want to cancel
                        elif var == "n" or var == "no":
                            break
                
                #what to see name of friends from his/her info
                elif usr_wan == "show_my_friends":
                    print("\nHere is your friends:-")
                    rawJsonUserDate = open(LoggingPage_Data__path,"r")
                    arrangedJsonUserData = jo.load(rawJsonUserDate)
                    for friend in arrangedJsonUserData[username]["Friends"]:
                        print(friend)
                    tim.sleep(6)
                
                #want to logout from the account
                elif usr_wan == "log_out":
                    append_to_log(LoggingPage_Log__path,username,"Logout from account")
                    usr_itract_pross = False   #after this they will directly go-
                    log_on = False             #-to logging section
                #if user given input in wrong way
                else:
                    print("No scho option! please give input from the given options.\n")
        usr_itract_pross = True
