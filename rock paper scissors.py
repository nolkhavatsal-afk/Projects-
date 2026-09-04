import random 

computer_choice=random.choice(['rock', 'paper', 'scissors'])
user_choice=input("Enter your choice (rock, paper, scissors): ").lower()
name=input("Enter your name: ")
print("computer choosed",computer_choice)
if user_choice== computer_choice:
    print("Match Tied")
elif user_choice=="rock" and computer_choice=="scissors":
    print(f"{name},Congratulations! You won the match")
elif user_choice=="paper" and computer_choice=="rock":
    print(f"{name},Congratulations! You won the match")
elif user_choice=="scissors" and computer_choice=="paper":
    print(f"{name},Congratulations! You won the match")
else:
    print(f"{name},Sorry! You lost the match. Computer chose {computer_choice}")