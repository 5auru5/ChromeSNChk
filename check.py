import csv
masterfile = input("Please enter the master file name: ")
checkfile = input("Please input the cvs to be checked: ")
with open(masterfile, 'rb') as master:
    master_indices = dict((r[0], i) for i, r in enumerate(csv.reader(master)))

with open(checkfile, 'rb') as hosts:
    with open('results.csv', 'wb') as results:
        reader = csv.reader(hosts)
        writer = csv.writer(results)

        writer.writerow(next(reader, []) + ['RESULTS'])

        for row in reader:
            index = master_indices.get(row[0])
            if index is not None:
                message = 'True'
            else:
                message = 'False'
            writer.writerow(row + [message])
