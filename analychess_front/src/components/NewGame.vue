<template>

    <div class="card m-2" style="width: 18rem">
                            <img
                        src="../assets/chesspiece.svg"
                        class="card-img-top"
                        alt="chess"
                    />
                    <div class="card-body">

        <button class="btn btn-primary mt-4 btn-lg" v-on:click="ok">New analysis</button>
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
