# demoList.py
# 문자열 처리
strA = "python is very powerful"
print(strA)
print(len(strA))
print(strA[0:6])
print(strA[:6])

x = 100
y = 3.14
print(dir())

#리스트 형식
colors = ["red", "blue", "green"]
print(type(colors))
colors.append("white")
print(colors)
colors.remove("blue")
print(colors)


#튜플
tp = (100, 200, 300)
print(type(tp))
print(tp.count(200))
print(tp.index(300))

#함수를 정의
def times(a,b):
    return a+b, a*b

#함수를 호출
result = times(3,4)
print(result)

print("id:%s, name:%s"%("kim","김유신"))

#세트 형식
a = {1,2,3,3}
b = {3,4,4,5}
print(a)
print(b)
print(a.union(b))
print(a.difference(b))
print(a.intersection(b))

#형식변환
a = set((1,2,3))
print(type(a))
b = list(a)
b.append(4)
print(b)
c = tuple(b)
print(c)

