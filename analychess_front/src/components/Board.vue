<template>
  <div class="m-2 p-5">
    <div class="row d-flex justify-content-center">
      <div class="col-md-auto">
        <label for="inputTitle">Title</label>
        <input type="text" class="form-control" id="inputTitle"  v-model="title"/>
        <label for="inputDescription">Description</label>
        <textarea class="form-control mb-2" id="inputDescription" v-model="description"/>
        <label for="comment">Comment</label>
        <CommentPanel
          ref="commentPanel"
          :index="currentMoveIndex"
          v-bind:game="this.game"
        />
        <button type="button" class="btn btn-lg btn-secondary m-2" @click="save">Save</button>
        <button type="button" class="btn btn-lg btn-secondary m-2" @click="share">Share</button>
      </div>
      <div class="col-md-auto d-inline-flex justify-content-center">
        <div class="row">
          <div class="d-flex justify-content-center">
            <div class="board" style="width: 100%; min-width: 400px">
              <div
                class="board-row"
                v-for="rowIndex in BOARD_SIZE"
                :key="rowIndex"
              >
                <div
                  class="board-cell"
                  v-for="fileIndex in BOARD_SIZE"
                  :key="fileIndex"
                ></div>
              </div>

              <ChessPiece
                v-for="piece in pieces"
                :key="piece.key"
                :piece="piece.piece"
                :row="piece.row"
                :file="piece.file"
                :hidden="piece.hidden"
              />
            </div>
          </div>
          <div class="row justify-content-center p-2">
            <div class="d-flex justify-content-center">
              <button class="btn btn-secondary m-1" @click="firstMove">First</button>
              <button class="btn btn-secondary m-1" @click="prevMove">Prev</button>
              <button class="btn btn-secondary m-1" @click="nextMove">Next</button>
              <button class="btn btn-secondary m-1" @click="lastMove">Last</button>
            </div>
          </div>
        </div>
      </div>

      <div class="col-md-auto">
        <MovesList
          :pgnMoves="pgnMoves"
          :selectedMoveIndex="currentMoveIndex"
          @move="moveAtIndex"
        />
      </div>
    </div>
    <div class="row">
      <SymbolPanel />
    </div>
  </div>
</template>

<script>
import ChessPiece from "./ChessPiece.vue";
import MovesList from "./MovesList.vue";
import MoveAction from "../tools/MoveAction";
import CommentPanel from "./CommentPanel.vue";
import SymbolPanel from "./SymbolPanel.vue";
import ApiRequester from '../tools/APIRequester';

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
  name: "Board",
  components: {
    ChessPiece,
    MovesList,
    CommentPanel,
    SymbolPanel,
  },
  data() {
    return {
      BOARD_SIZE: 8,
      pieces: [],
      actions: [],
      currentMoveIndex: 0,
      title: "Title",
      description: "Description",
      id: null
    };
  },
  mounted() {
    this.resetBoard();
    this.id = this.gameId;
    this.title = this.game.title;
    this.description = this.game.description;
    console.log(this.game);
    for (let { move } of this.game.moves) {
      //console.log(move)
      this.actions.push(new MoveAction(move.movements, this.pieces));
    }
  },
  computed: {
    pgnMoves() {
      return this.game.moves.map((m) => {
        return m.move.pgnMove;
      });
    },
  },
  methods: {
    resetBoard() {
      // Initial board state
      this.pieces = [];
      let pieceKey = 0;
      for (let rowIndex = 0; rowIndex < this.BOARD_SIZE; ++rowIndex) {
        for (let fileIndex = 0; fileIndex < this.BOARD_SIZE; ++fileIndex) {
          let color = rowIndex < this.BOARD_SIZE / 2 ? WHITE : BLACK;

          let piece = null;
          if (rowIndex == ROW_2 || rowIndex == ROW_7) {
            piece = color ? "p" : "P";
          } else if (rowIndex == ROW_1 || rowIndex == ROW_8) {
            switch (fileIndex) {
              case FILE_A:
              case FILE_H:
                piece = color ? "r" : "R";
                break;
              case FILE_B:
              case FILE_G:
                piece = color ? "n" : "N";
                break;
              case FILE_C:
              case FILE_F:
                piece = color ? "b" : "B";
                break;
              case FILE_D:
                piece = color ? "q" : "Q";
                break;
              case FILE_E:
                piece = color ? "k" : "K";
                break;
            }
          }

          if (piece) {
            this.pieces.push({
              piece,
              pieceKey: `pieceKey_${pieceKey++}`,
              row: rowIndex,
              file: fileIndex,
              hidden: false,
            });
          }
        }
      }
    },
    moveAtIndex(index) {
      while (this.currentMoveIndex < index && this.hasNextMove()) {
        this.nextMove();
      }
      while (this.currentMoveIndex > index && this.hasPrevMove()) {
        this.prevMove();
      }
      this.$refs.commentPanel.read(index);
    },
    hasNextMove() {
      return this.currentMoveIndex < this.actions.length;
    },
    nextMove() {
      if (this.hasNextMove()) {
        this.actions[this.currentMoveIndex++].apply();
        this.$refs.commentPanel.read(this.currentMoveIndex);
      }
    },
    hasPrevMove() {
      return this.currentMoveIndex > 0;
    },
    prevMove() {
      if (this.hasPrevMove()) {
        this.actions[--this.currentMoveIndex].undo();
        this.$refs.commentPanel.read(this.currentMoveIndex);
      }
    },
    lastMove() {
      while (this.hasNextMove()) {
        this.nextMove();
      }
      this.$refs.commentPanel.read(this.currentMoveIndex);
    },
    firstMove() {
      while (this.hasPrevMove()) {
        this.prevMove();
      }
      this.$refs.commentPanel.read(this.currentMoveIndex);
    },
    async save(){
      try
      {
        this.game.title = this.title;
        this.game.description = this.description;
        if (this.id != null)
        {
          await ApiRequester.getInstance().setRoute(`game/${this.id}`).setParam(this.game).patch()
        }
        else
        {
          let data = await ApiRequester.getInstance().setRoute('game').setParam(this.game).post()
          this.id = data.id;

        }

        //TODO toast ok
        
      }
      catch(error)
      {
        console.log(error)
      }
    },
    share()
    {
      console.log("Sahre");
    }
  },
  props: {
    selectedMoveIndex: {
      type: Number,
      required: true,
    },
    game: null,
    gameId: null,
  },
};
</script>

<style>
.board {
  padding: 0;
  display: flex;
  position: relative;
  flex-direction: column;
}

.board > .board-row {
  display: flex;
}

.board > .board-row > .board-cell {
  width: calc(100% / 8);
  padding-top: calc(100% / 8);
  background: white;
}

.board > .board-row:nth-of-type(2n + 1) > .board-cell:nth-of-type(2n),
.board > .board-row:nth-of-type(2n) > .board-cell:nth-of-type(2n + 1) {
  background: Teal;
}
textarea {
  resize: none;
}
</style>

