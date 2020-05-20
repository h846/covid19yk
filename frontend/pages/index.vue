<template>
  <b-container fluid="lg">
    <div>
      <b-jumbotron header="コロナ対策情報横浜" lead="Bootstrap v4 Components for Vue.js 2">
        <p>For more information visit website</p>
        <b-button variant="primary" href="#">このサイトについて</b-button>
      </b-jumbotron>
    </div>
    <b-row>
      <b-col>
        <h1 class="h1">コロナ感染者状況</h1>
      </b-col>
    </b-row>
    <b-row class="text-center justify-content-center mb-5">
      <b-col sm="5" cols="12" class="mb-4"><PatientNum/></b-col>
      <b-col sm="5" cols="12" class="mb-4"><PatientSituation/></b-col>
    </b-row>
    <b-row>
      <b-col><h1 class="h1">テイクアウト・デリバリー検索</h1></b-col>
    </b-row>
    <b-row class="justify-content-center">
      <b-col cols="10"><TkotDeli/></b-col>
    </b-row>

    <div class="spacer"></div>

  </b-container>
</template>

<script>

import PatientNum from '~/components/charts/PatientNum'
import PatientSituation from '~/components/charts/PatientSituation'
import TkotDeli from '~/components/TkotDeli'

export default {
  components: {
    PatientNum,
    PatientSituation,
    TkotDeli
    },
    data () {
      return {
      }
    },
  }
</script>

<style lang="sass">
.spacer{margin-bottom: 200px;}
</style>