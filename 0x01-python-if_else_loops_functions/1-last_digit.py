#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
nn = number % 10
if nn > 5:
    print(f'Last digit of {number} is {nn} and is greater than 5')
elif nn == 0:
    print(f'Last digit of {number} is {nn} and is 0')
else:
    print(f'Last digit of {number} is {nn} and is less that 6 and not 0')
