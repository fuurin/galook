<template>
  <div class="home">
    <img class="logo" alt="LOGO" src="../assets/logo_white_back.png">
    <h4 class="subtitle is-4">エロゲ/ギャルゲAI検索サービス</h4>
    <GameSearch></GameSearch>
    <SynopsisSearch></SynopsisSearch>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import GameSearch from '@/components/GameSearch.vue';
import SynopsisSearch from '@/components/SynopsisSearch.vue';

@Component({
  components: {
    GameSearch,
    SynopsisSearch,
  },
})
export default class Home extends Vue {}
</script>

<style scoped>
  .logo {
    width: 560px;
    height: 105px;
    margin-top: 100px;
    margin-bottom: 20px;
  }
</style>