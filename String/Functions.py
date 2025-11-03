w = "Welcome to Python"

n = w.lower()   #Convert to lower all character
print(n)

v = w.upper()  #Convert to upper all character
print(v)

x = w.title()   # Capital the 1st letter of the word
print(x)

c = w.capitalize() #Capital of the 1st letter of the scentence
print(c)

print('-------------------------------------------------------')

#Find function

str = "Welcome"
x = str.find('e')   #will return the index number of the 1st 'e'
y = str.find('el')  #will find more than one character
z = str.find('e',2)     # It'll start from 2 index to find 'e'
q = str.find('z')   #will return -1 as 'z' is not present in the string

print(x,y,z,q)

print('-------------------------------------------------------')

#Index function

m = str.index('o')
print(m)
#print(str.index('z'))   # If character is not present then will give error in index() function

print('-------------------------------------------------------')

#isalpha()

str1 = 'Welcome123'
print(str.isalpha())
print(str1.isalpha())
print('-------------------------------------------------------')

#isdigit()
str2 = '123'
print(str1.isdigit())
print(str2.isdigit())
print('-------------------------------------------------------')

#isalnum()

str3 = "Welcome@123"
print(str1.isalnum())
print(str2.isalnum())
print(str.isalnum())
print(str3.isalnum())   # will not take any special character or space

print('-------------------------------------------------------')

#chr() -> return the string by taking ASCII value
print(chr(65))
print(chr(67))
print(chr(68))
print('-------------------------------------------------------')

#ord() -> will give the ASCII value of the character
print(ord("A"))
print(ord("V"))
print(ord("X"))
print('-------------------------------------------------------')

#format()

name = "Hi.. My name is {fname} {Lname}".format(fname = "Shaswata",Lname = "Barua")
name1 = "Hi.. My name is {} {}".format("Shaswata","Barua")
name2 = "Hi.. My name is {0} {1}".format("Shaswata","Barua")
print(name)
print(name1)
print(name2)