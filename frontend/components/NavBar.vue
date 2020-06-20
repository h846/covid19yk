<template>
  <b-navbar toggleable="lg" type="dark" variant="primary" style="margin-bottom: 30px;">
    <b-navbar-brand to="/">野毛 桜木町 テイクアウト デリバリー検索</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        
        <b-nav-item to="/infectInfo">
          感染者の状況
        </b-nav-item>

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