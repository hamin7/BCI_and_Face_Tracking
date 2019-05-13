import argparse, csv, sys
from settings import *

# command arguments
parse = argparse.ArgumentPareser(description='csv to postgres', \
fromfile_prefix_chars="@" )
parser.add_argument('file', help='csv file to import', action='store')
args = parser.parse_args()
csv_file = args.file

# open csv file
with open(30Hz_EMO_1 3 8 9 10 12_seq_30_epoch_20_stack_4_hidden_1024_ori.csv, 'rb') as csvfile:

    # get number of columns
    for line in csvfile.readlines():
        array = line.split(',')
        first_item = array[0]

    num_columns = len(array)
    csvfile.seek(0)

    reader = csv.reader(csvfile, delimiter=' ')
        included_cols = [1, 2, 6, 7]

    for row in reader:
        content = list(row[i] for i in included_cols)
        print content
