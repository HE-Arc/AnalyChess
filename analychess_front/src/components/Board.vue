<template>
<div class="board">
    <div class="board-row" v-for="row_index in BOARD_SIZE" :key="row_index">
        <div class="board-cell" v-for="file_index in BOARD_SIZE" :key="file_index"></div>
    </div>
    <ChessPiece :piece="'r'" :file="0" :row="0" :size="100"/>
    <ChessPiece :piece="'n'" :file="1" :row="0" :size="100"/>
    <ChessPiece :piece="'b'" :file="2" :row="0" :size="100"/>
    <ChessPiece :piece="'q'" :file="3" :row="0" :size="100"/>
    <ChessPiece :piece="'k'" :file="4" :row="0" :size="100"/>
    <ChessPiece :piece="'b'" :file="5" :row="0" :size="100"/>
    <ChessPiece :piece="'n'" :file="6" :row="0" :size="100"/>
    <ChessPiece :piece="'r'" :file="7" :row="0" :size="100"/>

    <ChessPiece :piece="'p'" :file="0" :row="1" :size="100"/>
    <ChessPiece :piece="'p'" :file="1" :row="1" :size="100"/>
    <ChessPiece :piece="'p'" :file="2" :row="1" :size="100"/>
    <ChessPiece :piece="'p'" :file="3" :row="1" :size="100"/>
    <ChessPiece :piece="'p'" :file="4" :row="1" :size="100"/>
    <ChessPiece :piece="'p'" :file="5" :row="1" :size="100"/>
    <ChessPiece :piece="'p'" :file="6" :row="1" :size="100"/>
    <ChessPiece :piece="'p'" :file="7" :row="1" :size="100"/>

    <ChessPiece :piece="'P'" :file="0" :row="6" :size="100"/>
    <ChessPiece :piece="'P'" :file="1" :row="6" :size="100"/>
    <ChessPiece :piece="'P'" :file="2" :row="6" :size="100"/>
    <ChessPiece :piece="'P'" :file="3" :row="6" :size="100"/>
    <ChessPiece :piece="'P'" :file="4" :row="6" :size="100"/>
    <ChessPiece :piece="'P'" :file="5" :row="6" :size="100"/>
    <ChessPiece :piece="'P'" :file="6" :row="6" :size="100"/>
    <ChessPiece :piece="'P'" :file="7" :row="6" :size="100"/>

    <ChessPiece :piece="'R'" :file="0" :row="7" :size="100"/>
    <ChessPiece :piece="'N'" :file="1" :row="7" :size="100"/>
    <ChessPiece :piece="'B'" :file="2" :row="7" :size="100"/>
    <ChessPiece :piece="'Q'" :file="3" :row="7" :size="100"/>
    <ChessPiece :piece="'K'" :file="4" :row="7" :size="100"/>
    <ChessPiece :piece="'B'" :file="5" :row="7" :size="100"/>
    <ChessPiece :piece="'N'" :file="6" :row="7" :size="100"/>
    <ChessPiece :piece="'R'" :file="7" :row="7" :size="100"/>
</div>
</template>

<script>

import ChessPiece from "./ChessPiece.vue";

export default {
    name: 'Board',
    components: {
        ChessPiece
    },
    data() {
        return {
            BOARD_SIZE: 8,
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
    padding: 0;
    display: flex;
    position: relative;
    flex-direction: column;
}

.board > .board-row
{
    display: flex;
}

.board > .board-row > .board-cell
{
    width: 100px;
    height: 100px;
    background: white;
}

.board > .board-row:nth-of-type(2n + 1) > .board-cell:nth-of-type(2n),
.board > .board-row:nth-of-type(2n) > .board-cell:nth-of-type(2n + 1)
{
    background: brown;
}

</style>

