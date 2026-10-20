import random

LOW = 1
HIGH = 100


def you_guess():
    print("\nYOU GUESS")
    print("I'm thinking of a number between", LOW, "and", HIGH)
    secret = random.randint(LOW, HIGH)
    tries = 0

    while True:
        tries = tries + 1
        guess = int(input("Your guess #" + str(tries) + ": "))

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print("Correct! You got it in", tries, "tries.")
            return tries


def computer_guesses():
    print("\nCOMPUTER GUESSES")
    secret = int(input("Pick a secret number between " + str(LOW) + " and " + str(HIGH) + ": "))
    tries = 0

    while True:
        tries = tries + 1
        guess = random.randint(LOW, HIGH)
        print("Computer guess #" + str(tries) + ":", guess)

        answer = input("higher / lower / yes: ").strip().lower()

        if answer == "yes":
            if guess == secret:
                print("Computer got it in", tries, "tries!")
            else:
                print("Wait, your secret was", secret, "but I said", guess)
            return tries
        elif answer == "higher":
            pass
        elif answer == "lower":
            pass        
        else:
            print("Please type higher, lower, or yes.")


def main():
    print("GUESS THE NUMBER")
    print("You vs. the computer. Both guess randomly!\n")

    choice = input("Who starts? (you / computer): ").strip().lower()

    if choice == "you" or choice == "me":
        your_tries = you_guess()
        computer_tries = computer_guesses()
    elif choice == "computer":
        computer_tries = computer_guesses()
        your_tries = you_guess()
    else:
        print("Please type 'you' or 'computer'.")
        return

    print("\nRESULTS")
    print("You took      ", your_tries, "tries")
    print("Computer took ", computer_tries, "tries")

    if your_tries < computer_tries:
        print("You win!")
    elif computer_tries < your_tries:
        print("Computer wins!")
    else:
        print("It's a tie!")


if __name__ == "__main__":
    main()