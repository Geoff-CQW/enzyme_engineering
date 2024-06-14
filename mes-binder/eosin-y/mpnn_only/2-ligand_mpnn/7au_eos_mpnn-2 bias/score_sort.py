import argparse

import argparse

parser = argparse.ArgumentParser(description="Takes ligand mpnn fasta file(s) and sort according to category from user")
parser.add_argument("-f", "--filepath", type=str, required=True, help="path to files to be sorted")
parser.add_argument("-s", "--sort_by", type=str, required=False, help="Score to sort by. Default: overall_confidence")
parser.add_argument("-v", "--verbose", action="store_true", help="Print verbose output.")

args = parser.parse_args()

# to get the arguments as variables, access it directly
sort_by = args.sort_by
path = args.filepath

print(sort_by, path)
