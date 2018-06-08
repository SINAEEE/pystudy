


lst = [1,2,3,4,5,6,7,8,9,10]

print("1. 4,5,6,7 추출 : ",lst[3:7])

#lst[3:7]=[7,6,5,4]
print("2. 내부순서 일부 뒤집기 : ")
slice=lst[3:7]
slice.reverse()
lst[3:7]=slice
print(lst)

#lst[3:7].sort(reverse=True)
#print(lst)

#lst[3:7].reverse()
#print(lst)


#print(lst[3:7].reverse().print(lst))







