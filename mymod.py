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
    print("mymod testcode")
    print("add", add(10,20))
    print("subtract", subtract(20,10))

#모듈 - import했을때와 직접실행했을떄 차이를 잘 알아보자

if __name__ =="__main__": #__main일떄, __main__일때
    main()
#print(__name__)


