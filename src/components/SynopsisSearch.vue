<template>
    <div class="synopsis-search-area">
        <div class="field">
            <div class="control">
                <textarea class="textarea" placeholder="あらすじが似たゲームを検索" v-model="synopsis">
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
import { Component, Prop, Vue} from 'vue-property-decorator';

@Component
export default class SynopsisSearch extends Vue {
    private synopsis: string = "";

    private empty(): boolean {
        return this.synopsis === "";
    }
}
</script>

<style scoped>

</style>
