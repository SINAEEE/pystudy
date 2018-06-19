
"""
#generator : iterator를 생성해주는 함수
#interator는 next()함수를 통해 순차적으로 값을 가져오는 object
#generator는 일반함수와 다를것이 없지만 yield라는 큰 차이점을 가지고 있음
#yield는 n값을 main에 return하고 다시 함수로 돌아가게끔 해준다

def number_generator(n):
    print("Function Start")
    while n<6:
        yield n
        n += 1
    print("Function End")

if __name__ =="__main__":
    for i in number_generator(0):
        print(i)
"""



# yield
# 리스트 1,2,3을 바깥으로 전달
def number_generator2():
    x=[1,2,3]
    for i in x:
        yield i

for i in number_generator2():
    print(i)




"""
import math

#math.ceil : 올림함수
print(math.ceil(-45.7))
print(math.ceil(100.12))
print(math.ceil(100.72))
print(math.ceil(math.pi))
"""