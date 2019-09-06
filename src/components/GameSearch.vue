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
                <router-link v-for="cand in candidates" :key="cand.id"
                    class="list-item has-text-left has-text-primary"
                    :to="{name: 'game', params: {id: cand.id}}"
                >
                    {{ cand.title }}
                </router-link>
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
import { Component, Prop, Vue, Watch } from 'vue-property-decorator';
import { GameCandidate } from '@/types/GameCandidate';
import axios from 'axios';

const API_ADDRESS: string = "3.115.42.95/similar_games";
const ACCESS_INTERVAL: number = 500; // ms
const NUM_CANDIDATES: number = 10;

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
        // axios.get(API_ADDRESS).then((res: any) => {
        //     if (res.status !== 200) return;
        //     this.updateInterval(res.games);
        // });
        this.updateInterval(exampleResponce.games);
    }

    private updateInterval(games: any) {
        for (const game of games) {
            this.candidates.push(new GameCandidate(game.id, game.title));
        }
    }
}



// ゲーム名検索用にもっと軽いレスポンスのAPIが欲しい
const exampleResponce = {
    status: 200,
    message: "OK",
    games: [
        {
            id: 786920,
            brand: "Norn",
            category: ["妹", "あまあま", "中出し"],
            story: "お兄ちゃん大好きな二人の妹、ちせ と あいり。そんな彼女たちの望みは、お兄ちゃんのお嫁さんになること！そのためにふたりは、望みが叶うと言われる神社の湧き水を飲むが……強力な湧き水の効果で、妹たちはお兄ちゃんちんちんですぐ発情するエッチな体質に変わってしまい、エロエロ奇跡ばかりの種付け生活が始まるのだった！",
            subgebre: ["アドベンチャー"],
            title: "神様お願い！お兄ちゃんの赤ちゃん妊娠したいの！ 〜ツンデレ妹＆清純妹とエッチなキセキでトラブル子作り三昧♪〜",
            url: "http://www.getchu.com/soft.phtml?id=786920",
            writer: ["鷹之爪"],
        },
        {
            id: 754181,
            brand: "Norn",
            category: ["田舎", "妹", "あまあま", "中出し"],
            story: "田舎に帰省した主人公は、兄のことが大好きな4人の妹たちに早速じゃれつかれることに。妹たちはお互いが恋のライバルとして牽制しつつ、このチャンスに愛するお兄ちゃんと結ばれようと大胆なアタックを開始！こうして、かわいい妹4人と田舎暮らしをたっぷりエッチに楽しむ妹ハーレムが始まったのだった！",
            subgenre: ["アドベンチャー"],
            title: "妹4人と中出し性活！〜じゃれつき甘えにお世話♪妹たちとイチャイチャがとまらない！お兄ちゃんの精子は絶滅必至!?〜",
            url: "http://www.getchu.com/soft.phtml?id=754181",
            writer: ["鷹之爪"],
        },
        {
            id: 814447,
            brand: "Galette",
            category: ["同棲", "妹", "あまあま", "ラブコメ"],
            story: "「私たち、今日からお兄ちゃんの右手（コイビト）です」お兄ちゃんは一人暮らしの学園生。ある日、妹たちをかばって右手に怪我を負ってしてしまったお兄ちゃん。幸い怪我は軽傷、けれども妹たちは大怪我を負ったと勘違い !?治るまで学園を休まざるを得なくなってしまったのだった。さらに、妹たちによってしばらく右手の使用を禁止されてしまうお兄ちゃん。これでは毎日の生活が困る、そんなお兄ちゃんに妹たちは驚きの提案をしてきた。「私たちがつきっきりで、右手の代わりをしてあげる」ひとつの部屋で生活しながら、右手のすること全部を妹がしてくれる。そんな毎日がこうしてやってきたのであった……とにかく過保護な妹たちに、家事も買い物もオナニーも、全部をやってもらう日々。妹と二人きりの怠惰な日常、過ごしてみませんか？",
            subgenre: ["アドベンチャー"],
            title: "お兄ちゃん、右手の使用を禁止します！",
            url: "http://www.getchu.com/soft.phtml?id=814447",
            writer: ["七歌", "8", "東人"],
        },
    ],
};

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