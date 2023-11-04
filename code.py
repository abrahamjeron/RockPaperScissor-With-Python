import random
def get_user_choice():
    user_choice=input("Enter your choice: Rock,Paper or Scissors: ").capitalize()
    while user_choice not in ["Rock","Paper","Scissors"]:
        user_choice=input("Enter a valid choice: Rock, Paper or Scissors: ").capitalize()
    return user_choice
def get_computer_choice():
    return random.choice(["Rock","Paper","Scissors"])
def winner(user_choice,computer_choice):
    if user_choice==computer_choice:
        return "It's a tie"
    elif (user_choice=="Rock" and computer_choice=="Scissors") or (user_choice=="Paper" and computer_choice=="Rock") or (user_choice=="Scissors" and computer_choice=="Paper"):
        return "You Won!"
    else:
        return "Computer Won!"
def play_game():
    print("Let's play rock paper scissors")
    user_choice=get_user_choice()
    computer_choice=get_computer_choice()
    print("You Chose: "+user_choice)
    print("Computer chose: "+computer_choice)
    result=winner(user_choice,computer_choice)
    print(result)
play_game()