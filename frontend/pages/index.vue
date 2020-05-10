<template>
  <section>
    <NavDrawer/>
    <ContentBody/>
  </section>
</template>

<script>
import NavDrawer from '~/components/NavDrawer'
import ContentBody from '~/components/ContentBody'

export default {
  components: {
    NavDrawer,
    ContentBody,
  },
  data: function(){
    return {
      message: 'Yay'
    }
  },
  methods : {
  }
}
</script>

<style></style>
