class Constraint:
    def __init__(self):
        super().__init__()
    def checkConstraint(self, fileIndex, rowIndex):
        return True

class RowConstraint(Constraint):
    def __init__(self, boardRow):
        super().__init__()
        self.boardRow = boardRow

    def checkConstraint(self, fileIndex, rowIndex):
        return self.boardRow.value == rowIndex

class FileConstraint(Constraint):
    def __init__(self, boardFile):
        super().__init__()
        self.boardFile = boardFile

    def checkConstraint(self, fileIndex, rowIndex):
        return self.boardFile.value == fileIndex
