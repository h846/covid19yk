# -*- coding: utf-8 -*-
import json
import os
from datetime import datetime

from backend.getdata.getTODeliData import get_csv_data
from backend.getdata.getCoronaData import get_table_data

json_data = {"updated":str(datetime.now().strftime("%Y/%m/%d %H:%M"))}
json_data.update( get_csv_data() )
json_data.update( get_table_data() )

#Write data to json file
path = os.getcwd() #Get Current Directory
with open(path+'/data.json', 'w') as f:
    json.dump(json_data, f, ensure_ascii=False)