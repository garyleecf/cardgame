# Card Game

Instructions:
```bash
git clone https://github.com/garyleecf/cardgame.git
cd cardgame
pip install -e .
```

In Python:
```python
import gym
env = gym.make('gym_cardgame:threecard-game-v0') # Three cards, 4 rank game
env = gym.make('gym_cardgame:referential-game-v0', n_cards_shown=6, n_ranks=13, use_playing_cards=True) # Six cards, full playing cards (13 ranks, with A, K, Q, J)

# Game Simulation Starts:
observations = env.reset()
env.render()

# For actual game play:
observations, reward, done, info = env.step([speaker_action, listener_action])
# Game concludes in "2 steps": 1. Speaker decides on a hint and provides an action, 2. Listener gets the hint, makes a selection as the action
```
See testrun_cardgame.py and testrun_puzzle.py for how the environment and agents are used.
