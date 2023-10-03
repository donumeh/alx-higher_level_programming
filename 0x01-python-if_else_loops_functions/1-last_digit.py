#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

new_number = number
if number < 0:
    new_number = -number

last_digit = new_number % 10
if number < 0:
    last_digit = -last_digit
print(f"Last digit of {number:d} is {last_digit:d} and is", end=" ")

if last_digit > 5:
    print(f"greater than 5")
elif last_digit == 0:
    print(f"0")
elif last_digit < 6 and last_digit != 0:
    print(f"less than 6 and not 0")
