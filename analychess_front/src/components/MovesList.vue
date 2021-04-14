<template>
<div class="container">
    <div v-for="move in moves" :key="move.moveIndex">
        <span>{{move.moveIndex + 1}}. </span>
        <span
            :class="{btn: true, 'btn-primary': move.whiteMove.highlight}"
            @click="emitMoveChange(move.whiteMove.semiMoveIndex)"
        >{{move.whiteMove.move}} </span>
        <span
            v-if="move.blackMove"
            :class="{btn: true, 'btn-primary': move.blackMove.highlight}"
            @click="emitMoveChange(move.blackMove.semiMoveIndex)"
        >{{move.blackMove.move}} </span>
    </div>
</div>
</template>

<script>

export default {
    name: 'MovesList',
    props: {
        selectedMoveIndex: {
            type: Number,
            required: true
        },
        pgnMoves: {
            type: Array,
            require: true
        }
    },
    computed: {
        moves() {
            const moves = [];
            let currentMove = null;
            for(let pgnMoveIndex = 0; pgnMoveIndex < this.pgnMoves.length; ++pgnMoveIndex)
            {
                const semiMoveIndex = pgnMoveIndex + 1;
                const move = {
                    semiMoveIndex,
                    move: this.pgnMoves[pgnMoveIndex],
                    highlight: this.selectedMoveIndex == semiMoveIndex
                }
                if(pgnMoveIndex % 2 == 0)
                {
                    currentMove = {
                        moveIndex: pgnMoveIndex / 2,
                        whiteMove: move
                    }
                }
                else
                {
                    currentMove.blackMove = move;
                    moves.push(currentMove);
                    currentMove = null;
                }
            }

            if(currentMove) moves.push(currentMove);
            return moves;
        }
    },
    methods: {
        emitMoveChange(semiMoveIndex) {
            this.$emit("move", semiMoveIndex);
        }
    }
}
</script>

