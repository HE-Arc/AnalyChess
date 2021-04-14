<template>
    <section>
        <h1>GameViewer</h1>
        <h2>Test purpose only</h2>
        <router-link to="/">Account</router-link>
        <router-link to="/game">Game</router-link>
        <router-link to="/test">Test</router-link>
        <router-link to="/logout">Logout</router-link>
        <Board :selectedMoveIndex="1"/>
    </section>
</template>

<script>

import Board from '../components/Board.vue';

export default {
    name:"GameViewer",
    components:{
    Board,
},
}

</script> 