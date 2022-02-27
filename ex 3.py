import random

arr = []
win = 0
game = 10000
for i in range(100):
    arr.append(i + 1)
for _ in range(game):
    for i in arr:
        a = random.randint(1, 100)
        if i == 1:
            a = random.randint(2, 100)
        if a == i:
            win += 1
            break

print(win/game)