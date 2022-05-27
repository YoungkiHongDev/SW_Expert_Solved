# SW Expert Academy 1204. 최빈수 구하기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV13zo1KAAACFAYh&categoryId=AV13zo1KAAACFAYh&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1

'''
테스트케이스별 가장 개수가 많은 값 출력
가장 개수가 많은 값이 여러개면 비교해서 더 큰값 출력
원본 리스트, 중복제거 리스트 2가지를 준비
중복제거 리스트의 값을 하나씩 돌리기
원본 리스트의 가장 많은 값을 갱신하며 보다 큰 값 저장
'''

case = int(input())

for _ in range(case):
    freq_cnt = 0 # 빈도수 저장할 변수
    freq_num = 0 # 빈도수가 가장 큰 값을 저장할 변수
    n = int(input()) # 현재 테스트케이스 번호 입력
    numlist = list(map(int, input().split())) # 원본 리스트 입력
    numset = set(numlist) # set으로 중복 제거
    setlist = list(numset) # 중복제거 리스트 생성
    for s in setlist: # 중복제거 리스트 값을 하나씩 돌리기
        if freq_cnt < numlist.count(s): # 새로운 빈도수가 더 많을 경우
            freq_cnt = numlist.count(s) # 빈도수 저장
            freq_num = s # 값 저장
        elif freq_cnt > numlist.count(s): # 새로운 빈도수가 더 적을 경우 다음 반복문
            continue
        else: # 빈도수가 같을 경우
            if freq_num < s: # 새로운 값이 더 크면 값 저장하고 아니면 다음 반복문
                freq_num = s
            else:
                continue
    print("#{}".format(n), freq_num) # 결과 출력