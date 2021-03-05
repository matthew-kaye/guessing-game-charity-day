import random

number = random.randint(1, 9)

def have_a_guess(current_guess_count):
    guess = input("What's your guess?")
    current_guess_count += 1
    if guess == "exit":
        print("Exiting")
        return
    if int(guess) == number:
        print("You got it!")
        print("And it only took you",current_guess_count,"tries!")
        return
    elif int(guess) < number:
        print("Too low!")
    elif int(guess) > number:
        print("Too high!")
    have_a_guess(current_guess_count)
    
have_a_guess(0)
