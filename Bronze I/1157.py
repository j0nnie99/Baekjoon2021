#어렵다 어려워...
s = input()
s = s.upper()
counts = {}

maxString = 0 #가장 많이 사용된 알파벳
maxCount = 0 #사용횟수

for i in s:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1

for i in counts:
    if counts[i] > maxCount:
        maxCount = counts[i]
        maxString = i
    elif counts[i] == maxCount:
        maxString = "?"

print(maxString)
