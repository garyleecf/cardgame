import gym
import agents

from gym_cardgame.envs.puzzle_env import ChessboardPuzzle

_DEBUG = False

def main():
    env = gym.make('chessboard-puzzle-v0', n_cells=16)
     # n_cells defines both the number of "hints" for Speaker as well as the number of tiles to choose from for Listener

    # Choose your "players":
    # # Naive: Only does the first action
    # speaker = agents.SpeakerAgent(n_selection=env.n_cells, n_hint_choice=env.n_cells)
    # listener = agents.ListenerAgent(n_selection=env.n_cells, n_hint_choice=env.n_cells)

    # # Random: Chooses actions randomly from possible options
    # speaker = agents.RandomSpeakerAgent(n_selection=env.n_cells, n_hint_choice=env.n_cells)
    # listener = agents.RandomListenerAgent(n_selection=env.n_cells, n_hint_choice=env.n_cells)

    # Custom: Uses the logic as written in custom_agents
    speaker = agents.Puzzle_SpeakerAgent(n_selection=env.n_cells, n_hint_choice=env.n_cells)
    listener = agents.Puzzle_ListenerAgent(n_selection=env.n_cells, n_hint_choice=env.n_cells)


    # ==============================
    # Game Simulation Starts:
    observations = env.reset()
    env.render()

    # Phase 1: Speaker sees the cards + target, determines what to hint
    print("==============================")
    print("Phase 1: Speaker's Turn")
    print("==============================")
    speaker_obs, listener_obs = observations
    if _DEBUG:
        print(speaker_obs)
    speaker.observe(speaker_obs)
    listener.observe(listener_obs)

    speaker_action = speaker.choose_action() # random.randrange(4)
    listener_action = None

    observations, reward, done, info = env.step([speaker_action, listener_action])
    env.render()

    # Phase 2: Listener makes a choice among the cards
    print("==============================")
    print("Phase 2: Listener's Turn")
    print("==============================")
    speaker_obs, listener_obs = observations
    if _DEBUG:
        print(listener_obs)
    speaker.observe(speaker_obs)
    listener.observe(listener_obs)

    speaker_action = None
    listener_action = listener.choose_action() # random.randrange(env.n_cards_shown)

    observations = env.step([speaker_action, listener_action])
    env.render()

if __name__ == '__main__':
    main()
