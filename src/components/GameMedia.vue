<template>
    <div class="panel card ">
        <div class="card-content">
            <article class="media">
                <figure class="media-left">
                    <p class="image">
                        <img :src="game.image">
                    </p>
                </figure>
                <div class="media-content">
                    <div class="content">
                        <strong>
                            <a :href="game.url"
                                class="has-text-primary is-large"
                            >
                                {{ game.title }}
                            </a>
                        </strong>
                        <br>
                        {{ game.story }}
                    </div>
                </div>
            </article>
        </div>
    </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
import Game from '@/types/Game';

@Component
export default class GameMedia extends Vue {
    @Prop()
    private game!: Game;
}
</script>

<style scoped>
img {
    width: 120px;
}
</style>
