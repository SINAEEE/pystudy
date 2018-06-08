#list_ex.py
#리스트 예제

#리스트의 생성 []
l = [1,2,3,4,5,6,7,8,9,10]
print("l : ", l)
print("type l : ", type(l))

#인덱스 접근
print("l[0] : ",l[0])

#리스트의 길이를 구해봅시다.
print("length : ", len(l))

#연결
print("\n#연결")
print(l + [11,12,13])
print(l)

#슬라이스
print("\n#슬라이스")
print(l[3:6]) 
#슬라이스를 이용한 삭제
l[3:6] = []
print(l)

#주요 메서드
print("\n#주요 메서드")
a = [1,2,3]
print("a",a)

if 4 in a:
    print(a.index(4)) #요소의 인덱스 반환
else :
    print("없어요")


#항목 추가 : append
a.append(4)
print("append(4) : ",a)
#항목 삽입 : insert
a.insert(3,5) #3번인덱스에 5를 넣자
print("a.insert(3,5) : ",a)

#항목 개수 확인 : count
print("[1,2,3,1,2,3].count(3) : ",[1,2,3,1,2,3].count(3))
#리스트 뒤집기
a.reverse()
print("a.reverse() : ",a)
#항목의 정렬 : sort
a.sort()
print("a.sort() : ",a)
#항목의 삭제 : remove
a.remove(5)
print("a.remove(5) : ",a)


#리스트의 확장 : extend
a.extend([5,6,7])
print("a.extend[5,6,7] : ", a)

















