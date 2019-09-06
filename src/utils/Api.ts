import axios from 'axios';
import Game from '@/types/Game';

const BASE_URL = "http://3.115.42.95/";

export default class Api {
    public similarGamesGromSynopsis(text: string, callback: (res: any) => void, limit: number = 20) {
        this.access("similar_games", { text, limit }, callback);
    }

    public similarGamesFromId(id: number, callback: (res: any) => void, limit: number = 20) {
        this.access("similar_games", { id, limit }, callback);
    }

    public gamesFromInfo(game: Game, callback: (res: any) => void, limit: number = 20) {
        const params = {
            brand: game.brand,
            category: game.category,
            story: game.stroy,
            subgenre: game.subgenre,
            title: game.title,
            writer: game.writer,
            limit,
        };
        this.access("games", params, callback);
    }

    public game(id: number, callback: (res: any) => void) {
        this.access("games/" + id.toString(), {}, callback);
    }

    public gameTitleCandidates(text: string, callback: (res: any) => void, limit: number = 20) {
        this.access("games", { text, limit }, callback);
    }

    private access(endPointName: string, params: any, callback: (res: any) => void) {
        // axios.get(BASE_URL + endPointName, { params }).then(callback);
        callback(exampleResponce);
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
            image: "http://www.getchu.com/brandnew/786920/rc786920package.jpg",
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
            image: "http://www.getchu.com/brandnew/754181/c754181package.jpg",
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
            image: "http://www.getchu.com/brandnew/814447/c814447package.jpg",
            writer: ["七歌", "8", "東人"],
        },
    ],
};
