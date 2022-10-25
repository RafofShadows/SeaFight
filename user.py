from player import *


class User(Player):
    def ask(self):
        while True:
            in_str = input("Укажите цель:\n").strip()
            in_list = in_str.split()
            is_correct = len(in_list) == 2 and \
                     all(list(map(lambda s: (s.isdigit() and 0 <= int(s) < self.opponent_board.size), in_list)))
            if not is_correct:
                print("Неверный формат ввода. Попробуйте еще раз")
                continue
            else:
                x = int(in_list[0])
                y = int(in_list[1])
                return Dot(x, y)