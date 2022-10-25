from board import *

class Player:
    def __init__(self, my_board, other_board):
        self.board = my_board
        self.opponent_board = other_board

    def ask(self):
        pass

    def turn(self):
        while True:
            try:
                target = self.ask()
                res = self.opponent_board.shot(target)
                if res == ShotResult.miss:
                    print(f"{target}: Промах!")
                    return False
                elif res == ShotResult.wound:
                    print(f"{target}: Ранил!")
                    return True
                else:
                    print(f"{target}: Убил!")
                    return True
            except (OutOfBoundsError, IntersectionError):
                continue
            except Exception as e:
                raise e

