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

        <div class="section is-size-5" v-if="similarGames.length === 0">
            該当するゲームが見つかりませんでした。
        </div>

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

const EACH_RESULT_NUM = 5;
const MAX_RESULT_NUM = 15;

const api = new Api();

@Component({
    components: {
        GameContent,
    },
})
export default class SynopsisSearchResult extends Vue {
    private synopsis!: string;
    private similarGames: Game[] = [];
    private currentPage: number = 0;

    private created() {
        this.synopsis = this.$route.params.synopsis;
        // this.accessSimilarGames(this.synopsis);
    }

    private mounted() {
        window.addEventListener('scroll', () => {
            if (window.scrollY > document.body.clientHeight - window.innerHeight - 100) {
                this.showMore();
            }
        });
    }

    private accessSimilarGames(synopsis: string, page: number = 0) {
        api.similarGamesFromSynopsis(synopsis, (res: any) => {
            if (res.status !== 200) return;
            for (const game of res.games) {
                this.similarGames.push(Game.create(game));
            }
        }, page, EACH_RESULT_NUM);
    }

    private showMore() {
        if (this.similarGames.length >= MAX_RESULT_NUM) return;
        this.accessSimilarGames(this.synopsis, ++this.currentPage);
    }
}
</script>

<style scoped>
hr {
    width: 95%;
    margin: 0 auto;
}
</style>
