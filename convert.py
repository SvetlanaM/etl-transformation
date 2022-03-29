import csv
import glob
import requests
import unicodedata

manager_names = []
new_list = []
new_header = []
item1 = ""

def remove_accents(managerName):
    nfkd_form = unicodedata.normalize('NFC', unicode(managerName, "utf-8"))
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii

with open("managers.csv", "r") as infile:
    reader = csv.reader(infile)

    count = 0
    for index_row, data_in_row in enumerate(reader):
        for index_col, data_in_cell in enumerate(data_in_row):
            continue
        manager_names.append(data_in_row[2])
    new_list = list(set(manager_names))
    infile.close()

    for item in new_list:
        item1 = item.replace(" ", "")
        item1 = item1.replace("(", "")
        item1 = item1.replace(")", "")
        item1 = remove_accents(item1)
        with open(item1 + "_out.csv", "w") as outfile:
            writer = csv.writer(outfile)
            writer.writerow(new_header)
            with open("managers.csv", "r") as infile:

                reader = csv.reader(infile)
                new_header = next(reader, None)
                for index_row, data_in_row in enumerate(reader):
                    for index_col, data_in_cell in enumerate(data_in_row):

                        if data_in_cell == item:
                            writer.writerow(data_in_row)

listOfFiles = glob.glob("*.csv")
for fileName in listOfFiles:
    count = 0
    final_count = len(listOfFiles)
    for index, fileInList in enumerate(listOfFiles):
        with open(fileInList, 'rb') as f:
            files = {'data': open(fileInList, 'rb')}
            resp = requests.post(env.URL,
                             data = {"name" : "test" + str(fileInList[:-4])},
                             files = files,
                             headers={'X-StorageApi-Token':env.API}
                             )
            count += 1

    if count == final_count:
        break
