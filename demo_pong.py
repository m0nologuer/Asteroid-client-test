import os, sys, subprocess
import numpy as np
import gym
import asteroid

def play(env, pi, video):
    episode_n = 0
    while 1:
        episode_n += 1
        obs = env.reset()
        if video: video_recorder = gym.monitoring.video_recorder.VideoRecorder(env=env, base_path=("tmp/demo_pong_episode%i" % episode_n), enabled=True)
        for i in range(1000):
            a = pi.act(obs)
            obs, rew, done, info = env.step(a)
            if video: video_recorder.capture_frame()
            if done: break
        if video: video_recorder.close()
        break

env = gym.make("asteroid-v0")

from RoboschoolPong_v0_2017may1 import SmallReactivePolicy as Pol1

pi = Pol1(env.observation_space, env.action_space)

play(env, pi, video=True)   # set video = player_n==0 to record video

