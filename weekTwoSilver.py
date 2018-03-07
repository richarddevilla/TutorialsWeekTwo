import weekTwoBronze as w2b
from tkinter import StringVar
from tkinter import Tk
from tkinter import ttk
from tkinter import messagebox as msg
from tkcalendar import DateEntry

# Function to create a Tkinter window
def createWindow():
    mainWindow = Tk()
    mainWindow.title('PASSWORD GENERATOR')
    return mainWindow

# Function to create the widgets of the mainwindow.
# Their position, default value and behavior
def createEntryWidget(mainWindow):

    entryFrame = ttk.LabelFrame(mainWindow)
    entryFrame.pack()

    nameLabel = ttk.Label(entryFrame,text='Enter First Name :')
    dobLabel = ttk.Label(entryFrame,text='Enter DoB (dd/mm/yyyy) :')
    ageLabel = ttk.Label(entryFrame,text='Your age is :')
    passLabel = ttk.Label(entryFrame,text='Password :')
    nameEntry = ttk.Entry(entryFrame,textvariable = nameVar,width=30)
    nameEntry.bind("<FocusIn>", lambda e:nameVar.set(''))
    dobEntry = DateEntry(entryFrame,width=28,textvariable=dobVar)
    ageEntry = ttk.Entry(entryFrame,textvariable = ageVar,state='readonly',width=30)
    passEntry = ttk.Entry(entryFrame,textvariable=passVar,state='readonly')

    nameLabel.grid(column=0,row=0,sticky='E')
    dobLabel.grid(column=0,row=1,sticky='E')
    ageLabel.grid(column=0,row=2,sticky='E')
    passLabel.grid(column=0, row=3,sticky='E')
    nameEntry.grid(column=1,row=0,sticky='W')
    dobEntry.grid(column=1,row=1,sticky='W')
    ageEntry.grid(column=1, row=2,sticky='W')
    passEntry.grid(column=1,row=3,sticky='W')

    buttonFrame = ttk.LabelFrame(mainWindow)
    buttonFrame.pack()

    confirmButton = ttk.Button(buttonFrame,text='Confirm',command=validateEntry)
    confirmButton.grid(column=0,row=0)

# Function uses methods from weekTwoBronze module to validate dob and name,# calculate age and generate password
# Upon successful validation function asigns the age to ageVar and password to passVar
def validateEntry():
    validDOB=False
    try:
        validDOB = w2b.validateDOB(dobVar.get())
    except ValueError:
        msg.showerror('Error!', 'Please input a valid date of birth!')
    except AssertionError:
        msg.showerror('Error!', 'You cannot use future date!')
    except:
        msg.showerror('Error!', 'Unexpected error! Please try again.')
    validName = w2b.validateName(nameVar.get())
    if validName == False:
        msg.showerror('Error!', 'No special characters/space on names')
    if not validName == False and not validDOB == False:
        age = w2b.calculateAge(validDOB)
        ageVar.set(age)
        passVar.set(w2b.generatePassword(validDOB,age,validName))

#Initialize the StringVars and mainWindows's widget then run the mainloop
if __name__ == '__main__':
    mainWindow = createWindow()
    nameVar = StringVar(value='No special characters/space')
    dobVar = StringVar()
    passVar = StringVar()
    ageVar = StringVar(value='Click Confirm to Calculate Age')
    createEntryWidget(mainWindow)
    mainWindow.mainloop()