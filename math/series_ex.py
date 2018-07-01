
import pandas as pd

price = [92600, 92400, 92100, 94300, 92300]
s = pd.Series(price)
#print(s)
#print(s[0],s[1])

s= pd.Series(
    [92600, 92400, 92100, 94300, 92300],
    index=['2017-01-01', '2017-02-02', '2017-03-03', '2017-04-04', '2017-05-05'])
#print(s)
#print(s['2017-03-03'])

"""
for date in s.index:
    print(date,end=' ')
else:
    print()


for price in s.values:
    print(price, end = ' ')
else:
    print()
"""


d = {'a':10, 'b':20, 'c':30}
s = pd.Series(d)
#print(s)
#print(s.values)

"""
s = pd.Series(d, index=['a','b','c','d'])
print(s)

for i in s.index:
    print(i,end= ' ')
else:
    print()

for v in s.values:
    print(v, end=' ')
else:
    print()
"""

s1 = pd.Series([10,20,30], index=['A','B','C'])
s2 = pd.Series([10,20,30], index=['C','B','A'])
print(s1+s2)
print(s1-s2)
print(s1*s2)
print(s1/s2)

