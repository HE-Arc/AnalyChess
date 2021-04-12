<template>
    <div id="root">
        <Header />
            <div id="app">
                <h1>Account</h1>
                <!-- TODO : remove this -->
                <h3>For test purpose</h3>
                <button v-on:click="login">Login</button>
                <button v-on:click="get">GET</button>
                <button v-on:click="post">POST</button>
                <button v-on:click="put">PUT</button>
                <button v-on:click="del">DELETE</button>
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
      // test methods
      async login(){
          await this.requester.login("admin", "admin");
      },    
    async get() {
        let data = await this.requester.setRoute("user").get();
        console.log(data)
    },
    async post() {
        let data = await this.requester.setRoute("user").setParam({"username": "lol", 'password': "lol", "email": "ed@gmail.com.com", "test": "lol", "games" : []}).post();
        console.log(data)
    },
    async put() {
        let data = await this.requester.setRoute("user/13").setParam({"username": "lol1asdasd2", "password": "test", "email": "test2@gmail.com", "games" : []}).put();
        console.log(data)
    },
    async del() {
        let data = await this.requester.setRoute("user/13").delete();
        console.log(data)
    }
  }
};
</script>