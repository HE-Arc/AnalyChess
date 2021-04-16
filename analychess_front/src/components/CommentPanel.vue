<template>
<div>
  <input class= "comment-text" type="text" v-model="comment" v-on:change="write"/>
</div>
</template>

<script>
export default {
  name: 'CommentPanel',
      props: {
        game: null,
    },
  data(){
    return{
      comment : "",
      index: 1
    }
  },
  methods: {
    write(){
      this.game.moves[this.index].comment = this.comment
    },
    read(_index)
    {
      this.index = _index;
      this.comment = this.game.moves[this.index].comment
    }
  },

}
</script>
<style>
.comment-text
{
    height: 200px;
    width: 400px;
}

</style>