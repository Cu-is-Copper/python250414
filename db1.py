# db1.py
import sqlite3

#연결객체 리턴(메모리에서 작업)
con = sqlite3.connect(":memory:")
#커서객체 리턴
cur = con.cursor()

#테이블 구조 생성
cur.execute("create table PhoneBook(name text, phoneNum text);")

#1건 입력
cur.execute("insert into PhoneBook values ('derick', '010-222');")
#입력 파라메터 처리
name = "홍길동"
phoneNumber = "010-333"
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNumber))
#다중의 레코드(행데이터 입력)
datalist = (("전우치","010-123"),("이순신","010-555"))
cur.executemany("insert into PhoneBook values (?, ?);", datalist)

#검색
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row[0], row[1])
