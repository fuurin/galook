<template>
    <div class="main">
        <a v-if="!isShown" class="button show" @click="open">
            <i class="fas fa-plus"></i>&nbsp;詳細検索
        </a>
        <a v-else class="button close" @click="close">
            <i class="fas fa-minus"></i>&nbsp;閉じる
        </a>

        <transition>
            <div v-if="isShown" class="card details">
                <div class="card-header">
                    <p class="card-header-title">詳細検索</p>
                </div>
                <div class="card-content">
                    <div v-for="detail in details" :key="detail.name" class="detail">
                        <label class="label has-text-left">{{ detail.label }}</label>
                        <div class="columns is-desktop">
                            <div class="column is-6">
                                <input v-model="detail.input" class="input" type="search" :placeholder="detail.label">
                            </div>
                            <div class="column is-6">
                                <div class="buttons has-addons is-centered">
                                    <span @click="detail.match=match.perfect"
                                        class="button"
                                        :class="{'is-primary is-selected': detail.match === match.perfect}">
                                        完全一致
                                    </span>
                                    <span @click="detail.match=match.part"
                                        class="button"
                                        :class="{'is-success is-selected': detail.match === match.part}">
                                        部分一致
                                    </span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <router-link class="button is-primary search" 
                        :disabled="!searchable()"
                        :to="{name: 'detail', query: query()}">
                        <i class="fas fa-search"></i>検索
                    </router-link>
                </div>
            </div>
        </transition>
    </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
import GameQuery from '@/types/GameQuery';
import GameDetail from '@/types/GameDetail';
import Device from '@/utils/Device';

@Component
export default class DetailSearch extends Vue {
    private isShown: boolean = false;
    private d: Device = new Device();
    private match = GameQuery.match;
    private details: GameDetail[] = [
        new GameDetail("ブランド", new GameQuery("brand", "")),
        new GameDetail("カテゴリー", new GameQuery("category", "")),
        new GameDetail("ジャンル", new GameQuery("genre", "")),
        new GameDetail("ライター", new GameQuery("writer", "")),
    ];

    private open() {
        this.isShown = true;
        if (this.$route.name !== 'home') return;
        setTimeout(() => {
            window.scrollTo({top: 470, behavior: "smooth"});
        }, 100);
    }

    private close() {
        this.isShown = false;
        if (this.$route.name !== 'home') return;
        setTimeout(() => {
            window.scrollTo({top: 0, behavior: "smooth"});
        }, 100);
    }

    private query(): { [s: string]: string } {
        const q: { [s: string]: string } = {};
        for (const detail of this.details) {
            if (detail.input === "") continue;
            q[detail.name] = detail.input;
            q[detail.query().qmatch] = detail.match;
        }
        return q;
    }

    private searchable(): boolean {
        return this.details.reduce((acc, val) => acc + val.input, "").length > 0;
    }
}
</script>

<style scoped>
    .main {
        margin: 15px auto 0 auto;
    }

    .v-enter-active, .v-leave-active {
        transition: all 0.5s
    }

    .v-enter {
        transform: translateY(-10px);
    }

    .v-enter, .v-leave-to {
        opacity: 0
    }

    .details {
        margin-top: 25px;
    }

    .detail {
        margin-top: 25px;
    }

    .card-content {
        padding-top: 0;
    }

    .column {
        padding-bottom: 0;
    }

    .search {
        margin-top: 35px;
    }
</style>
