
import json


#json 인코딩 : python타입문자열 -> json

customer = {
    'id':'910103',
    'name':'김신애',
    'history':[
    {'date' : '2016-01-1','item':'iphone'},
    {'date' : '2017-01-01','item':'monitor'}]
}

print(customer)

print()
jsonString = json.dumps(customer,indent=4,ensure_ascii=False)
print(type(jsonString))
print(jsonString)


#JSON 디코딩 : json -> python타입 문자열
print()
d = json.loads(jsonString)
print(type(d))
print(d)

