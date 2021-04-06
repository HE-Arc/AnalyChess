<template>
<div class="card" style="width: 18rem;">
  <img src="../assets/chesspiece.svg" class="card-img-top" alt="chess">
  <div class="card-body">
    <h5 class="card-title">Game 1</h5>
    <p class="card-text">info sur la partie</p>
    <a class="btn btn-primary">viewGame</a>
  </div>
</div>
</template>

<script>

export default {
  name: 'GameThumnail',
    methods:{
        viewGame()
        {
            this.$router.push({name: "gameViewer"});
        }
    }
}
</script>
