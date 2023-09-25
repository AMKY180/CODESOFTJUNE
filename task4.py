import random
user_score = 0
computer_score =0
while True:
    user_choice =input("\n choose Rock, Paper or Scissors (or type  quit to exit the game ) : ").lower()
    if user_choice =="quit":
        print("Thanks For Playing! ")
        break
    choices =["rock","paper","scissors"]
    computer_choice = random.choice(choices)
    if user_choice==computer_choice:
        print("it's tie! ")
    elif((user_choice == "rock" and computer_choice  == "scissors") or
         (user_choice == "scissors" and computer_choice  == "paper") or
         (user_choice == "paper" and computer_choice  == "rock") 
    ):
        user_score += 1
        print(f"\n You chose {user_choice}  and the compuer chose {computer_choice}  You win this round! ")
    else:
        computer_score += 1
        print(f"\n You chose {user_choice}  and the compuer chose {computer_choice}  computer win this round! ")
    
    print(f"your score : {user_score} computer score : {computer_score}")
    feedback =input("enter you feedback ")
    
print("\n Final score")
print(f"your score : {user_score} computer score : {computer_score}")

        
        