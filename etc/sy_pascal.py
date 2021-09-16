n = int(input()) #실행횟수(출력되는 라인의 수)
list=[1] #초기 리스트
for i in range(n): #list를 n번 출력
    print(list) 
    newlist=[] #연산 결과를 넣을 새로운 list 생성
    newlist.append(list[0]) #newlist에 list의 첫 번째 값 넣기
    for i in range(len(list)-1):  #8번째 줄을 0~(i-1)번 실행 => i와 i+1의 연산이기 때문에 i까지가 아니라 i-1번째까지
        newlist.append(list[i]+list[i+1]) #i번째 값과 i+1번째 값을 더하여 newlist의 값에 추가
    newlist.append(list[-1]) #newlist 마지막 값으로는 list의 마지막 원소를 넣어줌 => "마지막 원소 + 0 = 마지막 원소"이므로 계산을 생략하고 바로 append
    list=newlist #list를 새롭게 만들어낸 newlist로 갱신 => 이후 4번째 줄의 print(list)를 통해 출력
    #print(list)가 하단에 있으면 초기 리스트인 [1] 출력이 생략되므로 최상단에서 출력 한번 하고 나서, 연산 들어감