import numpy as np
import gym
from keras.models import Model
from keras.layers.core import Dense
from keras.layers import Input
import random

class QAgent:
    def __init__(self, action_space, state_n):
        self.action_space = action_space
        self.state_n = state_n
        self.gamma = 0.9
        self.epsilon = 0.9
        self.memory = [] # 경험을 저장 하는 리스트(state, action, reward, next_state, done)
        self.replay_count = 0

        self.q_model = self.build_model(self.state_n, self.action_space.n)
        self.q_model.compile(loss='mse', optimizer='adam')
        self.q_target_model = self.build_model(self.state_n, self.action_space.n)
        self.update_weight()

    def build_model(self, n_input, n_output):
        inputs = Input(shape=(n_input,))
        x = Dense(units=256, activation='relu')(inputs)
        x = Dense(units=128, activation='relu')(x)
        x = Dense(units=64, activation='relu')(x)
        x = Dense(units=32, activation='relu')(x)
        outputs = Dense(units=n_output, activation='linear')(x)
        model = Model(inputs=inputs, outputs=outputs)
        model.summary()
        return model

    def act(self, state):
        if np.random.rand() < self.epsilon:
            action = self.action_space.sample()
        else:
            q_values = self.q_model.predict(state)
            action = np.argmax(q_values[0])
        return action

    def replay(self, batch_size):
        sars_batch = random.sample(self.memory, batch_size)
        state_batch = []
        q_value_batch = []

        for state, action, reward, next_state, done in sars_batch:
            q_values = self.q_model.predict(state)
            q_value = self.get_target_q_value(reward, next_state)
            q_values[0][action] = q_value if done else q_value

            state_batch.append(state[0])
            q_value_batch.append(q_values[0])

        self.q_model.fit(x=np.array(state_batch), y=np.array(q_value_batch))

        self.update_epsilon()
        self.replay_count += 1
        if self.replay_count % 10 == 0:
            self.update_weight()

    def get_target_q_value(self, reward, next_state):
        return reward + self.gamma * np.amax(self.q_target_model.predict(next_state)[0])

    def update_epsilon(self):
        if self.epsilon > 0.1:
            self.epsilon *= 0.1

    def update_weight(self):
        self.q_target_model.set_weights(self.q_model.get_weights())

    def get_memory_size(self):
        return len(self.memory)

    def rem(self, s, a, r, ns, d):
        self.memory.append((s, a, r, ns, d))

class QController:
    def __init__(self):
        self.env = gym.make('CartPole-v1', render_mode='human')
        self.agent = QAgent(self.env.action_space, self.env.observation_space.shape[0])

    def control(self):
        state_size = self.env.observation_space.shape[0]
        for episode in range(40000):
            state = np.array(self.env.reset())
            state = np.reshape(state[0],(1,state_size))
            done = False

            while not done:
                action = self.agent.act(state)
                next_state, reward, done, _, _ = self.env.step(action)
                self.env.render()
                next_state = np.reshape(next_state, (1,state_size))
                self.agent.rem(state, action, reward, next_state, done)
                if self.agent.get_memory_size() > 64:
                    self.agent.replay(64)


if __name__ == '__main__':
    controller = QController()
    controller.control()