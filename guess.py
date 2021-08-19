import random
random_num = random.randint(1,10)
print(random_num)

guess = None

while True:
    guess = input("Guess a number between 1-10: ")
    guess = int(guess)
    if guess == random_num:
        print("You won!")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again == "y":
            random_num = random.randint(1,10)
            guess = None
        else:
            print("quitting")
            break