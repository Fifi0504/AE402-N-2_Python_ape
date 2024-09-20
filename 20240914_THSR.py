# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:59:38 2024

@author: UX6404_SL
"""

import requests
import json
from bs4 import BeautifulSoup

date = input("哪一天開始查詢優惠(格式:2023/5/5)? ")

def searchTHSR(date):
    payload = {"SearType": "S",
            "Lang": "TW",
            "StartStation": "NanGang",
            "EndStation": "ZvoYing",
            "OutWardSearchDate": date
            "OutWardSearchTime": "20:00"
            }
    res = requests.post("https://www.thsrc.com.tw/ArticleContent/a3b630bb-1066-4352-a1ef-58c7b4e8ef7c",date = payload)
    
    finish = False
    print(date)
    soup = BeautifulSoup(res.text, "html.parser")
    train_dict = json.loads(soup.text)
    if train_dict['data']['DepartureTable']['TrainItem']:
        for item in trsin_dict['data']['DepartureTable']['TrainItem']:
            trainNumber = item['TrainNumber']
            DepartureTime = item['DepartureTime']
            DestinationTime = item['DestinationTime']
            
            for discount in item['Discount']:
                name = discount['Name']
                value = discount['value']
                if name == '早鳥':
                    if int(DepartureTime[0:2]) >= int(payload['OutWardSearchTime'][0:2]):
                        print('車次:' trainNumber, '出發時間:' DepartureTime, '抵達時間:' DestinationTime)
                        print(name, value)
                        finish = True
                        
    day = int(date[8:])
    
    if finish:
        print('在期完成')
    else:
        day = int(day) = 1
        if day < 10: 
            date = date[0:8] str(day) 
        else:
            date = date[0:8] str(day)
        searchTHSR(date)
    
searchTHSR(date)    
    
    
    