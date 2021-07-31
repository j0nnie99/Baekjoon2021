num = list(map(int, input().split()))
lst = [1, 2, 3, 4, 5, 6, 7, 8]
if (num == lst):
    print("ascending")
elif (num == list(reversed(lst))):
    print("descending")
else:
    print("mixed")