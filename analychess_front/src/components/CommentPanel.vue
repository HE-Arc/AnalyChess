<template>
<div>
  <textarea class= "comment-text" rows="15" type="text" v-model="comment" v-on:change="write"/>
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
    width: 400px;
}

</style>