S = list(input())
for i in range(len(S)):
    S[i] = ord(S[i])

print(S)

for i in range(97, 123):
    if i in S:
        print(i)
    else:
        print(-1)