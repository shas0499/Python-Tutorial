num1 = eval(input("Enter the 1st number : "))
num2 = eval(input("Enter the second number : "))

opr = input("Enter the operation that you want to perform (Add/Sub/Mul/Div) : ")

if opr == 'Add' or opr == 'add':
    print(num1 + num2)

elif opr == 'Sub' or opr == 'sub':
    print(num1 - num2)

elif opr == 'Mul' or opr =='mul':
    print(num1*num2)

elif opr == 'Div' or opr == 'div':
    print(num1/num2)

else:
    print("Invalid Operation. Please give correct operation...")