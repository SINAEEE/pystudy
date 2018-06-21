


num=[]
print("5개의 정수를 입력하세요 : ")
for i in range(0,5,1):
    num.append(input())
    
total=0
i=0

print(num)
print(type(num))



for i in num:
   total += num

print(total)



