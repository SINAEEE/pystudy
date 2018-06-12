

import re

states = ['alambama','Georgia!','georgia','Florlda','south carolina ','West virginia?']


def clean_strings(strings):
    results=[]
    for string in strings: #매개변수로 넘어온값을 하나씩 for문으로 돌려주기
        string = string.strip() #공백제거
        string = re.sub('[!#?]',"",string)
        string = string.title() #문장의 첫글자 대문자변환
        results.append(string) #결과값을 리스트에 저장
    return results

print(clean_strings(states))


"""
def clean_strings(strings, *funcs): #함수를 매개 변수로 받음 
    results=[]

    for string in strings: #string값 for문으로 하나씩 돌려주기
        for func in funcs: #함수 2개 차례로 실행
            string = func(string) #적용한 함수값 string에 다시 입력 후,
        results.append(string) #결과값 저장

    return results


states = clean_strings(states, str.strip, str.title)

print(states)

"""
