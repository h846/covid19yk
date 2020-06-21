<template>
  <b-container fluid>
    <!--ジャンボトロン-->
    <b-row class="justify-content-center">
      <b-col sm="10">
        <b-jumbotron class="jumbo">

          <template v-slot:header header-level="4">
            テイクアウト デリバリー <br/>野毛 桜木町 みなとみらい
          </template>

          <template v-slot:lead>
            桜木町駅近辺の野毛・みなとみらいでテイクアウト、デリバリーに対応している飲食店をリスト化
          </template>

          <p class="ts">
            横浜全域の検索も対応。<br/>新型コロナウィルス感染症動向も確認できます。
          </p>
          <b-button-group>
            <b-button variant="warning" @click="chgContents('noge')">野毛・みなとみらいショップリスト</b-button>
            <b-button variant="success" @click="chgContents('yokohama')">テイクアウトデリバリー横浜全域検索</b-button>
            <b-button variant="primary" @click="chgContents('infection')">新型コロナウィルス感染動向</b-button>
          </b-button-group>
        </b-jumbotron>
      </b-col>
    </b-row>
    <!-- 野毛ショップリスト -->
    <section v-if="isShow === 'noge'">
      <b-row align-h="center" class="my-3">
        <b-col sm="10">
          <h2>野毛・みなとみらいショップリスト</h2>
        </b-col>
      </b-row>

      <b-row class="justify-content-center">
        <b-col sm="10">
          <NogeList/>
        </b-col>
      </b-row>
    </section>
    <!-- 横浜全域テイクアウト・デリバリー検索セクション -->
    <section v-else-if="isShow === 'yokohama'">
      <b-row align-h="center" class="my-3">
        <b-col cols="10">
          <h2>横浜市テイクアウト・デリバリー検索</h2>
        </b-col>
      </b-row>

      <b-row class="justify-content-center">
        <b-col sm="10"><TakeoutDeli/></b-col>
      </b-row>
    </section>

    <!--感染者動向セクション-->
    <section v-else-if="isShow === 'infection'">
      <b-row align-h="center" class="mb-3">
          <b-col cols="10">
              <h2>横浜市内の最新感染動向</h2>
          </b-col>
      </b-row>
      <b-row class="text-center justify-content-center mb-5">
          <b-col sm="5" cols="12" class="mb-4"><PatientNum/></b-col>
          <b-col sm="5" cols="12" class="mb-4"><PatientSituation/></b-col>
      </b-row>
    </section>

    <div class="spacer"></div>

  </b-container>
</template>

<script>
import TakeoutDeli from '~/components/TakeoutDeli'
import NogeList from '~/components/NogeList'
import PatientNum from '~/components/charts/PatientNum'
import PatientSituation from '~/components/charts/PatientSituation'

export default {
  components: {
    TakeoutDeli,
    NogeList,
    PatientNum,
    PatientSituation
    },
    data () {
      return {
        isShow: 'noge'
      }
    },
    methods: {
      chgContents: function(val){
        this.isShow = val;
      }
    }
  }
</script>

<style lang="scss" scoped>
.spacer{
  margin-bottom: 200px;
}

.icons{
  width: 30px;
  height: 30px;
  font-weight: bold;
  cursor: pointer;
}

.jumbo{
  h1 { font-size: 2.5rem; margin-bottom: 10px;}
  .lead{ font-size: 1.0rem;}
  color: #FFF;
  max-height: 450px;
  background: center no-repeat #616161 url("~assets/img/bg.jpg");
  background-blend-mode: soft-light;
  background-size: cover;
}

@media screen and (max-width: 650px) {
  .jumbo{
    h1 {
      font-size: 1.2rem;
      margin-bottom: 20px;
    }
    .lead{
      font-size: 0.8rem;
    }
    .lead + p {
      margin-bottom: 20px;
    }
    button{
      font-size: 0.7rem;
    }
    font-size: 0.8rem;
  }
}

.ts{
    text-shadow: 
    #333 2px 0px 0px, #333 -2px 0px 0px,
    #333 0px -2px 0px, #333 0px 2px 0px,
    #333 2px 2px 0px, #333 -2px 2px 0px,
    #333 2px -2px 0px, #333 -2px -2px 0px,
    #333 1px 2px 0px, #333 -1px 2px 0px,
    #333 1px -2px 0px, #333 -1px -2px 0px,
    #333 2px 1px 0px, #333 -2px 1px 0px,
    #333 2px -1px 0px, #333 -2px -1px 0px,
    #333 1px 1px 0px, #333 -1px 1px 0px,
    #333 1px -1px 0px, #333 -1px -1px 0px;
}
</style>