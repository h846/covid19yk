<template>
    <b-overlay :show="showOverlay" spinner-variant="primary">
        <section>
            <b-table
                id="ng-shop-table" 
                stacked="sm"
                :striped = "isStriped"
                :fixed = "t_fixed"
                :items = "items"
                :fields = "fields"
                :per-page="perPage"
                :current-page="currentPage"
            >

            <template v-slot:cell(link)="row">
                <b-button lg="4" variant="warning" class="mr-2" :to="`shop/${row.item.id}`">
                    詳細へ
                </b-button>
            </template>

            </b-table>

            <!-- PAGE NATION-->
            <b-pagination
                v-model="currentPage"
                :per-page="perPage"
                :total-rows="totalRows"
                aria-controls="ng-shop-table"
                size="lg"
                class="justify-content-center"
            >
            </b-pagination>
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
            isStriped: true,
            perPage: '5',
            currentPage:'1',
            totalRows: 0,
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
            //テーブルにリンクセルを追加!!
            this.fields.push({key:"link",label:"詳細ページ"})

            let newBodyObj = {}
            let newBodyAry = []

            for(var i=0; i < items.length; i++){

                for(var k =0; k < fields.length; k++){
                    newBodyObj[fields[k]] = items[i][k]
                }
                newBodyAry.push(newBodyObj)
                newBodyObj = {}
            }

            //Array Filtering.
            //if nearest station of the shop is Sakuragi-cho, push to array it.
            this.items = newBodyAry.filter(item => 
            item['最寄駅'] == '桜木町' ||
            item['最寄駅'] == 'みなとみらい' ||
            item['最寄駅'] == '日ノ出町'
            )

            Object.assign(this.org_items, this.items)

            //for pagination
            this.totalRows = this.items.length

            this.showOverlay = false;

        }
    },
    created: function(){
        this.getJSON()
    }
}
</script>