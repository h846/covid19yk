
export default {
  mode: 'universal',
  server: {
    port: 8080,
    host: '0.0.0.0'
  },
  /*
  ** Headers of the page
  */
  head: {
    title: 'テイクアウトデリバリー横浜桜木町' || '',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1, shrink-to-fit=no' },
      { hid: 'description', name: 'description', content: '横浜全域はもとより桜木町駅近辺、野毛、みなとみらいのテイクアウト、デリバリーできるお店を紹介。' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ],
    script:[

    ]
  },
  /*
  ** Global CSS
  */
  css: [
    '@/assets/scss/app.scss'
  ],
  /*
  ** Plugins to load before mounting the App
  */
  plugins: [
    '~/plugins/chartjs-plugin-colorschemes',
    '~/plugins/BootStrapIcons'
  ],
  /*
  ** Nuxt.js dev-modules
  */
  buildModules: [
  ],
  /*
  ** Nuxt.js modules
  */
  modules: [
    // Doc: https://bootstrap-vue.js.org
    ['bootstrap-vue/nuxt', { css: false }],
    // Doc: https://axios.nuxtjs.org/usage
    '@nuxtjs/axios',
    '@nuxtjs/google-analytics',
  ],
  googleAnalytics: {
    id: 'UA-78352500-4'
  },
  /*
  ** Axios module configuration
  ** See https://axios.nuxtjs.org/options
  */
  axios: {
  },
  /*
  ** Build configuration
  */
  build: {
    /*
    ** You can extend webpack config here
    */
    extend (config, ctx) {
    }
  }
}
