import random
import sys
import os

tested_string = "ABX"
alphabet = [0] * 256
ind = 0
flague = 0

for i in range(0, len(tested_string)):
    ind = ord(tested_string[i])
    alphabet[ind] += 1
    if alphabet[ind] == 2:
        print(chr(ind))
        flague = 1
        break

if flague == 0:
    print("No recurrent characters found")
