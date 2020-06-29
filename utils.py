def collect_episode(env, policy, buffer, render):
    state = env.reset()
    done = False
    while not done:
        if render:
            env.render()
        action = policy(state)
        next_state, reward, done, _ = env.step(action)
        if done:
            reward = -1.0
        buffer.record(state, reward, next_state, action, done)
        state = next_state


def compute_avg_reward(env, policy, num_episodes):
    total_return = 0.0
    for _ in range(num_episodes):
        state = env.reset()
        done = False
        episode_return = 0.0
        while not done:
            action = policy(state)
            next_state, reward, done, _ = env.step(action)
            if done:
                reward = -1.0
            episode_return += reward
            state = next_state
        total_return += episode_return
    avg_return = total_return / num_episodes
    return avg_return