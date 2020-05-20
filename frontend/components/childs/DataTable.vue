<template>
    <section>
        <b-alert v-model="showDismissibleAlert" variant="danger" dismissible>
            項目を一つ以上選択してください！
        </b-alert>
        <b-table
            :fixed = "t_fixed"
            :items = "items"
            :fields = "fields"
        >

        </b-table>
    </section>
</template>
<script>
import axios from 'axios'

export default {
    props:['result'],
    data: function(){
        return {
            loading: true,
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
          let ward = val.ward
          let category = val.category
          let TorD = val.TorD

          if(ward == null && category == null && TorD == null){
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