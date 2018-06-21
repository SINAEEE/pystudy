
#리스트와 사전을 다루는 퀴즈

students = [{"name": "kim","kor":80,"eng":90,"math":80},
            {"name":"Lee","kor":90,"eng":85,"math":85}]

#print(students,type(students))

for student in students:
    total = student.get('kor') + student.get('eng') + student.get('math')
    avg = total / 3
    student['total'] = total
    student['avg'] = avg

print(students)


