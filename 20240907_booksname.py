# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 14:25:06 2024

@author: UX6404_SL
"""
import requests
from bs4 import BeautifulSoup
res = requests.get('https://www.books.com.tw/web/sys_saletopb/books/?attribute=30&loc=P_0008_books_002')
soup = BeautifulSoup(res.text, 'html.parser')
divs = soup.find_all("div", class_="type02_bd-a")

for each_div in divs:
    h4 = each_div.find('h4')
    if h4:
        a = h4.find('a')
        print(a)
        if a:
            bookName = a.text 
            #print(bookName)




































