import random

# b^2 - 4ac > 0 -> 16U^2 - 4 > 0 -> U > 1/2
win = 0
for _ in range(10000):
    a = random.uniform(0, 1)
    if a > 1/2:
        win += 1
prob = win/10000
print(prob)