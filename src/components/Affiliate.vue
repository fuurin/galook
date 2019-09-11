<template>
    <div class="Itemlink_Type01" style="background-color:#FFFFFF;color:#000000;font-size:10px;height:236px;width:200px;">
        <div class="In" style="">
            <div class="ItemBox">
                <a :href="game.url" target="_blank">
                    <img :src="imgLink()" border="0">
                </a>
            </div>

            <span class="DefiName" style="font-weight: bold;line-height:140%">
                <a :href="game.url" target="_blank">
                    {{ game.title }}
                </a>
            </span>
            <br>
            
            <span class="DefiAuthor" style="line-height:140%">
                <span style="color:#000000;">
                    ({{ game.brand }})
                </span>
            </span>
            <br>
            
            <span class="DefiAuthor" style="line-height:140%">
                <span style="color:#000000;">
                    発売日：2011/05/25
                </span>
            </span>
            <br>

            <span class="DefiPrice" style="line-height:140%">
                価格：
                <span style="font-weight: bold;color:#CC0000;">
                    ￥6,701
                </span>
            </span>
            <br>
            
            <div style="clear:both;">
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
import Game from '@/types/Game';

@Component
export default class Affiliate extends Vue {
    @Prop()
    private game!: Game;

    private imgLink(): string {
        const id = this.game.id;
        const num = Math.floor(this.game.id / 1000);
        return `https://image.getchu.com/afimage/${num}000/${id}/afimg_${id}_100.jpg`;
    }
}
</script>

<style scoped>
    .Itemlink_Type01 {
        margin: 0 auto;
    }
</style>
