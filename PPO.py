from vizdoom import *
import random
import time
import numpy as np
from gym import Env
from gym.spaces import Discrete, Box
import cv2
from matplotlib import pyplot as plt
import os
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.callbacks import BaseCallback

class TrainAndLoggingCallback(BaseCallback):

    def __init__(self, check_freq, save_path, log_path, verbose=1):
        super(TrainAndLoggingCallback, self).__init__(verbose)
        self.check_freq = check_freq
        self.save_path = save_path
        self.log_path = log_path

    def _init_callback(self):
        if self.save_path is not None:
            os.makedirs(self.save_path, exist_ok=True)
        if self.log_path is not None:
            os.makedirs(self.log_path, exist_ok=True)

    def _on_step(self):
        if self.n_calls % self.check_freq == 0:
            model_path = os.path.join(self.save_path, 'best_model_{}'.format(self.n_calls))
            self.model.save(model_path)
            print(f"Saved model checkpoint at: {model_path}")

        return True

class VizDoomGym(Env):
    def __init__(self, render=False):
        super().__init__()
        self.game = DoomGame()
        self.game.load_config('C:\\Users\\saimc\\Desktop\\MY PROJECT\\github\\vizdoom\\scenarios\\health_gathering.cfg')

        if render == False:
            self.game.set_window_visible(False)
        else:
            self.game.set_window_visible(True)

        self.game.init()
        self.observation_space = Box(low=0, high=255, shape=(100, 160, 1), dtype=np.uint8)
        self.action_space = Discrete(3)

    def step(self, action):
        actions = np.identity(3)
        reward = self.game.make_action(actions[action], 4)

        if self.game.get_state():
            state = self.game.get_state().screen_buffer
            state = self.grayscale(state)
            ammo = self.game.get_state().game_variables[0]
            info = ammo
        else:
            state = np.zeros(self.observation_space.shape)
            info = 0

        info = {"info": info}
        done = self.game.is_episode_finished()

        return state, reward, done, info

    def render(self):
        pass

    def reset(self):
        self.game.new_episode()
        state = self.game.get_state().screen_buffer
        return self.grayscale(state)

    def close(self):
        self.game.close()

    def grayscale(self, observation):
        gray = cv2.cvtColor(np.moveaxis(observation, 0, -1), cv2.COLOR_BGR2GRAY)
        resize = cv2.resize(gray, (160, 100), interpolation=cv2.INTER_CUBIC)
        state = np.reshape(resize, (100, 160, 1))
        return state

# Callback setup
CHECKPOINT_DIR = 'C:\\Users\\saimc\\Desktop\\MY PROJECT\\checkpoint'
LOG_DIR = 'C:\\Users\\saimc\\Desktop\\MY PROJECT\\logs'
callback = TrainAndLoggingCallback(check_freq=10000, save_path=CHECKPOINT_DIR, log_path=LOG_DIR)

# Create and visualize environment
env = VizDoomGym(render=True)
state = env.reset()
plt.imshow(state.squeeze(), cmap='gray')
plt.show()

# Wrap the environment in DummyVecEnv to make it compatible with Stable Baselines3
env = DummyVecEnv([lambda: env])

# PPO model training with hyperparameter tuning and increased initial timestep length
model = PPO('CnnPolicy', env, tensorboard_log=LOG_DIR, verbose=1, learning_rate=0.00001, n_steps=8192, clip_range=0.1, gamma=0.95, gae_lambda=0.9)

# Train the model with increased initial timestep length and hyperparameter tuning
model.learn(total_timesteps=int(5e6), callback=callback)  # Increase total_timesteps

# Save the final model
model.save('final_model')

# Close the environment
env.close()
