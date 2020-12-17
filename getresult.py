import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs



def getresult(author,college):
    chromeDriver = "D:\\chromedriver_win32\\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chromeDriver)
    url = 'https://kns.cnki.net/kns8/AdvSearch?dbprefix=SCDB&&crossDbcodes=CJFQ%2CCDMD%2CCIPD%2CCCND%2CCISD%2CSNAD%2CBDZK%2CCJFN%2CCCJD'
    driver.get(url=url)
    time.sleep(1)  # 休眠2秒
    driver.find_element_by_xpath('//*[@id="gradetxt"]/dd[2]/div[2]/input').clear()
    driver.find_element_by_xpath('//*[@id="gradetxt"]/dd[2]/div[2]/input').send_keys(author)

    driver.find_element_by_xpath('//*[@id="gradetxt"]/dd[3]/div[2]/input').clear()
    driver.find_element_by_xpath('//*[@id="gradetxt"]/dd[3]/div[2]/input').send_keys(college)

    driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/input').click()
    time.sleep(0.5)  # 休眠2秒
    try:
        title = driver.find_element_by_xpath('//*[@id="gridTable"]/table/tbody/tr/td[2]/a').text
        date= driver.find_element_by_xpath('//*[@id="gridTable"]/table/tbody/tr/td[5]').text
        print(title)
        print(date)
        result=[title,date]
    except:
        date='未找到'
        title='未找到'
        result = [title, date]
    finally:
        # time.sleep(0.2)
        driver.quit()
        return result


