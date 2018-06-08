
def try_f1():
    try:
        lst = [1,3,5,7,9]
        lst[5] # IndexError: list index out of range
    except:
        print("Error")


#try_f1() 

def try_f2():
    try:
        value = int("10a") # ValueError: invalid literal for int() with base 10: '10a'
    except ValueError as e: #특정상황의 error를 위쪽에서 처리하고
        print("변환할 수 없습니다.")
    except Exception as e: # 예상하지 못한 error를 맨마지막에 Exception으로 처리하자
        print("Exception e:",e)
        print("type e:", type(e))


#try_f2() 
         
def try_f3():
    result = 4/0 # ZeroDivisionError: division by zero

#try_f3()

def example(): #키보드로부터 숫자입력받아 나누기
    num1 = input("첫번째 숫자를 입력해주세요 : ")
    num2 = input("두번째 숫자를 입력해주세요 : ")

    try:
        num1 = int(num1)
        num2 = int(num2)
        result = num1 / num2
    except ValueError as e:
        print("정수형이 아니에요")
    except ZeroDivisionError as e:
        print("0으로는 나눌 수 없어요")
    except Exception as e:
        print("e : ",e)
    else: #는 오류가 없을떄만 실행
        print("{} / {} = {}".format(num1,num2, result))
    finally: #finally는 오류여부와 상관없이 마지막에 실행
        print("예외처리완료")

#example()

#특정 경우에는 일부러 예외를 발생시키기도 합니다. : raise
def beware_dog(animal):
    if animal == "dog":
        #강제예외발생
        raise RuntimeError("멍멍")
    else:
        print("어서오세요")
    
try:
    beware_dog("cow")
    beware_dog("cat")
    beware_dog("dog")
except RuntimeError as e: #as키워드 주의해서 보자!!
    print(e)
    print(type(e))







