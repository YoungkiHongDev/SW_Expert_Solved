# SW Expert Academy 1206. View
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV134DPqAA8CFAYh&categoryId=AV134DPqAA8CFAYh&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1

'''
왼쪽 2칸, 오른쪽 2칸이 비어있으면 조망권 확보
0 0 2 0 0 -> 2개
1 1 2 1 1 3 1 1 -> 3개
왼쪽 2건물, 오른쪽 2건물보다 현재 건물이 크면
왼쪽, 오른쪽 건물 중 가장 큰 건물과 현재 건물 비교해서 더 높은 만큼 저장
'''

t = 10

for i in range(1, t+1):
    clear = 0
    n = int(input())
    building = list(map(int, input().split()))
    for j in range(2, n-2):
        if building[j-2] < building[j] and building[j-1] < building[j] and building[j] > building[j+1] and building[j] > building[j+2]:
            clear += building[j] - max(building[j-2], building[j-1], building[j+1], building[j+2])
    print("#{}".format(i), clear)