<script>
import { Bar } from 'vue-chartjs'
export default {
  extends: Bar,
  data(){
    return {
        chartdata: {
            labels: ['January', 'February'],
            datasets: [
                {
                label: ['Data One'],
                data: [40, 30],
                backgroundColor: '#f87979'
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    }
  },
  mounted () {
    this.renderChart(this.chartdata, this.options)
  }
}
</script>