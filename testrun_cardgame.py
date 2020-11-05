import gym
import agents

_DEBUG = False

def main():
    env = gym.make('gym_cardgame:threecard-game-v0')
    # You can also use a harder game by using the following, and changing the arguments accordingly
    # env = gym.make('gym_cardgame:referential-game-v0', n_cards_shown=6, n_ranks=13, use_playing_cards=True)
    n_hint_choice = 4 # This defines the number of "words" we allow the speaker to choose from

    # Choose your "players":
    # # Naive: Only does the first action
    # speaker = agents.CardGame_SpeakerAgent(n_selection=env.n_cards_shown, n_hint_choice=n_hint_choice)
    # listener = agents.CardGame_ListenerAgent(n_selection=env.n_cards_shown, n_hint_choice=n_hint_choice)

    # # Random: Chooses actions randomly from possible options
    # speaker = agents.RandomSpeakerAgent(n_selection=env.n_cards_shown, n_hint_choice=n_hint_choice)
    # listener = agents.RandomListenerAgent(n_selection=env.n_cards_shown, n_hint_choice=n_hint_choice)

    # Custom: Uses the logic as written in custom_agents
    speaker = agents.CustomSpeakerAgent(n_selection=env.n_cards_shown, n_hint_choice=n_hint_choice)
    listener = agents.CustomListenerAgent(n_selection=env.n_cards_shown, n_hint_choice=n_hint_choice)


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
