# import tkinter als dit bestand in python 3 is geopend dan gebruikt hij module tkinter en bij python 2 Tkinter
try:
    from tkinter import *

except ImportError:

    from Tkinter import *
    print('Je gebruikt python 2')
#statements die bepaald moeten zijn aan het begin

#telt het aantal keer wat wordt geklikt op de help button in het beginscherm
helpStartFrameCounter = 0
#functies

# deze functie die zorgt ervoor dat de info die in het registerscherm wordt ingevoerd dat die opgeslagen wordt als variabele apart en als lijst samen.
def registerInfo():
    global voornaam,achternaam,telefoon,email,geboortedatum,fietsKleur,listOfRegisterInfo
    voornaam = voornaamRegisterText.get('1.0',END)
    achternaam = achternaamRegisterText.get('1.0',END)
    telefoon = telefoonRegisterText.get('1.0',END)
    email = emailRegisterText.get('1.0',END)
    geboortedatum = geboortedatumRegisterText.get('1.0',END)
    fietsKleur = kleurFietsRegisterText.get('1.0',END)
    listOfRegisterInfo = [voornaam,achternaam,telefoon,email,geboortedatum,fietsKleur]
    print(listOfRegisterInfo)
#sluit programma
def closeWindow():
    root.destroy()

#opent op het moment nog niks maar het gaat het stallen van een fiets scherm openen
def storingBike():
    startFrame.grid_remove()
    returnFrame.grid()
#opent nog niks moet ophalen/info over scherm openen
def collectInfo():
    startFrame.grid_remove()
    returnFrame.grid()
#opent het registreren van user/fiets scherm
def registerBike():
    startFrame.grid_remove()
    returnFrame.grid()
    registerFrame.grid()
#gaat weer terug naar het hoofdmenu
def returnMenu():
    returnFrame.grid_remove()
    startFrame.grid()
    registerFrame.grid_remove()
#telt het aantal klikken op de help knop als dit even is dan geeft hij extra info weer en oneven haalt hij het weer weg
def helpStartFrame():
    global helpStartFrameCounter

    if helpStartFrameCounter % 2 == 1:
            registerLabel.pack_forget()
            stallLabel.pack_forget()
            retrieveLabel.pack_forget()
            startHelpLabel.pack_forget()
            exitLabel.pack_forget()
    else:
        registerLabel.pack()
        stallLabel.pack()
        retrieveLabel.pack()
        startHelpLabel.pack()
        exitLabel.pack()
    helpStartFrameCounter += 1


#creeert het hoofdscherm
root = Tk()
#zet de achtergrondkleur van hoofdscherm
root.configure(background='#FFD700'	)
#maakt het fullscreen
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),root.winfo_screenheight()))
#frames
#frame hoofdscherm
startFrame = Frame(root)
startFrame.grid(row=0,column=0)
startFrame.configure(background='#FFD700')
#frame van registreren
startFrameRegister = Frame(startFrame)
startFrameRegister.grid(row=0,column=0)
startFrameRegister.configure(background='#FFD700')
#frame van stallen
startFrameStall = Frame(startFrame)
startFrameStall.grid(row=1,column=0)
startFrameStall.configure(background='#FFD700')
#frame ophalen en info
startFrameRetrieve = Frame(startFrame)
startFrameRetrieve.grid(row=2,column=0)
startFrameRetrieve.configure(background='#FFD700')
#frame hulpknop
startFrameHelp = Frame(startFrame)
startFrameHelp.grid(row=3,column=0)
startFrameHelp.configure(background='#FFD700')
#frame exitknop
exitFrame = Frame(startFrame)
exitFrame.grid(row=99,column=0)
exitFrame.configure(background='#FFD700')
#frame returnknop
returnFrame = Frame(root)
returnFrame.grid(row=98,column=0)
returnFrame.configure(background='#FFD700')
returnFrame.grid_remove()
#register scherm
registerFrame = Frame(root)
registerFrame.grid(row=0,column=0)
registerFrame.configure(background='#FFD700')
registerFrame.grid_remove()
#register frames
#voornaam textbox en labelframe
voornaamRegisterFrame = Frame(registerFrame)
voornaamRegisterFrame.grid(row=0,column=0)
voornaamRegisterFrame.configure(background='#FFD700')
#achternaam textbox en labelframe
achternaamRegisterFrame = Frame(registerFrame)
achternaamRegisterFrame.grid(row=1,column=0)
achternaamRegisterFrame.configure(background='#FFD700')
#telefoonnummer textbox en labelframe
telefoonRegisterFrame= Frame(registerFrame)
telefoonRegisterFrame.grid(row=2,column=0)
telefoonRegisterFrame.configure(background='#FFD700')
#email textbox en labelframe
emailRegisterFrame = Frame(registerFrame)
emailRegisterFrame.grid(row=3,column=0)
emailRegisterFrame.configure(background='#FFD700')
#fietskleur textbox en labelframe
kleurFietsRegisterFrame = Frame(registerFrame)
kleurFietsRegisterFrame.grid(row=5,column=0)
kleurFietsRegisterFrame.configure(background='#FFD700')
#geboortedatum textbox en labelframe
geboortedatumRegisterFrame = Frame(registerFrame)
geboortedatumRegisterFrame.grid(row=4,column=0)
geboortedatumRegisterFrame.configure(background='#FFD700')
#frame van de invoer knop
invoerRegisterFrame = Frame(registerFrame)
invoerRegisterFrame.grid(row=6,column=0)
invoerRegisterFrame.configure(background='#FFD700')

#widgets hoofdscherm
#buttons
#button om naar het scherm te gaan waar je je fiets  registreert
registrationButton = Button(master=startFrameRegister,
                            text='Registreer je fiets.',
                            height=3,
                            width=30,
                            background='#0000FF',
                            foreground='white',
                            command=registerBike)

registrationButton.pack( side=LEFT,padx= 20,pady=10)

#button om naar menu te gaan waar jr je fiets mee te stallen
storingButton = Button(master=startFrameStall,
                    text='Stal je fiets.',
                    height=3,
                    width=30,
                    background='#0000FF',
                    foreground='white',
                    command=storingBike)

storingButton.pack(side=LEFT,padx= 20,pady=10)

#button om naar het menu te gaan waar je je fiets op te halen of om informatie op te vragen
collectInformationButton = Button(master=startFrameRetrieve,
                                  text='Ophalen van je fiets/\ninformatie opvragen.',
                                  height=3,
                                  width=30,
                                  background='#0000FF',
                                  foreground='white',
                                  command=collectInfo)

collectInformationButton.pack( side=LEFT,padx= 20,pady=10)
#button die labels weergeeft als hulpmiddel bij de buttons op start menu
startHelpButton = Button(master=startFrameHelp,
                         text='?',
                         height=3,
                         width=30,
                         background='gray49',
                         foreground='white',
                         command = helpStartFrame)


startHelpButton.pack(side=LEFT,padx=20, pady=10)
#labels
# geeft info weer over registerknop
registerLabel = Label(master=startFrameRegister,
                      text='Gebruik deze knop om je fiets te registreren in het systeem',
                      background = '#FFD700',
                      height=3,
                      width=50,
                      foreground = 'black')
registerLabel.pack(side=RIGHT,padx=20,pady=10)
registerLabel.pack_forget()
#geeft info weer over stall knop
stallLabel = Label(master=startFrameStall,
                   text='Gebruik deze knop om je fiets te stallen',
                   background = '#FFD700',
                   height=3,
                   width=50,
                   foreground = 'black')
stallLabel.pack(side=RIGHT,padx=20,pady=10)
stallLabel.pack_forget()
#geeft info weer over collect/info knop
retrieveLabel = Label(master=startFrameRetrieve,
                      text='Gebruik deze knop om je fiets op te halen of om informatie op te vragen',
                      background = '#FFD700',
                      height=3,
                      width=50,
                      foreground = 'black')
retrieveLabel.pack(side=RIGHT,padx=20,pady=10)
retrieveLabel.pack_forget()
#label gemaakt om te ordenen
startHelpLabel = Label(master=startFrameHelp,
                      background = '#FFD700',
                      height=3,
                      width=50)
startHelpLabel.pack(side=RIGHT,padx=20,pady=10)
startHelpLabel.pack_forget()
#label gemaakt om te ordenen
exitLabel = Label(master=exitFrame,
                  background = '#FFD700',
                  height=3,
                  width=50)
exitLabel.pack(side=RIGHT,padx=20,pady=10)
exitLabel.pack_forget()

#registerscherm widgets

#labels
#geeft aan wat moet ingevuld worden bij voornaamRegisterText
voornaamRegisterLabel = Label(master=voornaamRegisterFrame,
                              text='voornaam:',
                              background='#FFD700',
                              height=1,
                              width=25)
voornaamRegisterLabel.pack(side=LEFT,pady=10)
#geeft aan wat moet ingevuld worden bij achternaamRegisterText
achternaamRegisterLabel = Label(master=achternaamRegisterFrame,
                                text='achternaam:',
                                background='#FFD700',
                                height=1,
                                width=25)
achternaamRegisterLabel.pack(side=LEFT,pady=10)
#geeft aan wat moet ingevuld worden bij telefoonRegisterText
telefoonRegisterLabel = Label(master=telefoonRegisterFrame,
                              text='telefoonnummer:',
                              background='#FFD700',
                              height=1,
                              width=25)
telefoonRegisterLabel.pack(side=LEFT,pady=10)
#geeft aan wat moet ingevuld worden bij emailRegisterText
emailRegisterLabel = Label(master=emailRegisterFrame,
                           text='email:',
                           background='#FFD700',
                           height=1,
                           width=25)
emailRegisterLabel.pack(side=LEFT,pady=10)
#geeft aan wat moet ingevuld worden bij kleurFietsRegisterText
kleurFietsRegisterLabel = Label(master=kleurFietsRegisterFrame,
                                text='Kleur van je fiets:',
                                background='#FFD700',
                                height=1,
                                width=25)
kleurFietsRegisterLabel.pack(side=LEFT,pady=10)
#geeft aan wat moet ingevuld worden bij geboortedatumRegisterText
geboortedatumRegisterLabel = Label(master=geboortedatumRegisterFrame,
                                   text='Geboortedatum(DD/MM/YY):',
                                   background='#FFD700',
                                   height=1,
                                   width=25)
geboortedatumRegisterLabel.pack(side=LEFT,pady=10)
#buttons
#zorgt ervoor dat de gegevens in het systeem worden gezet
invoerRegisterButton = Button(master=invoerRegisterFrame,
                              text='voer gegevens in.',
                              background='#0000FF',
                              foreground='white',
                              height=3,
                              width=30,
                              command=registerInfo)
invoerRegisterButton.pack(side=LEFT,pady=10,padx=20)
#register text boxes
#textbox waar je voornaam moet invullen
voornaamRegisterText = Text(master=voornaamRegisterFrame,
                            height=1,
                            width=30)
voornaamRegisterText.pack(side=RIGHT)
#textbox waar je achternaam moet invullen
achternaamRegisterText = Text(master=achternaamRegisterFrame,
                              height=1,
                              width=30)
achternaamRegisterText.pack(side=RIGHT)
#textbox waar je telefoonnummer moet invullen
telefoonRegisterText = Text(master=telefoonRegisterFrame,
                            height=1,
                            width=30)
telefoonRegisterText.pack(side=RIGHT)
#textbox waar je emailadres moet invullen
emailRegisterText= Text(master=emailRegisterFrame,
                        height=1,
                        width=30)
emailRegisterText.pack(side=RIGHT)
#textbox waar je geboortedatum moet invullen
geboortedatumRegisterText = Text(master=geboortedatumRegisterFrame,
                                 height=1,
                                 width=30)
geboortedatumRegisterText.pack(side=RIGHT)
#textbox waar je de kleur van je fiets moet invullen
kleurFietsRegisterText = Text(master=kleurFietsRegisterFrame,
                              height=1,
                              width=30)
kleurFietsRegisterText.pack(side=RIGHT)
#overige buttons

#button die teruggaat naar het startscherm
returnButton = Button(master=returnFrame,
                      text='teruggaan\n naar menu',
                      height=3,
                      width=30,
                      background='#0000FF',
                      foreground='white',
                      command=returnMenu
                      )
returnButton.pack(side=LEFT,padx=20,pady=10)
returnButton.grid_remove()

#button die het programma sluit
exitButton = Button(master=exitFrame,
                    text='afsluiten',
                    height= 3,
                    width = 30,
                    background = 'red',
                    foreground = 'white',
                    command = closeWindow)

exitButton.pack(side=LEFT,padx=20,pady=10)

#start de gui/ toont het hoofdscherm
root.mainloop()
