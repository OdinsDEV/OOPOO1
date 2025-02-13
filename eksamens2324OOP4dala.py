import csv
   
    #1. uzdevums
with open('agenti.csv', newline='',encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in spamreader:
        if (row[0] == "Izglītības iestāde") or (row[0] == "Valsts iestāde"):
            print(', '.join(row))
    csvfile.close()
print("###################################################")

    #2. uzdevums
with open('agenti.csv', newline='',encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in spamreader:
        if ("Rīga," in row[2]):
            print(', '.join(row))
    csvfile.close()        
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

    # 3.uzdevums
csvdata = []
with open('agenti.csv', newline='', encoding='utf-8') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';', quotechar='|')        
    for line in readCSV:
        csvdata.append(line)
    csvdata.sort(key=lambda rinda: rinda[1].lower())
    for line in csvdata:
        print(', '.join(line))
