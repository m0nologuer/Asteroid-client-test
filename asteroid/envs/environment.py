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
    def _configure(self, _url, _key):
        self.url = _url
        self.key = _key

        response = urllib.urlopen("http://{}:8000/simulator/init?key={}".format(self.url, self.key))
        dictionary = json.loads(response.read())

        action_dim = dictionary[u'action_dim']
        obs_dim = dictionary[u'obs_dim']

        high = np.ones([action_dim])
        self.action_space = gym.spaces.Box(-high, high)

        high = np.inf*np.ones([obs_dim])
        self.observation_space = gym.spaces.Box(-high, high)


    #Reset
    def _reset(self):
        response = urllib.urlopen("http://{}:8000/simulator/reset?key={}".format(self.url, self.key))
        
        return json.loads(response.read())[u'state']

    #Take action
    def _step(self, a):
        response  = urllib.urlopen("http://{}:8000/simulator/step?key={}&action={}".format(self.url, self.key, str(a)))
        dictionary = json.loads(response.read())

        state = dictionary[u'state']
        reward = dictionary[u'reward']
        episode_over = dictionary[u'episode_over']

        return state, reward, episode_over, {}
        return {}, {}, {}, {}

    #Refresh render
    def _render(self, mode, close):
        frame  = imread(urllib.urlopen("http://{}:8000/simulator/render?key={}".format(self.url, self.key)))
        return frame

        #Refresh render
    def _buffer(self, mode, close):
        frame  = imread(urllib.urlopen("http://{}:8000/simulator/buffer?key={}&mode={}".format(self.url, self.key, mode)))
        return frame


