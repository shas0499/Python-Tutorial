T = (10,20,30,40)
print(T)
print(type(T))

T1 = (10)  #Single element is not a tuple
print(T1)
print(type(T1))

T2 = (10,)  #Single element tuple
print(T2)

n = T[2] #Access Tuple element
print(n)
print('-----------------')

length = len(T) #Length of Tuple

for i in range(length): #tuple Iteration with for loop
    print(T[i])

#Functions on Tuple
print('-----------------')
print(T)

print(min(T)) #min() function
print(max(T)) #max() function
print(T.count(10)) #count() function
print(T.index(40))  #index() function
print(sum(T))  #sum() function
print(sum(T,20))  #Add 20 to the sum of tuple
print('-----------------')