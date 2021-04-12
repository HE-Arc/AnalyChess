import sys
import re
from .pieces import *
from .constraints import *
from .board import *

PGN_REG = r'((?:(?:(?:([a-h])x|(?:([KQRNB])([a-h]?[1-8]?)(x?))))?([a-h][1-8])|(O-O)|(O-O-O))(?:=([QRNB]))?(?:(\+)|(#))?)'

class ParsedMove(object):
    def __init__(self, regMatch):
        self.regMatch = regMatch 

    @staticmethod
    def __strToFile(strFile):
        if(strFile == "a"):
            return File.FILE_A
        elif(strFile == "b"):
            return File.FILE_B
        elif(strFile == "c"):
            return File.FILE_C
        elif(strFile == "d"):
            return File.FILE_D
        elif(strFile == "e"):
            return File.FILE_E
        elif(strFile == "f"):
            return File.FILE_F
        elif(strFile == "g"):
            return File.FILE_G
        elif(strFile == "h"):
            return File.FILE_H
        return None

    @staticmethod
    def __strToRow(strRow):
        if(strRow == "1"):
            return Row.ROW_1
        elif(strRow == "2"):
            return Row.ROW_2
        elif(strRow == "3"):
            return Row.ROW_3
        elif(strRow == "4"):
            return Row.ROW_4
        elif(strRow == "5"):
            return Row.ROW_5
        elif(strRow == "6"):
            return Row.ROW_6
        elif(strRow == "7"):
            return Row.ROW_7
        elif(strRow == "8"):
            return Row.ROW_8
        return None

    @staticmethod
    def __strToPiece(strPiece):
        if(strPiece == 'N'):
            return PieceType.KNIGHT
        elif(strPiece == 'B'):
            return PieceType.BISHOP
        elif(strPiece == 'R'):
            return PieceType.ROOK
        elif(strPiece == 'Q'):
            return PieceType.QUEEN
        elif(strPiece == 'K'):
            return PieceType.KING
        return None

    @staticmethod
    def __strToCoord(strCoord):
        return ParsedMove.__strToFile(strCoord[0]), ParsedMove.__strToRow(strCoord[1])

    def isPawnTakesMove(self):
        return bool(self.regMatch[1])
    
    def getPawnTakesStartRow(self):
        return ParsedMove.__strToFile(self.regMatch[1])
    
    def isPawnMove(self):
        return not self.isPieceMove() and not self.isCastleKingSideMove()\
               and not self.isCastleQueenSideMove() and not self.isPawnTakesMove()

    def isPieceMove(self):
        return bool(self.regMatch[2])
    
    def getConstraints(self):
        constraints = []
        fileConstraitReg = re.search('([a-h])', self.regMatch[3])
        if(fileConstraitReg):
            constraints.append(FileConstraint(ParsedMove.__strToFile(fileConstraitReg[0])))
        rowConstraitReg = re.search('([1-8])', self.regMatch[3])
        if(rowConstraitReg):
            constraints.append(RowConstraint(ParsedMove.__strToRow(rowConstraitReg[0])))
        return constraints

    def getPiece(self):
        return ParsedMove.__strToPiece(self.regMatch[2])
    
    def isTakes(self):
        return bool(self.regMatch[1]) or bool(self.regMatch[4])

    def isCastleKingSideMove(self):
        return bool(self.regMatch[6])

    def isCastleQueenSideMove(self):
        return bool(self.regMatch[7])

    def isPromoteMove(self):
        return bool(self.regMatch[8])
    
    def getPromotedPiece(self):
        return ParsedMove.__strToPiece(self.regMatch[8])

    def isCheck(self):
        return bool(self.regMatch[9])

    def isMate(self):
        return bool(self.regMatch[10])
    
    def getEndPos(self):
        return ParsedMove.__strToCoord(self.regMatch[5])

class Move(object):
    def __init__(self, pgnMove, movements):
        self.pgnMove = pgnMove
        self._movements = []
        for movement in movements:
            self._movements.append({
                "sFile": movement[0],
                "sRow": movement[1],
                "eFile": movement[2],
                "eRow": movement[3],
                "mPiece": str(movement[4]).lower(),
            })
    
    def __repr__(self):
        return self.pgnMove
    
def parse(pgnStr):
    matches = re.findall(PGN_REG, pgnStr)

    moves = []

    b = Board()
    for match in matches:
        parsedMove = ParsedMove(match)
        movements = b.getMove(parsedMove)
        moves.append(Move(match[0], movements))
        b.applyMove(movements)
        b.switchColor() 

    return moves

if(__name__ == '__main__'):
    with open(sys.argv[1], "r") as file:
        moves = parse(file.read())
        print(moves)
