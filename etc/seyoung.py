#2> (Dictionary and loop) Write a Python script to generate and print a dictionary
#that contains a number (between 1 and n) in the form (x, x*x).
#Sample Dictionary ( n = 5) :
#Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#n 입력 받기
#key 1~n
#value 1~n*n
n = int(input())
dic = {}
for i in range(1,n+1):
    dic[i] = i*i
print(dic)
