<template>
    <section>
        <h1>Home</h1>
        <h6>Test purpose only</h6>
        <router-link to="/">Home</router-link>
        <router-link to="/game">Game</router-link>
        <router-link to="/test">Test</router-link>
        <router-link to="/logout">Logout</router-link>
        <div class="container">
            <div class="row row-cols-4">
                <game-thumbnail v-for="game in this.games" v-bind:key="game.id" v-bind:game="game"/>
            </div>
        </div>
        <button class="btn btn-info" v-on:click="lol">New analysis</button>
        <new-game v-if="newGame"/>


    </section>
</template>
<script>

import GameThumbnail from '../components/GameThumbnail.vue';
import NewGame from '../components/NewGame.vue';
import ApiRequester from '../tools/APIRequester';

export default {
    name:"Home",
    components:{
        GameThumbnail,
        NewGame
    },
    data()
    {
        return{
            games: null,
            newGame: false
        }
    },
    created: async function () {
        this.games = await ApiRequester.getInstance().setRoute("game").get()
    },
    methods:{
        lol() {
            this.newGame = !this.newGame
        },
    }
};
</script>