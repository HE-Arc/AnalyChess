<template>
    <section class="m-5">
        <h1>Home</h1>
        <div class="container">
            <div class="row row-cols-4">
                

                <new-game v-if="newGame" />
                <game-thumbnail
                    v-for="game in this.games"
                    v-bind:key="game.id"
                    v-bind:game="game"
                />
            </div>
        </div>
    </section>
    
</template>
<script>
import GameThumbnail from "../components/GameThumbnail.vue";
import NewGame from "../components/NewGame.vue";
import ApiRequester from "../tools/APIRequester";

export default {
    name: "Home",
    components: {
        GameThumbnail,
        NewGame,
    },
    data() {
        return {
            games: null,
            newGame: true,
        };
    },
    created: async function () {
        this.games = await ApiRequester.getInstance().setRoute("game").get();
    },

};
</script>