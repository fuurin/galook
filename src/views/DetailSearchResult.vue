<template>
    <div class="container">
        <section class="section">
            <h1 v-for="detail in details" :key="detail.name"
                class="title is-size-4-desktop is-size-5-touch">
                {{ titleRow(detail) }}
            </h1>
            <p class="title is-pulled-right is-size-5-desktop is-size-6-touch">
                での詳細検索結果
            </p>
        </section>
        
        <hr>

        <section class="section">
            <GameContent
                v-for="game in games"
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
export default class DetailSearchResult extends Vue {
    private details = [
        { name: "brand", label: "ブランド", input: "", match: "perfect" },
        { name: "category", label: "カテゴリー", input: "", match: "perfect" },
        { name: "genre", label: "ジャンル", input: "", match: "perfect" },
        { name: "writer", label: "ライター", input: "", match: "perfect" },
    ];
    private searchGame: Game = new Game();
    private games: Game[] = [];
    private currentPage: number = 0;


    private created() {
        for (const detail of this.details) {
            if (!this.$route.query[detail.name]) continue;
            detail.input = this.$route.query[detail.name].toString();
            detail.match = this.$route.query[detail.name + "_match"].toString();
        }
        this.searchGames();
    }

    private mounted() {
        window.addEventListener('scroll', () => {
            if (window.scrollY > document.body.clientHeight - window.innerHeight - 100) {
                this.showMore();
            }
        });
    }

    private titleRow(detail: any) {
        if (!detail.input || !detail.label) return;
        return detail.label + "：" + detail.input;
    }

    private searchGames(page: number = 0) {
        api.gamesFromInfo(this.searchGame, (res: any) => {
            if (res.status !== 200) return;
            for (const game of res.games) {
                this.games.push(Game.create(game));
            }
        }, page, EACH_RESULT_NUM);
    }

    private showMore() {
        if (this.games.length >= MAX_RESULT_NUM) return;
        this.searchGames(++this.currentPage);
    }
}
</script>

<style scoped>
hr {
    width: 95%;
    margin: 0 auto;
}
</style>
