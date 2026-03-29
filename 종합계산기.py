a = int(input("1.입력한 수식 계산  2.두 수 사이의 합계 : "))
if a == 1 :
    b = input("*** 수식을 입력하시오")
    c = eval(b)
    print(b,"결과는",c,"입니다")

elif a == 2:
    b=int(input("***첫번째 숫자를 입력하시오"))
    c=int(input("***두번째 숫자를 입력하시오"))
    d=0
    for i in range (b,c+1) :
        d = d + i
    print(b,"+..+",c,"는",d,"입니다")