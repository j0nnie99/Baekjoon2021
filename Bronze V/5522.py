score = [0]*5
for i in range(5):
    score[i] = input()
sum = 0
for i in range(5):
    sum += int(score[i])
print(sum)