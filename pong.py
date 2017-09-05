import os, sys, subprocess
import numpy as np
import gym
import asteroid
import random

from twitchstream.outputvideo import TwitchBufferedOutputStream
from twitchstream.chat import TwitchChatStream

TWITCH_KEY = "live_86944108_XVDMuEvn7AFBEOLuvNeiyCSE4VX4bY"
OAUTH_KEY = "oauth:y56mfwbmq724genm9bchxqi11u5iac"

#env = gym.make("asteroid-v1")
#env._configure("ec2-34-249-73-16.eu-west-1.compute.amazonaws.com", "")

videostream = TwitchBufferedOutputStream(twitch_stream_key=TWITCH_KEY, width=1238, height=822)
#chat = TwitchChatStream(username='madamexpsychosis', oauth=OAUTH_KEY)

while True:
    if videostream.get_video_frame_buffer_state() < 30:
        videostream.send_video_frame(np.ones((822, 1238, 3)))


