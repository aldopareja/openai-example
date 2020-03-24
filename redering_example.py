import signal
import sys


def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    env.close()
    sys.stdout.flush()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


import gym
# env = gym.make('Ant-v2') #doesn't work yet
env = gym.make('Breakout-v0')
# env = gym.make('CartPole-v0')
env.reset()
while True:
    env.render()
    state = env.step(env.action_space.sample()) # take a random action
    if state[2]:
        env.reset()