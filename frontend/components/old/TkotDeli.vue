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
                        <b-button variant="primary"><b-icon icon="search" class="pr-1" @click="runSearch(frwdResult)"></b-icon>検索</b-button>
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
                        <b-button variant="primary" href="#" style="width:100%" @click="runSearch(selected_ward, selected_category, selected_tord)">検 索</b-button>
                    </b-col>
                </b-row>
            </b-card>
        </b-tab>
    </b-tabs>

    <DataTable :result="results" class="mt-3"/>

</section>
</template>

<script>
import DataTable from '~/components/childs/DataTable'

export default {
    components: {
        DataTable
    },
    data: function(){
        return {
            frwdResult: "",
            results: {
                "frwd":null,
                "ward":null,
                "category":null,
                "TorD":null
            },
            selected_ward: null,
            selected_category: null,
            selected_tord: null,
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
            ]
        }
    },
    methods: {
        runSearch: function(...args){

            if(args.length == 1){
                this.results = {
                    "frwd":args[0]
                }
            }else if(args.length == 3){
                this.results = {
                    "ward":args[0],
                    "category":args[1],
                    "TorD":args[2]
                }
            }
        }
    }
}
</script>