from random import randint
from gymjam.search import Agent
from gymjam.mapping.sizers import LinearSizer, ExponentialSizer
from gymjam.mapping.buffers import EmptyBuffer, SlidingBuffer

class FixedFeatureMap:
    
    def __init__(self, num_to_evaluate, buffer_size, boundaries, sizer):

        # Clock for resizing the map.
        self.num_individuals_to_evaluate = num_to_evaluate
        self.num_individuals_added = 0
        
        # Feature to individual mapping.
        self.num_features = len(boundaries)
        self.boundaries = boundaries
        self.elite_map = {}
        self.elite_indices = []

        # A group is the number of cells along 
        # each dimension in the feature space.
        self.group_sizer = sizer
        self.num_groups = 3

        if buffer_size == None:
            self.buffer = EmptyBuffer()
        else:
            self.buffer = SlidingBuffer(buffer_size)

    def get_feature_index(self, feature_id, feature):
        low_bound, high_bound = self.boundaries[feature_id]
        if feature <= low_bound:
            return 0
        if high_bound <= feature:
            return self.num_groups-1

        gap = high_bound - low_bound + 1
        pos = feature - low_bound
        index = int(self.num_groups * pos / gap)
        return index

    def get_index(self, agent):
        index = tuple(self.get_feature_index(i, v) \
                for i, v in enumerate(agent.features))
        return index

    def add_to_map(self, to_add):
        index = self.get_index(to_add)

        replaced_elite = False
        if index not in self.elite_map:
            self.elite_indices.append(index)
            self.elite_map[index] = to_add
            replaced_elite = True
        elif self.elite_map[index].fitness < to_add.fitness:
            self.elite_map[index] = to_add
            replaced_elite = True

        return replaced_elite

    def remove_from_map(self, to_remove):
        index = self.get_index(to_remove)
        if index in self.elite_map and self.elite_map[index] == to_remove:
            del self.elite_map[index]
            self.elite_indices.remove(index)
            return True

        return False

    def remap(self, next_num_groups):
        print('remap', '{}x{}'.format(next_num_groups, next_num_groups))
        self.num_groups = next_num_groups

        all_elites = self.elite_map.values()
        self.elite_indices = []
        self.elite_map = {}
        for elite in all_elites:
            self.add_to_map(elite)
        
    def add(self, to_add):
        self.num_individuals_added += 1
        portion_done = \
            self.num_individuals_added / self.num_individuals_to_evaluate
        next_num_groups = self.group_sizer.get_size(portion_done)
        if next_num_groups != self.num_groups:
            self.remap(next_num_groups)

        replaced_elite = self.add_to_map(to_add)
        self.buffer.add_individual(to_add)
        if self.buffer.is_overpopulated():
            self.remove_from_map(self.buffer.remove_individual())

        return replaced_elite

    def get_random_elite(self):
        pos = randint(0, len(self.elite_indices)-1)
        index = self.elite_indices[pos]
        return self.elite_map[index]

# For testing to make sure that the map works
if __name__ == '__main__':
    linear_sizer = LinearSizer(2, 10)
    linear_sizer = ExponentialSizer(2, 500)
    feature_map = FixedFeatureMap(100, None, [(0, 10), (0, 10)], linear_sizer)
    print(feature_map.num_individuals_to_evaluate)

    from gymjam.evaluation import GameEvaluator
    game = GameEvaluator('LunarLander-v2')

    for x in range(0, 100):
        agent = Agent(game, 200)
        agent.features = (x%10, (x+5)%10)
        agent.fitness = -x
        #print(x, feature_map.add(agent))
        feature_map.add(agent)
