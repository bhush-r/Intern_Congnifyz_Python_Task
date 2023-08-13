import random

random_num = random.randint(1, 100)
print(" 🎯 Welcome to the Guessing Game! 🎲")
name = input("Enter Name = ")

uGuess = int(input(f"{name} Guess a number between 1 and 100: "))

while uGuess != random_num:
        if uGuess < random_num:
            print("Your guess number is too low! 📉")
        elif uGuess > random_num:
            print(" Your guess number is Too high!  📈")
        uGuess = int(input("Guess again: "))

print(f"Congratulations! {name} 🎉 You guessed the correct number!")
print("Computer Number =",random_num)




