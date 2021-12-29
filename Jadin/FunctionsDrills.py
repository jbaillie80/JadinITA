'''
For this assignment you should read the task, then below the task do what it asks you to do.
For tasks with return statements, you can test out if you are correct by putting in some parameters
and printing what is returned outside of the function.

EXAMPLE TASK:
'''
#EX) Define a function that has two parameters. Make the function add the two
#numbers together and return the result.
from pickle import TRUE
def add_two_numbers(num1, num2):
    sumOfTwoNumbers = num1 + num2
    return sumOfTwoNumbers

'''
END OF EXAMPLE
'''

'''
START HERE
'''


#1) Define a function that has two int parameters. Make the function subtract 
#the first parameter minus the second one. Then, return the result. Now call 
#the function.
#Print what the function returns.
def sub(x,y):
    return x-y 
print(sub(9,6))
#2) Define a function that has one parameter. Make the function divide the 
#parameter by 2, multiply it by 77, and then add 10,000. Return the result.
#Now call the function.
#Print what the function returns.
def SerEq(x):
    return ((x/2)*77)+10000
print(SerEq(10))
#3) Define a function that has two int parameters. Make the function check if 
#two numbers are equal. If they are equal, return true. If they are not equal, 
#return false. Now call the function.
#Print what the function returns.
def Eq(x,y):
    if x==y:
        return True 
    else:
        return False 
print(Eq(2,2))
#4) Define a function that has two int parameters. Make the function
#check which parameter is bigger, and return the bigger parameter. 
#If they are the same, it should just return either parameter. Now call the 
#function.
#Print what the function returns.
def Bg(x,y):
    if x>y:
        return x 
    elif x<y:
        return y 
    else:
        x 
print(Bg(2,3))
#5) Define a function that has two string parameters. Make the function
#add the two strings together. And then return the combined string. Now call 
#the function.
#Print what the function returns.
def Add(x,y):
    return x+y 
print(Add("Do","g"))
#6) Define a function that has three int parameters. If the first number is 
#equal to the second OR the third number, return true. Else, return false. Now 
#call the function.
#Print what the function returns.
def Check(x,y,z):
    if x == y or x == z:
        return True 
    else:
        return False 
print(Check(1, 2, 1))
#7) Define a function that prints your name. It should have no parameters and 
#shouldn't return anything. Now call the function.
def name():
    return "Jadin"
print(name())
#8) Define a function that has one string parameter. The string should be a
#color. If that string is equal to your favorite color, it prints "That's my 
#favorite color!". If it is not, it prints "That is not my favorite color. 
#Try again.". It shouldn't return anything. Now call the function.
def FavColor(x):
    if x == "red":
        return "Thats my favorite color!"
    else:
        return "That is not my favorite color"
print(FavColor("red"))
#9) Define a function that has one int parameter. The int should be 
#positive. If the number is not equal to zero, the function runs a loop that
#decrements the parameter by 1 and prints it each time. Now call the function.
def Dec(x):
    if x > 0:
        while x > 0:
            print(x) 
            x = x-1
    else:
        return
Dec(4)