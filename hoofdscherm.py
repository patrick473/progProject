# Import tkinter for Python 3.X or Python 2.X
try:
    from tkinter import *
except ImportError:
    from Tkinter import *

from csvHandler import *
from sys import exit
from createWidgets import *
from sendEmail import sendEmail
from random import randint

#statements en variabelen
gold='#ffd700'
blue='#0000FF'
white='#FFFFFF'
grey='#666666'
red='#FF0000'
black='#000000'

# Functions

# Close main window
def close():
    root.withdraw()
    exit()

# Return to main menu
def hoofdmenu():
    registrationFrame.grid_remove()
    confirmRegistrationFrame.grid_remove()
    loginFrame.grid_remove()
    jouwGegevensFrame.grid_remove()
    loggedInFrame.grid_remove()
    verificationFrame.grid_remove()
    mainFrame.grid(padx=30, pady=30)
    logOutButton.place_forget()

# Create home button
def placeLogOut():
    logOutButton.place(rely=1, relx=0, x=30, y=-30, anchor=SW)

# Open register frame
def register():
    placeLogOut()
    mainFrame.grid_remove()
    registrationFrame.grid(padx=30, pady=30)

# Confirm registration
def confirmRegistration():
    entries = [voornaamEntry, achternaamEntry, geboorteEntry,
               telefoonEntry, emailEntry, kleurEntry, wachtwoordEntry]
    gegevens = []
    for entry in entries:
        gegevens.append(entry.get())
        entry.delete(0,END)
    gebruikerToevoegen(gegevens)
    hoofdmenu()

# Check registration
def checkRegistration():

    entries = [voornaamEntry, achternaamEntry, geboorteEntry,
               telefoonEntry, emailEntry, kleurEntry, wachtwoordEntry]
    gegevens = []
    emptyField = False
    for entry in entries:
        gegevens.append(entry.get())
        if len(gegevens[entries.index(entry)]) == 0:
            emptyField = True
    if emptyField == False:
        registrationFrame.grid_remove()
        confirmRegistrationFrame.grid(padx=30, pady=30)
        # Gegevens labels
        kloptDitLabel = createLabel(confirmRegistrationFrame,
                                    'Kloppen deze gegevens?')
        voornaamLabel = createLabel(confirmRegistrationFrame, 'Voornaam:')
        achternaamLabel = createLabel(confirmRegistrationFrame, 'Achternaam:')
        geboorteLabel = createLabel(confirmRegistrationFrame,
                                    'Geboortedatum(DD/MM/YYYY):')
        telefoonLabel = createLabel(confirmRegistrationFrame, 'Telefoonnummer:')
        emailLabel = createLabel(confirmRegistrationFrame, 'E-mailadres:')
        kleurLabel = createLabel(confirmRegistrationFrame,'Kleur van je fiets:')
        passwordLabel = createLabel(confirmRegistrationFrame, 'Wachtwoord:')
        fietsnummerLabel = createLabel(confirmRegistrationFrame, 'Fietsnummer:')

        gegevensLabels = [kloptDitLabel,voornaamLabel,achternaamLabel,
                          geboorteLabel,telefoonLabel,emailLabel,kleurLabel,
                          passwordLabel, fietsnummerLabel]
        for index, label in enumerate(gegevensLabels):
            label.grid(row=index, column=0, pady=5)

        # Ingevoerde gegevens labels
        kloptDitLabel = createLabel(confirmRegistrationFrame, '')
        voornaamLabel = createLabel(confirmRegistrationFrame, gegevens[0])
        achternaamLabel = createLabel(confirmRegistrationFrame, gegevens[1])
        geboorteLabel = createLabel(confirmRegistrationFrame, gegevens[2])
        telefoonLabel = createLabel(confirmRegistrationFrame, gegevens[3])
        emailLabel = createLabel(confirmRegistrationFrame, gegevens[4])
        kleurLabel = createLabel(confirmRegistrationFrame, gegevens[5])
        passwordLabel = createLabel(confirmRegistrationFrame, gegevens[6])
        fietsnummerLabel = createLabel(confirmRegistrationFrame,
                                       len(csvLezen('fietsen.csv'))+1)

        gegevensLabels = [kloptDitLabel,voornaamLabel,achternaamLabel,
                          geboorteLabel,telefoonLabel,emailLabel,kleurLabel,
                          passwordLabel, fietsnummerLabel]
        for index, label in enumerate(gegevensLabels):
            label.grid(row=index, column=1, pady=5)

        # Buttons
        acceptRegistrationButton = createButton(confirmRegistrationFrame,
                                                'Deze gegevens kloppen',
                                                confirmRegistration)
        denyRegistrationButton = createButton(confirmRegistrationFrame,
                                              'Deze gegevens kloppen niet',
                                              registrationDeny)
        acceptRegistrationButton.grid(row=9, column=0, pady=5)
        denyRegistrationButton.grid(row=10, column=0, pady=5)

    else:
        confirmButton['text'] = 'Vul alle gegevens in'

def registrationDeny():
    placeLogOut()
    confirmRegistrationFrame.grid_remove()
    registrationFrame.grid(padx=30, pady=30)

def login():
    placeLogOut()
    mainFrame.grid_remove()
    loginFrame.grid(padx=30, pady=30)

def confirmLogin():
    global verificationCode
    entries = [fietsNummerLoginEntry, passwordLoginEntry]
    gegevens = []
    for entry in entries:
        gegevens.append(entry.get())
    loggedIn = checkLogin(gegevens[0],gegevens[1])
    if loggedIn == True:
        loginFrame.grid_remove()
        verificationFrame.grid(padx=30, pady=30)
        verificationCode = str(randint(0,999999)).zfill(6)
        sendEmail(jouwGegevensOphalen(gegevens[0])[4], verificationCode)
    else:
        wrongLoginLabel.grid(row=0, column=2, pady=5)

def verify():
    global verificationCode
    entries = [fietsNummerLoginEntry, passwordLoginEntry]
    gegevens = []
    for entry in entries:
        gegevens.append(entry.get())
    if verificationEntry.get() == verificationCode:
        verificationFrame.grid_remove()
        loggedInFrame.grid(padx=30, pady=30)
        if fietsGestald(gegevens[0]) == True:
            stallingButton.grid_remove()
            ophaalButton.grid(row=2,column=0, pady=5)
        else:
            ophaalButton.grid_remove()
            stallingButton.grid(row=2,column=0, pady=5)
    else:
        verificationFailedLabel.grid(row=0, column=1, pady=5)

def fietsStallen():
    fietsnummer = fietsNummerLoginEntry.get()
    fietsNummerStallen(jouwGegevensOphalen(fietsnummer))
    loggedInFrame.grid_remove()
    stalFrame.grid()
    logOutButton.place_forget()

def jouwGegevens():
    loggedInFrame.grid_remove()
    jouwGegevensFrame.grid(padx=30, pady=30)
    gegevens = jouwGegevensOphalen(fietsNummerLoginEntry.get())
    ########## Jouw gegevens widgets ##########
    # Gegevens labels
    voornaamLabel = createLabel(jouwGegevensFrame, 'Voornaam:')
    achternaamLabel = createLabel(jouwGegevensFrame, 'Achternaam:')
    geboorteLabel = createLabel(jouwGegevensFrame, 'Geboortedatum(DD/MM/YYYY):')
    telefoonLabel = createLabel(jouwGegevensFrame, 'Telefoonnummer:')
    emailLabel = createLabel(jouwGegevensFrame, 'E-mailadres:')
    kleurLabel = createLabel(jouwGegevensFrame, 'Kleur van je fiets:')
    passwordLabel = createLabel(jouwGegevensFrame, 'Wachtwoord:')
    fietsnummerLabel = createLabel(jouwGegevensFrame, 'Fietsnummer:')

    gegevensLabels = [voornaamLabel,achternaamLabel,geboorteLabel,telefoonLabel,
                      emailLabel,kleurLabel,passwordLabel,fietsnummerLabel]
    for index, label in enumerate(gegevensLabels):
        label.grid(row=index, column=0,pady=5)

    # Jouw gegevens labels
    jouwVoornaamLabel = createLabel(jouwGegevensFrame, gegevens[0])
    jouwAchternaamLabel = createLabel(jouwGegevensFrame, gegevens[1])
    jouwGeboortedatumLabel = createLabel(jouwGegevensFrame, gegevens[2])
    jouwTelefoonLabel = createLabel(jouwGegevensFrame, gegevens[3])
    jouwEmailLabel = createLabel(jouwGegevensFrame, gegevens[4])
    jouwKleurLabel = createLabel(jouwGegevensFrame, gegevens[5])
    jouwPasswordLabel = createLabel(jouwGegevensFrame, gegevens[6])
    jouwFietsnummerLabel = createLabel(jouwGegevensFrame, gegevens[7])

    jouwGegevensLabels = [jouwVoornaamLabel,jouwAchternaamLabel,
                          jouwGeboortedatumLabel,jouwTelefoonLabel,
                          jouwEmailLabel,jouwKleurLabel,jouwPasswordLabel,
                          jouwFietsnummerLabel]
    for index, label in enumerate(jouwGegevensLabels):
        label.grid(row=index, column=1,pady=5)

# Haalt fietsen uit het csv bestand
def fietsOphalen():
    fietsOphalenCSV(fietsNummerLoginEntry.get())
    loggedInFrame.grid_remove()
    ophaalFrame.grid()
    logOutButton.place_forget()

# Main window
root = Tk()
root.config(bg=gold)
root.overrideredirect(True)
root.geometry('{}x{}'.format(root.winfo_screenwidth(),
                             root.winfo_screenheight()))

########## Frames ##########

# Main window widgets frame
mainFrame = Frame(root, bg=gold)
mainFrame.grid(padx=30, pady=30)

# Registration window widgets frame
registrationFrame = Frame(root, bg=gold)
#stal frame window widgets frame
stalFrame = Frame(root,bg=gold)
#ophaal frame window widgets frame
ophaalFrame = Frame(root, bg=gold)
#confirm registration window widgets frame
confirmRegistrationFrame = Frame(root, bg=gold)
# Login window widgets frame
loginFrame = Frame(root, bg=gold)
# Logged in Frame
loggedInFrame = Frame(root, bg=gold)
# Jouw gegevens Frame
jouwGegevensFrame = Frame(root, bg=gold)
# Verification Frame
verificationFrame = Frame(root, bg=gold)

########## Main window widgets ##########
registrationButton = createButton(mainFrame, 'Registreren', register)
loginButton = createButton(mainFrame, 'Inloggen', login)

registrationButton.grid(row=0,column=0, pady=5)
loginButton.grid(row=1,column=0, pady=5)

# Exit button
exitButton = createButton(root, 'Afsluiten', close, 'red')
exitButton.place(rely=1, relx=1, x=-30, y=-30, anchor=SE)

# Home button
logOutButton = createButton(root, 'Uitloggen', hoofdmenu)

########## Login widgets ##########

# Login labels
fietsNummerLabel = createLabel(loginFrame, 'Fietsnummer:')
passwordLabel = createLabel(loginFrame, 'Wachtwoord:')
wrongLoginLabel = createLabel(loginFrame, 'Dit is geen juiste combinatie '
                              'van fietsnummer en wachtwoord')

fietsNummerLabel.grid(row=0, column=0, pady=5)
passwordLabel.grid(row=1, column=0, pady=5)

# Login entries
fietsNummerLoginEntry = createEntry(loginFrame)
passwordLoginEntry = createEntry(loginFrame, '*')

fietsNummerLoginEntry.grid(row=0, column=1, pady=5)
passwordLoginEntry.grid(row=1, column=1, pady=5)

# Confirm button
confirmLoginButton = createButton(loginFrame, 'Inloggen', confirmLogin)
confirmLoginButton.grid(row=2, column=1, pady=5)

########## Verification widgets ##########
verificationLabel = createLabel(verificationFrame, 'Verificatiecode:')
verificationEntry = createEntry(verificationFrame)
verificationButton = createButton(verificationFrame, 'Verifiëren', verify)
verificationFailedLabel = createLabel(verificationFrame,
                                      'Deze verificatiecode is onjuist')
verificationLabel.grid(row=0, column=0, pady=5)
verificationEntry.grid(row=0, column=1, pady=5)
verificationButton.grid(row=1, column=1, pady=5)

########## Logged in widgets ##########
stallingButton = createButton(loggedInFrame, 'Fiets stallen', fietsStallen)
ophaalButton = createButton(loggedInFrame, 'Fiets ophalen', fietsOphalen)
infoButton =  createButton(loggedInFrame, 'Jouw gegevens', jouwGegevens)

infoButton.grid(row=1,column=0,pady=5)

########## Registration widgets ##########
# Registration Labels
registrationLabels = ['Voornaam:','Achternaam:','Geboortedatum (DD/MM/YYY)',
                      'Telefoonnummer:','E-mailadres:','Kleur van je fiets:',
                      'Wachtwoord:']
for index, text in enumerate(registrationLabels):
    registrationLabel = createLabel(registrationFrame, text)
    registrationLabel.grid(row=index, column=0, pady=5)

# Registration Entries
voornaamEntry = createEntry(registrationFrame)
achternaamEntry = createEntry(registrationFrame)
geboorteEntry = createEntry(registrationFrame)
telefoonEntry = createEntry(registrationFrame)
emailEntry = createEntry(registrationFrame)
kleurEntry = createEntry(registrationFrame)
wachtwoordEntry = createEntry(registrationFrame, '*')

registrationEntries = [voornaamEntry,achternaamEntry,geboorteEntry,
                       telefoonEntry,emailEntry,kleurEntry,wachtwoordEntry]
for index, entry in enumerate(registrationEntries):
    entry.grid(row=index, column=1, pady=5)

# Confirm button
confirmButton = createButton(registrationFrame, 'Bevestigen', checkRegistration)
confirmButton.grid(row=99,column=1,pady=5)

# confirm label stallen
stalConfirmLabel = createLabel(stalFrame,'Je fiets wordt nu gestald.\n\
Sluit het programma af.')
stalConfirmLabel.grid(row=5, column=0, pady=30,padx=30)

# confirm label ophalen
ophaalConfirmLabel = createLabel(ophaalFrame, 'Je fiets wordt nu opgehaald.\n\
Sluit het programma af.')
ophaalConfirmLabel.grid(row=5, column=0, pady=30,padx=30)

# Main loop
root.mainloop()
