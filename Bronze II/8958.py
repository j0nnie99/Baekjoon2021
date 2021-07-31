n = int(input())

for i in range(n):
    count = 0
    sum = 0
    result = list(input())
    for j in range(len(result)):
        if result[j] == "O":
            count += 1
            sum += count
        elif result[j] == "X":
            count = 0
    print(sum)
