# SW Expert Academy 14361. 숫자가 같은 배수
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AYCnY9Kqu6YDFARx

'''
같은 자리수의 모든 조합과 원래 숫자를 한번씩 비교
재배열 숫자 중 더 큰 배수가 있으면 possible
그렇지 않으면 impossible
'''

from itertools import permutations # 한 리스트에서 모든 조합을 구하기 위한 라이브러리

n = int(input()) # 입력할 숫자의 개수 입력받기

for i in range(1, n+1): # 숫자 개수만큼 반복
    check = 0 # 숫자가 possible이였는지 체크할 변수
    number = list(map(int, input().rstrip())) # 정수를 자리수별로 잘라서 리스트로 입력받기
    numset = int(''.join(map(str, number))) # 정수 리스트를 하나로 합친 원래 숫자
    combine = list(permutations(number, len(number))) # 정수 자리수와 같은 길이의 모든 조합 구하기 (리스트 안의 튜플 구조)
    for j in range(len(combine)): # 조합 개수만큼 반복
        target = int(''.join(map(str, combine[j]))) # 조합을 합쳐서 숫자로 만들어주기
        if target > numset and target % numset == 0: # 조합이 원래 숫자보다 크고 나눠서 나머지가 0인 조건을 만족해 배수로 판정날 경우
            print("#{}".format(i), "possible") # 입력된 순서와 possible 출력
            check = 1 # possible 체크
            break # 배수 판별이 끝났으므로 탈출
    if check == 0: # possible이 아니였을 경우
        print("#{}".format(i), "impossible") # 입력된 순서와 impossible 출력