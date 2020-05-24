<template>
    <section>
        <b-alert v-model="showDismissibleAlert" variant="danger" dismissible>
            {{ alertMsg }}
        </b-alert>
        <b-table responsive
            :fixed = "t_fixed"
            :items = "items"
            :fields = "fields"
        >

        <template v-slot:cell(show_details)="row">
            <b-button size="sm" @click="row.toggleDetails" class="mr-2">
                <span>詳細を</span>{{ row.detailsShowing ? '隠す' : '表示'}}
            </b-button>

        </template>

        <template v-slot:row-details="row">
            <b-card>
                <b-row class="mb-2">
                    <b-col sm="3" class="text-sm-right"><b>住所:</b></b-col>
                    <b-col>{{ row.item['店舗住所'] }}</b-col>
                </b-row>

                <b-row class="mb-2">
                    <b-col sm="3" class="text-sm-right"><b>地図:</b></b-col>
                    <b-col><a :href="'https://www.google.com/maps/search/?api=1&query='+row.item['店舗住所']" target="_blank">地図</a></b-col>
                </b-row>

                <b-row class="mb-2">
                    <b-col sm="3" class="text-sm-right"><b>電話番号:</b></b-col>
                    <b-col>{{ row.item['電話番号'] }}</b-col>
                </b-row>

                <b-row class="mb-2">
                    <b-col sm="3" class="text-sm-right"><b>最寄駅:</b></b-col>
                    <b-col>{{ row.item['最寄駅'] }}</b-col>
                </b-row>

                <b-row class="mb-2">
                    <b-col sm="3" class="text-sm-right"><b>提供条件</b></b-col>
                    <b-col>{{ row.item['提供条件'] }}</b-col>
                </b-row>

                <b-row class="mb-2">
                    <b-col sm="3" class="text-sm-right"><b>定休日:</b></b-col>
                    <b-col>{{ row.item['定休日'] }}</b-col>
                </b-row>

                <b-row class="mb-2">
                    <b-col sm="3" class="text-sm-right"><b>ウェブサイト:</b></b-col>
                    <b-col><a :href="row.item['ウェブサイト']" target="_blank">{{ row.item['ウェブサイト'] }}</a></b-col>
                </b-row>

                <b-row class="mb-2">
                    <b-col sm="3" class="text-sm-right"><b>SNS:</b></b-col>
                    <b-col><a :href="row.item['SNS']" target="_blank">{{ row.item['SNS'] }}</a></b-col>
                </b-row>

                <b-row class="mb-2">
                    <b-col sm="3" class="text-sm-right"><b>配送料</b></b-col>
                    <b-col>{{ row.item['配送料'] }}</b-col>
                </b-row>

                <b-row class="mb-4">
                    <b-col sm="3" class="text-sm-right"><b>店舗からのメッセージ:</b></b-col>
                    <b-col>{{ row.item['店舗からのメッセージ'] }}</b-col>
                </b-row>

                <b-row class="mb-0">
                    <b-col sm="3" class="text-sm-right"><b>メニュー１</b></b-col>
                    <b-col>{{ row.item['メニュー1'] }}</b-col>
                </b-row>

                <b-row class="mb-4">
                    <b-col sm="3" class="text-sm-right"><b>税込価格</b></b-col>
                    <b-col>{{ row.item['税込価格1'] }}</b-col>
                </b-row>

                <b-row class="mb-0">
                    <b-col sm="3" class="text-sm-right"><b>メニュー2</b></b-col>
                    <b-col>{{ row.item['メニュー2'] }}</b-col>
                </b-row>

                <b-row class="mb-4">
                    <b-col sm="3" class="text-sm-right"><b>税込価格</b></b-col>
                    <b-col>{{ row.item['税込価格2'] }}</b-col>
                </b-row>

                <b-row class="mb-0">
                    <b-col sm="3" class="text-sm-right"><b>メニュー3</b></b-col>
                    <b-col>{{ row.item['メニュー3'] }}</b-col>
                </b-row>

                <b-row class="mb-4">
                    <b-col sm="3" class="text-sm-right"><b>税込価格</b></b-col>
                    <b-col>{{ row.item['税込価格'] }}</b-col>
                </b-row>

                <b-row class="mb-2">
                    <b-col sm="3" class="text-sm-right"><b>その他のメニュー</b></b-col>
                    <b-col>{{ row.item['その他のメニュー'] }}</b-col>
                </b-row>
            </b-card>
        </template>

        </b-table>
    </section>
</template>
<script>
import axios from 'axios'

export default {
    props:{
        result: Object
    },
    data: function(){
        return {
            loading: true,
            alertMsg: "",
            showDismissibleAlert: false,
            t_fixed: true,
            org_items: [],
            items: [],
            fields: []
        }
    },
    methods: {
        getJSON : async function(){
            let res = await axios.get('http://84log.net/api/shop_list')

            let fields = res.data.header
            let items = res.data.body

            for(let idx in fields){
                if(fields[idx] == "店舗名" || fields[idx] == "区名" || fields[idx] == "料理ジャンル" || fields[idx] == "テイクアウト" || fields[idx] == "デリバリー"){
                    this.fields.push(
                        {
                            key: fields[idx],
                            label: fields[idx]
                        }
                    )
                }
            }

            this.fields.push({key:"show_details",label:"詳細"})

            let newBodyObj = {}
            let newBodyAry = []

            for(var i=0; i < items.length; i++){

                for(var k =0; k < fields.length; k++){
                    newBodyObj[fields[k]] = items[i][k]
                }
                newBodyAry.push(newBodyObj)
                newBodyObj = {}
            }

            this.items = newBodyAry;
            Object.assign(this.org_items, this.items)

        }
  },
  created: function(){
      this.getJSON()
  },
  watch: {
      result: function(val){
          //フリーワード検索の場合
          if("frwd" in val){
              if(val.frwd == null || val.frwd == undefined || val.frwd == ""){
                  this.alertMsg = "検索キーワードを入力してください"
                  this.showDismissibleAlert = true;
                  return
              }
              let results = [], item = ""

              for(let i in this.org_items){
                  for(let j in this.org_items[i]){
                      item = this.org_items[i][j]

                      if(item.indexOf(val.frwd) !== -1){
                          results.push(this.org_items[i])
                      }
                      //console.log(item)
                  }
              }
              this.items = results
              return;
          }
          // 通常店舗検索の場合
          let ward = val.ward
          let category = val.category
          let TorD = val.TorD

          if(ward == null && category == null && TorD == null){
              this.alertMsg = "項目を一つ以上選択してください"
              this.showDismissibleAlert = true;
              return 0;
          }

          let results = [], items = {}

          if(ward != null){
              
              for(let i in this.org_items){
                  items = this.org_items[i]

                  if(items['区名'].indexOf(ward) !== -1){
                      results.push(items)
                  }
              }
              items = {}
          }


          if(category != null){
              
            let lists = results.length > 0 ? results : this.org_items
            let sub_results = []

            for(let i in lists){
                items = lists[i]

                if(items['料理ジャンル'].indexOf(category) !== -1){
                    sub_results.push(items)
                }
            }
            items = {}
            results = sub_results
          }

          if(TorD !=null){
                let lists = results.length > 0 ? results : this.org_items
                let sub_results = []

                for(let i in lists){
                    items = lists[i]

                    if(TorD == "テイクアウト"){
                        if(items['テイクアウト'].indexOf("はい") !== -1){
                            sub_results.push(items)
                        }
                    }

                    if(TorD == "デリバリー"){
                        if(items['デリバリー'].indexOf("はい") !== -1){
                            sub_results.push(items)
                        }
                    }
                }
                items = {}
                results = sub_results
          }

          this.items = results
      }
  }
}
</script>