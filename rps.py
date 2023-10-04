import random
from enum import Enum
import sys

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playerpoint = 0
computerpoint = 0

print("")
print("Welome to Rock, Paper, Scissors game".center(50, '-'))
value = input("Press enter to play the game".center(50, '-'))
print(value)
if value != '':
    sys.exit("Thank you!!Let's play after some time")

while (playerpoint < 5) and (computerpoint < 5):
    print("")
    playerchoice = input("Enter ... \n1 for Rock,\n2 for Paper, or\n3 for Scissors.\n\n")
    player = int(playerchoice)
    print("")
    computerchoice = random.choice("123")
    computer = int(computerchoice)

    print("Your choice " + str(RPS(player)).replace("RPS.", "") + ".")
    print("Python choice " + str(RPS(computer)).replace("RPS.", "") + ".")

    if player == 1 and computer == 3:
        playerpoint+=1
        print("Player point: " + str(playerpoint) + "\nComputer point: " + str(computerpoint))
    elif player == 2 and computer == 1:
        playerpoint+=1
        print("Player point: " + str(playerpoint) + "\nComputer point: " + str(computerpoint))
    elif player == 3 and computer == 2:
        playerpoint+=1
        print("Player point: " + str(playerpoint) + "\nComputer point: " + str(computerpoint))
    elif player == computer:
        print("Game drawn!")
        print("Player point: " + str(playerpoint) + "\nComputer point: " + str(computerpoint))
    else:
        computerpoint+=1
        print("Player point: " + str(playerpoint) + "\nComputer point: " + str(computerpoint))

print("")
print("Result".center(20, "="))

if playerpoint == 5:
    print("WOW, You won!")
if computerpoint == 5:
    print("Python won! Better luck next time")
    