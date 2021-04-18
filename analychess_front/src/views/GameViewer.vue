<template>
    <section class="m-5">
        <h1>GameViewer</h1>
        <Board
            :selectedMoveIndex="1"
            v-bind:game="this.game"
            :gameId="this.gameId"
        />
    </section>
</template>

<script>
import Board from "../components/Board.vue";

export default {
    name: "GameViewer",
    components: {
        Board,
    },
    props: {
        game: null,
        gameId: null,
    },
};
</script> 
