<template>
    <div>
        <section class="section">
            <div class="columns is-tablet">
                <div class="column is-2">
                    <a :href="searchGame.url">
                        <img :class="d.respCls('image')" :src="searchGame.image">
                    </a>
                </div>
                <div class="column is-10 has-text-left">
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
import Device from '@/utils/Device';

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
    public d = new Device();

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
            this.similarGames = [];
            for (const game of res.games) {
                this.similarGames.push(Game.create(game));
            }
        });
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
    width: 300px;
}

.image-mobile {
    width: 200px;
}
</style>
