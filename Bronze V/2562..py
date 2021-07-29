num = []
max_num = 0
max_index = 0

for i in range(9):
    n = int(input()) 
    num.append(n)

for i in range(0, len(num)):
    if max_num < num[i]:
        max_num = num[i]
        max_index = i+1

print(max_num)
print(max_index)
#max와 index 없이 풀 수 있지 않을까

