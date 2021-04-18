<template>
    <div>
        <textarea
            class="comment-text form-control"
            rows="15"
            type="text"
            v-model="comment"
            v-on:change="write"
        />
    </div>
</template>

<script>
export default {
    name: "CommentPanel",
    monted()
    {
        this.read(0);
    },
    props: {
        game: null,
    },
    data() {
        return {
            comment: "",
            index: 0,
        }
    },
    methods: {
        write() {
            this.game.moves[this.index].comment = this.comment;
        },
        read(index) {
            this.index = index;
            this.comment = this.game.moves[this.index].comment;
        },
    },
};
</script>
<style>
.comment-text {
    width: 300px;
}
</style>
