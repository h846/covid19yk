<template>
    <!-- 野毛ショップリスト -->
    <section>
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
</template>
<script>
import NogeList from '~/components/NogeList'

export default {
    components: {
        NogeList
    }
}
</script>