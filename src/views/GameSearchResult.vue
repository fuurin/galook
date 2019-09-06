<template>
    <div>
        Game ID is {{ id }}
    </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

@Component
export default class GameSearchResult extends Vue {
    public id: number = 0;

    public created() {
        this.id = parseInt(this.$route.params.id);
    }
}
</script>

<style scoped>

</style>
