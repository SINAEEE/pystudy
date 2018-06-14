

#callable(object)
#param으로 받는 object가 callable이면 True, 아니면 false
#object class에는 __call__(self[,args..])이 정의되어있는데,
# callable이라는건 이 함수가 구현되어있는지 확인하는것

class Foo:
    def __call__(self):
        print('called')

foo_instance = Foo()
foo_instance()
