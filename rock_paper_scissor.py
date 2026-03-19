import random
list = ["rock", "paper", "scissor"]
guess = random.choice(list)
print(guess)
user_input = str(input("enter your choice :")).lower()
if guess == 'rock':
    if user_input == 'rock':
        print("tie")
    elif user_input == 'paper':
        print("u win!")
    elif user_input == 'scissor':
        print("u loose!")
    else:
        print("invalid input!")
if guess == 'paper':
    if user_input == 'rock':
        print("u loose")
    elif user_input == 'paper':
        print("tie")
    elif user_input == 'scissor':
        print("u win!")
    else:
        print("invalid input!")

if guess == 'scissor':
    if user_input == 'rock':
        print("u win!")
    elif user_input == 'paper':
        print("u loose!")
    elif user_input == 'scissor':
        print("Tie")
    else:
        print("invalid input!")
