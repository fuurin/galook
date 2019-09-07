<template>
  <div id="app">
    <nav class="navbar is-fixed-top has-background-primary level is-mobile">
      <div class="level-left has-text-left">
        <div class="level-item">
          <router-link to="/">
            <img class="head-logo" src="./assets/logo_white.png" alt="logo">
          </router-link>
        </div>
      </div>
      <div class="level-right">
        <div class="level-item">
          <a v-if="$route.path !== '/'" class="button" @click="openModal">
            <i class="fas fa-search"></i>検索
          </a>
        </div>
      </div>
    </nav>
    <div class="container main-container" v-if="galookAgeChecked">
      <transition mode="out-in">
        <router-view/>
      </transition>
    </div>
    <div class="container" v-else>
      <div class="hero">
        <div class="hero-body">
          <div class="container">
            <br><br><br><br><br>
            <p>恐れ入りますが、当サイトは18歳未満の方のご利用をお断りしております。</p>
          </div>
        </div>
      </div>
    </div>
    <footer class="footer">
      <p>ぎゃルック！ エロゲ/ギャルゲAI検索サービス by Noimin, fuurin (2019)</p>
      <p>Powered by <a href="http://www.getchu.com/">Getchu.com</a></p>
    </footer>

    <transition mode="out-in" name="modal">
      <div class="modal" :class="{'is-active': modalOpened}" v-show="modalOpened">
        <div class="modal-background" @click="closeModal"></div>
        <div class="modal-card">
          <header class="modal-card-head">
            <p class="modal-card-title">検索</p>
            <button class="delete" aria-label="close" @click="closeModal"></button>
          </header>
          <section class="modal-card-body">
            <GameSearch></GameSearch>
            <SynopsisSearch></SynopsisSearch>
          </section>
          <footer class="modal-card-foot">
          </footer>
        </div>
      </div>
    </transition>

    <div class="modal" :class="{'is-active': ageCheckOpened}">
      <div class="modal-background" @click="closeAgeCheck"></div>
      <div class="modal-card">
        <header class="modal-card-head">
          <p class="modal-card-title">警告</p>
        </header>
        <section class="modal-card-body">
          <p>本サイトはアダルトコンテンツを掲載しております。</p>
          <p>18歳未満の方が利用することはできません。</p>
          <p>あなたは18歳以上ですか？</p>
          <div class="level age-check-buttons is-mobile">
            <div class="level-left has-text-centered">
              <a class="button is-primary is-large" @click="ageCheck">はい</a>              
            </div>
            <div class="level-right has-text-centered">
              <a class="button is-large" @click="closeAgeCheck">いいえ</a>
            </div>
          </div>
        </section>
        <footer class="modal-card-foot">
        </footer>
      </div>
    </div>

  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue, Watch } from 'vue-property-decorator';
import GameSearch from './components/GameSearch.vue';
import SynopsisSearch from './components/SynopsisSearch.vue';
import Cookies from 'js-cookie';

const AGE_CHECK_KEY = "galookAgeChecked";

@Component({
  components: {
    GameSearch,
    SynopsisSearch,
  },
})
export default class Home extends Vue {
  private galookAgeChecked: boolean = false;
  private ageCheckOpened: boolean = true;
  private modalOpened: boolean = false;

  private created() {
    const checked = Cookies.get(AGE_CHECK_KEY);
    if (checked && checked === "true") {
      this.galookAgeChecked = true;
      this.closeAgeCheck();
    }
  }

  @Watch('$route')
  private routeUpdate() {
    this.closeModal();
  }

  private ageCheck() {
    this.galookAgeChecked = true;
    this.ageCheckOpened = false;
    Cookies.set(AGE_CHECK_KEY, "true");
  }

  private closeAgeCheck() {
    this.ageCheckOpened = false;
  }

  private openModal() {
    this.modalOpened = true;
  }

  private closeModal() {
    this.modalOpened = false;
  }
}
</script>

<style lang="scss">
@import "../node_modules/bulma/sass/utilities/initial-variables";
@import "../node_modules/bulma/sass/utilities/functions";

$primary: #00bcd4; // main color
$info: #ebdd1b; // accent color

@import "../node_modules/bulma/bulma.sass";

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  width: 100%;

  // for sticky footer
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.main-container {
  padding: 0 20px;
}

.v-enter-active, .v-leave-active {
  transition: opacity .2s;
}
.v-enter, .v-leave-to {
  opacity: 0.2;
}

.head-logo {
  width: 40%;
}

.level-left {
  margin: 4px 0px 6px 8px;
  max-width: 200px;
}

.level-right {
  margin-right: 16px;
}

.container {
  margin-top: 100px;
  margin-bottom: 100px;
}
 
.footer {
  margin-top: auto;
  padding: 24px;
}


.modal-enter-active {
  transition: opacity .2s;
}

.modal-enter {
  opacity: 0;
}

.modal-background {
  background-color: rgba(10, 10, 10, 0.5);
}

.modal-card {
  max-width: 560px;
  padding: 0 20px;
}

.age-check-buttons {
  width: 350px;
  margin: 15px auto 0px auto;
}
</style>
