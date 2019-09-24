<template>
    <div>
        <div class="field">
            <div class="control has-icons-left">
                <input v-model="searchText" class="input" type="search" 
                    @keydown.enter="scroll"
                    placeholder="類似ゲームを検索">
                <span class="icon is-small is-left">
                    <i class="fas fa-search"></i>
                </span>
            </div>
        </div>
        
        <div class="search-result has-text-right" v-show="!empty()"
            :class="d.respCls('search-result')">
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
import Device from '@/utils/Device';

const ACCESS_INTERVAL: number = 500; // ms
const NUM_CANDIDATES: number = 50; // APIに渡すlimit数

const api = new Api();

@Component
export default class GameSearch extends Vue {
    private searchText: string = "";
    private accessTimer: number | null = null;
    private candidates: GameCandidate[] = [];
    private numCandidates: number = NUM_CANDIDATES;
    private d: Device = new Device();

    @Watch("searchText")
    private onSearchTextChange() {
        if (this.accessTimer !== null) {
            clearTimeout(this.accessTimer);
        }
        this.accessTimer = setTimeout(() => {
            this.access(this.searchText);
            this.accessTimer = null;
        }, ACCESS_INTERVAL);

        if (this.searchText === "") {
            this.candidates = [];
        }
    }

    @Watch("$route")
    private clear() {
        this.searchText = "";
        this.candidates = [];
    }

    private scroll() {
        if (!this.d.isMobile() || this.$route.name !== "home") return;
        window.scrollTo({top: 170, behavior: "smooth"});
    }

    private empty(): boolean {
        return this.candidates.length <= 0;
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

        if (this.d.isMobile() && this.$route.name === "home" && !this.empty()) {
            setTimeout(() => {
                window.scrollTo({top: 170, behavior: "smooth"});
            }, 100);
        }
    }

    private isSearched(game: any): boolean {
        return game.id === this.$route.params.id;
    }
}

</script>

<style scoped>
.search-result {
    margin-bottom: 0.75rem;
    overflow-y: scroll;
    transform: translateZ(0); /* Retinaでは必要らしい？ */  
}

.search-result-desktop {
    height: 240px;
}

.search-result-mobile {
    height: 200px;
}
</style>