import random

print("Its your turn choose what you want to play.")
print("Rock, Papper, Scissors")
  
player_1 = input()

player2_Choice = random.randint(1,3)

player2 = ""
if player2_Choice == 1:
    player2 = "Scissors"
elif player2_Choice == 2:
     player2 = "Rock"
else:
     player2 = "Papper"

win_count = {'player_1': 0, 'player_2': 0}



for win in win_count:
     win_count += win
