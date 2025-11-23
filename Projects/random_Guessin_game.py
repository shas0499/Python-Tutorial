import random

input_num = int(input("Enter the number between 1 to 50 : "))

random_num = random.randint(1,50)
if(input_num == random_num):
    if(input_num > 50 or input_num <1):
        print("Please enter number between 1 to 50")

    else:
        print("Congrats!! Your guess is correct...")

elif (input_num > random_num):
    if(input_num > 50 or input_num <1):
        print("Please enter number between 1 to 50")
    else:
        print("Sorry!! incorrect guess. Generated number is : "+str(random_num))
        dif = input_num-random_num
        print("Your guess is "+str(dif)+" bigger")

elif (random_num > input_num):
    if(input_num > 50 or input_num <1):
        print("Please enter number between 1 to 50")
    else:
        print("Sorry!! incorrect guess. Generated number is : "+str(random_num))
        dif1 = random_num-input_num
        print("Your guess is "+str(dif1)+" lower")

print("Thank You...")