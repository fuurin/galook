<template>
    <div>
        <section class="section">
            <div class="columns is-tablet">
                <div class="column is-2">
                    <a :href="searchGame.url">
                        <img class="is-hidden-touch" :src="searchGame.image">
                        <img class="is-hidden-desktop" :src="searchGame.image">
                    </a>
                </div>
                <div class="column is-10 has-text-left">
                    <h1 class="title is-3">
                        <a  :href="searchGame.url" 
                            class="has-text-primary title is-3">
                            {{searchGame.title}}
                        </a>
                    </h1>
                    <p class="title is-4 is-pulled-right">に似たゲーム</p>
                </div>
            </div>
        </section>
        
        <hr>

        <section class="section">
            <GameContent
                v-for="game in similarGames"
                :game="game"
                :key="game.id"
            ></GameContent>
        </section>
    </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
import GameContent from '@/components/GameContent.vue';
import Game from '@/types/Game';
import Api from '@/utils/Api';

const api = new Api();

@Component({
  components: {
    GameContent,
  },
})
export default class GameSearchResult extends Vue {
    public id: number = 0;
    public searchGame!: Game;
    public similarGames: Game[] = [];

    private created() {
        this.id = parseInt(this.$route.params.id);
        this.accessGame(this.id);
        this.accessSimilarGames(this.id);
    }

    private accessGame(id: number) {
        api.game(id, (res: any) => {
            // const game = res.game;
            const game = res.games[0];
            this.searchGame = Game.create(game);
        });
    }

    private accessSimilarGames(id: number) {
        api.similarGamesFromId(id, (res: any) => {
            if (res.status !== 200) return;
            this.similarGames = res.games;
        });
    }
}

</script>

<style scoped>
img {
    margin: 0 auto;
}

.is-hidden-touch {
    width: 150px;
}

.is-hidden-desktop {
    width: 300px;
}
</style>
