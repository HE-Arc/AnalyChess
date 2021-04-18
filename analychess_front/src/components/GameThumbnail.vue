<template>
    <div class="card m-2" style="width: 18rem">
        <img src="../assets/chesspiece.svg" class="card-img-top" alt="chess" />
        <div class="card-body">
            <h5 class="card-title">{{ game.title }}</h5>
            <p class="card-text">{{ game.description }}</p>
            <button class="btn btn-primary mb-0" v-on:click="viewGame">
                Show analysis
            </button>
        </div>
    </div>
</template>

<script>
export default {
    name: "GameThumnail",
    props: {
        game: null,
    },
    methods: {
        viewGame() {
            this.$router.push({
                name: "Game",
                params: { gameId: this.game.id, game: this.game },
            });
        },
    },
};
</script>
