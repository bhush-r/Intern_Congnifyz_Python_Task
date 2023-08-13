import random

print("🎯Welcome to the Number Guesser Game! ")
print("Please Type Range 1 to 100 ")

lower_bond = int(input("Enter First Range = "))
upper_bond = int(input("Enter Second Range = "))
pc_number = random.randint(lower_bond,upper_bond)

while True:
    try:
        uGuess = int(input(f"Guess a number between {lower_bond} and {upper_bond}: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
    if uGuess == pc_number:
        print (f"🎉Congratulation ! You guessed the correct number {pc_number}. ")
        break
    elif uGuess < pc_number:
        print("Too low! Try again. 📉")
    else:
        print("Too high! Try again. 📈")