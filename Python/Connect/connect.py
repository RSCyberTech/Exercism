class ConnectGame:
    def __init__(self, board):
        self.board = board.splitlines()
        self.board = [s.split() for s in self.board]

    def get_winner(self):

        # takes care of single characters
        if len(self.board) == 1:
            return self.board[0][0]

        # check which spaces at the top and are filled to start checking
        toCheck = []
        for r in range(len(self.board[0])):
            if self.board[0][r] == "O":
                toCheck.append([(0, r)])
        for r in range(len(self.board)):
            if self.board[r][0] == "X":
                toCheck.append([(r, 0)])

        while len(toCheck) > 0:
            toWork = toCheck.pop(-1)
            coordinates = (toWork[-1][0], toWork[-1][1])
            coordinatesToCheck = [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0)]
            for c in coordinatesToCheck:
                newCoordinates = (coordinates[0] + c[0], coordinates[1] + c[1])
                try:
                    if self.board[coordinates[0]][coordinates[1]] == self.board[
                        newCoordinates[0]
                    ][newCoordinates[1]] and (
                        newCoordinates[0] >= 0 and newCoordinates[1] >= 0
                    ):
                        if (
                            toWork[0][0] == 0
                            and newCoordinates[0] == len(self.board) - 1
                        ) or (
                            toWork[0][1] == 0
                            and newCoordinates[1] == len(self.board[0]) - 1
                        ):
                            return self.board[toWork[0][0]][toWork[0][1]]
                        if newCoordinates not in toWork:
                            toAdd = toWork[:]
                            toAdd.append(newCoordinates)
                            toCheck.append(toAdd)
                except:
                    pass
        return ""
