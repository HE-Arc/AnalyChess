<template>
    <div id="root">
        <Header />
            <div id="app">
                <h1>Account</h1>
            </div>
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
    </div>
</template>
<script>

import Header from '../components/Header.vue';
import GameThumbnail from '../components/GameThumbnail.vue';

export default {
components:{

    Header,
    GameThumbnail,
},
  name: "Account",

};
</script>