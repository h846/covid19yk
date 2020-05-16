<template>
  <b-container fluid="lg">
    <b-row class="text-center justify-content-center">
      <b-col sm="6" cols="12"><PatientNum/></b-col>
      <b-col sm="6" cols="12"><PatientSituation/></b-col>
    </b-row>
  </b-container>
</template>

<script>

import PatientNum from '~/components/charts/PatientNum'
import PatientSituation from '~/components/charts/PatientSituation'

export default {
  components: {
    PatientNum,
    PatientSituation
    },
    data () {
      return {
      }
    },
  }
</script>