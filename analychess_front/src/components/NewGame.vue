<template>

    <div class="card m-2" style="width: 18rem">
                        <label for="pgn">PGN of the game</label>
                        <textarea id="pgn" v-model="pgn" rows="15"></textarea>
                        <div class="card-body">

        <button class="btn btn-primary mt-4 btn-lg" v-on:click="newGame">New analysis</button>
    </div>
    </div>
</template>

<script>
import ApiRequester from "../tools/APIRequester";

export default {
    name: "NewGame",
    data() {
        return {
            pgn: "",
        };
    },
    methods: {
        async newGame() {
        let game = await ApiRequester.getInstance()
                .setParam({ pgn: this.pgn })
                .setRoute("upload_pgn")
                .post();
        if(game.moves.length == 0)
        {
            this.$toasted.error("Invalid pgn !", {
            duration: 3500,
        });
        }
        else
        {

            this.$router.push({ name: "Game", params: { game: game } });
        }
        },
    },
};
</script>
