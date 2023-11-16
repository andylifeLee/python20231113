# web1.py 
#웹크롤링을 위한 선언 
#패키지 선언(크롤링 라이브러리)
from bs4 import BeautifulSoup

#페이지 로딩(메서드 체인)
page = open("test01.html", "rt", encoding="utf-8").read() 
#검색이 용이한 객체 
soup = BeautifulSoup(page, "html.parser")
#전체 페이지 보기
print(soup.prettify())



#페이지 로딩(연속으로 함수체인, 메서드체인)
page = open("test01.html", "rt", encoding="utf-8").read()

#검색할 객체 생성
soup = BeautifulSoup(page, "html.parser")
#페이지 보기 
#print(soup.prettify())
#<p>태그 몽땅 검색
#print(soup.find_all("p"))
#<p>하나만 검색
#print(soup.find("p"))
#검색의 조건
#<p class='outer-text'>컨텐츠</p>
#class가 파이썬의 키워드 
#print(soup.find_all("p", class_="outer-text"))
#특정 태그 검색: find_all() attrs =>속성들
#print(soup.find_all("p", attrs={"class":"outer-text"}))

#태그는 삭제하고 내부 컨텐츠: .text 
for tag in soup.find_all("p"):
    title = tag.text.strip()
    #치환
    title = title.replace("\n", "")
    title = title.replace(" ", "")
    print(title)


