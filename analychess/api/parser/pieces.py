from enum import Enum

class PieceColor(Enum):
    WHITE = 0
    BLACK = 1

class PieceType(Enum):
    PAWN = 0
    KNIGHT = 1
    BISHOP = 2
    ROOK = 3
    QUEEN = 4
    KING = 5

class ChessPiece:
    def __init__(self, color, pieceType):
        self.color = color
        self.pieceType = pieceType
    
    def __repr__(self):
        let = 'P'
        if(self.pieceType == PieceType.KNIGHT):
            let = 'N'
        elif(self.pieceType == PieceType.BISHOP):
            let = 'B'
        elif(self.pieceType == PieceType.ROOK):
            let = 'R'
        elif(self.pieceType == PieceType.QUEEN):
            let = 'Q'
        elif(self.pieceType == PieceType.KING):
            let = 'K'

        return let
