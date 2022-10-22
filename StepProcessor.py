from Step import Step


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

        return StepService.is_winning_situation(same_x) or StepService.is_winning_situation(same_y)

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
