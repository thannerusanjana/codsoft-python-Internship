import random

print(" Welcome to Rock-Paper-Scissors!")

options = ["rock", "paper", "scissors"]

while True:
    user = input("\nEnter rock, paper, or scissors: ").lower()

    if user not in options:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(options)

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win! ")

    else:
        print("Computer wins! ")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
