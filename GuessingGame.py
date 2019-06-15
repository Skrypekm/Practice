import random

# generates a random number between 1 and 9
secretNumb = random.randint(1, 9)

guessCount = 0
guessLimit = 3
goAgain = True

while goAgain:
    print("Guess a number between 1 and 9")
    while guessCount < guessLimit:
        guess = int(input("Enter your guess: "))
        guessCount += 1
        if guess == secretNumb:
            print(F"You guess correct. The number was {secretNumb}")
            break
        elif guess > secretNumb:
            print("Your guess was too high")
        elif guess < secretNumb:
            print("Your guess was too low")

        if guessCount == guessLimit:
            print(F"Too many tries. The number was {secretNumb}")

    print("Game over")
    i = input("Would you like to go again (y/n): ")
    if i.upper() == "N":
        goAgain = False

exit(0)
