<template>
    <div class="panel card">
        <div class="card-content" @click="closeDetail">
            <div class="columns">
                <div class="column is-3">
                    <a :href="game.url">
                        <img :class="d.respCls('image')" :src="game.image">
                    </a>
                    <div class="has-text-right">
                        <small class="is-size-7 has-text-grey">Image from Google</small>
                    </div>
                </div>
                <div class="column is-9">
                    <div class="has-text-left">
                        <div>
                            <a :href="game.url"
                                class="title has-text-primary is-size-4-desktop is-size-5-touch">
                                {{ game.title }}
                            </a>
                        </div>

                        <div class="dropdown" 
                            :class="{'is-hoverable': !d.isMobile(), 'is-active': detailIsOpened}">
                            <div class="dropdown-trigger" @click.stop="toggleDetailOpened">
                                <button class="button is-small">
                                    <span>詳細</span>
                                    <span class="icon is-small">
                                        <i class="fas fa-angle-down"></i>
                                    </span>
                                </button>
                            </div>
                            <div class="dropdown-menu" 
                                :class="{'dropdown-menu-desktop': !d.isMobile()}">
                                <div class="dropdown-content">
                                    <p class="dropdown-item">ブランド： {{ game.brand }}</p>
                                    <p class="dropdown-item">カテゴリー： {{ category() }}</p>
                                    <p class="dropdown-item">ジャンル： {{ subgenre() }}</p>
                                    <p class="dropdown-item">ライター： {{ writer() }}</p>
                                    <hr v-if="!isSearched()" class="dropdown-divider">
                                    <div v-if="!isSearched()" class="dropdown-item">
                                        <router-link 
                                            :to="{name: 'game', params: {id: game.id}}"
                                            class="has-text-primary">
                                            類似のゲーム
                                        </router-link>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="container story" :class="{'hidden-story': !storyIsOpened}" @click="toggleStoryOpened">
                            <label v-show="!storyIsOpened">
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
import Device from '@/utils/Device';

@Component
export default class GameContent extends Vue {
    @Prop()
    private game!: Game;
    private detailIsOpened: boolean = false;
    private storyIsOpened: boolean = false;
    private d: Device = new Device();

    private isSearched(): boolean {
        if (this.$route.name !== "game") return false;
        return this.game.id.toString() === this.$route.params.id.toString();
    }

    private category(): string {
        return this.game.category.join(', ');
    }

    private subgenre(): string {
        return this.game.subgenre.join(', ');
    }

    private writer(): string {
        return this.game.writer.join(", ");
    }

    private closeDetail() {
        if (this.detailIsOpened) this.toggleDetailOpened();
    }

    private toggleDetailOpened() {
        this.detailIsOpened = this.d.isMobile() && !this.detailIsOpened;
    }

    private toggleStoryOpened() {
        this.storyIsOpened = !this.storyIsOpened;
    }
}
</script>

<style scoped>
img {
    margin: 0 auto;
}

.image-desktop {
    width: 300px;
}

.image-mobile {
    width: 170px;
}

.dropdown {
    margin: 12px 0;
}

.dropdown-menu-desktop {
    width: 400px;
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
