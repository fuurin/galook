import Vue from 'vue';
import Router from 'vue-router';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: require('@/views/Home.vue').default,
    },
    {
      path: '/game/:id',
      name: 'game',
      component: require('@/views/GameSearchResult.vue').default,
    },
    {
      path: '/synopsis/:synopsis',
      name: 'synopsis',
      component: require('@/views/SynopsisSearchResult.vue').default,
    },
  ],
});
