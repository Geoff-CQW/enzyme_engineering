import argparse
import glob, os

# get arguments
parser = argparse.ArgumentParser(description="Takes ligand mpnn fasta file(s) and sort according to category from user")
parser.add_argument("-f", "--path", type=str, required=True, help="path to fasta files to be sorted, can be directory or single file. For directory, use wild card for filetype e.g: c:/path/*.fa")
parser.add_argument("-s", "--sort_by", type=str, required=False, default="overall_confidence", help="Score to sort by. Default: overall_confidence")
# parser.add_argument("-v", "--verbose", action="store_true", help="Print verbose output.")
#
args = parser.parse_args()

# to get the arguments as variables, access it directly
file_path = args.path
sort_by = args.sort_by

# get files as list
files = glob.glob(file_path)

### functions for reading, sorting and writing###
def read_and_sort_fasta(file_path, output_filename, sort_by='overall_confidence'):

    '''reads provided ligand/protein mpnn fasta file and returns a list of dictionaries sorted by desired score '''

    results = []

    with open(file_path, 'r') as f:
        for line in f:
            header = line
            seq = next(f, None)
            if 'model_path' in header.split(', ')[-1].split('='):
                read_mpnn_fa(header, seq, output_filename)
            else:
                results.append(read_mpnn_fa(header, seq, output_filename))

    return sorted(results, key = lambda d: d[sort_by], reverse=True)
 
def read_mpnn_fa(header, sequence, output_filename):
    ''' reads ligand/protein mpnn fasta file and returns dictionary of with scores as key : value pair and sequence '''

    # error checking
    if not header:
        print('error, empty header')
        return
    
    if not sequence:
        print('error, empty sequence')
        return
    
    info_dict = {}

    header_list = header.rstrip().split(', ')

    # check for template sequence that's always at the top of ligand mpnn fasta and write it to the file
    if 'model_path' in header_list[-1].split('='):
        print('input seq')
        file = open(output_filename, 'w+')
        file.writelines([header, sequence])
        file.close()
        return
    
    info_dict['seq_name'] = (header_list[0][1:])
    info_dict['id'] = int(header_list[1].split('=')[1])
    info_dict['temp'] = (header_list[2].split('=')[1])
    info_dict['overall_confidence'] = float(header_list[4].split('=')[1])
    info_dict['ligand_confidence'] = float(header_list[5].split('=')[1])
    info_dict['seq_rec'] = float(header_list[6].split('=')[1])
    info_dict['sequence'] = sequence.rstrip()

    return info_dict

def write_fasta(sorted_list, output_filename):

    ''' go through sorted list and write to file in fasta format '''
    outputs = []

    for seq_dict in sorted_list:
        seq_keys = list(seq_dict.keys())
        out_header = "" 
        out_seq = ''

        # write seq. name
        out_header += ">" + seq_dict['seq_name']
        out_seq = seq_dict['sequence'] + '\n'
        for key in seq_keys[1:-1]:
            out_header += ', ' + key + '=' + str(seq_dict[key])

        out_header += '\n'

        outputs.append(out_header)
        outputs.append(out_seq)
    
    file1 = open(output_filename, 'a+')
    file1.writelines(outputs)
    file1.close()


### loop files and sort ###

for file in files:
    output_filename = os.path.basename(file).rsplit(',', 1)[0] + '_sorted'

    '''to do'''
