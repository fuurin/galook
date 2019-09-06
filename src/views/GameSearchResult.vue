<template>
    <div>
        <section class="section">
            <h1 class="title">
                「{{searchGame.title}}」に似たゲーム
            </h1>
        </section>
        
        <hr>

        <section class="section">
            <GameMedia
                v-for="game in similarGames"
                :game="game"
                :key="game.id"
            ></GameMedia>
        </section>
    </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
import GameMedia from '@/components/GameMedia.vue';
import Game from '@/types/Game';
import Api from '@/utils/Api';

const api = new Api();

@Component({
  components: {
    GameMedia,
  },
})
export default class GameSearchResult extends Vue {
    public id: number = 0;
    public searchGame!: Game;
    public similarGames!: Game[];

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
            this.similarGames = res.games;
        });
    }
}

</script>

<style scoped>

</style>
