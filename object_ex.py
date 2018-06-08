#object_ex.py

print(id(3)) #id:객체의 주소를 반환하는 메서드

# '변수에 3을 담는다' 의 의미
# 3 객체를 만들고
# 변수에 3객체의 ID를 연결, 심볼 테이블에 저장하는것

a=3
# a의 ID값을 확인 해봅시다.
print("id a : ", id(a))

b=3
print("id b : ", id(b))

b=4
print("id b : ", id(b))


# 객체 심볼 테이블
g_a = 2018
g_b = "Symbol"

#글로벌 영역

print()
def f(): #로컬 영역 변수 확인을 위한 함수
    l_a = "local"
    l_b = 5
    print(locals()) #로컬 스코프의 심볼 테이블

print()
print("=============== : Local")
f()
print("=============== : Global")
print(globals())

print("f" in globals().keys())

# 객체 복사
print()
print("=============== Object Copy")
x = [1,2,3]

#레퍼런스 복사
print()
y = x
print(x == y)
print(hex(id(x)), hex(id(y)))

x[1] = 4
print(y[1])

#복제의 시도 : 1
print()
y = x[:] #슬라이싱을 이용한 복제
print("x",x)
print("y",y)

x[1] = 0
print(y[1])

#복제의 시도 : copy 모듈의 활용
print()
import copy

y = copy.copy(x)
print(x is y)   # --
print("x :", x)
print("y :", y)

x[1] = 100

print("x : ", x)
print("y : ", y)

#깊은 복제
print()
a = [1,2,3]
b = [4,5,6]
x = [a,b,100]

print("a : ", a)
print("b : ", b)
print("x : ", x)

y = copy.copy(x)
print("y :", y)


a[1] = 0

print("a : ", a)
print("b : ", b)
print("x : ", x)
print("y : ", y)


#deepcopy
print()
y = copy.deepcopy(x)

print("a : ", a)
print("b : ", b)
print("x : ", x)
print("y : ", y)

a[1] = 100

print("x : ", x)
print("y : ", y)

#deepcopy는 객체를 다룰때 아주 중요하다.
























































