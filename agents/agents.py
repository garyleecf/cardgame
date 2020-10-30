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
    def __init__(self, n_word_choice=4):
        super().__init__()
        self.n_word_choice = n_word_choice
    def reset(self):
        super().reset()

    def choose_action(self):
        return random.randrange(self.n_word_choice)

    def observe(self, speaker_obs):
        self.history.append(speaker_obs)
        table_cards = speaker_obs['Cards']
        target_index = speaker_obs['Target']
        target_card = table_cards[target_index]


class ListenerAgent(Agent):
    def __init__(self, n_card_choice):
        super().__init__()
        self.n_card_choice = n_card_choice
    def reset(self):
        super().reset()

    def choose_action(self):
        return random.randrange(self.n_card_choice)

    def observe(self, listener_obs):
        self.history.append(listener_obs)
        table_cards = listener_obs['Cards']
        hint = listener_obs['Hint']
