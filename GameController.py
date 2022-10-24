from Step import Step


class GameController:

    @staticmethod
    def get_step() -> Step:
        print("Координаты вводятся от 1 до 10")
        x = GameController.get_coordinate("Введите координаты для выставления фишки по горизонтали: ")
        y = GameController.get_coordinate("Введите координаты для выставления фишки по вертикали: ")

        return Step(x, y)

    @staticmethod
    def get_coordinate(text: str) -> int:
        coord = input(text)

        while not coord.isdigit() or int(coord) > 10 or int(coord) < 1:
            coord = input("Введите корректную координату! ")

        return int(coord) - 1

    @staticmethod
    def draw_field(history):
        filled_fields = [(step.x, step.y) for step in history]

        for y in range(10):
            for x in range(10):
                print(" F " if (x, y) in filled_fields else " . ", end="")
            print()

    @staticmethod
    def proclaim_victory(is_first_player_win: bool):
        if is_first_player_win:
            print("Игра окончена. Победил первый игрок!")
        else:
            print("Игра окончена. Победил второй игрок!")
