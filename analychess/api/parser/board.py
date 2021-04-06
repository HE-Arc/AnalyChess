from enum import Enum 
import pieces

BOARD_SIZE = 8
ROOK_MOVEMENT_TYPES = [pieces.PieceType.ROOK, pieces.PieceType.QUEEN]
BISHOP_MOVEMENT_TYPES = [pieces.PieceType.BISHOP, pieces.PieceType.QUEEN]
KNIGHT_MOVEMENT_TYPES = [pieces.PieceType.KNIGHT]
KING_MOVEMENT_TYPES = [pieces.PieceType.KING, pieces.PieceType.QUEEN]

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
    
    def applyMove(self, move):
        for movement in move:
            (startFile, startRow, endFile, endRow, endPiece) = movement

            if(startFile == None or startRow == None):
                self.board[endRow.value][endFile.value] = endPiece
            else:
                if(endPiece == None):
                    self.board[endRow.value][endFile.value] = self.board[startRow.value][startFile.value]
                else:
                    self.board[endRow.value][endFile.value] = endPiece
                self.board[startRow.value][startFile.value] = None

    def switchColor(self):
        if(self.currentPlayingColor == pieces.PieceColor.WHITE):
            self.currentPlayingColor = pieces.PieceColor.BLACK
        else:
            self.currentPlayingColor = pieces.PieceColor.WHITE

    def __getPieceMove(self, pieceType, color, constraints, endFile, endRow):
        bestmove = None
        bestDistance = 10000
        for rowIndex in range(len(self.board)):
            for fileIndex in range(len(self.board[rowIndex])):
                currentPiece = self.board[rowIndex][fileIndex]

                # Piece cannot move to the same cell
                if(currentPiece == None or currentPiece.pieceType != pieceType):
                    continue

                currentPieceColor = currentPiece.color
                currentPieceType = currentPiece.pieceType

                # Not the same sell
                if endFile.value == fileIndex and endRow.value == rowIndex:
                    continue

                if(not(
                    # Check rook movements
                    currentPieceType in ROOK_MOVEMENT_TYPES and (endFile.value == fileIndex or endRow.value == rowIndex) or 
                    
                    # Check bishop movements
                    currentPieceType in BISHOP_MOVEMENT_TYPES and (abs(endFile.value - fileIndex) == abs(endRow.value - rowIndex)) or 
                    
                    # Check knight movements
                    currentPieceType in KNIGHT_MOVEMENT_TYPES and (( \
                        (abs(endFile.value - fileIndex) == 2 and abs(endRow.value - rowIndex) == 1) or 
                        (abs(endFile.value - fileIndex) == 1 and abs(endRow.value - rowIndex) == 2)) 
                    ) or 
                    
                    # Check king movements
                    currentPieceType in KING_MOVEMENT_TYPES and (abs(endFile.value - fileIndex) <= 1 and abs(endRow.value - rowIndex) <= 1)
                )):
                    continue

                # If piece follow constraints
                constraintValid = True
                for constraint in constraints:
                    if not constraint.checkConstraint(fileIndex, rowIndex):
                        constraintValid = False
                if(not constraintValid):
                    continue

                if(currentPieceColor == color):
                    manDistance = abs(endFile.value - fileIndex) + abs(endRow.value - rowIndex)
                    if(manDistance < bestDistance):
                        bestDistance = manDistance
                        bestmove = (File(fileIndex), Row(rowIndex), endFile, endRow, None)
        return [bestmove]
    
    def __getCastleMove(self, color, queenSide = False):
        row = Row.ROW_1
        if(color == pieces.PieceColor.BLACK):
            row = Row.ROW_8

        if(queenSide):
            return [(File.FILE_E, row, File.FILE_C, row, None) ,(File.FILE_A, row, File.FILE_D, row, None)]
        else:
            return [(File.FILE_E, row, File.FILE_G, row, None) ,(File.FILE_H, row, File.FILE_F, row, None)]
    
    def __getPawnMove(self, color, endFile, endRow, promotes=None):
        canMove2Forward = False
        if((color == pieces.PieceColor.WHITE and endRow == Row.ROW_4) or (color == pieces.PieceColor.BLACK and endRow == Row.ROW_5)):
            canMove2Forward = True
        
        cellOneBackwardsRowIndex = 0
        cellTwoBackwardsRowIndex = 0
        if(color == pieces.PieceColor.WHITE):
            cellOneBackwardsRowIndex = endRow.value - 1
            cellTwoBackwardsRowIndex = endRow.value - 2
        elif(color == pieces.PieceColor.BLACK):
            cellOneBackwardsRowIndex = endRow.value + 1
            cellTwoBackwardsRowIndex = endRow.value + 2
        
        cellOneBackwards = self.board[cellOneBackwardsRowIndex][endFile.value]
        cellTwoBackwards = self.board[cellTwoBackwardsRowIndex][endFile.value]

        if(cellOneBackwards != None):
            if(cellOneBackwards.pieceType == pieces.PieceType.PAWN and cellOneBackwards.color == color):
                return [(endFile, Row(cellOneBackwardsRowIndex), endFile, endRow, promotes)]
        else:
            if(cellTwoBackwards != None and cellTwoBackwards.pieceType == pieces.PieceType.PAWN and cellTwoBackwards.color == color):
                return [(endFile, Row(cellTwoBackwardsRowIndex), endFile, endRow, promotes)]

        raise Exception("Cannot find a valid pawn move")
    
    def __getPawnTakesMove(self, color, startFile, endFile, endRow, promotes = None):
        movements = []
        startRow = Row(endRow.value - 1)
        if(color == pieces.PieceColor.BLACK):
            startRow = Row(endRow.value + 1)
        movements.append((startFile, startRow, endFile, endRow, promotes))

        # Takes en passant
        if(self.board[endRow.value][endFile.value] == None):
            movements.append((None, None, endFile, startRow, None))
        
        return movements


    def getMove(self, parsedMove):
        if(parsedMove.isPieceMove()):
            endFile, endRow = parsedMove.getEndPos()
            return self.__getPieceMove(parsedMove.getPiece(), self.currentPlayingColor, parsedMove.getConstraints(), endFile, endRow)
        elif(parsedMove.isCastleKingSideMove()):
            return self.__getCastleMove(self.currentPlayingColor)
        elif(parsedMove.isCastleQueenSideMove()):
            return self.__getCastleMove(self.currentPlayingColor, queenSide=True)
        elif(parsedMove.isPawnTakesMove()):
            promotedPiece = None
            if(parsedMove.isPromoteMove()):
                promotedPiece = pieces.ChessPiece(self.currentPlayingColor, parsedMove.getPromotedPiece())
            endFile, endRow = parsedMove.getEndPos()
            return self.__getPawnTakesMove(self.currentPlayingColor, parsedMove.getPawnTakesStartRow(), endFile, endRow, promotes=promotedPiece)
        elif(parsedMove.isPawnMove()):
            promotedPiece = None
            if(parsedMove.isPromoteMove()):
                promotedPiece = pieces.ChessPiece(self.currentPlayingColor, parsedMove.getPromotedPiece())
            endFile, endRow = parsedMove.getEndPos()
            return self.__getPawnMove(self.currentPlayingColor, endFile, endRow, promotes=promotedPiece)
        raise Exception("Not a valid move") 

