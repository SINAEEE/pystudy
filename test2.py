

drinks = {
    'martini' : {'vodka','vermouth'},
    'black russian' : {'vodka','khlua'},
    'white russian' : {'cream', 'khalua', 'vodka'},
    'manhattan' : {'rye','vermouth', 'bitters'},
    'screwdriver' : {'orange juice', 'vodka'}
}

#print(drinks)

"""
for k,v in drinks.items():
    if 'vodka' in v and not ('vermouth' in v or 'cream' in v):
        print(k)
"""

# for k,v in drinks.items():
#     if v & {'orange juice', 'vermouth'}:
#         print(k)

# for name,content in drinks.items():
#     if content & {'cream'}:
#         print(name)

# for name, contents in drinks.items():
#     if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
#         print(name)


bruss = drinks['black russian']
wruss = drinks['white russian']

#print(bruss)
#print(wruss)

a={1,2}
b={2,3}

# print(a.intersection(b))
# print(bruss.intersection(wruss))

# print(a|b)
# print(a.union(b))

# print(a-b)
# print(a.difference(b))

# print(a^b)
# print(a.symmetric_difference(b))

# print(a<=b)
# print(a.issubset(b))

