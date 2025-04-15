#demoStr.py
strA = "python is very powerful"
strB = "파이썬은 강력해"

print(len(strA))
print(len(strB))
print(strA.capitalize())

data = " spam and ham "
result = data.strip()
print(data)
print(result)
#치환
result = result.replace("spam", "spam egg")
#리스트로 변환
lst = result.split()
print(lst)
#문자열로 조립
print(":)".join(lst))

#정규표현식 사용
import re

result = re.search("[0-9]*th", " 35th")
print(result)
print(result.group())

#선택한 라인 주석처리:ctrl + /
# result = re.match("[0-9]*th", "35th")
# print(result)
# print(result.group())

result = re.search("apple", "this is apple")
print(result.group())

result = re.search("\d{4}", "올해는 2025년입니다.")
print(result.group())

result = re.search("\d{5}", "우리 동네는 51000")
print(result.group())