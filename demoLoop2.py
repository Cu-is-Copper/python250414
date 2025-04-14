# demoLoop2.py

for item in [1,2,3,]:
    print(item)

# 수열함수
print(list(range(1,11)))
print(list(range(2000, 2026)))
print(list(range(1,32)))

# 리스트 내장(함축)
lst = list(range(1,11))
print(lst)
print([i**2 for i in lst if i>5])
tp = ("apple", "kiwi")
print([len(i) for i in tp])
d = {100:"apple", 200:"kiwi"}
print([v.upper() for v in d.values()])

print("---필터링함수---")
def getBiggerThan20(i):
    return i >20

lst = [10,25,30]
itemL = filter(getBiggerThan20, lst)
for item in itemL:
    print(item)

print("---람다함수---")
lst = [10,25,30]
itemL = filter(lambda x:x>20, lst)
for item in itemL:
    print(item)