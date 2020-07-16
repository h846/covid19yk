<template>
  <b-navbar toggleable="lg" type="dark" variant="primary" style="margin-bottom: 30px;">
    <b-navbar-brand to="/" style="font-size: 1rem">テイクアウトデリバリー横浜桜木町</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>

        <b-nav-item to="/about">
          このサイトについて
        </b-nav-item>
        
      </b-navbar-nav>
    </b-collapse>

  </b-navbar>
</template>
<script>
export default {
  
}
</script>
<style lang="scss" scoped>
a{
  text-decoration: none;
  color: #FFF;
}
</style>