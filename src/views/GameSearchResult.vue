<template>
    <div>
        <section class="section">
            <div v-if="!searchGame">
                <p class="is-size-5">ID: {{ id }}のゲームは見つかりませんでした。</p>
            </div>
            <div v-else class="columns is-tablet">
                <div class="column is-3">
                    <Affiliate :game="searchGame"></Affiliate>
                </div>
                <div class="column is-9 has-text-left">
                    <p class="title is-size-3-desktop is-size-4-touch">
                        <a :href="searchGame.url" class="has-text-primary">
                            {{searchGame.title}}
                        </a>
                    </p>
                    <p class="title is-pulled-right is-size-4-desktop is-size-5-touch">
                        に似たゲーム
                    </p>
                </div>
            </div>
        </section>
        
        <hr>

        <section class="section">
            <div v-if="similarGames.length === 0">
                <p class="is-size-5">該当するゲームが見つかりませんでした。</p>
            </div>
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
import Affiliate from '@/components/Affiliate.vue';
import Game from '@/types/Game';
import Api from '@/utils/Api';
import Device from '@/utils/Device';

const EACH_RESULT_NUM = 5;
const MAX_RESULT_NUM = 10;

const api = new Api();

@Component({
  components: {
    GameContent,
    Affiliate,
  },
})
export default class GameSearchResult extends Vue {
    private id: number = 0;
    private searchGame: Game | null = null;
    private similarGames: Game[] = [];
    private currentPage: number = 0;
    private d = new Device();

    private created() {
        this.id = parseInt(this.$route.params.id);
        this.accessGame(this.id);
        this.accessSimilarGames(this.id);
    }

    private mounted() {
        window.addEventListener('scroll', () => {
            if (window.scrollY > document.body.clientHeight - window.innerHeight - 100) {
                this.showMore();
            }
        });
    }

    private accessGame(id: number) {
        api.game(id, (res: any) => {
            this.searchGame = Game.create(res.game);
        });
    }

    private accessSimilarGames(id: number, page: number = 0) {
        api.similarGamesFromId(id, (res: any) => {
            if (res.status !== 200) return;
            for (const game of res.games) {
                if (this.isSearched(game)) continue;
                this.similarGames.push(Game.create(game));
            }
        }, this.currentPage, EACH_RESULT_NUM);
    }

    private isSearched(game: Game): boolean {
        return game.id.toString() === this.$route.params.id.toString();
    }

    private showMore() {
        if (this.similarGames.length >= MAX_RESULT_NUM) return;
        this.accessSimilarGames(this.id, ++this.currentPage);
    }
}

</script>

<style scoped>
img {
    margin: 0 auto;
}

hr {
    width: 95%;
    margin: 0 auto;
}

.image-desktop {
    width: 350px;
}

.image-mobile {
    width: 200px;
}
</style>
