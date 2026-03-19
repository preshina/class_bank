# A program that:

# Computer chooses a random number.

# User tries to guess it.

# Program tells if the guess is too high, too low, or correct.

# import random
# number = random.randint(1, 10)

# attempt = 0

# while True:

#     user_input = int(input("Enter number between 1,10 :"))
#     if user_input < 1 or user_input > 10:
#         print("Please enter number between 1 and 10")
#     attempt += 1
#     if user_input > number:

#         print("Too high!")

#     elif user_input < number:

#         print("Too low")

#     else:
#         print("correct")
#         break
# print(f"you guessed in {attempt} tries!")


# Upgrade the game with difficulty levels.
# Easy → 1–10
# Medium → 1–50
# Hard → 1–100

import random
option = ['Easy', 'Medium', 'Hard']
print(option)
user_enter = str(
    input("Please make a choice of game difficulty from the options :")).lower()
if user_enter == 'easy':
    number = random.randint(1, 10)
elif user_enter == 'medium':
    number = random.randint(1, 50)
elif user_enter == 'hard':
    number = random.randint(1, 100)
else:
    print("Invalid Choices!")
    exit()
print(number)
