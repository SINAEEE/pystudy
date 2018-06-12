#mymod.py

pi = 3.14

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def main():
    print('최상위 모듈(독립실행시) 출력')


#모듈 - import했을때와 직접실행했을떄 차이를 잘 알아보자

print()
if __name__ =="__main__": # __main__일때
    main()
else:
    print('mymod.py의 모듈이름 : '+__name__)


