# import tkinter als dit bestand in python 3 is geopend dan gebruikt hij module tkinter en bij python 2 Tkinter
try:
    from tkinter import *

except ImportError:

    from Tkinter import *
    print('Je gebruikt python 2')

#creeert het hoofdscherm
root = Tk()
#zet de achtergrondkleur van hoofdscherm
root.configure(background='gold')
#button om je fiets mee te registreren
registrationButton = Button(master=root,
                            text='Registreer je fiets.',
                            height=2,
                            width=20,
                            background='blue',
                            foreground='white')

registrationButton.grid(row=0, column=0, padx= 20,pady=10)

#button om je fiets mee te stallen
storingButton = Button(master=root,
                    text='Stal je fiets.',
                    height=2,
                    width=20,
                    background='blue',
                    foreground='white')

storingButton.grid(row=1, column=0, padx= 20,pady=10)

#button om je fiets op te halen of om informatie op te vragen
collectInformationButton = Button(master=root,
                                  text='Ophalen van je fiets/\ninformatie opvragen.',
                                  height=2,
                                  width=20,
                                  background='blue',
                                  foreground='white')

collectInformationButton.grid(row=2, column=0, padx= 20,pady=10)




#start de gui/ toont het hoofdscherm
root.mainloop()
