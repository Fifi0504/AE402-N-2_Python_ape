# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 14:16:50 2024

@author: UX6404_SL
"""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
chrome.get('https://www.google.com')
inputBar = chrome.find_element(By.CLASS_NAME, 'gLFyf')
inputBar.send_keys('猿創力')
time.sleep(1)

chrome.find_element(By.CLASS_NAME, 'gNO89b').click()
time.sleep(1)

chrome.find_element(By.PARTIAL_LINK_TEXT, "猿創力程式設計學校").click()
time.sleep(1)

chrome.maximize_window()
chrome.get_screenshot_as_file('codingApe.png')