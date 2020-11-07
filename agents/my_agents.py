import random
import numpy as np
from agents import CardGame_SpeakerAgent, CardGame_ListenerAgent, Puzzle_SpeakerAgent, Puzzle_ListenerAgent


########## Agents for the Card Game ##########

class MyCardGameSpeakerAgent(CardGame_SpeakerAgent):
##    This has already been defined in the parent class
##    Uncomment only if you want to modify the __init__ and reset functions
#     def __init__(self, n_selection, n_hint_choice=4):
#         super().__init__(n_selection, n_hint_choice)
#         self.n_selection = n_selection
#         self.n_hint_choice = n_hint_choice
    
#     def reset(self):
#         super().reset()
        
    def choose_action(self):
        # You can choose an action based on the seen cards (self.table_cards)
        # or the target_index (self.target_index)/the target card (self.table_cards[self.target_index])
        return 0

    def observe(self, speaker_obs):
        super().observe(speaker_obs)
        ## You can do something with self.history, or this information:
        self.table_cards = speaker_obs['Cards']
        self.target_index = speaker_obs['Target']
        target_card = self.table_cards[self.target_index]


class MyCardGameListenerAgent(CardGame_ListenerAgent):
##    This has already been defined in the parent class
##    Uncomment only if you want to modify the __init__ and reset functions
#     def __init__(self, n_selection, n_hint_choice=4):
#         super().__init__(n_selection, n_hint_choice)
#         self.n_selection = n_selection
#         self.n_hint_choice = n_hint_choice
        
#     def reset(self):
#         super().reset()
        
    def choose_action(self):
        # You can choose an action based on the seen cards (self.table_cards)
        # or the hint (self.hint)
        return 0

    def observe(self, listener_obs):
        super().observe(listener_obs)
        ## You can do something with self.history, or this information:
        self.table_cards = listener_obs['Cards']
        self.hint = listener_obs['Hint']



########## Agents for the Chessboard Puzzle ##########

class MyPuzzleSpeakerAgent(Puzzle_SpeakerAgent):
##    This has already been defined in the parent class
##    Uncomment only if you want to modify the __init__ and reset functions
#     def __init__(self, n_selection, n_hint_choice=4):
#         super().__init__()
#         self.n_selection = n_selection
#         self.n_hint_choice = n_hint_choice
        
#     def reset(self):
#         super().reset()
        
    def choose_action(self):
        # You can choose an action based what is seen on the chessboard (self.chessboard)
        # and the target index square (self.target_index)
        return 0

    def observe(self, speaker_obs):
        super().observe(speaker_obs)
        ## You can do something with self.history, or this information:
        self.chessboard = speaker_obs['Chessboard']
        self.target_index = speaker_obs['Target']


class MyPuzzleListenerAgent(Puzzle_ListenerAgent):
##    This has already been defined in the parent class
##    Uncomment only if you want to modify the __init__ and reset functions
#     def __init__(self, n_selection, n_hint_choice=4):
#         super().__init__()
#         self.n_selection = n_selection
#         self.n_hint_choice = n_hint_choice
    
#     def reset(self):
#         super().reset()
        
    def choose_action(self):
        # You can choose an action based what is seen on the chessboard (self.chessboard)
        return 0

    def observe(self, listener_obs):
        super().observe(listener_obs)
        ## You can do something with self.history, or this information:
        self.chessboard = listener_obs['Chessboard']
