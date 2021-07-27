#평균값(avg, 올림) = 저작권멜로디수/앨범수록곡수(t)
t, avg = map(int, input().split())
total = (t * (avg-1)) + 1
print(total)