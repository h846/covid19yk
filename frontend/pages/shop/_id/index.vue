<template>
    <section>
        <b-row class="justify-content-center">
            <b-col cols="10">
                
                <table>
                    <tbody>
                        <tr>
                            <th>店舗名</th>
                            <td>{{ shopData['店舗名'] }}</td>
                        </tr>
                        <tr>
                            <th>料理ジャンル</th>
                            <td>{{ shopData['料理ジャンル'] }}</td>
                        </tr>
                        <tr>
                            <th>メニュー１</th>
                            <td>{{ shopData['メニュー1'] }}</td>
                        </tr>
                        <tr>
                            <th>税込価格</th>
                            <td>{{ shopData['税込価格1'] }}</td>
                        </tr>
                        <tr>
                            <th>メニュー2</th>
                            <td>{{ shopData['メニュー2'] }}</td>
                        </tr>
                        <tr>
                            <th>税込価格</th>
                            <td>{{ shopData['税込価格2'] }}</td>
                        </tr>
                        <tr>
                            <th>メニュー3</th>
                            <td>{{ shopData['メニュー3'] }}</td>
                        </tr>
                        <tr>
                            <th>税込価格</th>
                            <td>{{ shopData['税込価格3'] }}</td>
                        </tr>
                        <tr>
                            <th>その他のメニュー</th>
                            <td>{{ shopData['その他のメニュー'] }}</td>
                        </tr>
                        <tr>
                            <th>提供条件</th>
                            <td>{{ shopData['提供条件'] }}</td>
                        </tr>
                        <tr>
                            <th>最寄駅</th>
                            <td>{{ shopData['最寄駅']}}</td>
                        </tr>
                        <tr>
                            <th>店舗住所</th>
                            <td>
                                <a :href="'https://www.google.com/maps/search/?api=1&query='+shopData['店舗住所']" target="_blank">
                                    {{ shopData['店舗住所'] }}
                                </a>
                            </td>
                        </tr>
                        <tr>
                            <th>定休日</th>
                            <td>{{ shopData['定休日']}}</td>
                        </tr>
                        <tr>
                            <th>電話番号</th>
                            <td><a :href="'tel:'+ shopData['電話番号']">{{ shopData['電話番号']}}</a></td>
                        </tr>
                        <tr>
                            <th>ウェブサイト</th>
                            <td><a :href="shopData['ウェブサイト']">{{ shopData['ウェブサイト']}}</a></td>
                        </tr>
                        <tr>
                            <th>SNS</th>
                            <td><a :href="shopData['SNS']">{{ shopData['SNS']}}</a></td>
                        </tr>
                        <tr>
                            <th>店舗からのメッセージ</th>
                            <td>{{ shopData['店舗からのメッセージ']}}</td>
                        </tr>
                        <tr>
                            <th>配送料</th>
                            <td>{{ shopData['配送料']}}</td>
                        </tr>
                    </tbody>
                </table>

                <b-button lg="4" variant="outline-danger">
                    <a @click="$router.go(-1)">前のページへ</a>
                </b-button>

                <div class="spacer"></div>
            </b-col>
        </b-row>
    </section>
</template>
<script>
import axios from 'axios'
export default {
    data(){
        return {
            id: this.$route.params.id,
            shopData: {
                "id":"",
                "店舗名":"",
                "更新日":"",
                "区名":"",
                "店舗住所":"",
                "電話番号":"",
                "最寄駅":"",
                "提供条件":"",
                "テイクアウト":"",
                "デリバリー":"",
                "メニュー1":"",
                "税込価格1":"",
                "メニュー2":"",
                "税込価格2":"",
                "メニュー3":"",
                "税込価格3":"",
                "その他のメニュー":"",
                "変更フラグ":"",
                "定休日":"",
                "店舗ID":"",
                "店舗からのメッセージ":"",
                "料理ジャンル":"",
                "ウェブサイト":"",
                "配送料":""
                }
        }
    },
    computed:{

    },
    created: async function(){

        let res = await axios.get('https://84log.net/api/shop_list');
        let fields = res.data.header
        let items = res.data.body
        let shopData = {}
        
        for(let item of items){
            if(item[0] == this.id){
                for(let i=0; i < fields.length; i++){
                    this.shopData[fields[i]] = item[i];
                }
            }
        }
        
        console.log(this.shopData);
    },
    methods:{
        show: function(val){
            console.log(val);
        }
    }
}
</script>
<style lang="scss" scoped>
table{
  width: 100%;
  border-collapse: separate;
  border-spacing: 0 10px;
  table-layout: fixed;
  font-size: 0.9rem;;

  th{
      border-bottom: solid 2px #fb5144;
      text-align: center;
      width: 150px;
  }

  td{
      border-bottom: solid 2px #ddd;
      padding: 5px 10px;
  }
}
.btn{
    margin: 20px 0;
    a {
        display: inline-block;
        width: 100%;
        height: 100%;
        margin: 0;
        padding: 0;
    }
}
.spacer{
    margin-bottom: 100px;
}
</style>