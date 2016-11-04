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
def returnMenu():
    returnFrame.grid_remove()
    startFrame.grid()
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
#widgets hoofdscherm
#buttons
#button om je fiets mee te registreren
registrationButton = Button(master=startFrameRegister,
                            text='Registreer je fiets.',
                            height=3,
                            width=30,
                            background='blue',
                            foreground='white',
                            command=registerBike)

registrationButton.pack( side=LEFT,padx= 20,pady=10)

#button om je fiets mee te stallen
storingButton = Button(master=startFrameStall,
                    text='Stal je fiets.',
                    height=3,
                    width=30,
                    background='blue',
                    foreground='white',
                    command=storingBike)

storingButton.pack(side=LEFT,padx= 20,pady=10)

#button om je fiets op te halen of om informatie op te vragen
collectInformationButton = Button(master=startFrameRetrieve,
                                  text='Ophalen van je fiets/\ninformatie opvragen.',
                                  height=3,
                                  width=30,
                                  background='blue',
                                  foreground='white',
                                  command=collectInfo)

collectInformationButton.pack( side=LEFT,padx= 20,pady=10)
#button die labels weergeeft als hulpmiddel bij de buttons
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
