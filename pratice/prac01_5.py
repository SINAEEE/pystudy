

num=input("금액 : ")
num=int(num)


if(num/50000 !=0):
    c1=num/50000
    num= num-(5000*c1)
    if(num/10000 !=0):
        c2=num/10000
        if(num/5000 !=0):
            c3=num/5000
            if(num/1000):
                c4=num/1000

print("50000원 : ", c1)
#print("10000원 : ", c2)
#print("5000원 : ", c3)
#print("1000원 : ", c4)


