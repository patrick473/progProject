import csv

def gebruikerToevoegen(invoer):
    try:
        rows = []
        with open('fietsen.csv', 'r', newline = '') as myCSVFile:
            reader = csv.reader(myCSVFile, delimiter = ';')
            for row in reader:
                rows.append(row)
    except FileNotFoundError:
        pass
    nummer = len(rows) + 1
    gegevens = invoer
    gegevens.append(nummer)
    rows.append(gegevens)
    with open('fietsen.csv', 'w', newline = '') as myCSVFile:
        writer = csv.writer(myCSVFile, delimiter = ';')
        for row in rows:
              writer.writerow((row[0], row[1], row[2], row[3], row[4], row[5],
                               row[6], row[7]))

def checkLogin(fietsNummer, password):
    try:
        rows = []
        with open('fietsen.csv', 'r', newline = '') as myCSVFile:
            reader = csv.reader(myCSVFile, delimiter = ';')
            for row in reader:
                rows.append(row)
    except FileNotFoundError:
        return False
    for row in rows:
        if row[6] == password and row[7] == fietsNummer:
            return True
        else:
            return False

def checkLogin(fietsNummer, password):
    try:
        rows = []
        with open('fietsen.csv', 'r', newline = '') as myCSVFile:
            reader = csv.reader(myCSVFile, delimiter = ';')
            for row in reader:
                rows.append(row)
    except FileNotFoundError:
        return False
    for row in rows:
        print(row[6], row[7])
        if row[6] == password and row[7] == fietsNummer:
            return True
        else:
            return False
