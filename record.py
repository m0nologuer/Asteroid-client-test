import os, sys, subprocess
import numpy as np
import gym
import asteroid
import random

from twitchstream.outputvideo import TwitchBufferedOutputStream
from twitchstream.chat import TwitchChatStream

TWITCH_KEY = "live_86944108_XVDMuEvn7AFBEOLuvNeiyCSE4VX4bY"
OAUTH_KEY = "oauth:y56mfwbmq724genm9bchxqi11u5iac"

def play(env, video):
    episode_n = 0
    while 1:
        episode_n += 1
        #obs = env.reset()
        if video: video_recorder = gym.monitoring.video_recorder.VideoRecorder(env=env, base_path=("tmp/demo_pong_episode%i" % episode_n), enabled=True)
        for i in range(200):
            if video: video_recorder.capture_frame()
            #if done: break
        if video: video_recorder.close()
        break

env = gym.make("asteroid-v1")
env._configure("ec2-34-249-73-16.eu-west-1.compute.amazonaws.com", "")

play(env, video=True)
