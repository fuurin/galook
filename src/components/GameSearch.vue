<template>
    <div>
        <div class="field">
            <div class="control has-icons-left">
                <input class="input" type="text" placeholder="類似ゲームを検索" v-model="searchText">
                <span class="icon is-small is-left">
                    <i class="fas fa-search"></i>
                </span>
            </div>
        </div>

        <div class="search-result" v-show="candidates.length !== 0">
            <div class="result-list list is-hoverable">
                <div v-for="cand in candidates" :key="cand.id">
                    <router-link 
                        class="list-item has-text-left has-text-primary"
                        :to="{name: 'game', params: {id: cand.id}}"
                    >
                        {{ cand.title }}
                    </router-link>
                </div>
            </div>
            <div class="columns" v-if="candidates.length > numCandidates">
                <div class="column has-text-left">
                    <a class="button" disabled>←</a>
                </div>
                <div class="column has-text-right">
                    <a class="button">→</a>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { Component, Prop, Vue, Watch} from 'vue-property-decorator';
import GameCandidate from '@/types/GameCandidate';
import Api from '@/utils/Api';

const ACCESS_INTERVAL: number = 500; // ms
const NUM_CANDIDATES: number = 10;

const api = new Api();

@Component
export default class GameSearch extends Vue {
    private searchText: string = "";
    private accessTimer: number | null = null;
    private candidates: GameCandidate[] = [];
    private numCandidates: number = NUM_CANDIDATES;

    @Watch("searchText")
    private onSearchTextChange() {
        if (this.accessTimer !== null) {
            clearTimeout(this.accessTimer);
        }
        this.accessTimer = setTimeout(() => {
            this.access(this.searchText);
            this.accessTimer = null;
        }, ACCESS_INTERVAL);
    }

    private access(searchText: string) {
        this.candidates = [];
        if (!searchText) { return; }
        api.gameTitleCandidates(searchText, (res: any) => {
            this.updateInterval(res.games);
        });
    }

    private updateInterval(games: any) {
        for (const game of games) {
            this.candidates.push(new GameCandidate(game.id, game.title));
        }
    }
}

</script>

<style scoped>
.search-result {
    margin-bottom: 30px;
}

.result-list {
    margin-bottom: 15px;
}

.list-item {
    /* はみ出したところだけスクロールしたい https://webparts.cman.jp/string/scroll/ */
    max-width: 560px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}
</style>