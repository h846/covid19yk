<template>
    <transition>
    <b-button href="#tk-deli-search" variant="primary" class="backtotop" v-show="scrollY > 1500">
        <b-icon-arrow-bar-up style="width: 40px; height: 40px;">

        </b-icon-arrow-bar-up>
    </b-button>
    </transition>
</template>
<script>
export default {
    data: function(){
        return {
            scrollY: 0
        }
    },
    mounted(){
        window.addEventListener('scroll', this.calculateScrollY);
    },
    beforeDestroy() {
        window.removeEventListener('scroll', this.calculateScrollY);
    },
    methods: {
        calculateScrollY() {
            this.scrollY = window.scrollY;
            //console.log(this.scrollY);
        }
    }
}
</script>
<style lang="scss">
.backtotop {
    position: fixed;
    bottom: 20px;
    right: 20px;
}

.v-enter-active, .v-leave-active {
  transition: opacity .5s
}

.v-enter, .v-leave-to {
  opacity: 0
}
</style>