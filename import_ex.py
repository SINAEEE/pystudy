
import math
print(math.sin(math.pi/6))
print(math.cos(math.pi/3))
print(math.tan(math.pi/4))

print()

from math import pi,sin,cos,tan
print(sin(pi/6), cos(pi/3), tan(pi/4))

print()

from math import pi, sin, cos, tan
from mymath import pi

# 현재 모듈에 특정이름이 중복되는 경우 맨 마지막이 덮어쓰게 된다
print(sin(pi/6), cos(pi/3),tan(pi/4))

print()

from math import *
#math 모듈에정의된 모든이름을 현재 모듈로 가져오기
print(sin(pi/6),cos(pi/3),tan(pi/4))

print()

from math import *
import mymath as m
print(sin(pi/6), cos(pi/3), tan(pi/4))
print(m.pi)

print()

from math import sin as mysin, cos as mycos, tan as mytan
import mymath as m
print(mysin(m.pi/6), mycos(m.pi/3), mytan(m.pi/4))

