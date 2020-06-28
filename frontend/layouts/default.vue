<template>
  <div>
    <NavBar/>
    <b-container>
      <!--ジャンボトロン-->
      <b-row class="justify-content-center">
        <b-col sm="10">
          <b-jumbotron class="jumbo">
            <h1 class="title">
              テイクアウト デリバリー <br/>野毛 桜木町 みなとみらい
            </h1>

          </b-jumbotron>

          <div class="lead">
            桜木町駅近辺の野毛・みなとみらいでテイクアウト、
              デリバリーに対応している飲食店をリスト化。<br>
              横浜市全域の飲食店にも対応。
          </div>

          <b-button-group>
              <b-button variant="warning" to="/noge">野毛・みなとみらいショップリスト</b-button>
              <b-button variant="success" to="/yokohama">テイクアウトデリバリー横浜全域検索</b-button>
              <b-button variant="primary" to="/infections">新型コロナウィルス感染動向</b-button>
          </b-button-group>

        </b-col>
      </b-row>
      <!--MAIN BODY-->
      <transition>
        <nuxt/>
      </transition>
      <!--*********-->
    </b-container>
  </div>       
</template>
<script>
import NavBar from '~/components/NavBar'

export default {
  components:{
    NavBar
  }
}
</script>
<style lang="scss" scoped>

.v-enter-active, .v-leave-active {
  transition: opacity .5s;
}
.v-enter, .v-leave-to {
  opacity: 0;
}

.v-enter-active, .v-leave-active {
  transition: opacity .5s;
}
.v-enter, .v-leave-to {
  opacity: 0;
}
.jumbo{
  position: relative;
  height: 300px;
  margin: 0;
  margin-bottom: 10px;
  h1 {
      position: absolute;
      top :40px;
      left: 28%;
      font-size: 1.8rem;
    }
  color: #FFF;
  max-height: 350px;
  background: center 23% no-repeat url("~assets/img/bg.jpg");
  background-size: cover;
}

.lead{
  font-size: 1.2rem;
  margin-bottom: 10px;
}
.btn-group{
  margin-bottom:10px;
}
.btn{
  font-size: 0.9rem;
}



@media screen and (max-width: 650px) {
  .jumbo{
    h1 {
      font-size: 1.2rem;
    }
  }
  .lead{
    font-size: 0.8rem;
    margin-bottom: 10px;
  }
  .btn{
    font-size: 0.6rem;
  }
}

.title{
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