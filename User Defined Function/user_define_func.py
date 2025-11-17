#Simple Function
def simple_func():
    print("Hello This is Simple Function...")

simple_func()

#Function with Parameter
def arg_func(a,b):
    print("Sum of two number is : ",a+b)

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
arg_func(a,b)

#Function with Return Type
def ret_func(x,y):
    z = x*y
    return z

u = int(input("Enter first number : "))
z = int(input("Enter second number : "))
multiply = ret_func(u,z)
print("Multiplication of two number is : ",multiply)

print("Thank You....")
