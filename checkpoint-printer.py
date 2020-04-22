import argparse
import sys
from lunarlandercolab import FixedFeatureMap, Agent, GameEvaluator, LinearSizer, EmptyBuffer
from checkpointing import Checkpoint

# Use as a CLI when called directly
parser = argparse.ArgumentParser(description='Process checkpoints')
parser.add_argument('--files', metavar='F', type=str, nargs='+',
                    help='load checkpoints by name')

args = parser.parse_args()

checkpoints = []

print(len(sys.argv))
if args.files:
    for f in args.files:
        c = Checkpoint(checkpoint_file_name=f)
        checkpoints.append(c)
        if c.checkpoint_data:
            if isinstance(c.checkpoint_data, FixedFeatureMap):
                for key in c.checkpoint_data.elite_map:
                    elite = c.checkpoint_data.elite_map[key]
                    print("{}: fitness: {}, commands: {}".format(key, elite.fitness, elite.commands))
            else:
                    print(c.checkpoint_data.fitness, c.checkpoint_data.commands)