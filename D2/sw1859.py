# SW Expert Academy 1859. 백만 장자 프로젝트
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5LrsUaDxcDFAXc&categoryId=AV5LrsUaDxcDFAXc&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1&&&&&&&&&&

'''
1. 원재는 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있다.
2. 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입할 수 있다.
3. 판매는 얼마든지 할 수 있다.

예를 들어 3일 동안의 매매가가 1, 2, 3 이라면
처음 두 날에 원료를 구매하여
마지막 날에 팔면 3의 이익을 얻을 수 있다.
'''

'''
10 7 6
      +0

3 5 9
6 4 S +10

1 1 3 1 2
2 2 S 1 S +5

배열의 뒤부터 큰 값을 찾고 그 뒤 더 큰 값이 나올떄까지 누적시키면 답이 나옵니다.

1 1 3 1 2
    3
        2
2  2  1  
'''

n = int(input()) # 테스트 케이스 수 입력

for i in range(1, n+1): # 테스트 케이스 수 만큼 반복
    sell = 0 # 판매 이익을 저장할 변수 초기화
    numlen = int(input()) # 테스트 케이스의 길이 입력
    numlist = list(map(int, input().split())) # 테스트 케이스 값 입력
    num = numlist[numlen-1] # numlist의 마지막의 값 저장
    for j in range(numlen-2, -1, -1): # numlist 마지막 전 값부터 역순 순회
        if num < numlist[j]: # 새로운 값이 더 크면 교체
            num = numlist[j]
        elif num > numlist[j]: # 저장된 값이 더 크면 차이만큼 플러스
            sell += (num - numlist[j])
    print("#{}".format(i), sell) # 판매 이익 출력