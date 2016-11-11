import csv
import time
from random import randint
def fietsOphalenCSV(fietsnummer):
    rows = csvLezen('Stalling.csv')
    with open('Stalling.csv', 'w', newline='') as myCSVFile:
        writer = csv.writer(myCSVFile, delimiter=';')
        for row in rows:
            if row[0] != fietsnummer:
                writer.writerow(row)

def fietsNummerStallen(invoer):
    fietsnummer = invoer[-1]
    naam = invoer[0] + ' ' + invoer[1]
    dateTime = time.strftime('%d/%m/%Y at %H:%M:%S')
    try:
        with open('Stalling.csv', 'a', newline = '') as myCSVFile:
            file = csv.writer(myCSVFile, delimiter = ';')
            file.writerow([fietsnummer, naam, dateTime])
    except FileNotFoundError:
        return False

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

def csvLezen(csvfile):
    try:
        rows = []
        with open(csvfile, 'r', newline = '') as myCSVFile:
            reader = csv.reader(myCSVFile, delimiter = ';')
            for row in reader:
                rows.append(row)
    except FileNotFoundError:
        pass
    return rows

def gebruikerToevoegen(invoer):
    rows = csvLezen('fietsen.csv')
    nummer = len(rows) + 1
    gegevens = invoer
    gegevens.append(nummer)
    rows.append(gegevens)
    with open('fietsen.csv', 'w', newline = '') as myCSVFile:
        writer = csv.writer(myCSVFile, delimiter = ';')
        for row in rows:
            writer.writerow(row)

def checkLogin(fietsnummer, password):
    rows = csvLezen('fietsen.csv')
    if rows == []:
        return False
    for row in rows:
        if row[6] == password and row[7] == fietsnummer:
            return True
    return False

def jouwGegevensOphalen(fietsnummer):
    rows = csvLezen('fietsen.csv')
    for row in rows:
        if row[7] == fietsnummer:
            return row
