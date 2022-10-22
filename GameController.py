from Step import Step


class GameController:

    @staticmethod
    def get_step():
        x = int(input("Введите координаты для выставления фишки по горизонтали: "))
        y = int(input("Введите координаты для выставления фишки по вертикали: "))

        return Step(x, y)

    @staticmethod
    def draw_field(history):
        pass