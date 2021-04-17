<template>
    <div class="card" style="width: 18rem">
        <p>Modal</p>
        <input type="text" v-model="pgn" />
        <button v-on:click="ok">OK</button>
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
        async ok() {
            let game = await ApiRequester.getInstance()
                .setParam({ pgn: this.pgn })
                .setRoute("upload_pgn")
                .post();
            this.$router.push({ name: "Game", params: { game: game } });
        },
    },
};
</script>
