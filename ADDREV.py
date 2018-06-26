import sys



test = int(sys.stdin.readline())


for j in range(test):
    a,b = input().split()
    a,b = a[::-1],b[::-1]

    result = str(int(a) + int(b))
    result = result[::-1]
    print(int(result))