import gym
from gym import spaces
import random
from collections import deque
from rlcard.utils import elegent_form

class RefGame(gym.Env):
    """Referential Game with Cards -- Custom Environment that follows gym interface"""

    def __init__(self, n_cards_shown, n_ranks = 4):
        super().__init__()

        # Define action and observation space
        # Ignoring spaces for now
        self.action_space = None
        self.observation_space = None

        # Prepare a deck of cards
        self.all_cards = [f"{rank}{suit}" for rank in range(n_ranks) for suit in ['C','D','H','S']]
        self.deck = deque(self.all_cards)

    def reset(self, shuffle_deck=True, rand_seed=None):
        self.phase = 0
        self.saved_hint = None
        self.final_choice = None

        if shuffle_deck or seed is not None:
            self.deck = deque(self.all_cards)
            random.seed(rand_seed)
            random.shuffle(self.deck)
        self._deal_cards()

        speaker_obs  = {'Cards': self.table_cards, 'Target': self.target_index, 'Hint': None}
        listener_obs = {'Cards': self.table_cards, 'Target': None, 'Hint': None}
        observation = [speaker_obs, listener_obs]
        return observation  # reward, done, info can't be included

    def whose_turn(self):
        game_turns = ['Speaker', 'Listener', 'End']
        return game_turns[self.phase]

    def _deal_cards(self):
        self.table_cards = [self.deck.popleft() for _ in range(self.n_cards_shown)]
        self.target_index = random.randrange(self.n_cards_shown)
        self.target_card = self.table_cards[self.target_index]

    def step(self, actions):
        self.phase += 1
        done = False
        reward = 0

        speaker_hint, listener_choice = actions

        if self.phase == 2: # Game ends when we finish this step
            done = True
            self.final_choice = listener_choice
            # Check if Listener chose the Target Card
            if self.target_index == listener_choice:
                reward = 1

        if self.phase == 1: # Speaker just gave a hint
            self.saved_hint = speaker_hint

        speaker_obs  = {'Cards': self.table_cards, 'Target': self.target_index, 'Hint': self.saved_hint}
        listener_obs = {'Cards': self.table_cards, 'Target': None, 'Hint': self.saved_hint}
        observation = [speaker_obs, listener_obs]
        info = {'Cards': self.table_cards, 'Target': self.target_index, 'Hint': self.saved_hint, 'Chosen': listener_choice}
        return observation, reward, done, info

    def render(self, mode='human'):
        if self.phase == 1:
            for card_str in table_cards:
                print(elegent_form(card_str), end ="   ")
            print(f"Speaker's Hint: {self.saved_hint}")
            print()
        else:
            print(f"Listener's Final Choice: {self.table_cards[self.final_choice]}")
            print(f"Target Card: {self.table_cards[self.target_index]}")
            won = self.final_choice == self.target_index
            outcome_str = 'won' if won else 'lost'
            print(f"Players {outcome_str}"")


    def close (self):
        pass

class ThreeCardGame(RefGame):
    def __init__(self):
        super().__init__(n_cards_shown=3)
