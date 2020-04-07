import sys
import gymjam.search.es
import gymjam.search.me
import gymjam.search.random
import gymjam.mapping
from gymjam.evaluation import GameEvaluator

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    num_actions = 100
    search_type = 'ME'
    #game = GameEvaluator('Qbert-v0', seed=1009, num_rep=2)
    game = GameEvaluator('LunarLander-v2', seed=1008, num_rep=3)

    if search_type == 'ES':
        gymjam.search.es.run(game, 
                num_actions, 
                is_plus=False,
                num_parents=10, 
                population_size=100,
                num_generations=100,
            )
    elif search_type == 'RS':
        gymjam.search.random.run(game, num_actions, 10000)
    elif search_type == 'ME':
        gymjam.search.me.run(game, 
                num_actions, 
                init_pop_size=1000, 
                num_individuals=1000000, 
                sizer_type='Linear', 
                sizer_range=(7000, 8000), 
                buffer_size=None)
    elif search_type == 'test':
        from gymjam.search import Agent
        cur_agent = Agent(game, num_actions)
        while True:
            game.run(cur_agent, render=True)

    game.env.close()

if __name__ == '__main__':
    sys.exit(main())
