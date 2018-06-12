


import re

states = ['alambama','Georgia!','georgia','Florlda','south carolina ','West virginia?']


def clean_strings(strings):
    results=[] #
    for string in strings:
        string = string.strip()
        string = re.sub('[!#?]',"",string)
        string = string.title()
        results.append(string)
    return results

print(clean_strings(states))

"""
def clean_strings(strings, *funcs):
    results=[]

    for string in strings:
        for func in funcs:
            string = func(string)
        results.append(string)

    return results


states = clean_strings(states, str.strip, str.title)

print(states)

"""
