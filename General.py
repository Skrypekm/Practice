import math
import random


secretNumb = random.randint(1, 9)

guessCount = 0
guessLimit = 3

while guessCount < guessLimit:
    guess = int(input("Enter your guess: "))
    guessCount += 1
    
