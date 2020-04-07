from gymjam.search import Agent
from gymjam.mapping import FixedFeatureMap
from gymjam.mapping.sizers import LinearSizer, ExponentialSizer

def run(game, sequence_len, 
        init_pop_size=-1, num_individuals=-1, sizer_type='Linear',
        sizer_range=(10,10), buffer_size=None):

    best_fitness = -10 ** 18
    best_sequence = None

    sizer = None
    if sizer_type == 'Linear':
        sizer = LinearSizer(*sizer_range)
    elif sizer_type == 'Exponential':
        sizer = ExponentialSizer(*sizer_range)

    #feature_ranges = [(0, sequence_len)] * 2
    feature_ranges = [(-1.0, 1.0), (0.0, 1.0)]
    feature_ranges = feature_ranges[:2]
    print(feature_ranges)
    feature_map = FixedFeatureMap(num_individuals, buffer_size,
                                  feature_ranges, sizer)

    for individuals_evaluated in range(num_individuals):

        cur_agent = None
        if individuals_evaluated < init_pop_size:
            cur_agent = Agent(game, sequence_len)
        else:
            cur_agent = feature_map.get_random_elite().mutate()

        game.run(cur_agent)
        feature_map.add(cur_agent)
        
        if cur_agent.fitness > best_fitness:
            print('improved:', cur_agent.fitness, cur_agent.action_count)
            best_fitness = cur_agent.fitness
            best_sequence = cur_agent.commands
            game.run(cur_agent, render=True)

        if individuals_evaluated % 1000 == 0:
            #elites = [feature_map.elite_map[index] for index in feature_map.elite_map]
            #indicies = [index for index in feature_map.elite_map]
            #features = list(zip(*[a.features for a in elites]))
            #for f in features:
            #    print(sorted(f))
            #print(indicies)
            

            print(individuals_evaluated, best_fitness,
                  len(feature_map.elite_indices))

    return best_fitness, best_sequence
