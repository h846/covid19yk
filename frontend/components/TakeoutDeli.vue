<template>
<section id="tk-deli-search">
    <b-tabs content-class="mt-3">
        <!-- Free Word Search Form -->
        <b-tab title="フリーワード検索">
            <b-form-group description="店名・住所などで検索できます" class="mb-2">
                <b-input-group>
                    <b-form-input
                        type="text"
                        id="freeword_search"
                        v-model="frwdResult"
                        placeholder="フリーワード検索"
                    ></b-form-input>
                    <b-input-group-append>
                        <b-button variant="primary" @click="freeWordSrch(frwdResult)"><b-icon icon="search" class="pr-1"></b-icon>検索</b-button>
                    </b-input-group-append>
                </b-input-group>
            </b-form-group>
        </b-tab>
        <!--Advanced Search Form-->
        <b-tab title="店舗検索" active>
            <b-card bg-variant="light">
                <b-row>
                    <b-col sm="6" cols="12">
                        <b-form-group label-cols-sm="4" label="区名:" label-for="ward">
                            <b-form-select id="ward" v-model="selected_ward" :options="ward_options"></b-form-select>
                        </b-form-group>
                    </b-col>
                    <b-col sm="6" cols="12">
                        <b-form-group label-cols-sm="4" label="料理ジャンル:" label-for="category">
                            <b-form-select id="category" v-model="selected_category" :options="category_options"></b-form-select>
                        </b-form-group>
                    </b-col>
                </b-row>

                <b-row>
                    <b-col sm="6" cols="12">
                        <b-form-group
                            label-cols-sm="3"
                            label="提供方法"
                            class="mb-0"
                        >
                            <b-form-radio-group
                            class="pt-2"
                            :options="['テイクアウト', 'デリバリー']"
                            v-model="selected_tord"
                            ></b-form-radio-group>
                        </b-form-group>
                    </b-col>
                    <b-col class="mt-3" sm="6" cols="12">
                        <b-button variant="primary" href="#" style="width:100%" @click="advSearch(selected_ward, selected_category, selected_tord)">検 索</b-button>
                    </b-col>
                </b-row>
            </b-card>
        </b-tab>
    </b-tabs>
    <div style="margin-bottom:20px;"></div>
    <!--<DataTable :result="results" class="mt-3"/>-->
    <b-overlay :show="showOverlay" spinner-variant="primary">
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
    </b-overlay>
</section>
</template>

<script>
import axios from 'axios'

export default {
    data: function(){
        return {
            frwdResult: "",
            selected_ward: null,
            selected_category: null,
            selected_tord: null,
            showOverlay: false,
            ward_options:[
                {value: null, text: '検索したい区を選択'},
                {value: '鶴見区', text: '鶴見区'},
                {value: '神奈川区', text: '神奈川区'},
                {value: '西区', text: '西区'},
                {value: '中区', text: '中区'},
                {value: '南区', text: '南区'},
                {value: '港南区', text: '港南区'},
                {value: '保土ケ谷区', text: '保土ケ谷区'},
                {value: '旭区', text: '旭区'},
                {value: '磯子区', text: '磯子区'},
                {value: '金沢区', text: '金沢区'},
                {value: '港北区', text: '港北区'},
                {value: '緑区', text: '緑区'},
                {value: '青葉区', text: '青葉区'},
                {value: '都筑区', text: '都筑区'},
                {value: '戸塚区', text: '戸塚区'},
                {value: '栄区', text: '栄区'},
                {value: '泉区', text: '泉区'},
                {value: '瀬谷区', text: '瀬谷区'}
            ],
            category_options:[
                { value: null, text: 'お好きな料理を選択'},
                { value: '和食', text: '和食'},
                { value: '洋食', text: '洋食'},
                { value: '中華', text: '中華'},
                { value: '韓国', text: '韓国'},
                { value: 'イタリアン', text: 'イタリアン'},
                { value: 'インドネパール', text: 'インド・ネパール'},
                { value: 'ベトナム', text: 'ベトナム'},
                { value: '丼', text: '丼'},
                { value: 'カレー', text: 'カレー'},
                { value: 'そばうどん', text: 'そば・うどん'},
                { value: 'ピザ', text: 'ピザ'},
                { value: 'ハンバーガー', text: 'ハンバーガー'},
                { value: 'パンサンドイッチ', text: 'パン・サンドイッチ'},
                { value: '寿司', text: '寿司'},
                { value: '焼き鳥', text: '焼き鳥'},
                { value: '焼肉', text: '焼肉'},
                { value: 'ラーメン', text: 'ラーメン'},
                { value: 'お弁当', text: 'お弁当'},
                { value: 'お惣菜', text: 'お惣菜'},
                { value: 'お好み焼きたこ焼き', text: 'お好み焼き・たこ焼き'},
                { value: 'その他', text: 'その他の料理'}//お好み焼き・たこ焼き・焼きそば・広島焼
            ],
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
        freeWordSrch: function(wrd){
            if(wrd == null || wrd == undefined || wrd == ""){
                this.alertMsg = "検索キーワードを入力してください"
                this.showDismissibleAlert = true;
                return
            }
            let results = [], item = ""
            console.log("works")
            for(let i in this.org_items){
                for(let j in this.org_items[i]){
                    item = String(this.org_items[i][j]).trim()
                    if(item.indexOf(wrd) !== -1){
                        results.push(this.org_items[i])
                    }
                }
            }

            this.items = results;
            this.frwdResult = null;
        },
        advSearch: function(argWard, argCategory, argTorD){
            /*
            this.selected_ward=null;
            this.selected_category=null;
            this.selected_tord=null;
            */
            let ward = argWard
            let category = argCategory
            let TorD = argTorD

            if(ward == null && category == null && TorD == null){
                this.alertMsg = "項目を一つ以上選択してください"
                this.showDismissibleAlert = true;
                return 0;
            }

            let results = [], items = {}

            if(ward != null){
                
                for(let i in this.org_items){
                    items = this.org_items[i]
                    if(items['区名'] == ward){
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
                    let lists = ward != null || category != null ? results : this.org_items
                    let sub_results = []

                    for(let i in lists){
                        items = lists[i]

                        if(TorD == 'テイクアウト'){
                            if(items['テイクアウト'].indexOf('はい') !== -1){
                                sub_results.push(items)
                            }
                        }

                        if(TorD == 'デリバリー'){
                            if(items['デリバリー'].indexOf('はい') !== -1){
                                sub_results.push(items)
                            }
                        }
                    }
                    items = {}
                    results = sub_results
            }

            this.items = results

        },
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