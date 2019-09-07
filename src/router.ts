import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
import GameSearchResult from './views/GameSearchResult.vue';
import SynopsisSearchResult from './views/SynopsisSearchResult.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/game/:id',
      name: 'game',
      component: GameSearchResult,
    },
    {
      path: '/synopsis/:synopsis',
      name: 'synopsis',
      component: SynopsisSearchResult,
    },
  ],
});
