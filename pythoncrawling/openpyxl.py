import requests
from bs4 import BeautifulSoup
import openpyxl

#1.Workbook생성
wb=openpyxl.Workbook()

#2.Sheet활성
sheet=wb.active

#3.데이터프레임 내 header(변수명) 생성
sheet.append(["제목", "채널명", "조회수", "좋아요수"])

#4.데이터 크롤링 과정
raw = requests.get("https://tv.naver.com/r")
html = BeautifulSoup(raw.text, 'html.parser')

container = html.select("div.inner") #div내부 inner class
for con in container:
	t=con.select_one("dt.title").text.strip()
	c=con.select_one("dd.chn").text.strip()
	h=con.select_one("span.hit").text.strip()
	l=con.select_one("span.like").text.strip()
	
	#sheet내 각 행에 데이터 추가
	sheet.append([t,c,h,l]) #리스트로 넣어줌

#5.수집한 데이터 저장
wb.save("naver_tv.xlsx")