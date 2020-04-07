from random import randint

class Agent:
    
    def __init__(self, game, sequence_len):
        self.fitness = 0
        self.game = game
        self.sequence_len = sequence_len
        self.commands = [
            randint(0, game.num_actions-1) for _ in range(sequence_len)
        ]

    def mutate(self):
        child = Agent(self.game, self.sequence_len)
        i = randint(0, self.sequence_len-1)
        offset = randint(1, self.game.num_actions)
        child.commands[i] = \
            (child.commands[i] + offset) % self.game.num_actions
        return child
