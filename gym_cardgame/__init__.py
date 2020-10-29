from gym.envs.registration import register

register(
    id='threecard-game-v0',
    entry_point='gym_cardgame.envs:ThreeCardGame',
)
register(
    id='referential-game-v0',
    entry_point='gym_cardgame.envs:RefGame',
)
register(
    id='chessboard-puzzle-v0',
    entry_point='gym_cardgame.envs:ChessboardPuzzle',
)
