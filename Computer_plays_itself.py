import random

options = ["rock", "paper", "scissors"]


counter = 0

score1 = 0
score2 = 0

while score1 < 2 and score2 <2:
    player1 = random.choice(options)
    player2 = random.choice(options)
    print(f"Player 1: {player1}")
    print(f"Player 2: {player2}")
    counter += 1
    if player1 == player2:
        print("It's a Draw!")
    elif player1 == "rock":
        if player2 == "scissors":
            print ("Rock breaks scissors, Player 1 wins!")
            score1 += 1
        else:
            print("Paper covers rock, Player 2 wins!")
            score2 += 1
    elif player1 == "scissors":
        if player2 == "rock":
            print("Rock breaks scissors, Player 2 wins!")
            score2 += 1
        else:
            print("Scissors cut paper, Player 1 wins!")
            score1 += 1
    elif player1 == "paper":
        if player2 == "rock":
            print("Paper covers rock, Player 1 wins!")
            score1 += 1
        else:
            print("Scissors cut paper, Player 2 wins!")
            score2 += 1

print(f"Score: Player 1: {score1}, Player 2: {score2}")
print(f"How many games? {counter}")
