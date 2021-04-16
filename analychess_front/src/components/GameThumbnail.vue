<template>
<div class="card" style="width: 18rem;">
  <img src="../assets/chesspiece.svg" class="card-img-top" alt="chess">
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
        this.$router.push({name: "Game", params: {game_id: this.game.id, game: this.game}})
      }
  }
}
</script>
