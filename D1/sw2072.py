# SW Expert Academy 2072. 홀수만 더하기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QSEhaA5sDFAUq&categoryId=AV5QSEhaA5sDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=1&&&&&&&&&&

t = int(input())

for i in range(1, t+1):
    sum = 0
    numlist = list(map(int, input().split()))
    for num in numlist:
        if num % 2 != 0:
            sum += num
    print("#{}".format(i), sum)