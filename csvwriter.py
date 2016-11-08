def fietsToevoegen(invoer):
    import csv
    try:
        rows = []
        with open('fietsen.csv', 'r', newline = '') as myCSVFile:
            reader = csv.reader(myCSVFile, delimiter = ';')
            for row in reader:
                rows.append(row)
    except FileNotFoundError:
        pass
    nummer = len(rows) + 1
    print(nummer)
    gegevens = invoer
    gegevens.append(nummer)
    print(gegevens)
    rows.append(gegevens)
    with open('fietsen.csv', 'w', newline = '') as myCSVFile:
        writer = csv.writer(myCSVFile, delimiter = ';')
        for row in rows:
              writer.writerow((row[0], row[1], row[2], row[3], row[4], row[5],
                               row[6]))
              
