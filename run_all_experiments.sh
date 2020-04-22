#!/bin/bash

sbatch experiment_01_random.sh
sbatch experiment_02_ea_plus.sh
sbatch experiment_03_ea_minus.sh
sbatch experiment_04_ea_plus_100.sh
sbatch experiment_05_ea_minus_100.sh
sbatch experiment_06_me_endpointBC.sh
sbatch experiment_07_me_2D_polyhashBC.sh
sbatch experiment_08_me_1D_fitnessBC.sh
sbatch experiment_09_me_1D_entropyBC.sh

# Show status
squeue -u $USER