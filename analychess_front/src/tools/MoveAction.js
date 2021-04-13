export default class MoveAction
{
    constructor(movements, pieces)
    {
        this.movements = movements;
        this.pieces = pieces;
        this.removedPieces = [];
        this.movedPieces = [];
        this.changedPieces = [];
    }

    getCell(row, file) {
        let foundPieces = this.pieces.filter(p => p.row == row && p.file == file && !p.hidden);
        return foundPieces.length === 1 ? foundPieces[0] : null;
    }

    apply()
    {
        this.removedPieces = [];
        this.movedPieces = [];
        this.changedPieces = [];
        for(const {mPiece, sRow, sFile, eRow, eFile} of this.movements)
        {
            const startPosPiece = sRow !== null && sFile !== null ? this.getCell(sRow, sFile) : null;
            const endPosPiece = this.getCell(eRow, eFile);

            if(mPiece && startPosPiece)
            {
                this.changedPieces.push({
                    piece: startPosPiece,
                    prevPieceType: startPosPiece.piece
                });
                startPosPiece.piece = mPiece;
            }
            if(endPosPiece)
            {
                endPosPiece.hidden = true;
                this.removedPieces.push(endPosPiece);
            }

            if(startPosPiece)
            {
                this.movedPieces.push({ sRow, sFile, eRow, eFile, piece: startPosPiece });
                startPosPiece.row = eRow;
                startPosPiece.file = eFile;
            }
        }
    }

    undo()
    {
        for(const piece of this.movedPieces)
        {
            const pieceToUndo = this.getCell(piece.eRow, piece.eFile);
            pieceToUndo.row = piece.sRow;
            pieceToUndo.file = piece.sFile;
        }

        for(const piece of this.changedPieces)
        {
            piece.piece.piece = piece.prevPieceType;
        }

        for(const piece of this.removedPieces)
        {
            piece.hidden = false;
        }
    }
}
