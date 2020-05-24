<template>
<div>
  <b-navbar toggleable="lg" type="dark" variant="primary">
    <b-navbar-brand to="/">コロナ対策横浜</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item to="/about">
          このサイトについて
        </b-nav-item>
      </b-navbar-nav>
    </b-collapse>

  </b-navbar>
</div>
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