<template>
  <section>
    <v-container fluid fill-height>
      <v-row
        class="text-center"
      >
        <v-col cols="2">
          <p>Hey!</p>
        </v-col>
        <v-col cols="2">
          <v-btn
            color="primary"
          >
            Click Me!!
          </v-btn>
        </v-col>
        <v-col cols="6">
          <PatientNum/>
        </v-col>
      </v-row>
    </v-container>
  </section>
</template>

<script>
import PatientNum from '~/components/PatientNum'

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
