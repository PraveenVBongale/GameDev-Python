import random

guess = []

myComputer = random.randint(1,70)

player = int (input("Enter a Number between 1 to 70"))
guess.append(player)

while player != myComputer:
    if player > myComputer:
        print("Number is too high")
    else:
        print("Number is too low")

    player = int(input("Enter a Number Between 1 to 70"))
    guess.append(player)

else:
    print("You have guessed right, Good Job")
    print("It took you %l guess" %len(guess))
    print("These were your guess")
    print(guess)
