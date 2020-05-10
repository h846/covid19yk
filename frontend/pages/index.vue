<template>
  <section>

    <PatientNum/>
  </section>
</template>

<script>
import PatientNum from '~/components/charts/PatientNum'

export default {
  components: {
    PatientNum
  },
  data: function(){
    return {
      message: 'Yay',
    }
  },
  methods : {}
}
</script>

<style></style>
