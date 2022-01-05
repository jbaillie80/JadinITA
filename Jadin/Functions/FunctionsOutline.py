'''
This outline will help solidify concepts from the Functions lesson.
Fill in this outline as the instructor goes through the lesson.
'''
#1) Make a function that has two boolean parameters. If both booleans are
#true, return true. Else, return false. Then, call the function.
#Print what the function returns.
def check(x, y):
    if x == True and y == True:
        return True 
    else:
        return False 

print(check(False, True))
#2) Make a function that takes one int parameter: gallons. Convert gallons
#to cups (do this by multiplying gallons by 16). Then return cups. Then,
#call the function.
#Print what the function returns.
def conversion(gallons):
    return gallons*16
print(conversion(2))
#3) Make a function of any any kind with a common SYNTAX error. Then, call the
#function.
#Print what the function returns.
def conversion(gallons)
    return gallons*16
print(conversion(2))