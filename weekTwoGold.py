import weekTwoBronze as w2b
import customButtons as cb
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
from tkcalendar import Calendar

def createWindow():
    mainWindow = tk.Tk()
    mainWindow.title('PASSWORD GENERATOR')
    return mainWindow

def createEntryWidget(mainWindow):
    global nameVar
    global dobVar
    entryFrame = ttk.LabelFrame(mainWindow)
    entryFrame.pack()
    nameLabel = ttk.Label(entryFrame,text='Enter First Name :')
    dobLabel = ttk.Label(entryFrame,text='Enter Date of Birth :')
    nameEntry = ttk.Entry(entryFrame,textvariable = nameVar,width=30)
    nameEntry.bind("<FocusIn>", lambda e:nameVar.set(''))
    dobEntry = ttk.Entry(entryFrame,textvariable = dobVar,state='readonly',width=30)
    dobEntry.bind("<FocusIn>", lambda e: dobVar.set(''))
    calButton = cb.calendarButton(entryFrame)
    nameLabel.grid(column=0,row=0)
    dobLabel.grid(column=0,row=1)
    nameEntry.grid(column=1,row=0)
    dobEntry.grid(column=1,row=1)
    calButton.grid(column=2,row=1)

def createButtons(mainWindow):
    global nameVar
    global dobVar
    buttonFrame = ttk.LabelFrame(mainWindow)
    buttonFrame.pack()
    confirmButton = ttk.Button(buttonFrame,text='Confirm')
    clearButton = ttk.Button(buttonFrame,text='Clear')
    confirmButton.grid(column=0,row=0)
    clearButton.grid(column=0,row=1)

def calendarWindow(mainWindow):
    calWindow = tk.Toplevel(mainWindow)

mainWindow = createWindow()
nameVar = tk.StringVar(value='No special characters/space')
dobVar = tk.StringVar(value='Click Calendar to set DOB')
createEntryWidget(mainWindow)
createButtons(mainWindow)
calendarWindow(mainWindow)
mainWindow.mainloop()