A = int(input())
B = int(input())
C = int(input())
multi = str(A * B * C)
for i in range(0, 10):
    print(list(multi).count(str(i)))