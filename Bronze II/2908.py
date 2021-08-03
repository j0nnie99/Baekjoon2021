A, B = map(int, input().split())
A = str(A)
As = int(A[2]+A[1]+A[0])
B = str(B)
Bs = int(B[2]+B[1]+B[0])
if As > Bs:
    print(As)
else:
    print(Bs)