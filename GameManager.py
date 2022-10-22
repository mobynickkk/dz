from StateMachine import GameStateMachine
from StepProcessor import StepService


class GameManager:
    state_machine = GameStateMachine()
    step_service = StepService()

    def start(self):
        while not self.state_machine.is_state_final():
            step: Step = None
            is_winning_state = self.step_service.process_step(step)
            self.state_machine.change_state(is_winning_state)

        print()