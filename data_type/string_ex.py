#문자형
#  시퀀스형
#  변경불가 (immutable) 자료형입니다.
str1 ="Life is too short, you nee Python"
str2 ="Welcome Python"

#타입 판별
print("\n#타입 판별")
print(type(str1), type(str2))
#instnace 판별
print(str1, "str?:", isinstance(str1,str))

#여러줄 문자열
print("\n#여러줄 문자열")
multiline = """
Java
Python
Linux
"""
print(multiline)

#문자열 ",' 둘다 사용 가능
#print("I said "Yes"") #Syntax error
#-> solution 1:
print('I said "Yes"') #좋은 방법은 아님
#-> solution 2:
print("I said \"Yes\"")


#문자열의 인덱싱, 슬라이싱, len
print("\n#문자열의 인덱싱, 슬라이싱, len 관련 메서드")
print(len(str1))  # 길이 : len
print(str1[5])    # 인덱스 접근 가능 : 시퀀스형
print(str1[5:7])  # 슬라이싱
print(str1[5:])   # 생략하면 끝까지 
print(str1[:6])   # 앞을 생략하면 처음부터 
print(str1[:])    # 시퀀스 전체

#str1[0] = 'l' # 변경 안됨 - 변경 불가 객체 #typeerror

#대소문자 관련
#   upper() : 전체 대문자
#   lower() : 전체 소문자
#   swapcase() : 대 <-> 소문자 전환
#   capitalize() : 첫문자 대문자로
#   title() : 각 단어의 첫 글자를 대문자로

print("\n#대소문자관련 메서드")
#str3 = str1.lower()
str3 = str1.lower().title() #필요한메서드를 계속 연결해서 사용가능
print(str3)


#검색관련
print("\n#검색관련 메서드")
print("count() : ",str1.count("short"))   # 검색어의 수
print("find() : ",str1.find("Python"))    # 문자열 내 검색
print("find() : ", str1.find("Life",6))   # 6번 인덱스부터 Life를 검색
print("rfind() : ", str1.rfind("Life"))   # 우측으로부터 검색

print("find() 없는 값 : ", str1.find("Java")) #없는 값 찾기
#찾는 내용이없으면 -1을 반환
print("index() : " , str1.index("Python"))
#print("index() 없는 값 : ", str1.index("Java")) #index는 없으면 valueError

#분리와 결합
print("\n#분리와 결합")
s = "Java and Python"
lines = """\    
Java
Python
Linux
Oracle"""

#분리 : split - ' ' 문자를 기준으로 구분
print(s.split())         #공백 문자 기준 분리
print(s.split(" and "))   #특정 문자열 기준 분리
print()
#합치기 : join
t = s.split(" and ")
print(t)
# : 문자를 넣어서 합쳐 보겠습니다.
print(":".join(t))


print()
# : 기준으로 2개만 분리
s2 = "abc:def:ghi:jkl"
print(s2.split(":",2))
print(s2.rsplit(":",2))


#splitlines() : 개행문자를 기준으로 분리
print("\nsplitlines()")
print(lines.splitlines())

#판별 관련
#  isdigit() : 형태가 숫자 형태인가
#  isalpha() : 알파벳 형태인가
#  islower() : 소문자 형태인가
#  isupper() : 대문자 형태인가
#  isspace() : 공백문자 형태인가

print("\n#판별관련")
num = input("정수를 입력하세요 : ")
#result = num * 2    #이렇게 하면 파이썬은 문자가 입력되었다고 생각함
#print("result : ", result)

# Solution 1:
#result = int(num) * 2
#print("result : ", result)

# Solution 2: 만약 문자열이 입력된다면
if num.isdigit():
    result = int(num) * 2
else:
    result = "정수가 아니예요"
print("result : ", result)








































