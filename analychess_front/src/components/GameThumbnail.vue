<template>
<div class="card m-2 " style="width: 18rem;">
  <img src="../assets/chesspiece.svg" class="card-img-top mx-auto " alt="chess" style="width: 200px;">
  <div class="card-body">
    <h5 class="card-title">{{game.title}}</h5>
    <p class="card-text">{{game.description}}</p>
    <a class="btn btn-primary" v-on:click="viewGame">Show analysis</a>
  </div>
</div>
</template>

<script>

export default {
  name: 'GameThumnail',
  props: {
    game: null
  },
  methods:{
      viewGame()
      {
        this.$router.push({name: "Game", params: {game: this.game}})
      }
  }
}
</script>
