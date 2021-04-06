from enum import Enum 
import pieces
BOARD_SIZE = 8
class File(Enum):
    FILE_A = 0
    FILE_B = 1
    FILE_C = 2
    FILE_D = 3
    FILE_E = 4
    FILE_F = 5
    FILE_G = 6
    FILE_H = 7

class Row(Enum):
    ROW_1 = 0
    ROW_2 = 1
    ROW_3 = 2
    ROW_4 = 3
    ROW_5 = 4
    ROW_6 = 5
    ROW_7 = 6
    ROW_8 = 7

class Board:
    def __init__(self):
        self.board = []
        self.currentPlayingColor = pieces.PieceColor.WHITE

        for rowIndex in range(BOARD_SIZE):
            # Select color for the row
            color = pieces.PieceColor.WHITE
            if rowIndex > BOARD_SIZE / 2:
                color = pieces.PieceColor.BLACK

            row = self.__createEmptyRow__()
            # Pieces row
            if rowIndex in [Row.ROW_1.value, Row.ROW_8.value]:
                row = self.__createPieceRow__(color)
            # Pawns row
            elif rowIndex in [Row.ROW_2.value, Row.ROW_7.value]:
                row = self.__createPawnRow__(color)
            
            self.board.append(row)
    
    def __createPieceRow__(self, color):
        return [
            pieces.ChessPiece(color, pieces.PieceType.ROOK),
            pieces.ChessPiece(color, pieces.PieceType.KNIGHT),
            pieces.ChessPiece(color, pieces.PieceType.BISHOP),
            pieces.ChessPiece(color, pieces.PieceType.QUEEN),
            pieces.ChessPiece(color, pieces.PieceType.KING),
            pieces.ChessPiece(color, pieces.PieceType.BISHOP),
            pieces.ChessPiece(color, pieces.PieceType.KNIGHT),
            pieces.ChessPiece(color, pieces.PieceType.ROOK)
        ]

    def __createPawnRow__(self, color):
        row = []
        for i in range(BOARD_SIZE):
            row.append(pieces.ChessPiece(color, pieces.PieceType.PAWN))
        return row

    def __createEmptyRow__(self):
        row = []
        for i in range(BOARD_SIZE):
            row.append(None)
        return row

    def switchColor(self):
        if(self.currentPlayingColor == pieces.PieceColor.WHITE):
            self.currentPlayingColor = pieces.PieceColor.BLACK
        else:
            self.currentPlayingColor = pieces.PieceColor.WHITE

