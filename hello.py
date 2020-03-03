from selenium import webdriver
import chromedriver_binary  # Adds chromedriver binary to path
import time
import csv
driver = webdriver.Chrome("D:/chromedriver.exe")
driver.get("https://fantasiabunko.jp/")
path= driver.find_elements_by_xpath('/html/body/main/section[4]/div/section[2]/ul/li[*]/figure/div/a')
csvlist = []
ref = [i.get_attribute('href') for i in path]
for href in ref:
    driver.get(href)
    ddElem = driver.find_elements_by_xpath('/html/body/main/article/section[1]/div[2]/div[1]/dl/dd[*]')
    
csvw = csv.writer(open("output.csv", "w", encoding = "utf-8", newline = "\n"), delimiter = "\t")


#driver.get(ref)
csvlist.append(ddElem)
csvw.writerow(csvlist)     
#driver.quit()  
