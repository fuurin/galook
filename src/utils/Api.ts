import axios from 'axios';
import GameQuery from '@/types/GameQuery';

const BASE_URL = "https://api.galook.net/";

export default class Api {
    public gameTitleCandidates(text: string, callback: (res: any) => void, limit: number = 20) {
        // axios.get(BASE_URL + "games", {params: { text, limit }}).then(callback);
        const res: any = {games: []};
        for (let i = 0; i < 5; i++) {
            for (const game of exampleResponce.games) {
                res.games.push({ id: game.id, title: game.title});
            }
        }
        callback(res);
    }

    public similarGamesFromSynopsis(text: string, callback: (res: any) => void, page: number = 0, limit: number = 20) {
        this.search("similar_games", { text, page, limit }, callback);
    }

    public similarGamesFromId(id: number, callback: (res: any) => void, page: number = 0, limit: number = 20) {
        this.search("similar_games", { id, page, limit }, callback);
    }

    public gamesFromInfo(queries: GameQuery[], callback: (res: any) => void, page: number = 0, limit: number = 20) {
        const query = queries.reduce((acc, q) => Object.assign(acc, q.query(), {}));
        this.search("games", { query, page, limit }, callback);
    }

    public game(id: number, callback: (res: any) => void) {
        const cb = (res: any) => {
            res.game = res.games.filter((game: any) => game.id === id)[0];
            callback(res);
        };
        this.search("games/" + id.toString(), {}, cb);
    }

    private search(endPointName: string, params: any, callback: (res: any) => void) {
        // axios.get(BASE_URL + endPointName, { params }).then(callback);
        callback(Object.assign({}, exampleResponce));
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
            subgenre: ["アドベンチャー"],
            title: "神様お願い！お兄ちゃんの赤ちゃん妊娠したいの！ 〜ツンデレ妹＆清純妹とエッチなキセキでトラブル子作り三昧♪〜",
            url: "http://www.getchu.com/soft.phtml?id=786920",
            price: 2160,
            release: "2013/11/29",
            image: "http://norn-soft.com/154/image/top.jpg",
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
            price: 2160,
            release: "2012/11/09",
            image: "https://img.dlsite.jp/modpub/images2/parts/RJ103000/RJ102416/RJ102416_PTS0000002648_0.jpg",
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
            price: 9504,
            release: "2014/09/20",
            image: "https://images-na.ssl-images-amazon.com/images/I/51aQS5DwMCL.jpg",
            writer: ["七歌", "8", "東人"],
        },
    ],
};
