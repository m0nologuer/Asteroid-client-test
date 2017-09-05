from gym.envs.registration import register

register(
    id='asteroid-v1',
    entry_point='asteroid.envs:AsteroidSceneEnv',
)
