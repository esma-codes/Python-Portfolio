import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images=[rock,paper,scissors]

user_score=0
computer_score=0
rounds=3
for game in range(rounds):
    user_choice=int(input("What do you choose? type 0 for rock,type 1 for paper,type 2 for scissors\n"))
    if user_choice not in [0,1,2]:
        print("Invalid choice! Round skipped.")
        continue
    computer_choice=random.randint(0,2)

    print(f"You chose:{game_images[user_choice]}")
    print(f"Computer chose:{game_images[computer_choice]}")

    if computer_choice==user_choice:
        print("It's a draw!")
    elif (user_choice==1 and computer_choice==0) or \
         (user_choice==2 and computer_choice==1) or\
         (user_choice==0 and computer_choice==2):
        print("You Win this round!")
        user_score+=1
    else:
        print("You lost this round!")
        computer_score+=1

print("\n---Final Result---")
print(f"computer Score:{computer_score}")
print(f"user score:{user_score}")

if user_score>computer_score:
    print("Congratulations! You are the overall winner!")
elif computer_score>user_score:
    print("Computer wins overall! Better luck next time!")
else:
    print("It's overall draw!")

