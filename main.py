#required modules
import random as r

#creates an alphabet as a list
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
encodedMessage = 1
firstHalfAlf = []
secondHalfAlf = []
numbers = ['0','1','2','3','4','5','6','7','8','9']
scrambledNumbers = numbers
#used to print lists like strings
s = ''

#Scrables first half and second half of the alphabet making a double slide cipher
scrambleKey = ''
def scrambler():
    global scrambleKey
    global firstHalfAlf
    global secondHalfAlf
    global scrambledNumbers
    scrambleVal = r.randrange(3,8)
    scrambleVal = 7
    #This is the code that tells the decoder what to arrange the letters to
    if (scrambleVal == 3):
        scrambleKey = 'lf'
    elif (scrambleVal == 4):
        scrambleKey = 'bz'
    elif (scrambleVal == 5):
        scrambleKey = 'qk'
    elif (scrambleVal == 6):
        scrambleKey = 'rf'
    elif (scrambleVal == 7):
        scrambleKey = 'iw'
    elif (scrambleVal == 8):
        scrambleKey = 'xj'
    counterVal = 0
    firstHalfAlf = alphabet[0:13]
    secondHalfAlf = alphabet[13:26]
    while (counterVal < scrambleVal):
        helpVal1 = firstHalfAlf[0]
        firstHalfAlf.pop(0)
        firstHalfAlf.append(helpVal1)
        counterVal += 1
    counterVal = 0
    while (counterVal < scrambleVal):
        helpVal1 = secondHalfAlf[0]
        secondHalfAlf.pop(0)
        secondHalfAlf.append(helpVal1)
        counterVal += 1
    counterVal = 0
    while (counterVal < scrambleVal):
        helpVal1 = scrambledNumbers[0]
        scrambledNumbers.pop(0)
        scrambledNumbers.append(helpVal1)
        counterVal += 1

#Function that gets the input from the user and converts it into a format that the program can use
unEncodedList = []
def getInput(mode):
    if (mode == '0'):
        #basic user interactions - no way to handle unexpected input but that should not be necessary
        confirm = "n"
        while (confirm.lower() != "y"):
            unEncoded = input("Type you message here for it to be encoded:\n")
            confirm = input("You message says \"" + unEncoded + "\". Do you want to encode this message(y/n)?\n")
        global unEncodedList
        unEncodedList = list(unEncoded)
        return unEncodedList
    if (mode == '1'):
        confirm = 'n'
        while (confirm.lower() != "y"):
            Encoded = input("Type you message here for it to be decoded:\n")
            confirm = input("You message says \"" + Encoded + "\". Do you want to decode this message(y/n)?\n")
        EncodedList = list(Encoded)
        return EncodedList

#Keeps track of the  punctuation for the decoding process
punctuationCode = []
#encodes the message letter by letter
def funcEncode(message):
    #necessary global variables
    global encodedMessage
    global firstHalfAlf
    global secondHalfAlf
    global numbers
    global punctuationCode
    global scrambledNumbers
    #Letter counter will count letters before a space so then the punctuation distance is correct
    secondPlaceValue = 0
    letterCounter = 0
    isLower = False
    encodedMessage = []
    messageHelper = []
    messageHelper = message
    while (True):
        if (0 == len(messageHelper)):
            break
        helpVal1 = messageHelper[0]
        isLower = False
        #lower case checker
        if (helpVal1.lower() == helpVal1):
            isLower = True
        #first alphabet half checker with lowercase and uppercase checkers
        if (helpVal1.lower() in firstHalfAlf):
            place = alphabet.index(helpVal1.lower())
            if (isLower):
                encodedMessage.append(firstHalfAlf[place])
            else:
                encodedMessage.append(firstHalfAlf[place].upper())
        #second alphabet half checker with lowercase and uppercase checkers
        elif (helpVal1.lower() in secondHalfAlf):
            place = alphabet.index(helpVal1.lower()) - 13
            if (isLower):
                encodedMessage.append(secondHalfAlf[place])
            else:
                encodedMessage.append(secondHalfAlf[place].upper())
        #Function will eventually handle this punctuation '.', ' ', '!', '?'
        #might eventually be expanded to handle more if needed
        elif (helpVal1 == ' '):
            if (secondPlaceValue != 0):
                punctuationCode.append(scrambledNumbers[secondPlaceValue])
                secondPlaceValue = 0
            punctuationCode.append(scrambledNumbers[letterCounter])
            letterCounter = 0
            punctuationCode.append(':')
        elif (helpVal1 in numbers):
            numbers = ['0','1','2','3','4','5','6','7','8','9']
            place = numbers.index(helpVal1)
            encodedMessage.append(scrambledNumbers[place])
        elif (helpVal1 == '!'):
            encodedMessage.append('^')
        else:
            encodedMessage.append(helpVal1)
        messageHelper.pop(0)
        if not (helpVal1 == ' '):
            letterCounter += 1
            if (letterCounter > 9):
                letterCounter = 0
                secondPlaceValue += 1
    encodedMessage += ['!','!','!'] + punctuationCode
    encodedMessage = list(scrambleKey) + encodedMessage
    print('Encoded message: ' + s.join(encodedMessage))
    return s.join(encodedMessage)

unDecoded = []
#Finds what the letters and numbers should equal
def unScrambler(message):
    global unDecoded
    global firstHalfAlf
    global secondHalfAlf
    global scrambledNumbers
    global numbers
    unDecoded = list(message)
    key = unDecoded[0] + unDecoded [1]
    if (key == 'lf'):
        scrambleVal = 3
    elif (key == 'bz'):
        scrambleVal = 4
    elif (key == 'qk'):
        scrambleVal = 5
    elif (key == 'rf'):
        scrambleVal = 6
    elif (key == 'iw'):
        scrambleVal = 7
    elif (key == 'xj'):
        scrambleVal = 8
    counterVal = 0
    firstHalfAlf = alphabet[0:13]
    secondHalfAlf = alphabet[13:26]
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    scrambledNumbers = numbers
    while (counterVal < scrambleVal):
        helpVal1 = firstHalfAlf[0]
        firstHalfAlf.pop(0)
        firstHalfAlf.append(helpVal1)
        counterVal += 1
    counterVal = 0
    while (counterVal < scrambleVal):
        helpVal1 = secondHalfAlf[0]
        secondHalfAlf.pop(0)
        secondHalfAlf.append(helpVal1)
        counterVal += 1
    counterVal = 0
    while (counterVal < scrambleVal):
        helpVal1 = scrambledNumbers[0]
        scrambledNumbers.pop(0)
        scrambledNumbers.append(helpVal1)
        counterVal += 1
    numbers = ['0','1','2','3','4','5','6','7','8','9']

decodedMessage = []
#Decodes the message
def Decode(message):
    helperMessage = list(message)
    global decodedMessage
    global firstHalfAlf
    global secondHalfAlf
    global scrambledNumbers
    global alphabet
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    counter = 0
    place = 0
    isLower = False
    exclamationCounter = 0
    for x in range(2): helperMessage.pop(0)
    #Decodes the message but not the spaces
    while (True):
        if (0 == len(helperMessage)):
            break
        helpVal = helperMessage[0]
        if (helpVal.lower() == helpVal):
            isLower = True
        if (helpVal.lower() in firstHalfAlf):
            place = firstHalfAlf.index(helpVal.lower())
            if (isLower):
                decodedMessage.append(alphabet[place])
            else:
                decodedMessage.append(alphabet[place].upper())
        elif (helpVal.lower() in secondHalfAlf):
            place = secondHalfAlf.index(helpVal.lower()) + 13
            if (isLower):
                decodedMessage.append(alphabet[place])
            else:
                decodedMessage.append(alphabet[place].upper())
        elif (helpVal in numbers):
            numbers = ['0','1','2','3','4','5','6','7','8','9']
            place = scrambledNumbers.index(helpVal)
            decodedMessage.append(numbers[place])
        elif (helpVal == '^'):
            decodedMessage.append('!')
        else:
            decodedMessage.append(helpVal)
        if (helpVal == '!'):
            exclamationCounter += 1
        else:
            exclamationCounter = 0
        if (exclamationCounter == 3):
            exclamationCounter = 0
            decodedMessage.pop(-1)
            decodedMessage.pop(-1)
            decodedMessage.pop(-1)
            break
        helperMessage.pop(0)
    helperMessage = list(message)
    counter = 0
    #Finds where spaces begin
    while (True):
        helpVal = helperMessage[0]
        while (not helpVal == '!'):
            helperMessage.pop(0)
            helpVal = helperMessage[0]
        if (helperMessage[1] == '!' and helperMessage[2] == '!'):
            for x in range(3): helperMessage.pop(0)
        break
    #Decodes the space values
    spaceCode = []
    while (True):
        if (helperMessage == []):
            break
        helpVal = helperMessage[0]
        helperMessage.pop(0)
        if (helpVal in numbers):
            numbers = ['0','1','2','3','4','5','6','7','8','9']
            place = scrambledNumbers.index(helpVal)
            spaceCode.append(numbers[place])
        elif (helpVal == ':'):
            spaceCode.append(':')
    counter = 0
    #Adds spaces back in
    while (True):
        print(spaceCode)
        z = 2
        if (spaceCode == []):
            break
        helpVal = spaceCode[0]
        if (not spaceCode[1] == ':'):
            helpVal2 = (int(spaceCode[0])*10)+int(spaceCode[1])
            print(helpVal2)
            z = 3
        else:
            helpVal2 = spaceCode[0]
        counter += int(helpVal2)
        decodedMessage.insert(counter, ' ')
        for x in range(z): spaceCode.pop(0)
        counter += 1
    s = ''
    print('Decoded message: ' + s.join(decodedMessage))

#Runs the functions needed for a full decode
def fullDecode():
    message = getInput('1')
    unScrambler(message)
    Decode(message)

#Runs function for full encode
def fullEncode():
    scrambler()
    funcEncode(getInput('0'))

while (True):
    print("Choose a function \n0: Encode\n1: Decode\n2: Quit")
    input1 = input('')
    if (input1 == '0'):
        fullEncode()
        break
    elif (input1 == '1'):
        fullDecode()
        break
    elif (input1 == '2'):
        break
    else:
        print('\"' + input1 + '\" is not a recognized command.')