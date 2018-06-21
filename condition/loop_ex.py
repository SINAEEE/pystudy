#loop_ex.py

# for : for ... in (객체)
print()
for i in range(1,10,2):
    print(i,end=",")
else: #루프가 중료없이 끝났을 때
    print()


# 시퀀스 객체를 이용한 for문
print()
animals = ['dog', 'cat','cow','tiger']
for animal in animals:
    print(animal,end=",")
else:
    print()


#enumerate를 이용한 루프
print()
for index,value in enumerate(animals):
    print(index, value)


#while문
print()
sum, i = 0, 1

while i <= 1000:
    sum += i
    i += 1

print("합계는 : ", sum)




