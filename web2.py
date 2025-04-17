#web2.py
#웹 크롤링을 위한 선언
from bs4 import BeautifulSoup
#웹서버에 요청 선언
import urllib.request
#정규표현식 사용
import re

#파일로 저장
f = open("clien.txt", "wt", encoding="utf-8")
#페이지 처리
for i in range(0,10):
    url = "https://www.clien.net/service/board/sold?&od=T31&category=0&po=" + str(i)
    print(url)
    response = urllib.request.urlopen(url)
    page = response.read().decode('utf-8', 'ignore')
    #검색이 용이한 객체 생성
    soup = BeautifulSoup(page, "html.parser")
    list = soup.find_all("span", attrs={"data-role":"list-title-text"})

    for tag in list:
        title = tag.text.strip() #strip() : 앞뒤 공백 제거
        if re.search("아이패드", title):
            print(title)
            f.write(title + "\n")
    #<span class="category fixed" title="판매">판매</span>
    #						<span class="subject_fixed" data-role="list-title-text" title="아이패드 미니6 64기가">
    #							아이패드 미니6 64기가
    #						</span>

f.close()