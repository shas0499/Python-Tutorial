import random

Game_lst = ["Rock","Paper","Scissor"]
rand_choice = random.choice(Game_lst)

user_input = input("Enter you choice b/w Rock,Paper,Scissor... ")

if(rand_choice == "Rock" and user_input == "paper"):
    print("Computer choice is : "+rand_choice)
    print("Congrats!! You win..")

elif(rand_choice == "Rock" and user_input == "Scissor"):
    print("Computer choice is : "+rand_choice)
    print("Computer won...better luck next time..")

elif(rand_choice == "Paper" and user_input == "Scissor"):
    print("Computer choice is : "+rand_choice)
    print("Congrats!! You win..")