import random

class Agent:
    def __init__(self):
        self.reset()
    def reset(self):
        self.history = []

    def choose_action(self):
        return 0

    def observe(self, obs):
        pass


class SpeakerAgent(Agent):
    def __init__(self, n_selection, n_hint_choice=4):
        super().__init__()
        self.n_selection = n_selection
        self.n_hint_choice = n_hint_choice
    def reset(self):
        super().reset()

    def choose_action(self):
        return 0

    def observe(self, speaker_obs):
        pass


class ListenerAgent(Agent):
    def __init__(self, n_selection, n_hint_choice=4):
        super().__init__()
        self.n_selection = n_selection
        self.n_hint_choice = n_hint_choice
    def reset(self):
        super().reset()

    def choose_action(self):
        return 0

    def observe(self, listener_obs):
        pass
