import time
from selenium import webdriver




def getRR(driver,author,college):
    driver.refresh()
    time.sleep(1)
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
        # driver.quit()
        return result


