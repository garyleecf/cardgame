import random
import numpy as np
from agents import CardGame_SpeakerAgent, CardGame_ListenerAgent

HINT_ODD, HINT_EVEN, HINT_BLACK, HINT_RED = 0, 1, 2, 3
RANK_TO_ODDEVEN = {'A': HINT_ODD, '1': HINT_ODD, '2': HINT_EVEN, '3': HINT_ODD, '4': HINT_EVEN, '5': HINT_ODD, '6': HINT_EVEN, '7': HINT_ODD, '8': HINT_EVEN, '9': HINT_ODD, 'T': HINT_EVEN, '10': HINT_EVEN, 'J': HINT_ODD, 'Q': HINT_EVEN, 'K': HINT_ODD}
SUIT_TO_COLOR = {'S': HINT_BLACK, 'C': HINT_BLACK, 'D': HINT_RED, 'H': HINT_RED}

def get_feature_matrix(table_cards, n_hint_choice):
    # Collate a "possibility matrix":
    feature_matrix = np.zeros((len(table_cards), n_hint_choice))
    # fill out the "candidate hints" for each card on the table:
    for n, card in enumerate(table_cards):
        suit = card[0]
        rank = card[1]
        feature_matrix[n, SUIT_TO_COLOR[suit]] = 1
        feature_matrix[n, RANK_TO_ODDEVEN[rank]] = 1

    return feature_matrix

class CustomSpeakerAgent(CardGame_SpeakerAgent):

    def choose_action(self):
        feature_matrix = get_feature_matrix(self.table_cards, self.n_hint_choice)

        choices = feature_matrix[self.target_index, :]
        num_unique_identifiers = np.sum(feature_matrix, axis=0)

        best_option = None
        min_identifiers = len(self.table_cards) + 1
        for n, i in enumerate(num_unique_identifiers):
            if choices[n]:
                if i < min_identifiers:
                    best_option = n
                    min_identifiers = i
        return best_option

    def observe(self, speaker_obs):
        super().observe(speaker_obs)
        ## You can do something with self.history, or this information:
        self.table_cards = speaker_obs['Cards']
        self.target_index = speaker_obs['Target']
        target_card = self.table_cards[self.target_index]


class CustomListenerAgent(CardGame_ListenerAgent):

    def choose_action(self):
        feature_matrix = get_feature_matrix(self.table_cards, self.n_hint_choice)

        choices = feature_matrix[:, self.hint]
        num_unique_identifiers = np.sum(feature_matrix, axis=1)

        best_option = None
        min_identifiers = len(self.table_cards) + 1
        for n, i in enumerate(num_unique_identifiers):
            if choices[n]:
                if i < min_identifiers:
                    best_option = n
                    min_identifiers = i
        return best_option

    def observe(self, listener_obs):
        super().observe(listener_obs)
        ## You can do something with self.history, or this information:
        self.table_cards = listener_obs['Cards']
        self.hint = listener_obs['Hint']
