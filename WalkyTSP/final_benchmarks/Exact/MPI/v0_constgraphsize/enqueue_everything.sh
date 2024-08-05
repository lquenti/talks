for file in ./slurm_*.sh; do
  echo "$file"
  sbatch $file
  sleep 25
done

