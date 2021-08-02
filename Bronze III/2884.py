H, M = map(int, input().split())
if M < 45:
    if (H == 0):
        print("23 " + str(M+15))
    else:
        print(str(H-1) + " " + str(M+15))
else:
    print(str(H) + " " + str(M-45))