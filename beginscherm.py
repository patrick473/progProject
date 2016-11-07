# import tkinter als dit bestand in python 3 is geopend dan gebruikt hij module tkinter en bij python 2 Tkinter
try:
    from tkinter import *

except ImportError:

    from Tkinter import *
    print('Je gebruikt python 2')
#statements die bepaald moeten zijn aan het begin

helpStartFrameCounter = 0
#functies

#sluit programma
def closeWindow():
    root.destroy()

#registreren van een fiets
def storingBike():
    startFrame.grid_remove()
    returnFrame.grid()
def collectInfo():
    startFrame.grid_remove()
    returnFrame.grid()
def registerBike():
    startFrame.grid_remove()
    returnFrame.grid()
    registerFrame.grid()

def returnMenu():
    returnFrame.grid_remove()
    startFrame.grid()
    registerFrame.grid_remove()
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
root.configure(background='gold')
#maakt het fullscreen
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),root.winfo_screenheight()))
#frames
#frame hoofdscherm
startFrame = Frame(root)
startFrame.grid(row=0,column=0)
startFrame.configure(background='gold')
#frame van registreren
startFrameRegister = Frame(startFrame)
startFrameRegister.grid(row=0,column=0)
startFrameRegister.configure(background='gold')
#frame van stallen
startFrameStall = Frame(startFrame)
startFrameStall.grid(row=1,column=0)
startFrameStall.configure(background='gold')
#frame ophalen en info
startFrameRetrieve = Frame(startFrame)
startFrameRetrieve.grid(row=2,column=0)
startFrameRetrieve.configure(background='gold')
#frame hulpknop
startFrameHelp = Frame(startFrame)
startFrameHelp.grid(row=3,column=0)
startFrameHelp.configure(background='gold')
#frame exitknop
exitFrame = Frame(startFrame)
exitFrame.grid(row=99,column=0)
exitFrame.configure(background='gold')
#frame returnknop
returnFrame = Frame(root)
returnFrame.grid(row=98,column=0)
returnFrame.configure(background='gold')
returnFrame.grid_remove()
#register scherm
registerFrame = Frame(root)
registerFrame.grid(row=0,column=0)
registerFrame.configure(background='gold')
registerFrame.grid_remove()
#register frames
voornaamRegisterFrame = Frame(registerFrame)
voornaamRegisterFrame.grid(row=0,column=0)
voornaamRegisterFrame.configure(background='gold')

achternaamRegisterFrame = Frame(registerFrame)
achternaamRegisterFrame.grid(row=1,column=0)
achternaamRegisterFrame.configure(background='gold')

telefoonRegisterFrame= Frame(registerFrame)
telefoonRegisterFrame.grid(row=2,column=0)
telefoonRegisterFrame.configure(background='gold')

emailRegisterFrame = Frame(registerFrame)
emailRegisterFrame.grid(row=3,column=0)
emailRegisterFrame.configure(background='gold')

kleurFietsRegisterFrame = Frame(registerFrame)
kleurFietsRegisterFrame.grid(row=5,column=0)
kleurFietsRegisterFrame.configure(background='gold')

geboortedatumRegisterFrame = Frame(registerFrame)
geboortedatumRegisterFrame.grid(row=4,column=0)
geboortedatumRegisterFrame.configure(background='gold')

#widgets hoofdscherm
#buttons
#button om naar het scherm te gaan waar je je fiets  registreert
registrationButton = Button(master=startFrameRegister,
                            text='Registreer je fiets.',
                            height=3,
                            width=30,
                            background='blue',
                            foreground='white',
                            command=registerBike)

registrationButton.pack( side=LEFT,padx= 20,pady=10)

#button om naar menu te gaan waar jr je fiets mee te stallen
storingButton = Button(master=startFrameStall,
                    text='Stal je fiets.',
                    height=3,
                    width=30,
                    background='blue',
                    foreground='white',
                    command=storingBike)

storingButton.pack(side=LEFT,padx= 20,pady=10)

#button om naar het menu te gaan waar je je fiets op te halen of om informatie op te vragen
collectInformationButton = Button(master=startFrameRetrieve,
                                  text='Ophalen van je fiets/\ninformatie opvragen.',
                                  height=3,
                                  width=30,
                                  background='blue',
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
registerLabel = Label(master=startFrameRegister,
                      text='Gebruik deze knop om je fiets te registreren in het systeem',
                      background = 'gold',
                      height=3,
                      width=50,
                      foreground = 'black')
registerLabel.pack(side=RIGHT,padx=20,pady=10)
registerLabel.pack_forget()

stallLabel = Label(master=startFrameStall,
                   text='Gebruik deze knop om je fiets te registreren in het systeem',
                   background = 'gold',
                   height=3,
                   width=50,
                   foreground = 'black')
stallLabel.pack(side=RIGHT,padx=20,pady=10)
stallLabel.pack_forget()

retrieveLabel = Label(master=startFrameRetrieve,
                      text='Gebruik deze knop om je fiets te registreren in het systeem',
                      background = 'gold',
                      height=3,
                      width=50,
                      foreground = 'black')
retrieveLabel.pack(side=RIGHT,padx=20,pady=10)
retrieveLabel.pack_forget()
startHelpLabel = Label(master=startFrameHelp,
                      background = 'gold',
                      height=3,
                      width=50)
startHelpLabel.pack(side=RIGHT,padx=20,pady=10)
startHelpLabel.pack_forget()
exitLabel = Label(master=exitFrame,
                  background = 'gold',
                  height=3,
                  width=50)
exitLabel.pack(side=RIGHT,padx=20,pady=10)
exitLabel.pack_forget()

#registerscherm widgets

#labels
voornaamRegisterLabel = Label(master=voornaamRegisterFrame,
                              text='voornaam:',
                              background='gold',
                              height=1,
                              width=25)
voornaamRegisterLabel.pack(side=LEFT,pady=10)

achternaamRegisterLabel = Label(master=achternaamRegisterFrame,
                                text='achternaam:',
                                background='gold',
                                height=1,
                                width=25)
achternaamRegisterLabel.pack(side=LEFT,pady=10)

telefoonRegisterLabel = Label(master=telefoonRegisterFrame,
                              text='telefoonnummer:',
                              background='gold',
                              height=1,
                              width=25)
telefoonRegisterLabel.pack(side=LEFT,pady=10)
emailRegisterLabel = Label(master=emailRegisterFrame,
                           text='email:',
                           background='gold',
                           height=1,
                           width=25)
emailRegisterLabel.pack(side=LEFT,pady=10)

kleurFietsRegisterLabel = Label(master=kleurFietsRegisterFrame,
                                text='Kleur van je fiets:',
                                background='gold',
                                height=1,
                                width=25)
kleurFietsRegisterLabel.pack(side=LEFT,pady=10)

geboortedatumRegisterLabel = Label(master=geboortedatumRegisterFrame,
                                   text='Geboortedatum(DD/MM/YY):',
                                   background='gold',
                                   height=1,
                                   width=25)
geboortedatumRegisterLabel.pack(side=LEFT,pady=10)

#register text boxes
voornaamRegisterText = Text(master=voornaamRegisterFrame,
                            height=1,
                            width=30)
voornaamRegisterText.pack(side=RIGHT)

achternaamRegisterText = Text(master=achternaamRegisterFrame,
                              height=1,
                              width=30)
achternaamRegisterText.pack(side=RIGHT)

telefoonRegisterText = Text(master=telefoonRegisterFrame,
                            height=1,
                            width=30)
telefoonRegisterText.pack(side=RIGHT)

emailRegisterText= Text(master=emailRegisterFrame,
                        height=1,
                        width=30)
emailRegisterText.pack(side=RIGHT)
geboortedatumRegisterText = Text(master=geboortedatumRegisterFrame,
                                 height=1,
                                 width=30)
geboortedatumRegisterText.pack(side=RIGHT)

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
                      background='blue',
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
