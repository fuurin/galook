<template>
  <div class="home">
    <img class="logo" alt="LOGO" src="../assets/logo_white_back.png">
    <h4 class="subtitle is-size-4-desktop is-size-5-touch">エロゲ/ギャルゲAI検索サービス</h4>
    <GameSearch></GameSearch>
    <SynopsisSearch></SynopsisSearch>
    <DetailSearch></DetailSearch>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import GameSearch from '@/components/GameSearch.vue';
import SynopsisSearch from '@/components/SynopsisSearch.vue';
import DetailSearch from '@/components/DetailSearch.vue';

@Component({
  components: {
    GameSearch,
    SynopsisSearch,
    DetailSearch,
  },
})
export default class Home extends Vue {}
</script>

<style scoped>
  .home {
    max-width: 560px;
  }
  
  .logo {
    width: 90%;
    margin-top: 60px;
    margin-bottom: 20px;
  }
</style>