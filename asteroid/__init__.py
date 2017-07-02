from gym.envs.registration import register

register(
    id='asteroid-v0',
    entry_point='asteroid.envs:AsteroidSceneEnv',
)
