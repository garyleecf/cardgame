import random
from agents import SpeakerAgent, ListenerAgent


class RandomSpeakerAgent(SpeakerAgent):

    def choose_action(self):
        return random.randrange(self.n_hint_choice)

    def observe(self, speaker_obs):
        super().observe(speaker_obs)


class RandomListenerAgent(ListenerAgent):

    def choose_action(self):
        return random.randrange(self.n_selection)

    def observe(self, listener_obs):
        super().observe(listener_obs)
