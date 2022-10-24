from Step import Step

from itertools import permutations


class StepService:

    def __init__(self):
        self.history = []

    def process_step(self, step: Step) -> bool:
        self.accept_step(step)

        same_x = list(map(lambda el: el.y,
                          sorted(filter(lambda prev_step: prev_step.x == step.x, self.history),
                                 key=lambda el: el.y)))
        same_y = list(map(lambda el: el.x,
                          sorted(filter(lambda prev_step: prev_step.y == step.y, self.history),
                                 key=lambda el: el.x)))

        return StepService.is_winning_situation(same_x) or StepService.is_winning_situation(same_y) \
               or StepService.check_slash_like_win(self.history)

    def accept_step(self, step: Step):
        if any([step.x == el.x and step.y == el.y for el in self.history]):
            raise Exception("Step is already done")

        self.history.append(step)

    @staticmethod
    def is_winning_situation(steps) -> bool:
        if len(steps) < 3:
            return False

        first = steps[0]
        second = steps[1]

        for i in range(2, len(steps)):
            if abs(first - second) == 1 and abs(second - steps[i]) == 1:
                return True

            first = second
            second = steps[i]

        return False

    @staticmethod
    def check_slash_like_win(steps) -> bool:
        """ Наивная реализация проверки косых победных расстановок за O(n^3) """
        if len(steps) < 3:
            return False

        for i in range(len(steps)):
            for j in range(i + 1, len(steps)):
                for k in range(j + 1, len(steps)):
                    if any([StepService.check_slash_like(*p) for p in permutations([steps[i], steps[j], steps[k]])]):
                        return True
        return False

    @staticmethod
    def check_slash_like(s1, s2, s3):
        return (s1.x - 1 == s2.x and s2.x - 1 == s3.x) \
               and ((s1.y - 1 == s2.y and s2.y - 1 == s3.y)  # ascending s1->s3
                    or (s3.y - 1 == s2.y and s2.y - 1 == s1.y))  # descending s1->s3
