import gym
import numpy as np
import matplotlib.pyplot as plt
from gym.envs.registration import register

register(
    id='FrozenLake-v3',
    entry_point='gym.envs.toy_text:FrozenLakeEnv',
    kwargs={'map_name': '4x4', 'is_slippery': False}
)

env = gym.make('FrozenLake-v3')

Q = np.zeros([env.observation_space.n, env.action_space.n])

dis = .9
num_episodes = 2000

rList = []

for i in range(num_episodes):
    state = env.reset()
    rAll = 0
    done = False

    e = 1. / ((i // 100) + 1)

    while not done:
        # decaying E-greedy
        # if np.random.rand(1)<e:
        # action = env.action_space.sample()
        # else:
        # action = np.argmax(Q[state, :])

        # Random Noise
        action = np.argmax(Q[state, :] + np.random.randn(1, env.action_space.n) / (0.01 * (i + 1)))
        new_state, reward, done, _ = env.step(action)
        Q[state, action] = reward + dis * np.max(Q[new_state, :])
        rAll += reward
        state = new_state

    rList.append(rAll)

print("Success rate: ", str(sum(rList) / num_episodes))
print("Final Q-Table Values")
print("Left       Down       Right       Up")
print(Q)

plt.bar(range(len(rList)), rList, color='blue')
plt.show()