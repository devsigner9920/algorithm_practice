K = int(input())
number = []

for i in range(K):
    num = int(input())
    if num == 0:
        number.pop()
    else:
        number.append(num)

result = sum(number)
print(result)