<template>
  <div>
    <NavBar class="mb-5"/>
    <nuxt />
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