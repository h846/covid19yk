<template>
    <b-overlay :show="showOverlay" spinner-variant="primary">
        <section>
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
    </b-overlay>
</template>

<script>
import axios from 'axios'

export default {
    data: function(){
        return {
            showOverlay: false,
            t_fixed: true,
            org_items: [],
            items: [],
            fields: []
        }
    },
    methods: {
        getJSON : async function(){
            this.showOverlay = true;

            let res = await axios.get('https://84log.net/api/shop_list')

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

            this.showOverlay = false;

        }
    },
    created: function(){
        this.getJSON()
    }
}
</script>