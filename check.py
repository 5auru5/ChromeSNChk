import csv
masterfile = input("Please enter the master file name: ")
mastercol = input("Please enter the column to check (as a number starting from 1): ")
mastercol -= 1
checkfile = input("Please input the cvs to be checked: ")
checkcol = input("Please enter the column to check (as a number starting from 1): ")
checkcol -= 1
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
