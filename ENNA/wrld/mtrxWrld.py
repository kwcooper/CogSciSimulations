import numpy as np
import matplotlib.pyplot as plt
import os


def makeWrld(shape, wSze):
    if shape == "squ":
        newWrld = np.zeros((wSze,wSze))
    elif shape == "T":
        newWrld = np.zeros((wSze, wSze))
        for i in range(wSze):
            for j in range(wSze):
                #This logic makes a T based on the size of the array
                #the way this works works better on arrays larger
                #than 5, preferably 6 for a t of width 2
                #if a T of size 3 is wanted, then the matrix needs to
                #be non square (Which will f up the other functions)
                if i > (wSze/4) and (j < (wSze/4) or j > (wSze/2)):
                    newWrld[i][j] = 1
    #print(newWrld)
    return newWrld

def drwWld():
    

#this is for making a new one?
#
def mkNDrwWld(sze):
    return sze



#need to refactor this into two functions
def drawWrld(sze, agnt, rep, new=False, *wld):
    if new == True:
        print( )
        #below is the beginnings to make it look pretty in terminal (unnessary)
##        for i in range(sze):
##            print( )
##            for j in range(sze):
##                #need to think of a better solution for this
##                if rep == "V":
##                    rep = j
##                if i == agnt[0] and j == agnt[1]:
##                    
##                    print("*", " ", end='')
##                else:
##                    print(wld[0][i][j], " ", end='')
        print(wld[0])
    else:
        #one method to print np arrays
        #newW = ' '.join(map(str, wrld))
        print()
        for i in wld[0]:  
            print()
            for j in i:
                if j == 1:
                    print("*", " ", end="")
                else:
                    print(" ", " ", end="")

        
def udAgentPos(wld, pos):
    wld[pos[0]][pos[1]] = 1
    return wld

def tstWlk()


##drawWrld(wSze, "V", [1,1], False, wrld)
##udAgentPos(wrld, [0,0])
##drawWrld(wSze, "V", [1,1], False, wrld)


print()

wSze = 6
agnt = [0,0]

wrld = makeWrld("T", wSze)
drawWrld(wSze, "V", [1,1], True, wrld)


