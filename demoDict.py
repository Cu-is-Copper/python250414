#demoDict.py
color = {"apple":"red","banana":"yellow"}
print(color)
print(len(color))
print(color["apple"])

#입력
color["cherry"] = "red"
print(color)

#삭제
del color["apple"]
print(color)

for item in color.items():
    print(item)

#불린형식 
print(1 < 2)
print(1 != 2)
print(1 == 2)
print(True and True and False)
print(True and True and True)
print(True or False or False)

