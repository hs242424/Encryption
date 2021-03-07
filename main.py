#required module
import random as r

#creates an alphabet as a list
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
encodedMessage = 1
firstHalfAlf = []
secondHalfAlf = []
numbers = ['0','1','2','3','4','5','6','7','8','9']
scrambledNumbers = numbers

#Scrables first half and second half of the alphabet making a double slide cipher
scrambleKey = ''
def scrambler():
    global scrambleKey
    global firstHalfAlf
    global secondHalfAlf
    scrambleVal = r.randrange(3,8)
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
    print(scrambleKey)
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
    print(firstHalfAlf)
    print(secondHalfAlf)
    print(scrambledNumbers)

#Function that gets the input from the user and converts it into a format that the program can use
unEncodedList = []
def getInput():
    #basic user interactions - no way to handle unexpected input but that should not be necessary
    confirm = "n"
    while (confirm.lower() != "y"):
        unEncoded = input("Type you message here for it to be encoded:\n")
        confirm = input("You message says \"" + unEncoded + "\". Do you want to encode this message(y/n)?\n")
    global unEncodedList
    unEncodedList = list(unEncoded)
    return unEncodedList

#encodes the message letter by letter
punctuationCode = []
def funcEncode(message):
    #necessary global variables
    global encodedMessage
    global firstHalfAlf
    global secondHalfAlf
    global numbers
    global punctuationCode
    #Letter counter will count letters before a space so then the punctuation distance is correct
    secondPlaceValue = 0
    letterCounter = 0
    isLower = False
    encodedMessage = []
    messageHelper = []
    print(message)
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
        #currently does nothing for spaces but that will change with the plan below
        elif (helpVal1 == ' '):
            encodedMessage.append(' ')
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
        else:
            encodedMessage.append(helpVal1)
            print('2')
        messageHelper.pop(0)
        letterCounter += 1
        if (letterCounter > 9):
            letterCounter = 0
            secondPlaceValue += 1
    print(encodedMessage)
    print(punctuationCode)
    return encodedMessage
#DO NOT REMOVE
scrambler()
#DO NOT REMOVE
funcEncode(getInput())


#To count space I am going to use a series of numbers separated by ':'. The numbers will also be scrambles so you will need to code at the beggining of the 
#encrypted message to find out what it means
#Also, punctuation marks will be encrypted in the end of the message, making it impossible to read for someone who is trying to figure it our on their
# own