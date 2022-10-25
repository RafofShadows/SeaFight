from user import *
from ai import *


class Engine:

    def __init__(self):
        self.board_size = 6
        self.ship_sizes = [3, 2, 2, 1, 1, 1, 1]
        self.user_board = self.random_board(False)
        self.ai_board = self.random_board(True)
        self.user = User(self.user_board, self.ai_board)
        self.ai = AI(self.ai_board, self.user_board)

    def random_board(self, is_hidden):
        result = Board(self.board_size, is_hidden)
        for ship_size in self.ship_sizes:
            count = 0
            while True:
                try:
                    result.add_ship(Engine.random_ship(result.size, ship_size))
                    break
                except(OutOfBoundsError, IntersectionError):
                    count += 1
                    if count > 10000:
                        return self.random_board(is_hidden)
                    continue
                except Exception as e:
                    raise e
        return result

    @staticmethod
    def greetings():
        text = """Игра Морской бой
        Правила игры: игрок играет протик компьютерного соперника. Обе стороны играют на случайно сгенерированной доске.
        Игрок видит свою доску, но на доске соперника видно только те клетки, в которые игрок уже стрелял.
        Ходят по очереди совершая выстрелы. Если произошло попадание, игрок ходит еще раз.
        Ввод осуществляется с клавиатуры. Игрок должен указать координаты цели через пробел, например '1 1'
        Чтобы выйти во время игры, введите 'exit' в конце хода"""
        print(text)
        input("Для продолжения нажмите Enter...")

    def draw(self):
        dist = "                "
        outstr = f"Ваша доска:{dist}    Доска компьютера:\n"
        player_lines = str(self.user_board).split("\n")
        ai_lines = str(self.ai_board).split("\n")

        for i, line in enumerate(player_lines):
            outstr += line + dist + ai_lines[i] + "\n"
        print(outstr)

    def loop(self):
        while True:
            user_turn = True
            while user_turn:
                self.draw()
                user_turn = self.user.turn()
                if self.win():
                    return
            ai_turn = True
            while ai_turn:
                print("Ход ИИ:")
                self.draw()
                ai_turn = self.ai.turn()
                if self.win():
                    return
                instr = input("Для продолжения нажмите Enter")
                if "exit" in instr:
                    return

    def win(self):
        if self.ai_board.ships_left() < 1:
            print("Победил Игрок!")
            return True
        elif self.user_board.ships_left() < 1:
            print("Победил Компьютер!")
            return True
        else:
            return False


    @staticmethod
    def random_ship(board_size, ship_size):
        r_dot = Dot(random.randint(0, board_size-1), random.randint(0, board_size-1))
        direction = random.randint(0, 1)
        return Ship(r_dot, ShipDirection(direction), ship_size)
