from GameController import GameController
from StateMachine import GameStateMachine
from StepService import StepService


class GameManager:
    state_machine = GameStateMachine()
    step_service = StepService()

    def start(self):
        while not self.state_machine.is_state_final():
            GameController.draw_field(self.step_service.history)
            step = GameController.get_step()
            is_winning_state = self.step_service.process_step(step)
            self.state_machine.change_state(is_winning_state)
        else:
            GameController.draw_field(self.step_service.history)
            GameController.proclaim_victory(self.state_machine.is_first_player_win())
