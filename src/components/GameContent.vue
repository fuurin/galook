<template>
    <div class="panel card">
        <div class="card-content">
            <div class="columns">
                <div class="column is-2">
                    <a :href="game.url">
                        <img class="is-hidden-touch" :src="game.image">
                        <img class="is-hidden-desktop" :src="game.image">
                    </a>
                </div>
                <div class="column is-10">
                    <div class="has-text-left">
                        <div>
                            <a :href="game.url"
                                class="has-text-primary title is-4"
                            >
                                {{ game.title }}
                            </a>
                        </div>
                        <nav class="breadcrumb">
                            <ul>
                                <li class="is-active"><a>ブランド： {{ game.brand }}</a></li>
                                <li class="is-active"><a>カテゴリー： {{ category() }}</a></li>
                                <li class="is-active"><a>ライター： {{ writer() }}</a></li>
                            </ul>
                        </nav>
                        <div class="container story" :class="{'hidden-story': !isOpened}" @click="toggleOpened">
                            <label v-show="!isOpened">
                                <i class="fas fa-chevron-down"></i>
                            </label>
                            <p>{{ game.story }}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
import Game from '@/types/Game';

@Component
export default class GameContent extends Vue {
    @Prop()
    private game!: Game;

    private isOpened: boolean = false;

    private category(): string {
        return this.game.category.join(', ');
    }

    private subgenre(): string {
        return this.game.subgenre.join(', ');
    }

    private writer(): string {
        return this.game.writer.join(", ");
    }

    private toggleOpened() {
        this.isOpened = !this.isOpened;
    }
}
</script>

<style scoped>
img {
    margin: 0 auto;
}

.is-hidden-touch {
    width: 120px;
}

.is-hidden-desktop {
    width: 300px;
}

.breadcrumb {
    margin: 10px 0;
}

.story {
    min-height: 100px;
    margin: 0;
}

.hidden-story {
    max-height: 100px;
    overflow: hidden;
}

.hidden-story label {
	position: absolute;
    bottom: 0;
	width: 100%;
	height: 100px; /* グラデーションの高さ */
    padding-top: 75px;
    text-align: center;
    vertical-align: text-bottom;
    cursor: pointer;
	background: linear-gradient(to bottom, rgba(255, 255, 255, 0) 60%, rgba(255, 255, 255, 0.95) 100%); /* グラデーション */
}
</style>
