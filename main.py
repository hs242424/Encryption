#required modulels
import random as r

#alphabet for basic functions
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#final scramble code
def reset():
    global scrambledAlpabet
    scrambledAlpabet =[]
reset()
#Scrables first half and second half of the alphabet making a double slide cifer or sifer or scifer of whatever if is called, IDEs don't have autocorrect
def scrambler():
    global scrambleVal
    scrambleVal = r.randrange(3,11)
    counterVal = 0
    firstHalfAlf = alphabet[0:13]
    secondHalfAlf = alphabet[13:26]
    print(firstHalfAlf)
    print(secondHalfAlf)
    while (counterVal < scrambleVal):
        helpVal1 = firstHalfAlf[0]
        firstHalfAlf.pop(0)
        firstHalfAlf.append(helpVal1)
        print(firstHalfAlf)
        counterVal += 1
scrambler()
'''
using a place holder value that can be made using keypresses or gets exchanged with another place holder value you can replace characters in a string
'''