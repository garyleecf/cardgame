# Card Game & Chessboard Puzzle

Instructions:
If using an interface like Jupyter Lab/Notebook (and unfamiliar with bash/command prompt):
* Under "Code", click on "Download Zip". Extract the files and put it on your work directory.
* Start up Jupyter Lab or Notebook, navigate to this folder
* Open either "notebook_cardgame.ipynb" or "notebook_puzzle.ipynb" to get started. Make sure to run the first cell to set things up.
* To create your own "strategies" to play the game, find the "my_agents.py" file (inside agents folder), and modify "observe" and "choose_action" functions accordingly.

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



## About the functions of the env and agents:
### Card Game:
To create:
```python
env = gym.make('gym_cardgame:threecard-game-v0')
# You can also use a harder game by using the following, and changing the arguments accordingly
# env = gym.make('gym_cardgame:referential-game-v0', n_cards_shown=6, n_ranks=13, use_playing_cards=True)
n_hint_choice = 4 # This defines the number of "words" we allow the speaker to choose from
```
```python
observation, reward, done, info = env.step(actions):
```

observation:
```python
speaker_obs, listener_obs = observation

speaker_obs['Cards'] -- list of table cards (e.g. ['S4', 'C3', 'H2'])
speaker_obs['Target'] -- the index of the target card (e.g. 0)
(speaker_obs['Hint'] will be None)

listener_obs['Cards'] -- list of table cards (e.g. ['S4', 'C3', 'H2'])
listener_obs['Hint'] -- int corresponding to the chosen hint
(listener_obs['Target'] will be None)
```

How to use:
```python
observations, reward, done, info = env.step([speaker_action, listener_action])
```

Recommended structure for agents:
```python
speaker = agents.SpeakerAgent(n_selection=env.n_cards_shown, n_hint_choice=n_hint_choice)
listener = agents.ListenerAgent(n_selection=env.n_cards_shown, n_hint_choice=n_hint_choice)

speaker.observe(speaker_obs)
listener.observe(listener_obs)

speaker_action = speaker.choose_action() #or None
listener_action = listener.choose_action() #or None
```
### Chessboard Puzzle
To create:
```python
env = gym.make('chessboard-puzzle-v0', n_cells=16)
```
```python
observation, reward, done, info = env.step(actions):
```

observation:
```python
speaker_obs, listener_obs = observation

speaker_obs['Chessboard'] -- list of coin faces, row-wise (e.g. [0, 0, 1, 1, 0, 0, 1, 1...])
speaker_obs['Target'] -- the index of the target square (e.g. 12)


listener_obs['Chessboard'] -- list of coin faces, row-wise (e.g. [0, 0, 1, 1, 0, 0, 1, 1...])
(listener_obs['Target'] will be None)
```

How to use:
```python
observations, reward, done, info = env.step([speaker_action, listener_action])
```

Recommended structure for agents:
```python
speaker = agents.Puzzle_SpeakerAgent(n_selection=env.n_cells, n_hint_choice=env.n_cells)
listener = agents.Puzzle_ListenerAgent(n_selection=env.n_cells, n_hint_choice=env.n_cells)

speaker.observe(speaker_obs)
listener.observe(listener_obs)

speaker_action = speaker.choose_action() # random.randrange(4)
listener_action = None

observations, reward, done, info = env.step([speaker_action, listener_action])
```    
