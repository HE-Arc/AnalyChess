<template>
    <section>
        <h1>GameViewer</h1>
        <h2>Test purpose only</h2>
        <router-link to="/">Account</router-link>
        <router-link to="/Game">Game</router-link>
        <router-link to="/Login">Login</router-link>
        <router-link to="/Test">Test</router-link>
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