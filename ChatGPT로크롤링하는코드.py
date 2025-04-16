import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
import openpyxl

# 검색어 설정 (예: "반도체")
query = "반도체"
url = f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={quote(query)}"

# 헤더 설정 (User-Agent를 넣지 않으면 차단될 수 있음)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

# 요청
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# 뉴스 기사 제목 추출
titles = soup.select(".news_tit")  # 뉴스 제목 링크에 해당하는 클래스

print("뉴스 기사 제목:")
for idx, title in enumerate(titles, 1):
    print(f"{idx}. {title.get_text()}")

# 엑셀 파일 생성
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "뉴스 기사 제목"

# 헤더 추가
sheet.append(["번호", "제목"])

# 뉴스 기사 제목을 엑셀에 저장
for idx, title in enumerate(titles, 1):
    sheet.append([idx, title.get_text()])

# 엑셀 파일 저장
workbook.save("results.xlsx")
print("뉴스 기사 제목이 results.xlsx 파일에 저장되었습니다.")
