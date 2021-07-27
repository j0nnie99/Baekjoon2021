toSch = int(input())
toPc = int(input())
toAcd = int(input())
toHome = int(input())

total = toAcd + toPc + toHome + toSch
m = total//60
s = total%60

print(m)
print(s)