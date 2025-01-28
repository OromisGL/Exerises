import random

money = 1000
rounds = 1000

for current_round in range(rounds):
    stake = 1 # stake per round
    money -= stake # player pays stake

    # allright partner, keep on rolling!
    dice  = [random.randint(1, 6) for _ in range(3)]

    # check if there is at least one six
    six = dice.count(6)

    if six > 0:
        money += stake # get stake back
        money += six # profit for rolled six

# Result
print(f"Nach {rounds} Runden beträgt das Kapital: {money} Euro")