<template>
  <b-container fluid="lg">
    <BackToTop/>
    <b-row>
      <b-col>
        <h1 class="h1">市内の最新感染動向</h1>
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

import BackToTop from '~/components/BackToTop'

export default {
  components: {
    BackToTop,
    PatientNum,
    PatientSituation,
    TkotDeli
    },
    data () {
      return {
      }
    },
    methods: {

    }
  }
</script>

<style lang="scss">
.spacer{
  margin-bottom: 200px;
}
</style>