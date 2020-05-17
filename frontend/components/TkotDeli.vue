<template>
    
</template>

<script>
export default {
    data: function(){
        return: {

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

    }
}
</script>