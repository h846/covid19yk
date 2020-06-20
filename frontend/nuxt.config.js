
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
    title: '野毛 桜木町 テイクアウト・デリバリー検索 | ヤシログ' || '',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1, shrink-to-fit=no' },
      { hid: 'description', name: 'description', content: process.env.npm_package_description || '' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ],
    script:[
      {
        src: "https://code.jquery.com/jquery-3.5.1.slim.js",
        integrity: "sha256-DrT5NfxfbHvMHux31Lkhxg42LY6of8TaYyK50jnxRnM=",
        crossorigin: "anonymous",
        type: "text/javascript"
    }
  ]
  },
  /*
  ** Customize the progress-bar color
  */
  loading: { color: '#fff' },
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
