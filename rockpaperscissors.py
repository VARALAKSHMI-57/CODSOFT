import random
print(" ROCK PAPER SCISSORS GAME ")
print("Instructions:")
print("1. Choose rock, paper, or scissors")
print("2. Rock beats Scissors")
print("3. Scissors beats paper")
print("4. Paper beats Rock")
print("5. Type 'exit' anytime to quit")
choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
tie_score = 0
while True:
    user_choice = input("Enter your choice (rock/paper/scissors):").lower()
    if user_choice == "exit":
        print("\nThanks for playing!")
        break
    if user_choice not in choices:
        print("Invalid choice! Please enter rock,paper, or scissors.\n")
    computer_choice = random.choice(choices)
    print(f"\nYou chose     : {user_choice}")
    print(f"Computer chose  : {computer_choice}")
    if user_choice == computer_choice:
       print("Result: It's a Tie")
       tie_score += 1
    elif (
        (user_choice == "rock" and computer_choice == "scissors")or
        (user_choice == "paper" and computer_choice == "rock")or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
         print("Result: You Win!")
         user_score += 1
    else:
        print("Result: Computer Wins!")
        computer_score += 1
    print("\n========= SCORE BOARD =========")
    print(f"Your Score     : {user_score}")
    print(f"Computer Score : {computer_score}")
    print(f"Ties           : {tie_score}")
    print("===================================")
    play_again = input("Do you want to play again? (yes/no): ").lower()         
    if play_again != "yes":
        print("\nFinal Scores:")
        print(f"Your Score       : {user_score}")
        print(f"Computer Score   : {computer_score}")
        print(f"ties             : {tie_score}")
        print("\nThank you for playing the game!")
        break