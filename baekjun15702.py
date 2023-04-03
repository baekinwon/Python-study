# 문제 개수 N 응시자 수 M 입력
nm = list(map(int,input().split(" ")))
n = nm[0]
m = nm[1]



# 문제의 배점
point = list(map(int,input().split(" ")))

stu = []

# 응시자 정보
for j in range(m):
    st = input().split(" ")
    st[0] = int(st[0])
    stu.append(st)

sum = []
sum_point = 0

# 점수체크
for i in range(m):
    for j in range(n):
        if stu[i][j+1] == "O":
            sum_point+=point[j]
    sum.append(sum_point)
    sum_point = 0

lage_point = sum[0]
lage_stu = stu[0][0]

# 출력
for i in range(m):
    if lage_point ==sum[i]:
        if lage_stu > stu[i][0]:
            lage_stu = stu[i][0]
    elif lage_point < sum[i]:
        lage_point = sum[i]
        lage_stu = stu[i][0]
print(lage_stu, lage_point)