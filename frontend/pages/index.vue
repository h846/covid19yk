<template>
  <b-container fluid="lg">
    <div>
      <b-jumbotron header="コロナ対策情報横浜" lead="Bootstrap v4 Components for Vue.js 2">
        <p>For more information visit website</p>
        <b-button variant="primary" href="#">このサイトについて</b-button>
      </b-jumbotron>
    </div>
    <b-row class="text-center justify-content-center">
      <b-col sm="5" cols="12" class="mb-4"><PatientNum/></b-col>
      <b-col sm="5" cols="12" class="mb-4"><PatientSituation/></b-col>
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