a=11
b=2
print(a+b) #print 13

print(id(a)) #a random memory location for a

print(id(b)) #similar id for b
print ("\n") #new line

# Camel case

"""🐍 Snake Case

Words are all lowercase, separated by underscores.
Common in Python for variables & functions.

user_name = "Ayush"
max_speed = 120"""

#example camel case
myVariableName=10
print(myVariableName) #gives output 10


# Snake case
"""🐪 Camel Case

-> First word is lowercase, each next word starts with a capital letter.
-> Common in JavaScript & Java variables/functions.

userName = "Ayush";
maxSpeed = 120;"""

#example camel case
my_variable_name=10
print(my_variable_name) #gives output 10


# Pascal case

"""🏛 Pascal Case

-> Every word starts with a capital letter, including the first one.
-> Often used for classes in Python, Java, C#.

class UserProfile:
    pass

class MaxSpeedCalculator:
    pass
"""
#example pascal case
MyVariableName=10 
print(MyVariableName)


# Many value to multiple variables
x,y,z=10,20,30
print(x,y,z) #prints 10 20 30 separtely as assigned each values to each vairable
print(id(x))
print(id(y))  
print(id(z))



# Unpack a collection
fruits=["apple","banana","cherry"]
x,y,z=fruits
print(x)    #prints apple
print(y)    #print banana
print(z)    #print cherry



# Global variable
x="awesome"
def myfunc():
    print("Python is "+x)
myfunc()