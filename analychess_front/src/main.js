import Vue from 'vue'
import router from './router/router'
import App from './App.vue'
import Toasted from 'vue-toasted';

Vue.use(Toasted)


Vue.config.productionTip = false
new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
