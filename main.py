#required modulels
import random as r

#alphabet for basic functions
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#final scramble code
def reset():
    global scrambledAlpabet
    scrambledAlpabet =[]
reset()
def scrambler(x):
    firstHalfAlf = alphabet[0:13]
    secondHalfAlf = alphabet[13:26]
    print(firstHalfAlf)
    print(secondHalfAlf)
scrambler(12)
'''
using a place holder value that can be made using keypresses or gets exchanged with another place holder value you can replace characters in a string
'''