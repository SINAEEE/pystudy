

lst = [1,2,3,4,5,6,7,8,9,10,15]

c=0
t=0
for i in lst:
    if(i%3==0):
        c += 1
        t += i
    else:
        continue

print("3의 배수의 개수 : ",c)
print("3의 배수의 합 : ",t)


