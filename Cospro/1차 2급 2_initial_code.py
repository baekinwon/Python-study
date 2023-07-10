#You may use import as below.
#import math

def solution(price, grade):
    if grade == 'S':
        min = price*0.05
    elif grade =='G':
        min = price*0.1
    else:
        min = price*0.15
    answer = price - min
    return int(answer)

#The following is code to output testcase.
price1 = 2500
grade1 = "V"
ret1 = solution(price1, grade1)

#Press Run button to receive output.
print("Solution: return value of the function is", ret1, ".")
    
price2 = 96900
grade2 = "S"
ret2 = solution(price2, grade2)

#Press Run button to receive output.
print("Solution: return value of the function is", ret2, ".")