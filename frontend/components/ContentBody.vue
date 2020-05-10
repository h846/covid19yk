<template>
    <v-content>
      <v-container
        class="fill-height"
        fluid
      >
        <v-row>
          
          <v-col cols="6">
            <PatientNum/>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
</template>

<script>
import PatientNum from '~/components/charts/PatientNum'

export default {
    components:{
        PatientNum
    }
}
</script>