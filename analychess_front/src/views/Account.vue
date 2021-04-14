<template>
    <section>
        <h1>Account</h1>
        <h2>Test purpose only</h2>
        <router-link to="/">Account</router-link>
        <router-link to="/game">Game</router-link>
        <router-link to="/test">Test</router-link>
        <router-link to="/logout">Logout</router-link>
        <div class="container">
            <div class="row row-cols-4">
                <game-thumbnail/>
                <game-thumbnail/> 
                <game-thumbnail/>
                <game-thumbnail/>
                <game-thumbnail/> 
                <game-thumbnail/> 
                <game-thumbnail/>
                <game-thumbnail/>
            </div>
        </div>
    </section>
</template>
<script>

import GameThumbnail from '../components/GameThumbnail.vue';


export default {
    name:"Account",
    components:{
        GameThumbnail,
    }
};
</script> 
