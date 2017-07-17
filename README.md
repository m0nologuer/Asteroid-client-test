# Asteroid-client-test


## To install
To get started, you'll need to have Python 2.7 or Python 3.5. Fetch the asteroid code using:

```
git clone https://github.com/m0nologuer/Asteroid-client-test
cd gym
pip install -e . # minimal install
```

You can then use Asteroid with OpenAI gym by doing

```
import gym
import asteroid
env = gym.make('asteroid-v0')
```

## Setup

To use a running Asteroid simulation with this gem, simply take the url and key from the web app.

Then do:

```
import gym
import asteroid
env = gym.make('asteroid-v0')
env.configure(url=URL, key=KEY)
```

## Run

It can take between 10-15 minutes for a simulation to start and become usable.

The commands - init, render, step, and reset - are standard OpenAI Gym environment variables.

The only new command - buffer - is used to get the rendered output of alternate buffers

```
#Get rendered output of alternate buffer 
x = env.buffer(mode='segmentation')
```

## Example

Check out the demo.py file for how to set up an agent to deal with an Asteroid environment (warning - sim is not currently running, it is purely there as an example)