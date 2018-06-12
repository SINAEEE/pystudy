


#최상위 모듈(인터프리터에서 실행되는 모듈)의 모듈이름은 "__main__"
print('modulename.py의 모듈 이름 : '+__name__)

#하지만 import되어지는 모듈의 이름은 파일이름이 됨
import mymod
print("modulename.py의 모듈이름 : " +__name__)

print()
print("mymod.py의 모듈이름 : " +__name__)
print(mymod.add(10,20))

print()
#파이썬변수, 함수, 클래스는
# 각각 자신의 정의된 모듈의 이름이 저장된 __module__속성을 가지고있음

from math import sin
from mymath import add
from cmd import Cmd

print(sin.__module__)
print(add.__module__)
print(Cmd.__module__)