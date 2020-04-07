from gymjam.search import Agent
from random import randint

def run(game, sequence_len, is_plus=False, 
        num_parents=None, population_size=None, 
        num_generations=None):

    best_fitness = -10 ** 18
    best_sequence = None

    population = [Agent(game, sequence_len) for _ in range(population_size)]
    for p in population:
        game.run(p)
        if p.fitness > best_fitness:
            best_fitness = p.fitness
            best_sequence = p.commands
    
    print(best_fitness)

    for curGen in range(num_generations):
        population.sort(reverse=True, key=lambda p: p.fitness)
        parents = population[:num_parents]

        population = []
        for i in range(population_size):
            p = parents[randint(0, len(parents)-1)]
            child = p.mutate()
            game.run(child)

            if child.fitness > best_fitness:
                best_fitness = child.fitness
                best_sequence = child.commands
                game.run(child, render=True)
            population.append(child)
        
        print(curGen, parents[0].fitness, best_fitness)

        if is_plus:
            population += parents

    return best_fitness, best_sequence
