<template>
    <section>
        <BarChart :chart-data="chartdata" :options="options"/>
    </section>
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
      totalVal: 0,
      chartdata: {
        labels: [],
        datasets: [{}]
      },
      options: {
        title: {display:true, text: '区別陽性患者数'},
        legend: {display: false},
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
        colorschemes: {
          scheme: 'brewer.Accent8'
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
      console.log(keys)
      chartdata.labels = keys

      vals = res.data.vals
      this.totalVal = vals.pop()

      chartdata.datasets = []
      chartdata.datasets.push({data:vals})

      this.chartdata = chartdata
      
      console.log(chartdata.labels)
      console.log(chartdata.datasets[0].data)
    }
  },
  created: function(){
    this.getJSON()
  }
}
</script>