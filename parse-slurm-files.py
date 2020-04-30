import argparse
import re
import csv
import statistics

"""

If results files are unavailable due to an interrupted/killed run.  This script can recover data from a log file.

NOTE: Aggregations will not be appended only logged to the console

Example input:

python parse-slurm-files.py \
    --files ../gymjam_results/2020_04_22_experiments/logfiles/*_e02*.out
    --outFile e02_stats
"""

# Use as a CLI when called directly
parser = argparse.ArgumentParser(description='Process checkpoints')
parser.add_argument('--files', metavar='F', type=str, nargs='+',
                    help='load checkpoints by name')
parser.add_argument('--outFile', metavar='O', type=str,
                    help='outfile name')
args = parser.parse_args()

checkpoints = []

# print(len(sys.argv))
# print(sys.argv)

commands_delimeter = '/'

results_by_run = {}

# MAX_LINES = 100

if args.files:
    files = args.files
    for f in files:
        try:
            i = 0
            fp = open(f)
            line = fp.readline()
            run_num = 1

            # Put results in a dictionary
            results_by_run[run_num] = {
                # 'results': [],  # if results are needed line by line
                'best_fitness': None,
                'best_fitness_generation': None
            }
            run_results = results_by_run[run_num]
            # results = run_results['results']
            last_generation = 0
            while line:
                parts = re.split('\s+', line)
                # print(parts)
                if len(parts) >= 3:
                    current_generation = int(parts[0] or 0)
                    if current_generation == 1:
                        run_num += 1
                        # Create new dictionary for next run
                        results_by_run[run_num] = {
                            # 'results': [], # if results are needed, line by line
                            'best_fitness': None,
                            'best_fitness_generation': None
                        }
                        run_results = results_by_run[run_num]
                        # results = run_results['results']
                    else:
                        last_generation = current_generation

                    parent_fitness = float(parts[1] or 0.0)
                    best_fitness = float(parts[2] or 0.0)

                    if run_results['best_fitness'] is None or best_fitness > run_results['best_fitness']:
                        run_results['best_fitness'] = best_fitness
                        run_results['best_fitness_generation'] = current_generation

                    # NOTE: for debugging its useful to see the line-by-line results
                    # ## print(curGen, parents[0].fitness, best_fitness)
                    # result = {
                    #     'run_number': run_num,
                    #     'current_generation': current_generation,
                    #     'parent_fitness': parent_fitness,
                    #     'best_fitness': best_fitness
                    # }
                    # results.append(result)
                else:
                    print("WARNING: file '{}' has no parsable output on line 1 '{}'".format(f, line))
                line = fp.readline()
                i += 1
            # do stuff with fp
        finally:
            fp.close()

        # Normalize values to match other files
        print("run_num: ", run_num, "keys: ", len(results_by_run.keys()))
        print(results_by_run)

        results = []
        for k in results_by_run:
            result_dict = results_by_run[k]
            result = {
                'file_name': 'result_file_{}_r{}'.format(f, k),
                'experiment_time': result_dict['best_fitness_generation'],
                'experiment_fitness': result_dict['best_fitness']
            }
            results.append(result)

        # Write CSV
        if args.outFile:
            f_name = args.outFile
            # Write stats per runs
            if results:
                with open('{}_time_results.csv'.format(f_name), 'w', newline='\n') as csvfile:
                    fieldnames = results[0].keys()
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()  # Add a header
                    writer.writerows(results)


        # Aggregations
        aggs_dict = {}

        if results:
            best_fitness_times = [int(r['experiment_time']) for r in results]
            avg_best_fitness_time = sum(best_fitness_times) / len(best_fitness_times)
            stdev_best_fitness_times = statistics.pstdev(best_fitness_times)

            aggs_dict['best_fitness_times_mean'] = avg_best_fitness_time
            aggs_dict['best_fitness_times_std'] = stdev_best_fitness_times


        print("aggregations: ", aggs_dict)