<template>
    <section>
        <h1>GameViewer</h1>
        <h2>Test purpose only</h2>
        <router-link to="/">Home</router-link>
        <router-link to="/game">Game</router-link>
        <router-link to="/test">Test</router-link>
        <router-link to="/logout">Logout</router-link>
        <Board :selectedMoveIndex="1" v-bind:game="this.game" :gameId="this.gameId"/>
    </section>
</template>

<script>

import Board from '../components/Board.vue';

export default {
    name:"GameViewer",
    components:{
    Board,
    },
  props: {
    game: null,
    gameId: null
  },
}

</script> 