#You may use import as below.
#import math

def solution(shirt_size):
    a = [0,0,0,0,0,0]
    for i in shirt_size:
        if i == 'XS':
            a[0]+=1
        elif i == 'S':
            a[1]+=1
        elif i == 'M':
            a[2]+=1
        elif i == 'L':
            a[3]+=1
        elif i == 'XL':
            a[4]+=1
        else:
            a[5]+=1
    answer = a
    return answer

#The following is code to output testcase.
shirt_size = ["XS", "S", "L", "L", "XL", "S"]
ret = solution(shirt_size);

#Press Run button to receive output.
print("Solution: return value of the function is ", ret, " .")