from State import State


class GameStateMachine:
    first_player_step = State(identifier="FIRST_PLAYER_STEP", final=False)
    second_player_step = State(identifier="SECOND_PLAYER_STEP", final=False)
    first_player_win = State(identifier="FIRST_PLAYER_WIN", final=True)
    second_player_win = State(identifier="SECOND_PLAYER_WIN", final=True)

    def __init__(self):
        self.current_state = GameStateMachine.first_player_step

    def change_state(self, is_winning_step: bool):
        if self.current_state.final:
            raise Exception("Game is over")

        if is_winning_step:
            if self.current_state == GameStateMachine.first_player_step:
                self.current_state = GameStateMachine.first_player_win
                return
            elif self.current_state == GameStateMachine.second_player_step:
                self.current_state = GameStateMachine.second_player_win
                return
        else:
            if self.current_state == GameStateMachine.first_player_step:
                self.current_state = GameStateMachine.second_player_step
                return
            elif self.current_state == GameStateMachine.second_player_step:
                self.current_state = GameStateMachine.first_player_step
                return

        raise Exception("Invalid state")

    def is_state_final(self) -> bool:
        return self.current_state.final
