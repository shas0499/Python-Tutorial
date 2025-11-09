# Create list with using append function
l = [] # creating an empty list
for a in range(1,101):
    l.append(a)

print("Normal List : ", l)

print('------------List Comprehension-------------------')
s = [x for x in range(0,101)]
print("List Comprehension : ",s)

print('------------List Comprehension with Filter-------------------')
h = [i for i in range(1,101) if i%2 == 0]
print(h)

print('------------List Comprehension of string-------------------')
str = 'Hello'
str1 = [j for j in str]
print(str1)