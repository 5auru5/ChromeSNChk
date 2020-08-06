import csv
while True:  #input validation
    fileType = input("Please Select a File Type\n 1: CSV\n 2: TSV\n Selection: ")
    try:
        filetype = int(fileType)
    except:
        print("Please user numeric digits.")
        continue
    if int(fileType) > 2 or int(fileType) < 0:
        print("Please enter a valid number")
        continue
    else:
        break
fileType = int(fileType) ##cast file type to int
if fileType == 1: #assign extension based on file type
    extension = ".csv"
if fileType == 2:
    extension = ".tsv"
masterfile = input("Please enter the master file name: ") + extension
mastercol = int(input("Please enter the column to check (as a number starting from 1): ")) - 1
checkfile = input("Please input the csv to be checked: ") + extension
checkcol = int(input("Please enter the column to check (as a number starting from 1): ")) - 1
with open(masterfile, 'rb') as master:
    master_indices = dict((r[mastercol], i) for i, r in enumerate(csv.reader(master)))

with open(checkfile, 'rb') as check:
    with open('results.csv', 'wb') as results:
        reader = csv.reader(check)
        writer = csv.writer(results)

        writer.writerow(next(reader, []) + ['Compare Value'])

        for row in reader:
            index = master_indices.get(row[checkcol])
            if index is not None:
                message = 'True'
            else:
                message = 'False'
            writer.writerow(row + [message])
