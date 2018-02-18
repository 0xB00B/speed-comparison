#!/usr/bin/env python
# coding=utf-8
import os


with open("rounds.txt") as file:
    rounds = int(file.read())

x = 1
pi = 1

for i in range(2, rounds + 2):
    x *= -1
    pi += x / (2 * i - 1)

pi *= 4

print("π = {0}".format(pi))

