#required modulels
import random as r

#alphabet for basic functions
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#final scramble code
scrambledAlpabet =[]
def scrambler():
    helperAlphabet = alphabet
    for x in alphabet:
        currentVal = helperAlphabet[0]
        print(currentVal)
scrambler()