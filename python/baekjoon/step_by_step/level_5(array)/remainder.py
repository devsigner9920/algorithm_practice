from sys import stdin

x = [int(stdin.readline().rstrip()) % 42 for _ in range(10)]

print(len(set(x)))