#!/bin/sh
#
#SBATCH --verbose
#SBATCH --job-name=lunarLander
#SBATCH --output=slurm_%j.out
#SBATCH --error=slurm_%j.err
#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --mem=1GB

/bin/hostname
/bin/pwd

#module load python3/intel/3.6.3

eval "$(pyenv init -)"
pyenv activate lunarlander

# Where results are going to be written
OUTDIR=/scratch/od356/me_100k

for n in {1..20}
do
    python lunarlandercolab.py \
           --search-type ME \
           --num-individuals 100000 \
           --checkpoint-dir $OUTDIR \
           --checkpoint-enabled
done
