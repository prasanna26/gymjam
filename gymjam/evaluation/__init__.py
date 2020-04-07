import gym
from time import time
from gym.wrappers import Monitor

# A generic game evaluator.
# Make specific evaluators if feature info is
# required to be recorded and stored.
class GameEvaluator:
    def __init__(self, game_name, seed=1009, num_rep=1):
        self.env = gym.make(game_name)
        self.seed = seed
        self.num_rep = num_rep
        self.num_actions = self.env.action_space.n
        print(self.num_actions)

    def run(self, agent, render=False):
        agent.fitness = 0
        self.env.seed(self.seed)
        env = self.env
        if render:
            env = Monitor(env, './videos/'+str(time())+'/')
        observation = env.reset()

        action_frequency = [0] * self.num_actions
        
        action_count = 0
        done = False
        while not done:
            #if render:
            #    env.render()
            
            pos = min(action_count//self.num_rep, len(agent.commands)-1)
            action = agent.commands[pos]
            action_count += 1

            observation, reward, done, info = env.step(action)
            agent.fitness += reward

            action_frequency[action] += 1
        
        final_observation = list(observation)

        agent.features = tuple(final_observation[:1])
        agent.action_count = action_count
