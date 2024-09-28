# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 14:45:52 2024

@author: UX6404_SL
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import requests

chrome = webdriver.Chrome()
chrome.get('https://pic.sogou.com')
time.sleep(1)
inputBar = chrome.find_element(By.CLASS_NAME, "query.query-defalut")
inputBar.send_keys("puppy")
inputBar.send_keys(Keys.ENTER)
time.sleep(0.5)
chrome.maximize_window()
time.sleep(0.5)
for i in range(2):
    chrome.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(1)
i=1
for element in chrome.find_elements(By.CSS_SELECTOR, 'img'):
    try:
        img_url = element.get_attribute('src')
        imgRespond = requests.get(img_url) 
        with open(str(i)+" .jpg","wb") as file:
            file.write(imgRespond.content)
            print("done")
        if i ==10:
            break
        i+=1
    except:
        print("Failed to Dowmload")
time.sleep(0.5)
chrome.close()