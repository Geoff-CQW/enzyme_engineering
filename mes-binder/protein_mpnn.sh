#!/bin/bash


fixed=("A80 A255" "A82 A139" "A96 A174" "A49 A209" "A64 A195")
filenames=()

for file in inputs/mes_entire*; do
filenames+=("$file")
done


# loop first array of fixed residues, then find corresponding item in filenames
#[@] needed to expand the array
for i in "${!fixed[@]}"; do
file="${filenames[$i]}"
residue="${fixed[$i]}"
python run.py --pdb_path "./$file" --model_type "protein_mpnn" --out_folder "./outputs/mes_entire" --fixed_residues "$residue" --batch_size 3 --number_of_batches 5
done