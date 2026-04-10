import random

print(" ** 로또 추첨을 시작합니다 **")

random.randrange(1,46)
     
lotto=[]

while len(lotto)<6:
    number=random.randrange(1,46)
    if lotto.count(number)==0 :
        lotto.append (number)
    elif lotto.count(number)>=1 :
        continue
lotto.sort()
print("추첨된 로또 번호 ==> ",end="")
for i in range (6):
    print(lotto[i],end=" ")


