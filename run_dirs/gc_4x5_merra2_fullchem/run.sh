#!/bin/bash

#SBATCH --job-name=GC_sim
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --mem=32gb
#SBATCH --time=10:00:00

###############################################################################

# Source the environment file you have created for your system
source /projects/b56h/GC_scripts/GCClassic.env

# Set the proper # of threads for OpenMP
# SLURM_CPUS_PER_TASK ensures this matches the number you set with -c above
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

# Archive old log if it exists
if [ -f GC.log ]; then
    mv GC.log "GC.log.$(date +%Y%m%d_%H%M%S)"
fi

time -p ./gcclassic >> GC.log 2>&1

# Exit normally
exit 0 