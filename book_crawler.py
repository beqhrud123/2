#student_1 
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:/Users/hp/Desktop/12/chromedriver.exe")
url = "http://www.kyobobook.co.kr/index.laf?orderClick=LJd"
driver.get(url)

time.sleep(2)

serch = driver.find_element_by_xpath(
    '//*[@id="searchKeyword"]')
serch.click()
driver.find_element_by_xpath(
    '//*[@id="searchKeyword"]').send_keys('수학')
serch.send_keys(Keys.ENTER)

res = []
for _ in range(15):
    time.sleep(1)
    for j in range(1, 2):
        try:
            name = driver.find_element_by_xpath(
                f'//*[@id="search_list"]/tr[1]/td[2]/div[2]/a/strong').text
            print(f'---{name}---')
        except:
            name = "NAN"
            pass
#student_2
        try:
            money = driver.find_element_by_xpath(
                f'//*[@id="search_list"]/tr[1]/td[4]/div[2]/strong').text
            print(f'---{money}---')
        except:
            money = "NAN"
            pass
        res.append((name, money))
    driver.find_element_by_css_selector('#contents_section > div.list_button_wrap > div.list_paging > a:nth-child(4)').click()
print(res)
driver.quit()


data = pd.DataFrame(res)
data.to_csv('./data1.csv')        
