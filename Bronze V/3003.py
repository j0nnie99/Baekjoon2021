std = [1, 1, 2, 2, 2, 8]
flist = list(map(int, input().split()))
for i in range(6):
    print(std[i] - flist[i], end=" ")