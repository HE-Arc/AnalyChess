<template>
<div class="board">
    <div class="row" v-for="row_index in BOARD_SIZE" :key="row_index">
        <div class="cell" v-for="file_index in BOARD_SIZE" :key="file_index"></div>
    </div>
</div>
</template>

<script>

export default {
    name: 'Board',
    data() {
        return {
            BOARD_SIZE: 8
        }
    },
    props: {
        selectedMoveIndex: {
            type: Number,
            required: true
        }
    }
}
</script>

<style>

.board
{
    display: flex;
    flex-direction: column;
}

.board > .row
{
    display: flex;
}

.board > .row > .cell
{
    width: 100px;
    height: 100px;
    background: white;
}

.board > .row:nth-of-type(2n) > .cell:nth-of-type(2n),
.board > .row:nth-of-type(2n + 1) > .cell:nth-of-type(2n + 1)
{
    background: brown;
}

</style>

