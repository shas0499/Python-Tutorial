L = [20,30,40,60,70]
len = len(L)

print("length of the List is : ",len)

print("Elements in the List are : ")
for n in range(len):
    print(L[n])

print('----------2nd Methode--------------------')

for i in L:
    print(i)

print('-------------Reverse-----------------')

print("Normal List",L)

print("Revese : ")
for x in range(len-1,-1,-1):
    print(L[x])