
from bs4 import BeautifulSoup

html =  '<td class="title">'\
		'<div class="tit3">'\
		 '<a href="/movie/bi/mi/basic.nhn?code=159892" title="탐정: 리턴즈">탐정: 리턴즈</a>'\
		 '</div>'\
		 '</td>'




#1. tag 조회
def ex1():
    bs = BeautifulSoup(html,'html.parser')
    print(bs)

    tag = bs.td
    print(tag)
    print(tag.div)

    tag = bs.a
    print(tag)
    print(tag.name)

def ex2():
    bs = BeautifulSoup(html, 'html.parser')

    tag = bs.td
    print(type(tag),tag) #type : <class 'bs4.element.Tag'>
    print(tag['class'])

    tag =bs.div
    print(tag.attrs)

def ex3():
    #find() 하나의 태그 가져오기
    #find_all(): 여러개의 태그 가져오기
    bs = BeautifulSoup(html, 'html.parser')

    tag = bs.find('td',attrs={'class':'title'})
    print(tag)

    tag = bs.find(attrs={'class':'tit3'})
    print(tag)

def ex4():
    #문자열 추출
    bs = BeautifulSoup(html, 'html.parser')

    s = list(bs.strings)
    print(s)



if __name__ =='__main__':
    #ex1()
    #ex2()
    #ex3()
    ex4()