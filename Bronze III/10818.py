N = int(input())
num = list(map(int, input().split())) #이렇게 하면 N을 받는 의미가 없어지는데?
max_num = num[0]
min_num = num[0]
for i in range(len(num)):
    if max_num < num[i]:
        max_num = num[i]
    elif min_num > num[i]:
        min_num = num[i]
print(str(min_num) + " " + str(max_num))
    