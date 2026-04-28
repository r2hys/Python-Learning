import random 

roll = random.randint(1,6)

#randint outputs a random integer between the two or more given values

guess = int(input("Guess the dice roll. The Numbers are between 1 and 6:\n"))

if guess == roll:
    print("You have guessed correctly!")
else:
    print("Unlucky, the number actually was " + str(roll))

