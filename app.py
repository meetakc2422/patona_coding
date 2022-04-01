
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
import requests
from parsel import Selector
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import csv
import os
from selenium.webdriver.support import expected_conditions as EC
ser = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=ser)
driver.get('https://dermnetnz.org/image-library/')
sleep(2)
wait = WebDriverWait(driver, 20)
wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@class="imageList__group__item"]')))
sel = Selector(text=driver.page_source)
target_path = r'./images'
target_folder = os.path.join(target_path)
if not os.path.exists(target_folder):
            os.makedirs(target_folder)
counter = 0
with open('output.csv','w',encoding='utf8',newline='') as myfile:
    csv_writer = csv.writer(myfile)
    csv_writer.writerow(['Disease Name','URL'])
    for link in sel.xpath('//a[@class="imageList__group__item"]'):
        f = open(os.path.join(target_folder, 'jpg' + "_" + str(counter) + ".jpg"), 'wb')
        url = 'https://dermnetnz.org/' + link.xpath('./@href').extract_first()
        image = link.xpath('./div/img/@src').extract_first()
        image_content = requests.get(image).content
        disease_name = link.xpath('./div[@class="imageList__group__item__copy"]/h6/text()').extract_first()
        f.write(image_content)
        csv_writer.writerow([disease_name,url])
        print(disease_name)


    counter += 1
myfile.close()
