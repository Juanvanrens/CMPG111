import random
def guess_number():

    num = random.randint(1,100)

    guess = int(input("Guess number between 1 - 100 (or 0 to quit): "))
    counter = 1
    while guess != num and guess != 0:

        if guess > num:
            print("Your guess is too high")
            guess = int(input("Guess number between 1 - 100 (or 0 to quit): "))
        elif guess < num:
            print("Your guess is too low")
            guess = int(input("Guess number between 1 - 100 (or 0 to quit): "))

        counter += 1
    if guess == num:
        print(f"You guessed the number in {counter} attempts!")

guess_number()
