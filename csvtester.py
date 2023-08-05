import csv
from docutils.utils import column_indices
with open ("times.csv", "r") as file:
    csvreader = csv.reader(file)

    next (csvreader)

    for column in csvreader:
        if "NA" in column[5]:
            print("America Spotted")
