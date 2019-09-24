<template>
    <div class="synopsis-search-area">
        <div class="field">
            <div class="control">
                <textarea class="textarea" v-model="synopsis" 
                    minlength="1" :maxlength="maxTextSize"
                    placeholder="あらすじが似たゲームを検索"
                >
                </textarea>
            </div>
        </div>
        <router-link 
            class="button is-primary is-medium is-outlined is-rounded"
            :to="{name: 'synopsis', params: {synopsis: synopsis || 'no text'}}"
            :disabled="empty()" 
            :style="{pointerEvents: empty() ? 'none' : 'all'}"
        >
            あらすじ検索
        </router-link>
    </div>
</template>

<script lang="ts">
import { Component, Prop, Vue, Watch } from 'vue-property-decorator';

const MAX_TEXT_SIZE = 100;

@Component
export default class SynopsisSearch extends Vue {
    private synopsis: string = "";
    private maxTextSize: number = MAX_TEXT_SIZE;

    @Watch("$route")
    private takeSynopsis(to: any, from: any) {
        if (to.name !== "synopsis") return;
        this.synopsis = to.params.synopsis;
    }

    private empty(): boolean {
        return this.synopsis === "";
    }
}
</script>

<style scoped>

</style>
