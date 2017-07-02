import gym, gym.spaces, gym.utils, gym.utils.seeding
import numpy as np
import os, sys

import time
import urllib
import json
from scipy.misc import imread

# -- Environment itself here --

class AsteroidSceneEnv(gym.Env):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second' : 60
    }

    #Initialize scene
    def __init__(self):
        response = urllib.urlopen("http://127.0.0.1:8000/simulator/init/")
        dictionary = json.loads(response.read())

        action_dim = dictionary[u'action_dim']
        obs_dim = dictionary[u'obs_dim']

        high = np.ones([action_dim])
        self.action_space = gym.spaces.Box(-high, high)

        high = np.inf*np.ones([obs_dim])
        self.observation_space = gym.spaces.Box(-high, high)
        

    #Reset
    def _reset(self):
        response = urllib.urlopen("http://127.0.0.1:8000/simulator/reset/")
        
        return json.loads(response.read())[u'state']

    #Take action
    def _step(self, a):
        response  = urllib.urlopen("http://127.0.0.1:8000/simulator/step?action={}".format(a))
        dictionary = json.loads(response.read())

        state = dictionary[u'state']
        reward = dictionary[u'reward']
        episode_over = dictionary[u'episode_over']

        return state, reward, episode_over, {}

    #Refresh render
    def _render(self, mode, close):
        frame  = imread(urllib.urlopen("http://127.0.0.1:8000/simulator/render"))
        return frame

