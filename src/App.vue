<template>
  <div id="app">
    <nav class="navbar is-fixed-top has-background-primary">
      <router-link to="/">
        <img class="head-logo" src="./assets/logo_gray.png" alt="logo">
      </router-link>
    </nav>
    <div class="container">
      <router-view/>
    </div>
    <footer class="footer">
      <p>ぎゃルック！ エロゲ/ギャルゲAI検索サービス ©️ Noimin, fuurin 2019</p>
    </footer>
  </div>
</template>

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

  // for sticky footer
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.head-logo {
  width: 320px;
  height: 60px;
  margin: 4px 8px;
}

.container {
  margin-top: 100px;
  margin-bottom: 100px;
}
 
.footer {
  margin-top: auto;
  padding: 24px;
}

</style>
