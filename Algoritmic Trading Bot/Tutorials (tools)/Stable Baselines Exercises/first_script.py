import gym
import time 

import matplotlib.image as mpimg
import matplotlib.pyplot as plt


env = gym.make(
    "LunarLander-v2", 
    render_mode="rgb_array"
)

env.reset()

print(f"sample action: {env.action_space.sample()}")
print(f"Observation space shape: {env.observation_space.shape}")
print(f"Observation space sample: {env.observation_space.sample()}")

for step in range(200):
    env.render()
    #time.sleep(0.2)
    episode_action = env.action_space.sample()
    print(episode_action)
    env.step(episode_action)

env.close()
