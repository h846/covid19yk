<template>
    <!--感染者動向セクション-->
    <section>
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
</template>
<script>
import PatientNum from '~/components/charts/PatientNum'
import PatientSituation from '~/components/charts/PatientSituation'

export default {
    components: {
        PatientNum,
        PatientSituation
    }
}
</script>