import random
count = 0
name = input("Hello! What is your name??\n")
num = random.randint(1, 20)

print("Well,{} ,I am thinking of a number between 1 and 20.".format(name))
while count < 20:
    guess = int(input('Number: '))
    count += 1
    if guess < num:
        print ("Your guess is too low.")

    if guess > num:
        print ("Your guess is too big.")

    if guess == num:
        print ("Good job, {0}!,You guessed my number in {1} guesses!".format(name, count))
        break