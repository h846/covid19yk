from bs4 import BeautifulSoup
import requests

import json

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
    return t_data