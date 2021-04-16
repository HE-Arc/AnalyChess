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
                <button type="button" class="btn btn-lg btn-secondary m-2" @click="del">Delete</button>
			</div>
			<div class="col-md-auto d-inline-flex justify-content-center">
				<div class="row">
					<div class="d-flex justify-content-center">
						<div class="board">
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

                            <ArrowDrawingZone
                                @arrowStart="startArrow"
                                @arrowUpdate="updateArrow"
                                @arrowEnd="toggleArrow"
                            />

							<ChessPiece
								v-for="piece in pieces"
								:key="piece.key"
								:piece="piece.piece"
								:row="piece.row"
								:file="piece.file"
								:hidden="piece.hidden"
							/>

                            <Arrow
                                v-for="(arrow, index) in arrows"
                                :key="`arrow_${index}`"
                                :sFile="arrow.sFile"
                                :sRow="arrow.sRow"
                                :eFile="arrow.eFile"
                                :eRow="arrow.eRow"
                                :color="arrow.color"
                            />
                            <Arrow
                                v-if="currentArrow"
                                :sFile="currentArrow.sFile"
                                :sRow="currentArrow.sRow"
                                :eFile="currentArrow.eFile"
                                :eRow="currentArrow.eRow"
                                :color="currentArrow.color"
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
            <SymbolPanel 
                ref="symPanel"
                v-bind:game="this.game"/>
		</div>
	</div>
</template>

<script>
import ChessPiece from "./ChessPiece.vue";
import Arrow from "./Arrow.vue";
import ArrowDrawingZone from "./ArrowDrawingZone.vue";
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
        Arrow,
        ArrowDrawingZone
	},
	data() {
		return {
			BOARD_SIZE: 8,
			pieces: [],
            currentArrow: null,
            highlightedCells: [],
			actions: [],
			currentMoveIndex: 0,
			title: "Title",
			description: "Description",
			id: null
		};
	},
	props: {
		selectedMoveIndex: {
			type: Number,
			required: true,
		},
		game: null,
		gameId: null,
	},
	mounted() {
		this.resetBoard();
		this.id = this.gameId;
		this.title = this.game.title;
		this.description = this.game.description;
		for (let { move } of this.game.moves) {
			this.actions.push(new MoveAction(move.movements, this.pieces));
		}
	},
	computed: {
		pgnMoves() {
			return this.game.moves.map((m) => {
				return m.move.pgnMove;
			});
        },
        arrows() {
            return this.game.moves[this.currentMoveIndex].arrows;
        }
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
        startArrow(fileIndex, rowIndex) {
            this.currentArrow = {
                sFile: fileIndex,
                sRow: rowIndex,
                eFile: fileIndex,
                eRow: rowIndex,
                color: "red"
            }
        },
        updateArrow(fileIndex, rowIndex) {
            this.currentArrow.eFile = fileIndex;
            this.currentArrow.eRow = rowIndex;
        },
        toggleArrow() {
            const previousArrowsCount = this.arrows.length;

            const newArrows = this.arrows.filter(a => {
                return !(this.currentArrow.sFile == a.sFile && this.currentArrow.eFile == a.eFile &&
                         this.currentArrow.sRow == a.sRow && this.currentArrow.eRow == a.eRow);
            });

            if(previousArrowsCount == newArrows.length)
            {
                this.arrows.push(this.currentArrow);
            }
            else
            {
                this.game.moves[this.currentMoveIndex].arrows = newArrows;
            }
            this.currentArrow = null;
        },
		hasNextMove() {
			return this.currentMoveIndex < this.actions.length;
		},
		nextMove() {
			if (this.hasNextMove()) {
				this.actions[this.currentMoveIndex++].apply();
				this.$refs.commentPanel.read(this.currentMoveIndex);
                this.$refs.symPanel.read(this.currentMoveIndex);
			}
		},
		hasPrevMove() {
			return this.currentMoveIndex > 0;
		},
		prevMove() {
			if (this.hasPrevMove()) {
				this.actions[--this.currentMoveIndex].undo();
				this.$refs.commentPanel.read(this.currentMoveIndex);
                this.$refs.symPanel.read(this.currentMoveIndex);
			}
		},
		lastMove() {
			while (this.hasNextMove()) {
				this.nextMove();
			}
			this.$refs.commentPanel.read(this.currentMoveIndex);
            this.$refs.symPanel.read(this.currentMoveIndex);
		},
		firstMove() {
			while (this.hasPrevMove()) {
				this.prevMove();
			}
			this.$refs.commentPanel.read(this.currentMoveIndex);
            this.$refs.symPanel.read(this.currentMoveIndex);
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
        async share()
        {
            if(this.id != null)
            {
                try{
                    let data = await ApiRequester.getInstance().setRoute("share").setParam({"id": this.id}).post();
                    console.log(data)
                    navigator.clipboard.writeText(`https://analychess.srvz-webapp.he-arc.ch/#/join/${data.token}`)
                    //TODO toast copied
                }
                catch(e)
                {
                    console.log(e)
                }
            }
            else
            {
                //TODO toat error
                console.log("not id")
            }
        },
        async del()
        {
            if(this.id != null)
            {
                try
                {
                    await ApiRequester.getInstance().setRoute(`game/${this.id}`).delete();
                    this.$router.push({name:'Home'})
                }
                catch(e)
                {
                    console.log(e)
                }
            }
            else
            {
                //TODO toat error
                console.log("not id")
            }
        }
	},
};

</script>

<style>
.board {
	padding: 0;
	display: flex;
	position: relative;
	flex-direction: column;
    width: 100%;
    min-width: 400px;
}

.board > .board-row {
	display: flex;
}

.board > .board-row > .board-cell {
	width: calc(100% / 8);
	padding-top: calc(100% / 8);
	background: white;
	position: relative;
}
.board > .board-row > .board-cell::after
{
	content: "";
	position: absolute;
	background: transparent;
	top: 0;  
	bottom: 0;  
	left: 0;  
	right: 0;  
}
.board > .board-row > .board-cell.blue::after
{
    background: blue;
}

.board > .board-row:nth-of-type(2n + 1) > .board-cell:nth-of-type(2n),
.board > .board-row:nth-of-type(2n) > .board-cell:nth-of-type(2n + 1) {
	background: Teal;
}
textarea {
	resize: none;
}
</style>

