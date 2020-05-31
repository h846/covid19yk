<template>
  <b-card
    :title="cardTitle"
  >
    <template v-slot:header>
        <h6 class="mb-0">合計: {{totalVal}}人</h6>
        <span class="text-secondary small">最終更新: {{ updateTime }}</span>
    </template>
    <PieChart :chart-data="chartdata" :options="options"/>
    <template v-slot:footer>
        <b-link :href="link.url" class="text-secondary small">{{ link.txt }}</b-link>
    </template>
  </b-card>
</template>
<script>
import axios from 'axios'
import PieChart from '~/components/core/PieChart.vue'

export default {
  components: {
    PieChart
  },
  data: function(){
    return {
      cardTitle:"陽性患者の状況",
      updateTime: '',
      link:{
        txt: "出典：横浜市内の陽性患者の発生状況データ・相談件数",
        url: "https://www.city.yokohama.lg.jp/city-info/koho-kocho/koho/topics/corona-data.html"
        },
      totalVal: 0,
      chartdata: {
        labels: [],
        datasets: [{
          data: []
        }]
      },
      options: {
        legend: {display: true},
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
      let res = await axios.get('https://84log.net/api/patient_situation')

      let labels, data, total
      labels = res.data.keys
      data = res.data.vals
      //remove total from data array
      labels.shift()
      this.totalVal = data.shift()
      
      this.sortData(labels, data)

      //JSONファイル更新時間取得
      res = await axios.get('https://84log.net/api/updated')
      this.updateTime = res.data
    },
    //Data Sorting
    sortData : function(aryLabel, aryData){
      //Combine label and data arrays and objectify them.
      let aryObj = aryLabel.map(function(d, i){
        return {
          label: d,
          data: aryData[i] || 0
        };
      });
      //Sorting object data
      let sortedAryObj = aryObj.sort(function(a,b){
        return b.data > a.data
      })

      let newAryLabel = []
      let newAryData = []

      sortedAryObj.forEach(function(d){
        newAryLabel.push(d.label)
        newAryData.push(d.data)
      });

      let chartdata = {};
      chartdata.labels = newAryLabel;
      chartdata.datasets = []
      chartdata.datasets.push({data: newAryData})
      
      this.chartdata = chartdata;
    }
  },
  created: function(){
    this.getJSON()
  }
}
</script>