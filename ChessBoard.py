import enum

############################################################
class ChessPeice(object):
    class Team(enum):
        WHITE = "WHITE"
        BLACK = "BLACK"

    def __init__(self,row:int,col:int):
        self.row:int = row
        self.col:int = col
        
        self.color:ChessPeice.Team = None

        self.moveset:function = None 

    def __str__(self):
        return f"{self.__class__.__name__}({self.row},{self.col})"
    
    def getValidMoveset(self) -> list[list[bool]]: #can be boolean map, can be an arr of indexes # ->list[tuple[int,int]], what ever is needed
        return self.moveset(self.row,self.col)
#-----------------------------
class Pawn(ChessPeice):
    def __init__(self, row, col):
        super().__init__(row, col)

        self.moveset:function = None

    def getValidMoveset(self) -> list[any]: #annotation is currently temporary
        return super().getValidMoveset()
#-----------------------------
class Knight(ChessPeice):
    def __init__(self, row, col):
        super().__init__(row, col)

        self.moveset:function = None

    def getValidMoveset(self) -> list[any]: #annotation is currently temporary
        return super().getValidMoveset()
#-----------------------------
class Bishop(ChessPeice):
    def __init__(self, row, col):
        super().__init__(row, col)

        self.moveset:function = None

    def getValidMoveset(self) -> list[any]: #annotation is currently temporary
        return super().getValidMoveset()
#-----------------------------
class Rook(ChessPeice):
    def __init__(self, row, col):
        super().__init__(row, col)

        self.moveset:function = None

    def getValidMoveset(self) -> list[any]: #annotation is currently temporary
        return super().getValidMoveset()
#-----------------------------
class Queen(ChessPeice):
    def __init__(self, row, col):
        super().__init__(row, col)

        self.moveset:function = None

    def getValidMoveset(self) -> list[any]: #annotation is currently temporary
        return super().getValidMoveset()
#-----------------------------
class King(ChessPeice):
    def __init__(self, row, col):
        super().__init__(row, col)

        self.moveset:function = None

    def getValidMoveset(self) -> list[any]: #annotation is currently temporary
        return super().getValidMoveset()
############################################################
class Board(object):
    board_size:int = 8
    def __init__(self):
        self.places = [ [(i,j) for j in range(Board.board_size)] for i in range(Board.board_size)]

        self.place_peices_on_board()

    def __getitem__(self, idx:int) -> ChessPeice: #make this indexing better, could also do row col indexing
        return self.places[idx]

    def __str__(self):
        ret:str = f""

        for row in board:
            for peice in row:
                ret += f" {peice} "
            ret += '\n'

        return ret

    def place_peices_on_board(self,):
        for row in self.places:
            for i , j in row:
                self.places[i][j] = ChessPeice(i,j) #make this a proper function in implementation

############################################################

if __name__ == "__main__":
    board = Board()
    print(board)

    print(f"board[0][0] = {board[0][0]}")