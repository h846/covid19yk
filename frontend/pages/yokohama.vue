<template>
    <!-- 横浜全域テイクアウト・デリバリー検索セクション -->
    <section>
      <b-row align-h="center" class="my-3">
        <b-col cols="10">
          <h2>横浜市テイクアウト・デリバリー検索</h2>
        </b-col>
      </b-row>

      <b-row class="justify-content-center">
        <b-col sm="10"><YokohamaList/></b-col>
      </b-row>
    </section>
</template>
<script>
import YokohamaList from '~/components/YokohamaList'

export default {
    components: {
        YokohamaList
    }
}
</script>
<style lang="scss">

</style>