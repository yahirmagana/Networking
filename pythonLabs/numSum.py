#!/usr/bin/python
import os
import sys

n = int(input("Enter a positive number: "))

total_sum = sum(range(1, n + 1))

if total_sum % 2 == 0:
    check = "EVEN"
else:
    check = "ODD"

print("You entered: {}".format(n))
print("The sum of numbers form 1-{} is: {}".format(n, total_sum))
print("The sum ({}) is an {} number.".format(total_sum, check))
