# Import tkinter for Python 3.X or Python 2.X
try:
    from tkinter import *
except ImportError:
    from Tkinter import *

from csvwriter import *
from sys import exit

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
    global returnButton
    registrationFrame.grid_remove()
    confirmRegistrationFrame.grid_remove()
    loginFrame.grid_remove()
    jouwGegevensFrame.grid_remove()
    loggedInFrame.grid_remove()
    mainFrame.grid(padx=30, pady=30)
    returnButton.place_forget()

# Create home button
def homebutton():
    global returnButton
    returnButton = Button(master=root,
                          text='Hoofdmenu',
                          height=3,
                          width=30,
                          bg=blue,
                          fg=white,
                          command=hoofdmenu)
    returnButton.place(rely=1, relx=0, x=30, y=-30, anchor=SW)

# Open register frame
def register():
    homebutton()
    mainFrame.grid_remove()
    registrationFrame.grid(padx=30, pady=30)

# Confirm registration
def confirmRegistration():
    entries = [voornaamEntry, achternaamEntry, geboortedatumEntry,
               telefoonEntry, emailEntry, kleurEntry, wachtwoordEntry]
    gegevens = []
    for entry in entries:
        gegevens.append(entry.get())
        if len(gegevens[entries.index(entry)]) == 0:
            emptyField = True
        entry.delete(0,END)
    gebruikerToevoegen(gegevens)
    hoofdmenu()

# Confirm registration
def checkRegistration():
    global acceptRegistrationButton
    global denyRegistrationButton
    global confirmLabel
    entries = [voornaamEntry, achternaamEntry, geboortedatumEntry,
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
        
        confirmLabelText = Label(master=confirmRegistrationFrame,
                             text=('Kloppen deze Gegevens?\nNaam:\n'+
                             'Geboortedatum:\nTelefoonnummer:\nEmailadres:\n'+
                             'Kleur van je fiets:\nWachtwoord:\n\n'+
                             'Je fietsnummer is:'),
                             background = gold,
                             width=30,
                             foreground = black,
                             anchor=W,
                             justify=LEFT)
        confirmLabelText.grid(row=0, column=0, pady=5)
        confirmLabelVariables = Label(master=confirmRegistrationFrame,
                             text=('\n{} {}\n{}\n{}\n{}\n{}\n{}\n\n{}'
                                   .format(gegevens[0],gegevens[1],gegevens[2],
                                           gegevens[3],gegevens[4],gegevens[5],
                                           gegevens[6],len(csvLezen('fietsen.csv'))+1)),
                             background = gold,
                             width=30,
                             foreground = black,
                             anchor=W,
                             justify=LEFT)
        confirmLabelVariables.grid(row=0, column=1, pady=5)
        acceptRegistrationButton = Button(master=confirmRegistrationFrame,
                      text='Deze gegegevens kloppen.',
                      height=3,
                      width=30,
                      bg=blue,
                      fg=white,
                      command=confirmRegistration)
        acceptRegistrationButton.grid(row=1, column=0, pady=5)
        
        denyRegistrationButton = Button(confirmRegistrationFrame,
                      text='Deze gegevens Kloppen niet.',
                      height=3,
                      width=30,
                      bg=blue,
                      fg=white,
                      command=registrationDeny)
        denyRegistrationButton.grid(row=2, column=0, pady=5)

    else:
        confirmButton['text'] = 'Vul alle gegevens in'
        
def registrationDeny():
    
    homebutton()
    confirmRegistrationFrame.grid_remove()
    registrationFrame.grid(padx=30, pady=30)
    
def login():
    homebutton()
    mainFrame.grid_remove()
    loginFrame.grid(padx=30, pady=30)

def confirmLogin():
    entries = [fietsNummerLoginEntry, passwordLoginEntry]
    gegevens = []
    for entry in entries:
        gegevens.append(entry.get())
    loggedIn = checkLogin(gegevens[0],gegevens[1])
    if loggedIn == True:
        loginFrame.grid_remove()
        loggedInFrame.grid(padx=30, pady=30)
        if fietsGestald(gegevens[0]) == True:
            stallingButton.grid_remove()
            ophaalButton.grid(row=2,column=0, pady=5)
        else:
            ophaalButton.grid_remove()
            stallingButton.grid(row=2,column=0, pady=5)
    else:
        wrongLoginLabel.grid(row=0, column=2, pady=5)

def fietsStallen():
    fietsnummer = fietsNummerLoginEntry.get()
    fietsNummerStallen(jouwGegevensOphalen(fietsnummer))
    hoofdmenu()

def jouwGegevens():
    loggedInFrame.grid_remove()
    jouwGegevensFrame.grid(padx=30, pady=30)
        ########## Jouw gegevens widgets ##########

    # Voornaam label
    voornaamLabel = Label(master=jouwGegevensFrame,
                          text='Voornaam:',
                          anchor=W,
                          width=30,
                          bg=gold)
    voornaamLabel.grid(row=0, column=0, pady=5)

    # Achternaam Label
    achternaamLabel = Label(master=jouwGegevensFrame,
                            text='Achternaam:',
                            anchor=W,
                            width=30,
                            bg=gold)
    achternaamLabel.grid(row=1, column=0, pady=5)

    # Geboortedatum label
    geboortedatumLabel = Label(master=jouwGegevensFrame,
                               text='Geboortedatum (DD/MM/YYYY):',
                               anchor=W,
                               width=30,
                               bg=gold)
    geboortedatumLabel.grid(row=2, column=0, pady=5)

    # Telefoonnummer label
    telefoonLabel = Label(master=jouwGegevensFrame,
                          text='Telefoonnummer:',
                          anchor=W,
                          width=30,
                          bg=gold)
    telefoonLabel.grid(row=3, column=0, pady=5)

    # E-mailadres label
    emailLabel = Label(master=jouwGegevensFrame,
                       text='E-mailadres:',
                       anchor=W,
                       width=30,
                       bg=gold)
    emailLabel.grid(row=4, column=0, pady=5)

    # Kleur van fiets label
    kleurLabel = Label(master=jouwGegevensFrame,
                       text='Kleur van je fiets:',
                       anchor=W,
                       width=30,
                       bg=gold)
    kleurLabel.grid(row=5, column=0, pady=5)

    # Wachtwoord
    passwordLabel = Label(master=jouwGegevensFrame,
                          text='Wachtwoord:',
                          anchor=W,
                          width=30,
                          bg=gold)
    passwordLabel.grid(row=6, column=0, pady=5)

    # Jouw voornaam label
    jouwVoornaamLabel = Label(master=jouwGegevensFrame,
                              text=
                              jouwGegevensOphalen(fietsNummerLoginEntry.get())[0],
                              anchor=W,
                              width=30,
                              bg=gold)
    jouwVoornaamLabel.grid(row=0, column=1, pady=5)

    # Jouw achternaam Label
    jouwAchternaamLabel = Label(master=jouwGegevensFrame,
                                text=
                              jouwGegevensOphalen(fietsNummerLoginEntry.get())[1],
                                anchor=W,
                                width=30,
                                bg=gold)
    jouwAchternaamLabel.grid(row=1, column=1, pady=5)

    # Jouw geboortedatum label
    jouwGeboortedatumLabel = Label(master=jouwGegevensFrame,
                                   text=
                              jouwGegevensOphalen(fietsNummerLoginEntry.get())[2],
                                   anchor=W,
                                   width=30,
                                   bg=gold)
    jouwGeboortedatumLabel.grid(row=2, column=1, pady=5)

    # Jouw telefoonnummer label
    jouwTelefoonLabel = Label(master=jouwGegevensFrame,
                              text=
                              jouwGegevensOphalen(fietsNummerLoginEntry.get())[3],
                              anchor=W,
                              width=30,
                              bg=gold)
    jouwTelefoonLabel.grid(row=3, column=1, pady=5)

    # Jouw e-mailadres label
    jouwEmailLabel = Label(master=jouwGegevensFrame,
                           text=
                              jouwGegevensOphalen(fietsNummerLoginEntry.get())[4],
                           anchor=W,
                           width=30,
                           bg=gold)
    jouwEmailLabel.grid(row=4, column=1, pady=5)

    # Jouw kleur van fiets label
    jouwKleurLabel = Label(master=jouwGegevensFrame,
                           text=
                              jouwGegevensOphalen(fietsNummerLoginEntry.get())[5],
                           anchor=W,
                           width=30,
                           bg=gold)
    jouwKleurLabel.grid(row=5, column=1, pady=5)

    # Jouw wachtwoord label
    jouwPasswordLabel = Label(master=jouwGegevensFrame,
                              text=
                              jouwGegevensOphalen(fietsNummerLoginEntry.get())[6],
                              anchor=W,
                              width=30,
                              bg=gold)
    jouwPasswordLabel.grid(row=6, column=1, pady=5)

# Haalt fietsen uit het csv bestand
def fietsOphalen():
    fietsOphalenCSV(fietsNummerLoginEntry.get())
    hoofdmenu()

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

#confirm registration window widgets frame
confirmRegistrationFrame = Frame(root, bg=gold)

# Login window widgets frame
loginFrame = Frame(root, bg=gold)

# Logged in Frame
loggedInFrame = Frame(root, bg=gold)

# Jouw gegevens Frame
jouwGegevensFrame = Frame(root, bg=gold)
########## Main window widgets ##########

# Registration button
registrationButton = Button(master=mainFrame,
                            text='Registreer je fiets.',
                            height=3,
                            width=30,
                            bg=blue,
                            fg=white,
                            command=register)
registrationButton.grid(row=0,column=0, pady=5)

# Log in button
loginButton = Button(master=mainFrame,
                       text='Inloggen.',
                       command=login,
                       height=3,
                       width=30,
                       bg=blue,
                       fg=white)
loginButton.grid(row=1,column=0, pady=5)

# Exit button
exitButton = Button(master=root,
                    text='Afsluiten',
                    height=3,
                    width=30,
                    bg=red,
                    fg=white,
                    command=close)
exitButton.place(rely=1, relx=1, x=-30, y=-30, anchor=SE)

########## Login widgets ##########

# Fietsnummer label
fietsNummerLabel = Label(master=loginFrame,
                         text='Fietsnummer:',
                         anchor=W,
                         width=20,
                         bg=gold)
fietsNummerLabel.grid(row=0, column=0, pady=5)

# Password label
passwordLabel = Label(master=loginFrame,
                      text='Wachtwoord:',
                      anchor=W,
                      width=20,
                      bg=gold)
passwordLabel.grid(row=1, column=0, pady=5)

wrongLoginLabel = Label(master=loginFrame,
                        text='Dit is geen juiste combinatie '
                             'van fietsnummer en wachtwoord.',
                        anchor=W,
                        bg=gold)
# Fietsnummer entry
fietsNummerLoginEntry = Entry(master=loginFrame,
                         width=30)
fietsNummerLoginEntry.grid(row=0, column=1, pady=5)

# Password entry
passwordLoginEntry = Entry(master=loginFrame,
                      width=30)
passwordLoginEntry.grid(row=1, column=1, pady=5)

confirmLoginButton = Button(master=loginFrame,
                            text='Inloggen',
                            height=3,
                            width=30,
                            bg=blue,
                            fg=white,
                            command=confirmLogin)
confirmLoginButton.grid(row=2, column=1, pady=5)

########## Logged in widgets ##########
# Stalling button
stallingButton = Button(master=loggedInFrame,
                       text='Fiets stallen',
                       command=fietsStallen,
                       height=3,
                       width=30,
                       bg=blue,
                       fg=white)

# Ophaal button
ophaalButton = Button(master=loggedInFrame,
                      text='Fiets ophalen',
                      height=3,
                      width=30,
                      bg=blue,
                      fg=white,
                      command=fietsOphalen)

# Info button
infoButton = Button(master=loggedInFrame,
                    text='Jouw gegevens',
                    height=3,
                    width=30,
                    background=blue,
                    foreground=white,
                    command=jouwGegevens)
infoButton.grid(row=1,column=0,pady=5)

########## Registration widgets ##########

# Voornaam label
voornaamLabel = Label(master=registrationFrame,
                      text='Voornaam:',
                      anchor=W,
                      width=30,
                      bg=gold)
voornaamLabel.grid(row=0, column=0, pady=5)

# Achternaam Label
achternaamLabel = Label(master=registrationFrame,
                        text='Achternaam:',
                        anchor=W,
                        width=30,
                        bg=gold)
achternaamLabel.grid(row=1, column=0, pady=5)

# Geboortedatum label
geboortedatumLabel = Label(master=registrationFrame,
                           text='Geboortedatum (DD/MM/YYYY):',
                           anchor=W,
                           width=30,
                           bg=gold)
geboortedatumLabel.grid(row=2, column=0, pady=5)

# Telefoonnummer label
telefoonLabel = Label(master=registrationFrame,
                      text='Telefoonnummer:',
                      anchor=W,
                      width=30,
                      bg=gold)
telefoonLabel.grid(row=3, column=0, pady=5)

# E-mailadres label
emailLabel = Label(master=registrationFrame,
                   text='E-mailadres:',
                   anchor=W,
                   width=30,
                   bg=gold)
emailLabel.grid(row=4, column=0, pady=5)

# Kleur van fiets label
kleurLabel = Label(master=registrationFrame,
                   text='Kleur van je fiets:',
                   anchor=W,
                   width=30,
                   bg=gold)
kleurLabel.grid(row=5, column=0, pady=5)

# Wachtwoord
passwordLabel = Label(master=registrationFrame,
                      text='Wachtwoord:',
                      anchor=W,
                      width=30,
                      bg=gold)
passwordLabel.grid(row=6, column=0, pady=5)

# Voornaam entry
voornaamEntry = Entry(master=registrationFrame,
                      width=30)
voornaamEntry.grid(row=0, column=1, pady=5)

# Achternaam entry
achternaamEntry = Entry(master=registrationFrame,
                        width=30)
achternaamEntry.grid(row=1, column=1, pady=5)

# Geboortedatum entry
geboortedatumEntry = Entry(master=registrationFrame,
                           width=30)
geboortedatumEntry.grid(row=2, column=1, pady=5)

# Telefoonnummer entry
telefoonEntry = Entry(master=registrationFrame,
                      width=30)
telefoonEntry.grid(row=3, column=1, pady=5)

# E-mailadres entry
emailEntry = Entry(master=registrationFrame,
                   width=30)
emailEntry.grid(row=4, column=1, pady=5)

# Kleur fiets entry
kleurEntry = Entry(master=registrationFrame,
                   width=30)
kleurEntry.grid(row=5, column=1, pady=5)

# Wachtwoord entry
wachtwoordEntry = Entry(master=registrationFrame,
                        width=30)
wachtwoordEntry.grid(row=6, column=1, pady=5)

# Confirm button
confirmButton = Button(master=registrationFrame,
                      text='Bevestigen',
                      height=3,
                      width=30,
                      background=blue,
                      foreground=white,
                      command=checkRegistration)
confirmButton.grid(row=99,column=1,pady=5)

# Main loop
root.mainloop()
