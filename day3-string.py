# numeric data type

var1=1
var2=True
var3=10.023
var4=10+3j

print(type(var1)) #prints <class 'int'>
print(type(var2)) #prints <class 'bool'>
print(type(var3)) #prints <class 'float'>
print(type(var4)) #print <class 'complex'>

print(id(var1)) #prints the memory address of the variables
print(id(var2))
print(id(var3))
print(id(var4))


# String data type

#multiline string
a="""jgasjgasvdjhavd 
dbjasvdhjdhjad
anmdvjhadvhkDB"""

K='''JAHVDJGASVDJHASD
ASKJDHVBJHASVDHJA'''


#Single line string
b="vahscSDAHGDAH"


#STRING LENGTH
print(len(a))

print(a[4]) #prints the 4th index character of string a


#CHECK STRING
txt="hi i am just building and python program"
print("i" in txt) #prints True if 'i' is present in txt else False
print("i" not in txt) #print True if 'i' is not present in txt else False

print("rajat" in txt) #print False as 'rajat' is not present in txt


# SLICING String (start index : end index : step) "end index is excluded"

b= "hello world"
print(b[2:]) #prints string from index 2 to end
print(b[:3]) #prints string from start to index 3-1
print(b[0:5]) #prints string from index 0 to 5-1
print(b[-4:-2])    #prints string from index -4 to -2-1


#MODIFY STRING

a="heLLo"
print(a.upper())
print(a.lower())


#REMOVE WHITESPACES

a="   hello world    "
print(a)
print(a.strip())