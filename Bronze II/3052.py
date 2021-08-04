num = []
count = 0
for i in range(10):
    n = int(input())
    resultN = n % 42
    if resultN not in num:
        count += 1
    num.append(resultN)
print(count)