# db2.py 
import sqlite3
#연결객체 리턴받기(영구적인 파일로 저장) 
con = sqlite3.connect("c:\\work\\sample.db")
#커서객체 리턴
cur = con.cursor() 

#테이블구조(자료구조 생성)
cur.execute("create table if not exists PhoneBook (name text, phoneNum text);")

#1건 입력
cur.execute("insert into PhoneBook values ('홍길동','010-222');")

#입력 파라메터 처리
name = "전우치"
phoneNumber = "010-123"
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNumber))

#N건을 입력 
datalist = (("박문수","010-333"),("김길동","010-567"))
cur.executemany("insert into PhoneBook values (?, ?);", datalist)
#검색
cur.execute("select * from PhoneBook;")
print(cur.fetchall())

#작업 정상 완료(커밋)
con.commit() 


