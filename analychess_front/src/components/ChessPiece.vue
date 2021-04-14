<template>
<div :class="{chesspiece: true, hidden}" :style="style">
    <img src="../assets/black_king.png" alt="black king" v-if="piece === 'k'">
    <img src="../assets/black_queen.png" alt="black queen" v-if="piece === 'q'">
    <img src="../assets/black_rook.png" alt="black rook" v-if="piece === 'r'">
    <img src="../assets/black_bishop.png" alt="black bishop" v-if="piece === 'b'">
    <img src="../assets/black_knight.png" alt="black knight" v-if="piece === 'n'">
    <img src="../assets/black_pawn.png" alt="black pawn" v-if="piece === 'p'">
    <img src="../assets/white_king.png" alt="black king" v-if="piece === 'K'">
    <img src="../assets/white_queen.png" alt="black queen" v-if="piece === 'Q'">
    <img src="../assets/white_rook.png" alt="black rook" v-if="piece === 'R'">
    <img src="../assets/white_bishop.png" alt="black bishop" v-if="piece === 'B'">
    <img src="../assets/white_knight.png" alt="black knight" v-if="piece === 'N'">
    <img src="../assets/white_pawn.png" alt="black pawn" v-if="piece === 'P'">
</div>
</template>

<script>

export default {
    name: 'ChessPiece',
    props: {
        hidden: {
            type: Boolean,
            required: true
        },
        piece: {
            type: String,
            require: true
        },
        size: {
            type: Number,
            required: true
        },
        file: {
            type: Number,
            required: true
        },
        row: {
            type: Number,
            required: true
        }
    },
    computed: {
        style() {
            return `bottom: ${this.size * this.row}px;left: ${this.size * this.file}px;width:${this.size}px;height:${this.size}px`;
        }
    }
}
</script>

<style>

.chesspiece
{
    position: absolute;
    transition: bottom 250ms linear, left 250ms linear, opacity 250ms linear;
}

.chesspiece.hidden
{
    opacity: 0;
}

.chesspiece img
{
    width: 100%;
    height: 100%;
}

</style>

