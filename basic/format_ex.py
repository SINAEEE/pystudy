#format_ex.py
#문자열 서식

#서식 문자
'''
%s : 문자열
%d : wjdtn
%f : 부동소수
%% : % 리터럴
'''

format = "I have %d apples"
print(format % 10)

print("Interest Rate is %f%%" % 1.24) # %자체 문자를 출력하고싶다면, %%
print("Interest Rate is %.2f%%" % 1.24) #소수점아래 2자리까지만 표기

#두 개 이상의 값을 넣고 싶을 때
format = "total : %d개, get : %d개"
print(format % (10,3)) #튜플로 묶어주자

#format과 값의 형식이 일치하지 않으면 TypeError 발생

#고급 Formatting
format_str = "I have {} apples, and I ate {} apples"
print(format_str.format(5,3))


#서식에 설정된 공간의 개수와 실제 값의 개수가 다르면 IndexError 발생
print(format_str.format(10,3,1)) # but 값이 넘치는것은 괜찮음
#print(format_str.format(10)) #IndexError: tuple index out of range


#이름 기반의 포맷
format_str = "I have {total} apples, and I ate {num} apples"
print(format_str.format(total=10,num=3))
#print(format_str.format(total=10)) #KeyError: 'num' -> num인자를 넘겨주지 않았다는 의미

#dict 객체를 이용한 포맷
print(format_str.format_map({"total":5, "num":2}))





