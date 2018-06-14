

def plus_ten(x):
    return x+10

print(list(map(plus_ten,[1,2,3])))

print(list(map(lambda x: x+10,[1,2,3])))


"""
strings=['foo','card','bar','abab','aaaa','abab','foo']

print(len(strings))
print(strings.count('foo'))
print(sorted(strings))

print()
strings.sort(key=lambda x:len(x))
print(strings)

strings.sort(key=lambda x:strings.count(x))
print(strings)
"""


"""
for i in range(10):
    print('{0}:{1}'.format(i,(lambda x:x*2)(i)))
else:
    print()
"""

"""
def blahblah(x):
    return x*2

for i in range(10):
    print('{0}:{1}'.format(i,blahblah(i)))
else:
    print()
"""
