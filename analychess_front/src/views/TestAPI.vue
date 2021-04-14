<template>
    <section>
        <h1>Login</h1>
        <h2>Test purpose only</h2>
        <router-link to="/">Account</router-link>
        <router-link to="/Game">Game</router-link>
        <router-link to="/Login">Login</router-link>
        <router-link to="/Test">Test</router-link>
        <div>
            <button v-on:click="login">Login</button>
            <button v-on:click="get">GET</button>
            <button v-on:click="post">POST</button>
            <button v-on:click="put">PUT</button>
            <button v-on:click="del">DELETE</button>
            <button v-on:click="up">UP</button>
            <button v-on:click="create_game">POST GAME</button>
            <button v-on:click="get_game">GET GAME</button>
            <button v-on:click="put_game">PUT GAME</button>
            <button v-on:click="del_game">DEL GAME</button>
        </div>
    </section>
</template>



<script>

import APIRequester from '@/tools/APIRequester.js'

export default {
    name:"TestAPI",
  data(){
      return{
          game : null,
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
    },
    async up() {
        let data = await this.requester.setParam({"pgn": "1. d4 d5 2. c4 dxc4 3. e4 Nc6 4. Be3 Nf6 5. Nc3 e5 6. d5 Ne7 7. Bxc4 Ng6 8. f3 Bd6 9. Qd2 Bd7 10. Nge2 a6 11. Bb3 b5 12. a4 O-O 13. O-O Qe7 14. Rac1 Nh5 15. g3 h6 16. Bc2 Rab8 17. axb5 axb5 18. Ra1 Ra8 19. Bd3 Bb4 20. Rxa8 Rxa8 21. Qc2 Bc5 22. Nd1 Bd6 23. Nf2 Nhf4 24. Rc1 Qg5 25. Kh1 Qh5 26. Ng1 Nxd3 27. Nxd3 f5 28. Nc5 Bc8 29. Rf1 Ne7 30. Qd3 fxe4 31. fxe4 Qg6 32. Kg2 Kh7 33. Nf3 Ng8 34. Nh4 Qg4 35. Nf5 Nf6 36. h3 Qg6 37. Ne6 Ra4 38. b3 Rxe4 39. Nxd6 Bxe6 40. dxe6 cxd6 41. e7 d5 42. Bc5 Qe8 43. Qf3 Qc6 44. b4 Qe8 45. Qf5+ Kh8 46. Qxf6 gxf6 47. Rxf6 Qh5 48. Rf8+ Kg7 49. e8=Q Re2+ 50. Kf1 Qxh3+ 51. Kxe2 Qg2+ 52. Rf2 Qe4+ 53. Kd2"}).setRoute("upload_pgn").post();
        console.log(data)
        this.game = data.moves
    },
    async create_game() {
        let data = await this.requester.setParam({"title" : "title1", "result": "result1", "description": "desc1", "moves": this.game}).setRoute("game").post();
        console.log(data)
        this.game = data
    },
    async get_game() {
        let data = await this.requester.setRoute("game").get();
        console.log(data)
        this.game = data
    },
    async put_game() {
        let data = await this.requester.setParam({"title" : "title2", "result": "result1", "description": "desc1", "moves": this.game}).setRoute("game/26").put();
        console.log(data)
        this.game = data
    },
    async del_game() {
        let data = await this.requester.setRoute("game/24").delete();
        console.log(data)
        this.game = data
    }
  }
};
</script> 
