import Vue from 'vue';
import App from './App.vue';
import router from './router';

import '@fortawesome/fontawesome-free-webfonts/css/fontawesome.css'; // 基本ファイル
import '@fortawesome/fontawesome-free-webfonts/css/fa-brands.css'; // fab
import '@fortawesome/fontawesome-free-webfonts/css/fa-regular.css'; // far
import '@fortawesome/fontawesome-free-webfonts/css/fa-solid.css';  // fas

Vue.config.productionTip = false;

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
