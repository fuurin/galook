<template>
    <div>
        <section class="section">
            <h1 class="synopsis title is-3">
                『{{ synopsis }}』
            </h1>
            <p class="title is-4 is-pulled-right">
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
            this.similarGames = res.games;
        });
    }
}
</script>

<style scoped>
.synopsis {
    padding: 0 30px;
}
</style>
