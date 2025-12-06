from enum import Enum 

############################################################
class BoardSqaure(object):
    def __init__(self,row:int, col:int):
        self.row:int = row
        self.col:int = col
        
        self.peice:ChessPeice = None

    def setPeice(self,peice:ChessPeice):
        self.peice = peice

    def __str__(self):
        if (self.peice is not None):
            return f"{self.peice.team.value}-{self.peice}"
        else:
            return f"{"EMPTY SQUARE":^{30}}" #spacing

############################################################
class ChessPeice(object):
    class Team(Enum):
        WHITE = "WHITE"
        BLACK = "BLACK"
        UNASSIGNED = "UNASSIGNED"
    #-----------------------------
    def __init__(self,row:int, col:int, team:ChessPeice.Team=Team.UNASSIGNED):
        self.row:int = row
        self.col:int = col
        
        self.team:ChessPeice.Team = team

        self.moveset:function = None 

    def __str__(self):
        return f"{self.__class__.__name__}({self.row},{self.col})"
    
    def getValidMoveset(self) -> list[tuple[int,int]]:
        return self.moveset(self.row,self.col)
#-----------------------------
class Pawn(ChessPeice):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.moveset:function = None

    def getValidMoveset(self):
        return super().getValidMoveset()
#-----------------------------
class Knight(ChessPeice):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.moveset:function = None

    def getValidMoveset(self):
        return super().getValidMoveset()
#-----------------------------
class Bishop(ChessPeice):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.moveset:function = None

    def getValidMoveset(self):
        return super().getValidMoveset()
#-----------------------------
class Rook(ChessPeice):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.moveset:function = None

    def getValidMoveset(self):
        return super().getValidMoveset()
#-----------------------------
class Queen(ChessPeice):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.moveset:function = None

    def getValidMoveset(self):
        return super().getValidMoveset()
#-----------------------------
class King(ChessPeice):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.moveset:function = None

    def getValidMoveset(self):
        return super().getValidMoveset()
############################################################
class Board(object):
    board_size:int = 8
    #-----------------------------
    def __init__(self):
        self.places = [ [BoardSqaure(i,j) for j in range(Board.board_size)] for i in range(Board.board_size)]

        self.place_peices_on_board()

    def __getitem__(self, idx:int) -> ChessPeice: #make this indexing better, could also do row col indexing
        return self.places[idx]

    def __str__(self):
        ret:str = f""

        for row in board:
            for peice in row:
                ret += f"|{str(peice):^{30}}"
            ret += f"\n"

        return ret

    def place_peices_on_board(self,):
        for row in self.places[0:2] + self.places[-2:]:
            for square in row:
                square.setPeice(ChessPeice(square.row,square.col))

############################################################

if __name__ == "__main__":
    board = Board()
    print(board)

    print(f"board[0][0] = {board[0][0]}")