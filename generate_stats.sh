#!/bin/bash

# Define checkpoints directory
CHECKPOINTS_DIR=../gymjam_results/2020_04_28_experiments/checkpoints
PREV_RUN_CHECKPOINTS_DIR=../gymjam_results/2020_04_22_experiments/checkpoints
RESULTS_DIR=../gymjam_results/2020_04_28_experiments/results


# Create aggregations file
AGGS_FILE=aggregations.csv
echo "file_name,best_fitness,best_fitnesss_mean,best_fitness_std,best_fitness_times_mean,best_fitness_times_std,summed_fitness_mean,summed_fitness_std,cells_filled_mean,cells_filled_std" > $AGGS_FILE

# Experiment 1
python checkpoint-printer.py \
    --files $CHECKPOINTS_DIR/experiment01_*_latest.pkl \
    --result-files $RESULTS_DIR/results_e01* \
    --outFile="exp01_stats" \
    --aggregations=$AGGS_FILE

# Experiment 2
python checkpoint-printer.py \
    --files $PREV_RUN_CHECKPOINTS_DIR/experiment02_*_latest.pkl \
    --outFile="exp02_stats" \
    --aggregations=$AGGS_FILE

# Experiment 3
python checkpoint-printer.py \
    --files $PREV_RUN_CHECKPOINTS_DIR/experiment03_*_latest.pkl \
    --outFile="exp03_stats" \
    --aggregations=$AGGS_FILE

# Experiment 4
python checkpoint-printer.py \
    --files $CHECKPOINTS_DIR/experiment04_*_latest.pkl \
    --result-files $RESULTS_DIR/results_e04* \
    --outFile="exp04_stats" \
    --aggregations=$AGGS_FILE

# Experiment 5
python checkpoint-printer.py \
    --files $CHECKPOINTS_DIR/experiment05_*_latest.pkl \
    --result-files $RESULTS_DIR/results_e05* \
    --outFile="exp05_stats" \
    --aggregations=$AGGS_FILE

# Experiment 6
python checkpoint-printer.py \
    --files $CHECKPOINTS_DIR/experiment06_*_latest.pkl \
    --result-files $RESULTS_DIR/results_e06* \
    --outFile="exp06_stats" \
    --aggregations=$AGGS_FILE

# Experiment 7
python checkpoint-printer.py \
    --files $CHECKPOINTS_DIR/experiment07_*_latest.pkl \
    --result-files $RESULTS_DIR/results_e07* \
    --outFile="exp07_stats" \
    --aggregations=$AGGS_FILE

# Experiment 8
python checkpoint-printer.py \
    --files $CHECKPOINTS_DIR/experiment08_*_latest.pkl \
    --result-files $RESULTS_DIR/results_e08* \
    --outFile="exp08_stats" \
    --aggregations=$AGGS_FILE

# Experiment 9
python checkpoint-printer.py \
    --files $CHECKPOINTS_DIR/experiment09_*_latest.pkl \
    --result-files $RESULTS_DIR/results_e09* \
    --outFile="exp09_stats" \
    --aggregations=$AGGS_FILE