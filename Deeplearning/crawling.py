import urllib
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver as wb


# 네이버 이미지
url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
kword = input('검색어를 입력하세요: ')
base_url = url + quote_plus(kword)
base_url


wd = webdriver.Chrome('chromedriver', chrome_options=chrome_options)
wd.get(base_url)
wd.save_screenshot("naver_search.png")  # 검색후 정보가 없음(로딩중 )


body = wd.find_element_by_css_selector('body')

for i in range(20):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)


imgs = wd.find_elements_by_css_selector('img')

for idx, img in enumerate(imgs):
    print(idx, img.get_attribute('src'))
    imgUrl = img.get_attribute('src')
    imgPath = './crawling/' + kword + str(idx) + '.jpg'
    urllib.request.urlretrieve(imgUrl, imgPath)



# 네이버 검색

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless') #내부 창을 띄울 수 없으므로 설정
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = wb.Chrome('chromedriver', chrome_options=chrome_options)


# wd.implicitly_wait(5) 최대지연 5초

# 해당 URL을 브라우저로 실행
url = 'https://www.naver.com'

driver.get(url)

input_search = driver.find_element_by_id('query')
input_search.send_keys('서울날씨')
input_search.send_keys(Keys.ENTER)



### 구글에서 검색어 입력한 후 웹 페이지 결과 띄우기
url = 'http://www.google.com'

driver.get(url)

search = driver.find_element_by_tag_name('input')
search.send_keys('고양이')
search.send_keys(Keys.ENTER)
search.send_keys(Keys.BACK)