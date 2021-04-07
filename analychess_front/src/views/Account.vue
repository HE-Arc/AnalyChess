<template>
    <div id="root">
        <Header />
            <div id="app">
                <h1>Account</h1>
                <button v-on:click="test">Test</button>
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
import APIRequester from '@/tools/APIRequester.js'

export default {
components:{

    Header,
    GameThumbnail,
},
  name: "Account",
  data(){
      return{
          requester : APIRequester.getInstance(),
      }
  },
  methods: {
      test() {
          this.requester = APIRequester.getInstance()
          this.requester.setRoute("login");
          this.requester.setParam({"username": "test", "password": "test"});
          this.requester.post();
      }
  }
    

};
</script>