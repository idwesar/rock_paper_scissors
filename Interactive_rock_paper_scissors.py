import random

while True:
    score1 = 0
    score2 = 0
    counter = 0

    while score1 < 2 and score2 < 2:
        player1 = input("Enter a choice (rock, paper, scissors): ")
        possible_actions = ["rock", "paper", "scissors"]
        player2 = random.choice(possible_actions)
        print(f"\nYou Chose {player1}, computer chose {player2}.\n")

        if player1 == player2:
            print(f"It's a Draw! Both players selected {player1}!")
        elif player1 == "rock":
            if player2 == "scissors":
                print ("Rock breaks scissors, You win!")
                score1 += 1
            else:
                print("Paper covers rock, Computer wins!")
                score2 += 1
        elif player1 == "scissors":
            if player2 == "rock":
                print("Rock breaks scissors, Computer wins!")
                score2 += 1
            else:
                print("Scissors cut paper, You win!")
                score1 += 1
        elif player1 == "paper":
            if player2 == "rock":
                print("Paper covers rock, You win!")
                score1 += 1
            else:
                print("Scissors cut paper, Computer wins!")
                score2 += 1
        print(f"{score1}:{score2}")
        counter +=1

    play_again = input("Play again? ")
    if play_again != "yes":
        break
