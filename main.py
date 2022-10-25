from engine import *


def main():
    game = Engine()
    Engine.greetings()
    game.loop()
    input("Для выхода нажмите Enter")


if __name__ == '__main__':
    main()

