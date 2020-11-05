import random
from agents import SpeakerAgent, ListenerAgent


class CardGame_SpeakerAgent(SpeakerAgent):
    def __init__(self, n_selection, n_hint_choice=4):
        super().__init__(n_selection, n_hint_choice)
        self.n_selection = n_selection
        self.n_hint_choice = n_hint_choice
    def reset(self):
        super().reset()

    def choose_action(self):
        return 0

    def observe(self, speaker_obs):
        self.history.append(speaker_obs)
        table_cards = speaker_obs['Cards']
        target_index = speaker_obs['Target']
        target_card = table_cards[target_index]


class CardGame_ListenerAgent(ListenerAgent):
    def __init__(self, n_selection, n_hint_choice=4):
        super().__init__(n_selection, n_hint_choice)
        self.n_selection = n_selection
        self.n_hint_choice = n_hint_choice
    def reset(self):
        super().reset()

    def choose_action(self):
        return 0

    def observe(self, listener_obs):
        self.history.append(listener_obs)
        table_cards = listener_obs['Cards']
        hint = listener_obs['Hint']
