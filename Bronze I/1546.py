N = int(input())
scores = list(map(int, input().split()))
M = scores[0]
sum = 0

for i in scores:
    if i > M:
        M = i

for i in range(N):
    ns = scores[i]/M*100
    sum += ns

avg = sum/N
print(avg)