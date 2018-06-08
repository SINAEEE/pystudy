


num = input("숫자를 입력하세요 : ")
#print(type(num))

if num.isdigit():
    r=int(num)
    if(r%3==0):
        print("3의 배수입니다.")
    else:
        print("3의 배수가 아닙니다.")
else:
    print("정수가 아닙니다.")








    