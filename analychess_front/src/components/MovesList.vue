<template>
<div class="container">
    <div v-for="move in moves" :key="move.moveIndex">
        <span>{{move.moveIndex + 1}}. </span>
        <span @click="emitMoveChange(move.moveIndex)">{{move.whiteMove}} </span>
        <span @click="emitMoveChange(move.moveIndex, true)">{{move.blackMove}}</span>
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
            for(let semiMoveIndex = 0; semiMoveIndex < this.pgnMoves.length; ++semiMoveIndex)
            {
                if(semiMoveIndex % 2 == 0)
                {
                    currentMove = {
                        moveIndex: semiMoveIndex / 2,
                        whiteMove: this.pgnMoves[semiMoveIndex],
                        blackMove: ""
                    }
                }
                else
                {
                    currentMove.blackMove = this.pgnMoves[semiMoveIndex];
                }

                if(semiMoveIndex % 2 != 0)
                {
                    moves.push(currentMove);
                    currentMove = null;
                }
            }

            if(currentMove) moves.push(currentMove);
            return moves;
        }
    },
    methods: {
        emitMoveChange(moveIndex, black = false) {
            const semiMoveIndex = moveIndex * 2 + (black ? 1 : 0) + 1;
            this.$emit("move", semiMoveIndex);
        }
    }
}
</script>

