

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

for k,v in drinks.items():
    if v & {'orange juice', 'vermouth'}:
        print(k)

for name,content in drinks.items():
    if content & {'cream'}:
        print(name)





