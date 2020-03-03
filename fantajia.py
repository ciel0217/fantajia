from selenium import webdriver
import chromedriver_binary  # Adds chromedriver binary to path
import time
import csv
import urllib.request
count=0
driver = webdriver.Chrome()
driver.get("https://fantasiabunko.jp/")
path= driver.find_elements_by_xpath('/html/body/main/section[4]/div/section[2]/ul/li[*]/figure/div/a')
csvlist = []

ref = [i.get_attribute('href') for i in path]
for href in ref:
    driver.get(href)
    img = driver.find_element_by_class_name('js-img-fallback').get_attribute('src')
    title = driver.find_element_by_class_name('js-img-fallback').get_attribute('alt')
    date = driver.find_element_by_xpath('/html/body/main/article/section[1]/div[2]/div[1]/dl/dd[1]/time').get_attribute('datetime')
    prise = driver.find_element_by_xpath('/html/body/main/article/section[1]/div[2]/div[1]/dl/dd[2]')
    isbn = driver.find_element_by_xpath('/html/body/main/article/section[1]/div[2]/div[1]/dl/dd[4]')
    savename = 'Fantajia'+str(count)+'.png'
    s = date+title+prise.text+isbn.text
    csvlist.append(s)
    urllib.request.urlretrieve(img,savename)
    count+=1

csvw = csv.writer(open("output.csv", "w", encoding = "utf-8", newline = "\n"), delimiter = "\t")
csvw.writerow(csvlist)     
#driver.quit()  
