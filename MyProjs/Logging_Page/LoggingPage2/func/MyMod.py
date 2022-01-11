'''
                                       This is filter function
                            it can filter user input to a form that can code process easily
                                                   "filter()"
'''
def myFilter(var):
    var = str(var)
    var = var.lower()
    var = var.replace(" ","")
    return var
