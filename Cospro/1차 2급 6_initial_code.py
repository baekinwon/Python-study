def solution(number):
    count = 0
    for i in range(1, number + 1):
        current = i
        temp = count
        while current != 0:
            if current%10==3:
                count += 1
                print("pair", end = '')
            current = current // 10
        if temp == count:
            print(i, end = '')
        print(" ", end = '')
    print("")
    return count

#The following is code to output testcase.
number = 40
ret = solution(number)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")