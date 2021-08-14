S = list(input())
alpahbet = list('abcdefghijklmnopqrstuvwxyz')
dic = {}

#a-z 딕셔너리에 대한 value값 -1로 초기화
for i in alpahbet:
    dic[i] = -1

#처음 등장하는 위치를 dic[i]값에 저장
for i in S:
    if dic[i] == -1:
        dic[i] = S.index(i)

#value값 출력
for i in dic:
    print(dic[i], end=" ")