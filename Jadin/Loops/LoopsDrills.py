
'''
START HERE
'''

'''While Loops'''
#1) Declare a variable set to 4. Make a while loop that prints the variable 
#    you just created and decrements the variable by one each time through
#    the loop. Meanwhile, make the loop run until the variable you created 
#    equals 1.
x=4
while x>=1:
    print(x)
    x=x-1
#2) Declare a variable set to 14. Make a while loop that prints the variable 
#    you just created and increments the variable by one each time through
#    the loop. Meanwhile, make the loop run until the variable you created 
#    equals 20.
x=14
while x <=20:
    print(x)
    x=x+1
#3) Declare a variable set to 55. Make a while loop that prints the variable 
#   you just created. Then make an if statement that makes the loop break when
#   the variable is equal to 50. 
x=55
while x>0:
    print(x)
    x=x-1
    if x==50:
        break
'''For Loops'''
#4) Create a list named sports. Put three sports into the list. Create
#   a for loop that prints each sport in the list
sports=["Lacrosse", "Cheer", "Football"]
for x in sports:
    print(x)
#5) Create a for loop that loops through each letter in a string of one of your
#   favorite songs. Each iteration should print should a letter of the word. 
song="Amen"
for x in range(len(song)):
    print(song[x])
#6) Create a list named movies. Put five of your favorite movies into the list.
#   However, make sure one of the movies is Avatar. 
#   Create a for loop that iterates over the list. In the loop print the movie
#   being looped over, but create an if statement that breaks out of the 
#   loop if it is Avatar.
movies=["Pixels", "Spare Parts", "Kung Fu Panda 2", "Shang Chi", "Avatar"]
for x in movies:
    if x == "Avatar":
        break
    print(x) 
