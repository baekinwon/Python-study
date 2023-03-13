inpt = int(input()) # 테스트 케이스 개수를 정수형으로 받음
a = list() # 빈 리스트 생성
c = list()
for i in range(inpt): # 입력받은 값 만큼 반복
    b = input().split() # 학생의 수와 점수를 입력받음
    b = list(map(int,b)) # 받은 값을 정수형으로 모두 변환함
    c.append(b) # 받은 값을 c 리스트 안에 저장함 2차원 배열로 저장됨

stu = 0
for j in c: # j 변수에 리스트가 하나씩 전달됨
    sum = 0
    avrage = 0
    for x in j[1:]: # x에 학생의 점수만 들어감
        sum+=x # 점수 모두 더함
    avrage = sum/j[0] # 평균 구함
    for z in j[1:]:
        if z > avrage: # 평균 보다 많은 점수를 받은 학생 수를 stu변수에 더함
            stu +=1
    print("{:.3f}%".format((stu/j[0])*100)) # 백분율로 평균 보다 많은 점수를 받은 학생의 비율을 구함
    stu = 0 # 변수 초기화
    


