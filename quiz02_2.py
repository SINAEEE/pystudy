
lst = [1, 3.14, 'python', 7, 89.1, 3]

lst_cleaned = []

for item in lst:
    #if isinstance(item, int) or isinstance(item, float):
    if isinstance(item, (int,float)): #튜플사용
        lst_cleaned.append(item)

print(lst_cleaned)

