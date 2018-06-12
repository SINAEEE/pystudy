

with open('file_ex.py','r',encoding='utf-8') as f3:
    for line in f3.readlines():
        print(line, end="")

print(f3.closed)


"""
f2 = open('test.txt','r',encoding='utf-8')

for line in f2.readlines():
    print(line, end="")
f2.close()
"""

"""
f1 = open('test.txt','r',encoding='utf-8')

while True:
    line = f1.readline()
    if line=="":
        f1.close()
        break
    print(line,end="")
"""



"""
f = open('test.txt','r',encoding='utf-8')

text = f.read()
print(text)

pos=f.tell() #현재 파일에서 어디까지 읽고 썼는지 위치를 반환
print(pos)


f.seek(16)#현재 사용자가 원하는 위치로 파일 포인터 이동
text=f.read()
print(text)
"""


"""
# write test

f = open("test.txt",'w',encoding='utf-8')
write_size = f.write("안녕하세요 김신애입니다.\n")
print(write_size)
f.close()



# read test
f=open('test.txt','r',encoding='utf-8')
text=f.read()
print(text)
f.close()
"""


