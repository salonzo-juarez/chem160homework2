from random import choices
nrolls = 10000
player1wins = 0
player2wins = 0
n1dice = 2
n2dice = 3
for i in range(nrolls):
    dice = choices(range(1, 7), k=n1dice)
    dice.sort(reverse=True)
    player2wins = player2wins+dice[0]+dice[1]
for j in range(nrolls):
    dice = choices(range(1, 7), k=n2dice)
    dice.sort(reverse=True)
    player1wins = player1wins+1+dice[0]+dice[1]
print("Average roll=", player2wins/nrolls, player1wins/nrolls)