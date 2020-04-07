from gymjam.search import Agent

def run(game, sequence_len, num_individuals):
    best_fitness = -10 ** 18
    best_sequence = None

    for agent_id in range(num_individuals):
        agent = Agent(game, sequence_len)
        game.run(agent)
        if agent.fitness > best_fitness:
            best_fitness = agent.fitness
            best_sequence = agent.commands
            game.run(agent, render=True)
        if agent_id % 100 == 0:
            print(agent_id, best_fitness)

    return best_fitness, best_sequence
