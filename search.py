import pandas as pd
import getSS
from selenium import webdriver
import xlwt
import time

data1=pd.read_excel('./data/data3.xlsx')
# data2=pd.read_excel('./data/题目抓取（第二部分）.xlsx')
dfS=data1

file =xlwt.Workbook() #新建一个excel
table=file.add_sheet('输出结果')
table_row=0#这是行数，从0行开始写
table.write(table_row, 0, '姓名')  # 将,,写入
table.write(table_row, 1, '导师')  # 将,,写入
table.write(table_row, 2, '题目')  # 将,,写入
table.write(table_row, 3, '日期')  # 将,,写入
table_row=table_row+1


# dfS=pd.concat([data1,data2],axis=0,ignore_index=True)
college='吉林大学'

#打开网址
chromeDriver = "D:\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromeDriver)
url = 'https://kns.cnki.net/kns8/AdvSearch?dbprefix=SCDB&&crossDbcodes=CJFQ%2CCDMD%2CCIPD%2CCCND%2CCISD%2CSNAD%2CBDZK%2CCJFN%2CCCJD'
driver.get(url=url)
time.sleep(1)  # 休眠2秒

for i in range(len(dfS)):
    # print(i)
    # print(dfS.iloc[i,0])
    # print(dfS[i, 1])
    author=dfS.iloc[i, 0]
    tutor=dfS.iloc[i, 1]
    # college='吉林大学'

    result=getSS.getSS(driver,author,college)
    title=result[0]
    date=result[1]
    print(table_row)
    table.write(table_row, 0, author)  # 将,,写入
    table.write(table_row, 1, tutor)  # 将,,写入
    table.write(table_row, 2, title)  # 将,,写入
    table.write(table_row, 3, date)  # 将,,写入
    table_row=table_row+1
    if(table_row==98):
        file.save('查询结果3部分.xls')


file.save('查询结果3.xls')

