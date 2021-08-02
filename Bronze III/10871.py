N, X = map(int, input().split())
num = list(map(int, input().split()))
sNum = []
for i in range(0, N):
    if num[i] < X:
        sNum.append(num[i])

for i in range(len(sNum)):
    print(sNum[i], end=" ")    