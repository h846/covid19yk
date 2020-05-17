# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

import json, csv
import os

json_data = {}

def get_csv_data(url):# Yokohama takeout&deli csv

    """
    return data:
        {
            shop_list:{
                header:{},
                body:{}
                }
        }
    """
    templist = []
    takeout_shop_list = {}

    with requests.Session() as s:
        download = s.get(url)

        decoded_content = download.content.decode('utf-8')

        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        #listfy from csv reader object!!
        for row in cr:
            templist.append(row)
        
        takeout_shop_list['header'] = templist.pop(0)
        takeout_shop_list['body'] = templist.copy()
        #print(takeout_shop_list['header'])
        shop_list = {'shop_list':takeout_shop_list}
        json_data.update(shop_list)

url = 'https://www.city.yokohama.lg.jp/business/kigyoshien/syogyo/covid-19/'\
      'takeout-delivery/takeout.files/takeoutyokohama.csv'

get_csv_data(url)

def get_site_data(url):
    res = requests.get(url)
    res.encoding = res.apparent_encoding # Anti MOJIBAKE
    return BeautifulSoup(res.text, 'lxml')

def get_table_data():

    #for data storage
    t_data = {
        'patient_situation':{},
        'outbreak_per_ward':{},
        'pcr_test_num':{'num':''},
        #'population_change':{}
    }

    soup = get_site_data('https://www.city.yokohama.lg.jp/city-info/koho-kocho/koho/topics/corona-data.html')
    tables = soup.find_all('table', class_='table01')

    for idx, key in enumerate(t_data):
        
        if key == 'pcr_test_num':
            nums = tables[idx].find_all("td")
            t_data[key]['num'] = nums[8].get_text()#Total number of infections
            continue
        ths = tables[idx].find_all('th')
        tds = tables[idx].find_all('td')

        for th, td in zip(ths, tds):
            t_data[key][th.get_text()] = td.get_text()
    #print(json.dumps(t_data, ensure_ascii=False))
    json_data.update(t_data)

get_table_data()

#Write data to json file
path = os.getcwd() #Get Current Directory
with open(path+'/data.json', 'w') as f:
    json.dump(json_data, f, ensure_ascii=False)