import gym
from gym import spaces
import random
import math
from collections import deque

class ChessboardPuzzle(gym.Env):
    """Referential Game with Cards -- Custom Environment that follows gym interface"""

    def __init__(self, n_cells):
        super().__init__()
        self.n_cells = n_cells
        self.n_rows = 2**math.ceil(math.log2(n_cells)/2)

        # Define action and observation space
        # Ignoring spaces for now
        self.action_space = None
        self.observation_space = None


    def reset(self, shuffle_chessboard=True, rand_seed=None):
        self.phase = 0
        self.saved_hint = None
        self.final_choice = None

        # Prepare the chessboard
        if shuffle_chessboard or seed is not None:
            random.seed(rand_seed)
            self.chessboard = random.choices([0, 1], k=self.n_cells)
        self.target_index = random.randrange(self.n_cells)

        speaker_obs  = {'Chessboard': self.chessboard, 'Target': self.target_index}
        listener_obs = {'Chessboard': self.chessboard, 'Target': None}
        observation = [speaker_obs, listener_obs]
        return observation  # reward, done, info can't be included

    def whose_turn(self):
        game_turns = ['Hinter', 'Selector', 'End']
        return game_turns[self.phase]

    def _check_valid_actions(self, actions):
        # Hinter's Turn
        if self.phase == 0:
            actions[1] = None # Selector does nothing
            assert isinstance(actions[0], int), f"Hinter's action should be an int, input given: {actions[0]}"
            assert actions[0] >= 0 and actions[0]<self.n_cells, f"Hinter should choose a coin to flip (between 0 and {self.n_cells-1}), input given: {actions[0]}"
        # Selector's Turn
        if self.phase == 1:
            actions[0] = None # Hinter does nothing
            assert isinstance(actions[1], int), f"Selector's choice should be an int, input given: {actions[1]}"
            assert actions[1] >= 0 and actions[1]<self.n_cells, f"Selector's choice should be between 0 and {self.n_cells-1}, input given: {actions[1]}"
        return actions

    def step(self, actions):
        actions = self._check_valid_actions(actions)
        coin_to_flip, selected_cell = actions

        self.phase += 1
        done = False
        reward = 0

        if self.phase == 2: # Game ends when we finish this step
            done = True
            self.final_choice = selected_cell
            # Check if Listener chose the Target Card
            if self.target_index == selected_cell:
                reward = 1

        if self.phase == 1: # Speaker just gave a hint
            self.saved_hint = coin_to_flip
            self.chessboard[coin_to_flip] = (self.chessboard[coin_to_flip]+1)%2

        speaker_obs  = {'Chessboard': self.chessboard, 'Target': self.target_index}
        listener_obs = {'Chessboard': self.chessboard, 'Target': None}
        observation = [speaker_obs, listener_obs]
        info = {'Chessboard': self.chessboard, 'Target': self.target_index, 'Hint': self.saved_hint, 'Chosen': selected_cell}
        return observation, reward, done, info

    def render(self, mode='human'):
        self.print_chessboard()
        if self.phase == 0:
            print(f"Hinter has to flip a coin")
            print()
        elif self.phase == 1:
            print(f"Chosen Coin to Flip: {self.index_to_coordinate(self.saved_hint)} (Index {self.saved_hint})")
            print(f"Selector has to find the key")
            print()
        else:
            print(f"Selector's Final Choice  : {self.index_to_coordinate(self.final_choice)} (Index {self.final_choice})")
            print(f"Target Cell of Hidden Key: {self.index_to_coordinate(self.target_index)} (Index {self.target_index})")

            print()
            won = self.final_choice == self.target_index
            outcome_str = 'won' if won else 'lost'
            print(f"Players {outcome_str}")

    def index_to_coordinate(self, index):
        return (int(index//self.n_rows), int(index%self.n_rows))

    def print_chessboard(self):
        for idx, coin in enumerate(self.chessboard):
            if idx%self.n_rows == 0:
                print()
                print("-"*int(self.n_rows*4 + 1))
                print("| ", end="")
            print("H |" if coin else "T |", end=" ")
        print()
        print("-"*int(self.n_rows*4 + 1))

    def close (self):
        pass
