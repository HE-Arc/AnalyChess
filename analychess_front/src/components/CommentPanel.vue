<template>
<div>
  <input type="text" v-model="comment"/>
</div>
</template>

<script>
export default {
  name: 'CommentPanel',
      props: {

        selectedMoveIndex: {
            type: Number,
            required: true
        },
        game: null,
    },
  data(){
    return{
      comment : this.game.moves[this.selectedMoveIndex].comment 
    };
  },
  methods: {
    write(){
      this.game.moves[this.selectedMoveIndex].comment = this.comment
    }
  },

}
</script>
