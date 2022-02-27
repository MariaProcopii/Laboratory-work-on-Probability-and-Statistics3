import random

game = 10000
winA = winB = winC = winD = 0
for i in range(game):
    a = random.uniform(-10, 10)
    b = random.uniform(0, 10)
    if a >= 0 and b >= 0:
        winA += 1
    if -5 < a < 5 and b < 5:
        winB += 1
    if -5 <= a <= 5 and 0 <= b <= 10:
        winD += 1
probA = winA/game
probB = winB/game
probC = 1 - probB
probD = winD/game
print(probA, probB, probC, probD)
