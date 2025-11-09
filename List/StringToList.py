str = input("Enter the string : ")
print('Original String : ',str)

lst1 = str.split()
print('Converted List',lst1) 

print('-------------Multiple Input------------------')

lst2 = []

count = int(input('Enter the number of input : '))

for n in range(count):
    str1 = input("Enter the value: ")
    lst2.append(str1)

print(lst2)