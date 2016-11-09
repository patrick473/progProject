import csv
import time

def fietsOphalenCSV(fietsnummer):
    try:
        rows=[]
        with open('Stalling.csv', 'r', newline = '') as myCSVFile:
            file = csv.reader(myCSVFile, delimiter = ';')
            for row in file:
                rows.append(row)
    except FileNotFoundError:
        pass
    with open('Stalling.csv', 'w', newline='') as myCSVFile:
        writer = csv.writer(myCSVFile, delimiter=';')
        for row in rows:
            if row[0] != fietsnummer:
                writer.writerow(row)
                
def fietsNummerStallen(invoer):
    naam = 'LUL'
    dateTime = time.strftime('%c')
    Data = [invoer,naam,dateTime]
    try:
        with open('Stalling.csv', 'a', newline = '') as myCSVFile:
            file = csv.writer(myCSVFile, delimiter = ';')
            file.writerow(Data)
    except FileNotFoundError:
        return False
    
def fietsStallenCSV(gegevens):
    fietsnummer = gegevens[-1]
    naam = gegevens[0], gegevens[1]
    tijd = time.strftime('%d/%m/%Y at %H:%M:%S')
    try:
        with open('Stalling.csv', 'a', newline = '') as myCSVFile:
            writer = csv.writer(myCSVFile, delimiter = ';')
            writer.writerow([fietsnummer, naam, tijd])
    except FileNotFoundError:
        pass

def fietsGestald(fietsnummer):
    try:
        with open('Stalling.csv', 'r', newline='') as myCSVFile:
            reader = csv.reader(myCSVFile, delimiter=';')
            for row in reader:
                if row[0] == fietsnummer:
                    return True
            return False
    except FileNotFoundError:
        return False

def gebruikersLezen():
    try:
        rows = []
        with open('fietsen.csv', 'r', newline = '') as myCSVFile:
            reader = csv.reader(myCSVFile, delimiter = ';')
            for row in reader:
                rows.append(row)
    except FileNotFoundError:
        pass
    return rows

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
            writer.writerow(row)

def checkLogin(fietsnummer, password):
    try:
        rows = []
        with open('fietsen.csv', 'r', newline = '') as myCSVFile:
            reader = csv.reader(myCSVFile, delimiter = ';')
            for row in reader:
                rows.append(row)
    except FileNotFoundError:
        return False
    for row in rows:
        if row[6] == password and row[7] == fietsnummer:
            return True
    return False

def jouwGegevensOphalen(fietsnummer):
    rows = gebruikersLezen()
    for row in rows:
        if row[7] == fietsnummer:
            return row
