L1 = [10,20,40,60]
print(L1)

del L1[2]
print(L1)

print('-------------------------------------------------------')

L2 = [20,23,53,45,22]
print(L2.pop(2))
print(L2)

print('-------------------------------------------------------')

L3 = [22,34,56,75,12,90]
print("Original List is : ",L3)
L3.remove(34)
print(L3)

print('-------------------------------------------------------')

L4 = [25,15,35,65,55,75]
print("Original List is : ",L4)

L4.clear()
print(L4)

print('------------Update List value-------------------')

L5 = [20,60,33,24,67]
print("Original List : ",L5)

L5[2] = 44
print(L5)

print('-------------------------------------------------------')

L6 = [20,30,40,60,70]
print("Original List : ",L6)

L6.insert(1,35)
print(L6)

print('-------------------------------------------------------')

L7 = [45,55,65,75,85]
print("Original List : ",L7)

L7.append(95)
print(L7)

s = ['Kolkata','Bangalore']
L7.append(s)
print(L7)

print('-------------------------------------------------------')

L8 = [21,11,34,41,51]
print("Original List : ",L8)

L8.extend(s)
print(L8)

print('-------------------------------------------------------')

#count()
L9 = [10,20,40,20,60,20]
a = L9.count(20)
print(a)

print('-------------------------------------------------------')

#Max()
L10 = [10,90,70,60]
maxima = max(L10)

L11 = ["Hello","Dog"]
maxima1 = max(L11)

print(maxima)
print(maxima1)

print('-------------------------------------------------------')

#min()
L12 = [5,2,40,30]
minima = min(L12)
print(minima)

print('-------------------------------------------------------')

#sort()
L13 = [20,10,200,5,55]
print("Original List : ",L13)

L13.sort()
print("Sorted List : ",L13)

print('-------------------------------------------------------')

#reverser()

L14 = [10,40,20,50]
print("Original List : ",L14)

L14.reverse()
print("Reverse List : ",L14)

print('-------------------------------------------------------')

#index()

L15 = [10,90,40,55,35]
print(L15.index(55))

print('----------------Zip Function------------------')

lst1 = [10,20,30,40]
lst2 = [2,4,6,8]

for a,b in zip(lst1,lst2):
    print(a,b)

print("-.-.-.-.-.-.-.-.-.")

lst3 = [25,35,45,55,60]
lst4 = [5,10,15,20]

for x,y in zip(lst3,lst4):
    print(x,y)

print('-----------Without Zip Function------------------')

lst5 = [11,22,33,44]
lst6 = [10,20,30,40]

len = len(lst5)

for i in range(len):
    print(lst5[i], lst6[i])