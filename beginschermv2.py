# Import tkinter for Python 3.X or Python 2.X
try:
    from tkinter import *
except ImportError:
    from Tkinter import *

from csvwriter import fietsToevoegen
#statements en variabelen
helpDisplayed = False
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

# Return to main menu
def hoofdmenu():
    global returnButton
    registrationFrame.grid_remove()
    fietsStallenFrame.grid_remove()
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
    voornaam = voornaamEntry.get()
    achternaam = achternaamEntry.get()
    geboortedatum = geboortedatumEntry.get()
    telefoon = telefoonEntry.get()
    email = emailEntry.get()
    kleur = kleurEntry.get()
    wachtwoord = wachtwoordEntry.get()
    gegevens = [voornaam, achternaam, geboortedatum, telefoon, email, kleur, wachtwoord]
    fietsToevoegen(gegevens)
    hoofdmenu()

def fietsStallen():
    homebutton()
    mainFrame.grid_remove()
    fietsStallenFrame.grid(padx=30,pady=30)
# Display help widgets
def menuHelp():
    global helpDisplayed
    labels = [registerLabel, stallLabel, collectLabel]
    if helpDisplayed == False:
        registerLabel.grid(row=0, column=1, padx=30)
        stallLabel.grid(row=1, column=1, padx=30)
        collectLabel.grid(row=2, column=1, padx=30)
        helpDisplayed = True
    else:
        registerLabel.grid_remove()
        stallLabel.grid_remove()
        collectLabel.grid_remove()
        helpDisplayed = False
        
# Main window
root = Tk()
root.config(bg=gold)
root.overrideredirect(True)
root.geometry('{}x{}'.format(root.winfo_screenwidth(),
                             root.winfo_screenheight()))

########## Frames ##########

# Main window widgets frame
mainFrame = Frame(root)
mainFrame.config(bg=gold)
mainFrame.grid(padx=30, pady=30)

# Registration window widgets frame
registrationFrame = Frame(root)
registrationFrame.config(bg=gold)

# stalling window widgets frame
fietsStallenFrame = Frame(root)
fietsStallenFrame.config(bg='gold')

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

# stalling button
stallingButton = Button(master=mainFrame,
                       text='Stal je fiets.',
                       command=fietsStallen,
                       height=3,
                       width=30,
                       bg=blue,
                       fg=white)
stallingButton.grid(row=1,column=0, pady=5)

# Info button
infoButton = Button(master=mainFrame,
                           text='Ophalen van je fiets/\ninformatie opvragen.',
                           height=3,
                           width=30,
                           background=blue,
                           foreground=white)
infoButton.grid(row=2,column=0,pady=5)

# Help button
helpButton = Button(master=mainFrame,
                    text='?',
                    height=3,
                    width=30,
                    bg=blue,
                    fg=white,
                    command=menuHelp)
helpButton.grid(row=3,column=0,pady=5)

# Exit button
exitButton = Button(master=root,
                    text='Afsluiten',
                    height=3,
                    width=30,
                    bg=red,
                    fg=white,
                    command=close)
exitButton.place(rely=1, relx=1, x=-30, y=-30, anchor=SE)

# Register Label
registerLabel = Label(master=mainFrame,
                      text='Gebruik deze knop om je fiets te registreren in het systeem',
                      background = gold,
                      height=3,
                      width=80,
                      foreground = black,
                      anchor=W)

# Stall label
stallLabel = Label(master=mainFrame,
                   text='Gebruik deze knop om je fiets te stallen',
                   background = gold,
                   height=3,
                   width=80,
                   foreground = black,
                   anchor=W)

# Collect label
collectLabel = Label(master=mainFrame,
                     text='Gebruik deze knop om je fiets op te halen of om informatie op te vragen',
                     background = gold,
                     height=3,
                     width=80,
                     foreground = black,
                     anchor=W)

# Exit label
exitLabel = Label(master=mainFrame,
                  text='Gebruik deze knop om af te sluiten',
                  background = gold,
                  height=3,
                  width=30,
                  foreground = black,
                  anchor=W)
###### Fiets stallen widgets #######

##### stal Entry ######
fietsNummerEntry = Entry(master=fietsStallenFrame,
                         width=30)
fietsNummerEntry.grid(row=0, column=2, pady=5)

####stal Label####
fietsNummerLabel = Label(master=fietsStallenFrame,
                        text='Uw fietsnummer:',
                        anchor=W,
                        width=20,
                        bg='gold')
fietsNummerLabel.grid(row=0, column=1, pady=5)

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
returnButton = Button(master=registrationFrame,
                      text='Bevestigen',
                      height=3,
                      width=30,
                      background=blue,
                      foreground=white,
                      command=confirmRegistration)
returnButton.grid(row=99,column=1,pady=5)

# Main loop
root.mainloop()
