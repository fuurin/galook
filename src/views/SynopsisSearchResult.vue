<template>
    <div class="container">
        <section class="section">
            <h1 class="title is-size-3-desktop is-size-4-touch">
                『{{ synopsis }}』
            </h1>
            <p class="title is-pulled-right is-size-4-desktop is-size-5-touch">
                というあらすじに近いゲーム
            </p>
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
export default class SynopsisSearchResult extends Vue {
    private synopsis!: string;
    private similarGames: Game[] = [];

    private created() {
        this.synopsis = this.$route.params.synopsis;
        this.accessSimilarGames(this.synopsis);
    }

    private accessSimilarGames(synopsis: string) {
        api.similarGamesGromSynopsis(synopsis, (res: any) => {
            if (res.status !== 200) return;
            this.similarGames = [];
            for (const game of res.games) {
                this.similarGames.push(Game.create(game));
            }
        });
    }
}
</script>

<style scoped>
hr {
    width: 95%;
    margin: 0 auto;
}
</style>
