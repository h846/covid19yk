<template>
  <b-card
    :title="cardTitle"
  >
    <template v-slot:header>
        <h6 class="mb-0">合計: {{totalVal}}人</h6>
        <span class="text-secondary small">最終更新: {{ updateTime }}</span>
    </template>
    <BarChart :chart-data="chartdata" :options="options"/>
    <template v-slot:footer>
        <b-link :href="link.url" class="text-secondary small">{{ link.txt }}</b-link>
    </template>
  </b-card>
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
      cardTitle:"区ごとの陽性患者数",
      updateTime: "",
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
        legend: {display: false},
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
      let res = await axios.get('https://84log.net/api/outbreak_per_ward')
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
      //JSONファイル更新時間取得
      res = await axios.get('https://84log.net/api/updated')
      this.updateTime = res.data
    }
  },
  created: function(){
    this.getJSON()
  }
}
</script>