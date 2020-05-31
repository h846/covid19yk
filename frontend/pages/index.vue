<template>
  <b-container fluid="lg">
    <!-- トップへ戻るボタン -->
    <BackToTop/>
    <!-- 感染者情報セクション -->
    <b-row align-h="center" class="mb-3" @click="toggle">
      <b-col cols="10" v-b-toggle.collapse-1>
        <span class="h1">市内の最新感染動向</span>
        <b-icon-chevron-down class="icons" v-show="!isActive"></b-icon-chevron-down>
        <b-icon-chevron-up class="icons" v-show="isActive"></b-icon-chevron-up>
      </b-col>
    </b-row>
    <b-collapse id="collapse-1" visible>
      <b-row class="text-center justify-content-center mb-5">
        <b-col sm="5" cols="12" class="mb-4"><PatientNum/></b-col>
        <b-col sm="5" cols="12" class="mb-4"><PatientSituation/></b-col>
      </b-row>
    </b-collapse>
    <!-- テイクアウト・デリバリー検索セクション -->
    <b-row align-h="center">
      <b-col cols="10">
        <h1 class="h1">テイクアウト・デリバリー検索</h1>
      </b-col>
    </b-row>
    <b-row class="justify-content-center">
      <b-col cols="10"><TakeoutDeli/></b-col>
    </b-row>

    <div class="spacer"></div>

  </b-container>
</template>

<script>

import PatientNum from '~/components/charts/PatientNum'
import PatientSituation from '~/components/charts/PatientSituation'
import TakeoutDeli from '~/components/TakeoutDeli'

import BackToTop from '~/components/BackToTop'

export default {
  components: {
    BackToTop,
    PatientNum,
    PatientSituation,
    TakeoutDeli
    },
    data () {
      return {
        isActive: true
      }
    },
    methods: {
      toggle:function(){
        this.isActive = !this.isActive;
      }
    }
  }
</script>

<style lang="scss" scoped>
.spacer{
  margin-bottom: 200px;
}

.h1{
  color:#333;
  font-size: 2rem;
  margin-bottom: 20px;
}

.icons{
  width: 30px;
  height: 30px;
  font-weight: bold;
  cursor: pointer;
}
</style>