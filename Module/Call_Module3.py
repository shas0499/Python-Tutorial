from Module import *

a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number:"))

print("Sum of the two number is : ",sum(a,b))
print("Multiplication of the two number is : ",mul(a,b)) # pyright: ignore[reportUndefinedVariable]
print("Subtraction of the two number is : ",sub(a,b)) # pyright: ignore[reportUndefinedVariable]