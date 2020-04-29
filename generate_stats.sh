#!/bin/bash

# Define checkpoints directory
CHECKPOINTS_DIR=../gymjam_results/2020_04_22_experiments/checkpoints


# Create aggregations file
AGGS_FILE=aggregations.csv
echo "file_name,best_fitnesss_mean,best_fitness_std,summed_fitness_mean,summed_fitness_std,cells_filled_mean,cells_filled_std" > $AGGS_FILE

# Experiment 1
python checkpoint-printer.py \
    --files $CHECKPOINTS_DIR/experiment01_*_latest.pkl \
    --outFile="exp01_stats" \
    --aggregations=$AGGS_FILE

# Experiment 2
python checkpoint-printer.py \
    --files $CHECKPOINTS_DIR/experiment02_*_latest.pkl \
    --outFile="exp02_stats" \
    --aggregations=$AGGS_FILE
#
# Experiment 3
python checkpoint-printer.py \
    --files $CHECKPOINTS_DIR/experiment03_*_latest.pkl \
    --outFile="exp03_stats" \
    --aggregations=$AGGS_FILE

# Experiment 4
python checkpoint-printer.py \
    --files $CHECKPOINTS_DIR/experiment04_*_latest.pkl \
    --outFile="exp04_stats" \
    --aggregations=$AGGS_FILE

# Experiment 5
python checkpoint-printer.py \
    --files $CHECKPOINTS_DIR/experiment05_*_latest.pkl \
    --outFile="exp05_stats" \
    --aggregations=$AGGS_FILE

# Experiment 6
python checkpoint-printer.py \
    --files $CHECKPOINTS_DIR/experiment06_*_latest.pkl \
    --outFile="exp06_stats" \
    --aggregations=$AGGS_FILE

# Experiment 7
python checkpoint-printer.py \
    --files $CHECKPOINTS_DIR/experiment07_*_latest.pkl \
    --outFile="exp07_stats" \
    --aggregations=$AGGS_FILE

# Experiment 8
python checkpoint-printer.py \
    --files $CHECKPOINTS_DIR/experiment08_*_latest.pkl \
    --outFile="exp08_stats" \
    --aggregations=$AGGS_FILE

# Experiment 9
python checkpoint-printer.py \
    --files $CHECKPOINTS_DIR/experiment09_*_latest.pkl \
    --outFile="exp09_stats" \
    --aggregations=$AGGS_FILE