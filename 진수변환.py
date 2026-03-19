input_a=int(input("입력진수결정(16/10/8/2): "))
input_b=input("값 입력: ")
if input_a==16 :
    num=int(input_b,16)
    
    
    
elif input_a==10 :
    num=int(input_b,10)

elif input_a==8 :
    num=int(input_b,8)
 
elif input_a==2 :
    num=int(input_b,2)

print("16진수 ->",hex(num))
print("10진수 ->",num)
print("8진수 ->",oct(num))
print("2진수 ->",bin(num))

