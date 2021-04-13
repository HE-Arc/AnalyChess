<template>
<div class="board">
    <div class="board-row" v-for="rowIndex in BOARD_SIZE" :key="rowIndex">
        <div class="board-cell" v-for="fileIndex in BOARD_SIZE" :key="fileIndex"></div>
    </div>

    <ChessPiece
        v-for="piece in pieces"
        :size="100"
        :key="piece.key"
        :piece="piece.piece"
        :row="piece.row"
        :file="piece.file"
    />
</div>
</template>

<script>

import ChessPiece from "./ChessPiece.vue";

const WHITE = 0;
const BLACK = 1;
const ROW_1 = 0;
const ROW_2 = 1;
const ROW_7 = 6;
const ROW_8 = 7;
const FILE_A = 0;
const FILE_B = 1;
const FILE_C = 2;
const FILE_D = 3;
const FILE_E = 4;
const FILE_F = 5;
const FILE_G = 6;
const FILE_H = 7;

export default {
    name: 'Board',
    components: {
        ChessPiece
    },
    data() {
        return {
            BOARD_SIZE: 8,
            pieces: []
        };
    },
    mounted() {
        this.resetBoard();
    },
    methods: {
        getCell(row, file) {
            let foundPieces = this.pieces.filter(p => p.row == row && p.file == file);
            return foundPieces.length === 1 ? foundPieces[0] : null;
        },
        resetBoard() {
            // Initial board state
            this.pieces = [];
            let pieceKey = 0;
            for(let rowIndex = 0; rowIndex < this.BOARD_SIZE; ++rowIndex)
            {
                for(let fileIndex = 0; fileIndex < this.BOARD_SIZE; ++fileIndex)
                {
                    let color = rowIndex < this.BOARD_SIZE / 2 ? WHITE : BLACK;

                    let piece = null;
                    if(rowIndex == ROW_2 || rowIndex == ROW_7)
                    {
                        piece = color ? "p" : "P";
                    }
                    else if(rowIndex == ROW_1 || rowIndex == ROW_8)
                    {
                        switch(fileIndex)
                        {
                            case FILE_A:
                            case FILE_H: piece = color ? "r" : "R"; break;
                            case FILE_B:
                            case FILE_G: piece = color ? "n" : "N"; break;
                            case FILE_C:
                            case FILE_F: piece = color ? "b" : "B"; break;
                            case FILE_D: piece = color ? "q" : "Q"; break;
                            case FILE_E: piece = color ? "k" : "K"; break;
                        }
                    }

                    if(piece)
                    {
                        this.pieces.push({
                            piece,
                            pieceKey: `pieceKey_${pieceKey++}`,
                            row: rowIndex,
                            file: fileIndex
                        });
                    }
                }
            }
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

