import random
while True:
    user_action = input("Enter your choice(Rock, Paper or scissor:)")
    possible_actions = ["Rock", "Paper", "Scissor"]
    computer_action = random.choice(possible_actions)
    print(f"\n You choose {user_action}, computer choose {computer_action}")
    if computer_action == user_action:
        print(f"Both selected {user_action}, It's a tie!")
    elif user_action == "Rock":
        if computer_action == "scissor":
            print("Rock smashes scissor, You win!")  
        else:
            print("Paper cover the rock, You loose!")
    elif user_action == "paper":
        if computer_action == "Rock":
            print("Paper cover the rock, You win!")
        else:
            print("scissor cuts paper, You loose!")
    elif user_action == "scissor":
        if computer_action == "paper":
            print("Scissor cuts paper, You win!")
        else:
            print("Rock smashes scissor, You loose!")
    play_again = input("Play again?(Y or N)")
    if play_again != "Y":
        break