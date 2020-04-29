import argparse
import sys
from lunarlandercolab import FixedFeatureMap, Agent, GameEvaluator, LinearSizer, EmptyBuffer
from checkpointing import Checkpoint
import csv
import statistics

# Use as a CLI when called directly
parser = argparse.ArgumentParser(description='Process checkpoints')
parser.add_argument('--files', metavar='F', type=str, nargs='+',
                    help='load checkpoints by name')
parser.add_argument('--logs', metavar='L', type=str, nargs='+',
                    help='load logs by filename')
parser.add_argument('--outFile', metavar='O', type=str,
                    help='outfile name')
parser.add_argument('--aggregations', metavar='A', type=str,
                    help='a file to append aggregations to')
args = parser.parse_args()

checkpoints = []

# print(len(sys.argv))
# print(sys.argv)

commands_delimeter = '/'

runs = []

if args.files:
    for f in args.files:
        c = Checkpoint(checkpoint_file_name=f)
        checkpoints.append(c)
        if c.checkpoint_data:
            run = {
                'file_name': f
            }
            if isinstance(c.checkpoint_data, FixedFeatureMap):
                # NOTE: these are only for the FINAL map at the end of the run
                # Spreadsheet I column - mean cells filled is avg of these across all runs
                cells_filled_for_given_run = len(c.checkpoint_data.elite_map.keys())
                run['cells_filled'] = cells_filled_for_given_run
                # Spreadsheet G col -
                # print("num_keys: {}".format(cells_filled_for_given_run))
                # Summed mean fitness = sum(for_each cell get fitness) / num_cells
                # aka average fitness per cell in map for run
                sum_fitness = 0
                max_fitness = None
                max_fitness_commands = None
                for key in c.checkpoint_data.elite_map:
                    elite = c.checkpoint_data.elite_map[key]
                    if max_fitness is None or elite.fitness > max_fitness:
                        max_fitness = elite.fitness
                        max_fitness_commands = elite.commands
                    sum_fitness += elite.fitness
                    # print("{}: fitness: {}, commands: {}".format(key, elite.fitness, elite.commands))
                run['sum_fitness'] = sum_fitness
                run['best_fitness'] = max_fitness
                run['best_fitness_commands'] = commands_delimeter.join(list(map(str, max_fitness_commands)))
            else:
                # print(c.checkpoint_data)
                # print(c.checkpoint_data.fitness, c.checkpoint_data.commands)
                run['cells_filled'] = -1
                run['best_fitness'] = c.checkpoint_data.fitness
                run['sum_fitness'] = -1
                run['best_fitness_commands'] = commands_delimeter.join(list(map(str, c.checkpoint_data.commands)))
            runs.append(run)
    # for r in runs:
    #     print(r)

# Write CSVs
if runs and args.outFile:
    f_name = args.outFile
    # Write stats per run
    with open('{}.csv'.format(f_name), 'w', newline='\n') as csvfile:
        fieldnames = run.keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader() # Add a header
        writer.writerows(runs)

    # Write aggregations
    if args.aggregations:
        aggs_file = args.aggregations

        # NOTE: these must match column order in aggs file
        cols = ['file_name', 'best_fitnesss_mean', 'best_fitness_std', 'summed_fitness_mean', 'summed_fitness_std', 'cells_filled_mean', 'cells_filled_std']

        ## Calculate aggregations
        # Write stats per run
        best_fitnesses = [r['best_fitness'] for r in runs]
        # 1. Best Fitnesses
        avg_best_fitness = sum(best_fitnesses) / len(best_fitnesses)
        stdev_best_fitness = statistics.pstdev(best_fitnesses)

        # 2. Summed Fitness
        summed_fitness = [r['sum_fitness'] / r['cells_filled'] for r in runs]
        avg_summed_fitness = sum(summed_fitness) / len(summed_fitness)
        stdev_summed_fitnesses = statistics.pstdev(summed_fitness)

        # 3. Cells filled
        cells_filled = [r['cells_filled'] for r in runs]
        avg_cells_filled = sum(cells_filled) / len(runs)
        stdev_cells_filled = statistics.pstdev(cells_filled)

        aggs_dict = {
            'file_name': f_name,
            'best_fitnesss_mean': avg_best_fitness,
            'best_fitness_std': stdev_best_fitness,
            'summed_fitness_mean': avg_summed_fitness,
            'summed_fitness_std': stdev_summed_fitnesses,
            'cells_filled_mean': avg_cells_filled,
            'cells_filled_std': stdev_cells_filled
        }
        print(aggs_dict)
        with open('{}'.format(aggs_file), 'a', newline='\n') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cols)
            # writer.writeheader() # NOTE: only add when not appending
            writer.writerow(aggs_dict)