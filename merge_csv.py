
# Script to merge several CSVs into one

import glob
csvs = glob.glob('*.csv')

f = open('merged_data.csv', 'wb')
master_csv = csv.writer(f)

# Take the header of the first CSV and make it the master header
current_csv = open(csvs[0], 'rb')
headers = current_csv.readline().strip().split(';')
master_csv.writerow(headers)
# Write remaining rows
for line in current_csv:
    master_csv.writerow(line.strip())

# Read reminaing CSVs andskip the first row
for csv in csvs[1:]:
    for line_num, line in enumerate(csv):
        if line_num > 0:
            master_csv.writerow(line.strip().split(';'))