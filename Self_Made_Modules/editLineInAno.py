'''
                                            editLineInAno
                                 it is a module make by AMRUT KUMER MEHER,
                                it can edit any text file by without open it.
            Adding: it has a function called addLineInFile that can add new lines in the text in any text file
            Removing: it has a function called delLineInFile can remove lines in any text file, and in some cases you
                      to remove some line but multiples line looking same as your line that you have to remove so, it
                      has a function called delLineInFil2, this will find the list of lines similar to line that have
                      to remove any remove any particular of them. it require a number that the number of line have to
                      remove from list of simular line.
            Replacing: it has two function called replcLineInFil and replcLineInFil2, replcLineInFil can replace any line
                      from another however other one replcLineInFil2 can replace the line in list of similar line by number
                       of anyparticular line ,same as delLineInFil2.
            searhing: it has a function called searchLineInFile that can search any particular line in file and it position
                      (in number) in file

AUTHOR CONTACT:-
emails: amrutkumarmeher@gmail.com
        Aeo_royals@outlook.com
Github account: https://github.com/Royals-Aeo-Gamer/Heo-Leo
Facebook account:
'''

#delLineInFil
#write the line which have to remove
#the other argument is from which file(path) the line have to remove.
def delLineLnFil(line_have_to_remove,from_file):
    read_to_make_list = open(str(from_file),"r")
    list_of_lines = read_to_make_list.readlines()
    format_to_edit = open(str(from_file),"w")
    for line in list_of_lines:
        if line.replace("\n","") != line_have_to_remove:
            format_to_edit.write(line)
    format_to_edit.close()
    read_to_make_list.close()

#delLineInFile2
#write the line which have to remove in first argument.
#write the name of file(Path) from which have to remove.
#it require one more argument that is "num", adc the number of line list of similur line similur to your given line.
def delLineInFil2(line_have_to_remove,from_file,num):
    read_to_make_list = open(str(from_file),"r")
    list_of_lines = read_to_make_list.readlines()
    format_to_edit = open(str(from_file),"w")
    indexe = 0
    for line in list_of_lines:
        if line.replace("\n","") != str(line_have_to_remove):
            format_to_edit.write(line)
        elif line.replace("\n","") == str(line_have_to_remove):
            indexe+=1
            if indexe == int(num):
                pass
            elif indexe != int(num):
                format_to_edit.write(line)
    format_to_edit.close()
    read_to_make_list.close()

#replcLineInFil
#Write which line have to remove by which line.
#write the line by which this existing line have to replace.
#write the file(path) from which the line have to remove.
def replcLineInFil(line_have_to_replace,line_have_to_replace_from,from_file):
    read_to_make_list = open(str(from_file),"r")
    list_of_lines = read_to_make_list.readlines()
    format_to_edit = open(str(from_file),"w")
    for line in list_of_lines:
        if line.replace("\n","") != line_have_to_replace:
            format_to_edit.write(line)
        elif line.replace("\n","") == line_have_to_replace:
            format_to_edit.write(line_have_to_replace_from)
    format_to_edit.close()
    read_to_make_list.close()

#searchLineInFile
#write the line which have to remove.
#wirite the file in which this line can be lye
def searchLineInFile(which_line_have_to_search,in_which_file):
    read_to_make_list = open(str(in_which_file),"r")
    list_of_lines = read_to_make_list.readlines()
    for line in list_of_lines:
        if which_line_have_to_search == line.replace("\n",""):
            return list_of_lines.index(line) + 1

#replcLineInFile
#write tha line which have to replace.
#write the line by which the existing line have to replace.
#write the file in which the replacement have to do.
#write the number of line in the list of similar lines similar to your given line.
def replcLineInFil2(what_have_to_replace,what_have_to_replace_by,in_which_file,number):
    read_to_make_list = open(str(in_which_file),"r")
    list_of_lines = read_to_make_list.readlines()
    format_to_edit = open(str(in_which_file),"w")
    indexe = 0
    for line in list_of_lines:
        if line.replace("\n","") == what_have_to_replace:
            indexe+=1
            if indexe == number:
                format_to_edit.write(what_have_to_replace_by)
            elif number != what_have_to_replace:
                format_to_edit.write(line)
        elif line.replace("\n","") != what_have_to_replace:
            format_to_edit.write(line)

#addLineInFile
#write the line that have to add.
#write the file(path) in which these line\lines have to add.
#it has a parameter "multi_line", it is for if you have to multiple line in text then assign it as True then it defalt
#value is False, fo single line
def addLineInFile(what_have_to_add,In_which_file,multi_lines=False):
    readToMakeList = open(str(In_which_file),"r")

    list_of_lines = readToMakeList.readlines()
    formatToEdit = open(str(In_which_file),"w")
    for line in list_of_lines:
        formatToEdit.write(line)
    if multi_lines == False:
        formatToEdit.write(what_have_to_add)
    elif multi_lines == True:
        for line in what_have_to_add:
            formatToEdit.write(line)


