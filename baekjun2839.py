kg_inpt = int(input())

kg = kg_inpt

kg_5 = 0
kg_3 = 0

if kg % 5==0:
    print(kg//5)
else:
    while(True):
        if kg <= 0:
            break
        if kg %5 == 3 and kg !=3:
            kg -= 5
            kg_5+=1
        else:
            kg-=3
            kg_3+=1
        
    if kg_5 * 5 + kg_3 * 3 == kg_inpt:
        print(kg_5+kg_3)
    else:
        print(-1)



# kg_5 = 0
# kg_3 = 0

# kg_change = kg

# if kg_change % 5  == 0:
#     print(kg_change//5)
# else:
#     while(True):
#         if kg_change >= 5:
#             kg_change -= 5
#             kg_5+=1
#             if kg_change % 3==0 and kg_change % 5 <3:
#                 break
#         else:
#             if kg_change % 3 !=0:
#                 if kg_5 !=0:
#                     kg_5-=1
#                 kg_change+=5
#             break

#     while(True):
#         if kg_change >= 3:
#             kg_change -=3
#             kg_3+=1
#         else:
#             break
#     print(kg_5)
#     print(kg_3)
#     if kg_5 * 5 + kg_3 * 3 == kg:
#         print(kg_5+kg_3)
#     else:
#         print(-1)        