from datetime import datetime

def inputDOB():

    #Function will loop prompt until user input passes validateDOB function
    #Returns a valid date of birth

    while True:
        dob = input('Input your date of birth(dd/mm/yyyy): ')
        validDOB=''
        try:
            validDOB = validateDOB(dob)
        except ValueError:
            print('Please input a valid date of birth!')
        except AssertionError:
            print('You cannot use future date!')
        except:
            print('Unexpected error! Please try again.')
        if validDOB:
            break
    return validDOB

def validateDOB(dob):

    #Takes a string argument and try to parse it as datetime object
    #Returns datetime object if parsing succeeds
        dobParsed = datetime.strptime(dob, '%d/%m/%Y')
        assert dobParsed < datetime.now()
        return dobParsed


def calculateAge(validDOB):

    #Function to caculate age by subtracting DOB year to Current year
    #and check whether the user had his birthday for the current year if not deduct 1 to age
    #Returns an integer/float age

    currentDate = datetime.now()
    age = currentDate.year - validDOB.year
    if age == 0:
        age = (currentDate-validDOB).days/365.25
    elif (currentDate.month, currentDate.day) < (validDOB.month, validDOB.day):
        age -= 1
    return age

def inputName():

    # Function will loop prompt until user input passes validateName function
    # Returns letter only string

    while True:
        name = input('Input your name: ')
        validName = validateName(name)
        if validName:
            break
    return validName

def validateName(name):

    # Function accepts string as argument and check if all the element of the string are letters
    # Return the string name if True
    # Return False and display a prompt if the strings are not all letters
    if name.isalpha():
        return name
    else:
        print('Please input letters only!')
        return False

def generatePassword(dob,age,name):

    # Function takes dob as a datetime object, age as an integer, string as required paramater
    # Function combine arguments and translate it to string then to binary string
    passwordLength = 6
    fullInfo = str(dob) + str(age) + name
    basePassword = datetime.strftime(dob,'%d%m%y')
    binarySequence = ''
    for char in fullInfo:
        binarySequence += (format(ord(char), 'b'))
    cipherKey = int(binarySequence,2)
    #calculate the maximum possible size of bits
    #based on the binarySequence and passwordLength
    counter = 0
    password = ''
    while not len(password) == passwordLength:
        shiftKey = (int(basePassword[counter]) + cipherKey) % 96
        password += chr(32+shiftKey)
        counter += 1
    return password

if __name__ == '__main__':
    while True:
        name = inputName()
        dob = inputDOB()
        age = calculateAge(dob)
        password = generatePassword(dob,age,name)
        print('Hi! {}'.format(name))
        print('You are {} years old!'.format(round(age,2)))
        print('Your password is : {}'.format(password))

        tryAgain = input('Press Y to try again!')
        if not tryAgain.upper() == 'Y':
            break


