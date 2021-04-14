<template>
    <section>
        <h1>Account</h1>
        <h2>Test purpose only</h2>
        <router-link to="/">Account</router-link>
        <router-link to="/Game">Game</router-link>
        <router-link to="/Login">Login</router-link>
        <router-link to="/Test">Test</router-link>
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
import APIRequester from '@/tools/APIRequester.js'


export default {
    name:"Account",
    components:{
    GameThumbnail,
},
  data(){
      return{
          game : null,
          requester : APIRequester.getInstance(),
      }
  },
};
</script> 
