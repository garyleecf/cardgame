import random
import numpy as np
from agents import SpeakerAgent, ListenerAgent


class Puzzle_SpeakerAgent(SpeakerAgent):

    def choose_action(self):
        return 0

    def observe(self, speaker_obs):
        super().observe(speaker_obs)
        ## You can do something with self.history, or this information:
        self.chessboard = speaker_obs['Chessboard']
        self.target_index = speaker_obs['Target']


class Puzzle_ListenerAgent(ListenerAgent):

    def choose_action(self):
        return 0

    def observe(self, listener_obs):
        super().observe(listener_obs)
        ## You can do something with self.history, or this information:
        self.chessboard = listener_obs['Chessboard']
