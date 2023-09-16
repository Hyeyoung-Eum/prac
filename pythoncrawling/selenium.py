import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv



# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


# chrome창 (웹드라이버) 열기
driver = webdriver.Chrome(options=chrome_options)
# 실행할 웹페이지 불러오기 (학교 수강신청 사이트)
driver.get("https://sugang.korea.ac.kr/")


time.sleep(1)

content = driver.find_element(By.TAG_NAME,"iframe")
driver.switch_to.frame(content)

guidebtn = driver.find_element(By.CSS_SELECTOR, "#chkNoti")
guidebtn.click()

driver.switch_to.default_content()

# 스크롤 내리기
time.sleep(1)
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)

# 과목 조회 클릭!
time.sleep(1)
content = driver.find_element(By.TAG_NAME,"iframe")
driver.switch_to.frame(content)
morebtn = driver.find_element(By.XPATH, "//*[@id='menu_hakbu']")
morebtn.click()
driver.switch_to.default_content()



# 검색
time.sleep(1)
second_content = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(second_content)
time.sleep(1)


frame_inside = driver.find_element(By.CSS_SELECTOR, "#coreMain")
driver.switch_to.frame(frame_inside)
searchbox = driver.find_element(By.XPATH, "//*[@id='pCourNm']")
searchbox.send_keys("통계")
time.sleep(1)
searchbox.send_keys(Keys.ENTER)
time.sleep(1)

infos = driver.find_elements(By.CSS_SELECTOR, "#gridLecture > tbody > tr" )

file = open('korea.csv', mode="w", newline='')
writer = csv.writer(file)
writer.writerow(["title","professor","timespace"])

for info in infos:
    title = info.find_element(By.CSS_SELECTOR,"td:nth-child(6)").text
    professor = info.find_element(By.CSS_SELECTOR,"td:nth-child(7)").text
    timespace =  info.find_element(By.CSS_SELECTOR,"td:nth-child(9)").text
    print(title, professor, timespace)

    writer.writerow([title, professor, timespace])

print(title, professor, timespace)

file.close()
driver.quit()

