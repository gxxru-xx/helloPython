import sys
import random


'''inicjalizacja'''
prompt = "xxx"
min = 1
max = 6
random.seed()

'''glowna petla'''
'''
while True:
    print("Podaj zakres: ")
    min, max = map(int, sys.stdin.readline().split())
    print(int(random.random()*(max-min)+min))
    print("Chcesz kontynować? (wpisz 'n' w celu zakonczenia")
    if input()=='n':
        break
'''

'''alternatywne rozwiazanie'''
while True:
    try:
        line = input("Podaj zakres: ").split()
        min, max = int(line[0]), int(line[1])
        print(int(random.random() * (max - min) + min))
    except ValueError:
        print("Oops! Wymagany format zakresu to: 'int' 'int'. Sprobuj ponownie...")
'''    except EOFError:
        break
    except:
        print("Oops! Wymagany format zakresu to: 'int' 'int'. Sprobuj ponownie...")'''
