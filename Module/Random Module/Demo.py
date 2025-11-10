import random

#5 and 10  will also include
print(random.randint(5,10))

#2 will be include but 9 will not include
print(random.randrange(2,9))

lst = [2,10,'Kolkata',10.5]
print(random.choice(lst))

print(random.random())

lst1 = [2,10,'Kolkata',10.5]
random.shuffle(lst1)
print(lst1)

print(random.uniform(10,30))

lst2 = ["Rock","paper","Scissor"]
print(random.choice(lst2))