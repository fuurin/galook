<template>
    <div>
        Synopsis is {{ synopsis }}
    </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

@Component
export default class SynopsisSearchResult extends Vue {
    private synopsis: string = "";

    private created() {
        this.synopsis = this.$route.params.synopsis;
    }
}
</script>

<style scoped>

</style>
