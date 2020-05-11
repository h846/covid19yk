<template>
    <v-card class="px-7 pb-3" elevation="10" width="600">
        <v-card-title v-text="cardtext"></v-card-title>
        <BarChart :chart-data="chartdata" :options="options"/>
        <v-card-text>
          <p class="display-1 text--primary">
            合計: {{ totalVal }}人
          </p>
          <v-btn class="display-20" text :href="link.url">{{link.txt}}</v-btn>
        </v-card-text>
    </v-card>
</template>
<script>
import axios from 'axios'
import BarChart from '~/components/core/BarChart.vue'

export default {
  components: {
    BarChart
  },
  data: function(){
    return {
      cardtext:"区ごとの陽性患者数",
      link:{
        txt: "出典：横浜市内の陽性患者の発生状況データ・相談件数",
        url: "https://www.city.yokohama.lg.jp/city-info/koho-kocho/koho/topics/corona-data.html"
        },
      totalVal: 0,
      chartdata: {
        labels: [],
        datasets: [{}]
      },
      options: {
        //title: {display:true, text: '区別陽性患者数'},
        legend: {display: false},
        responsive: true,
        maintainAspectRatio: true,
        plugins: {
          colorschemes: {
            scheme: 'brewer.Paired12'
          }
        }
      }
    }
  },
  methods: {
    getJSON : async function(){
      let res = await axios.get('http://84log.net/api/outbreak_per_ward')
      let chartdata = {}
      let keys, vals, totalVal

      keys = res.data.keys
      keys.pop()
      
      chartdata.labels = keys

      vals = res.data.vals
      this.totalVal = vals.pop()

      chartdata.datasets = []
      chartdata.datasets.push({data:vals})

      this.chartdata = chartdata
      
    }
  },
  created: function(){
    this.getJSON()
  }
}
</script>