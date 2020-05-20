import requests, csv, json

def get_csv_data():# Yokohama takeout&deli csv
    """
    *** return data ****
        {
            shop_list:{
                header:{},
                body:{}
                }
        }
    """
    url = 'https://www.city.yokohama.lg.jp/business/kigyoshien/syogyo/covid-19/'\
        'takeout-delivery/takeout.files/takeoutyokohama.csv'

    templist = []
    takeout_shop_list = {}

    with requests.Session() as s:
        download = s.get(url)

        decoded_content = download.content.decode('utf-8')

        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        #listfy from csv reader object!!
        for row in cr:
            templist.append(row)
        
        #Remove Original Header Data
        templist.pop(0)
        #Create New Header
        takeout_shop_list['header'] = [
            "更新日",
            "店舗名",
            "区名",
            "店舗住所",
            "電話番号",
            "最寄駅",
            "提供条件",
            "定休日",
            "ウェブサイト",
            "SNS",
            "料理ジャンル",
            "テイクアウト",
            "デリバリー",
            "配送料",
            "店舗からのメッセージ",
            "メニュー1",
            "税込価格",
            "メニュー2",
            "税込価格",
            "メニュー3",
            "税込価格",
            "その他のメニュー",
            "店舗ID",
            "変更フラグ"
        ]

        #create new list body
        body_list = []
        row = []

        for inner_list in templist:
            for idx, item in enumerate(inner_list):
                item = item.replace("　"," ")#全角スペースを半角スペースに

                if idx == 1:# 新規?/修正?
                    continue
                elif idx == 3:# 住所列結合

                    row.append(item)

                    adrs = inner_list[idx] + inner_list[idx+1] + inner_list[idx+2]

                    del inner_list[idx+1]
                    del inner_list[idx+2]

                    row.append(adrs)
                elif idx == 4:#経度緯度
                    continue
                else:
                    row.append(item)

            body_list.append(row)
            row = []

        takeout_shop_list['body'] = body_list.copy()
        
        shop_list = {'shop_list':takeout_shop_list}
        return shop_list
#get_csv_data()