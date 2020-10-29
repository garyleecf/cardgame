# Card Game

Instructions:
```bash
git clone https://github.mit.edu/sia/cardgame.git
cd cardgame
pip install -e .
```

In Python:
```python
import gym
env = gym.make('gym_cardgame:threecard-game-v0')
env.reset()

env.render()
```
