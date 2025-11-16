s = {10,20,30,40,50}
for i in s:
    print(i)    #Iterating Set. Return random order

print('-----------------')
lst = [10,20,30,40,50,10,20]
s1 = set(lst)   #Convert List to Set
print(s1)

print('-----------------')
s2 = {10,20,30,40,50,10,20}
s2.remove(20)   #Remove element from set
print(s2)   
s2.discard(100) #Discard element from set. No error if element not found
print(s2)

print('-----------------')
s3 = {1,2,3}
print(s3.pop())  #Remove random element from set
print(s3)

print('-----------------')
s4 = {11,22,33}
s4.clear()  #Clear the set
print(s4)

print('-----------------')
s5 = {25,35,45}
s5.add(55)  #Add element to set
print(s5)

print('-----------------')
s6 = {100,200,300}
s6.update(lst)  #Add multiple elements to set
print(s6)

print('Thank You...')