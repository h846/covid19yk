<template>
  <section>
    <div class="container">
      <div>
        <input type="button" @click="getJSON" value="Get JSON">
        <PieChart :chart-data="chartdata" :options="options" />
      </div>
    </div>
  </section>
</template>

<script>
import Logo from '~/components/Logo.vue'
import PieChart from '~/components/PieChart.vue'

import axios from 'axios'

export default {
  components: {
    Logo,
    PieChart
  },
  data: function(){
    return {
      message : 'Yay',
      chartdata: {
        labels: ['20代', '30代', '40代'],
        datasets: [
          {
            data: [
              10,
              20,
              30
            ],
            backgroundColor: [
              "#BB5179",
              "#FAFF67",
              "#58A27C"
            ]
          }
        ]
      },
      options: {
        title: {display:true, text: '現在の陽性患者数'},
        responsive: true,
        maintainAspectRatio: false
      }
    }
  },
  methods : {
    getJSON : async function(){
      let res = await axios.get('http://84log.net/api/outbreak_per_ward')
      //console.log(res.data)
      let chartdata = {}
      chartdata.labels = res.data.keys

      chartdata.datasets = []
      chartdata.datasets.push({data:res.data.vals})

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

<style>
.container {
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.title {
  font-family: 'Quicksand', 'Source Sans Pro', -apple-system, BlinkMacSystemFont,
    'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  display: block;
  font-weight: 300;
  font-size: 24px;
  color: #35495e;
  letter-spacing: 1px;
}

.links {
  padding-top: 15px;
}
</style>
