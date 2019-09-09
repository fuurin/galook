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
        
        <div class="search-result" v-show="empty()">
            <div class="result-list list is-hoverable">
                <div v-for="cand in candidates" :key="cand.id" 
                    class="list-item has-text-left">
                    <small>
                        <router-link class="has-text-primary"
                            :to="{name: 'game', params: {id: cand.id}}">
                            {{ cand.title }}
                        </router-link>
                    </small>
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
const NUM_CANDIDATES: number = 50;

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

    @Watch("$route")
    private clear() {
        this.searchText = "";
        this.candidates = [];
    }

    private empty(): boolean {
        return this.candidates.length > 0;
    }

    private paged(): boolean {
        return this.candidates.length >= this.numCandidates;
    }

    private access(searchText: string) {
        this.candidates = [];
        if (!searchText) { return; }
        api.gameTitleCandidates(searchText, (res: any) => {
            this.update(res.games);
        }, this.numCandidates);
    }

    private update(games: any) {
        for (const game of games) {
            if (this.isSearched(game)) continue;
            this.candidates.push(new GameCandidate(game.id, game.title));
        }
    }

    private isSearched(game: any): boolean {
        return game.id === this.$route.params.id;
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
    max-width: 560px;
}

</style>