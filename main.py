#required modulels
import random as r

#alphabet for basic functions
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
encodedMessage = 1
firstHalfAlf = 1
secondHalfAlf = 1
#creates an alphabet as a list

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
    print(firstHalfAlf)
    print(secondHalfAlf)

#Function that gets the input from the user and converts it into a format that the program can use
unEncodedList = []
def getInput():
    #basic user interactions - no way to handle unxpected input but that should not be nessesary
    confirm = "n"
    while (confirm.lower() != "y"):
        unEncoded = input("Type you message here for it to be encoded:\n")
        confirm = input("You message says \"" + unEncoded + "\". Do you want to encode this message(y/n)?\n")
    global unEncodedList
    unEncodedList = list(unEncoded)
    print(unEncodedList)
    return unEncodedList

#encodes the message letter by letter
def funcEncode(message):
    #necessary global variables
    global encodedMessage
    global firstHalfAlf
    global secondHalfAlf
    isLower = False
    encodedMessage = []
    messageHelper = []
    print(message)
    message = messageHelper
    helpVal1 = messageHelper[0]
    isLower = False
    if (helpVal1.lower() == helpVal1):
        isLower = True
    if (helpVal1.lower() in firstHalfAlf):
        place = alphabet.index(helpVal1)
        if (isLower):
            encodedMessage.append(firstHalfAlf[place])
        else:
            encodedMessage.append(firstHalfAlf[place].upper())
    elif (helpVal1.lower() in secondHalfAlf):
        place = alphabet.index(helpVal1) - 13
        if (isLower):
            encodedMessage.append(secondHalfAlf[place])
        else:
            encodedMessage.append(secondHalfAlf[place].upper())
    messageHelper.pop(0)
    return encodedMessage
#DO NOT REMOVE
scrambler()
#DO NOT REMOVE
print(funcEncode(['a']))