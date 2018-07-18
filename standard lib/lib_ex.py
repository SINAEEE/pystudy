
periodic_table ={'Hydrogen':1, 'Helium':2}
print(periodic_table)

carbon = periodic_table.setdefault('Carbon',12)

print(carbon)
print(periodic_table)


from collections import defaultdict
periodic_table = defaultdict(int)
print(periodic_table)

periodic_table['hydrogen']=1
print(periodic_table['hydrogen'])
print(periodic_table['Carbon'])

periodic_table['Carbon'] = 2

print(periodic_table['Carbon'])

"""
def no_idea():
    return 'Huh?'

bestiary = defaultdict(no_idea)

bestiary['A'] = 'aa'
print(bestiary['A'])
bestiary['B'] = 'bb'
print(bestiary['B'])
print(bestiary['C'])
"""

bestiary = defaultdict(lambda : 'huh?')
print(bestiary['E'])


from collections import defaultdict
