inpt = list(map(int,input().split(' ')))

sum = 0

for i in range(inpt[0],inpt[1]+1):
    div = 2
    dec = []
    sosu=0
    while div<=i:
        if i% div==0:
            dec.append(div)
            i/=div
        else:
            div+=1
    div = 2
    dec_len = len(dec)
    if dec_len==1:
        continue
    else:
        for j in range(2,dec_len):
            if dec_len%j == 0:
                sosu=1
        if sosu != 1:
            sum+=1
print(sum)