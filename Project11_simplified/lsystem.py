# Eli Decker
# 4/28/17
# lsystem.py
# version 5

import sys
import random

class Lsystem:
    '''L-system class. Contains the functions necessary to read an L-system
    file of generate a string from the L-system rules'''
    
    
    def __init__( self, filename=None ):
        ''' load in a file or just initialize fields to indicate there is an 
        empty l-system'''
        self.base = ''
        self.rules = {}
        if filename != None:
            self.read( filename )
            
    def setBase( self, newbase ):
        ''' sets the base for lstring'''
        self.base = newbase
        
    def getBase( self ):
        ''' returns base '''
        return self.base
        
    def addRule( self, newrule ):
        '''adds rule '''
        self.rules[newrule[0]] = newrule[1:]
        
    def read( self, filename ):
        ''' reads the given file '''
        # assign to a variable (e.g. fp) the file object created with filename in read mode
        fp = file( filename, 'r' )
        # assign to a variable (e.g. lines) the list of lines in the file
        lines = fp.readlines()
        # call the close method of the file
        fp.close()

        # for each element in the lines list
        for element in lines:
          # assign to a variable (e.g. words) the loop variable split on spaces
            words = element.split()
          # if the first item in words is equal to the string 'base'
            if words[0] == 'base':
              # call the setBase method of self with the new base string
                self.setBase( words[1] )
          # else if the first item in words is equal to the string 'rule'
            elif words[0] == 'rule':
              # call the addRule method of self with the new rule
                self.addRule( words[1:] )
                
    def substitute(self, sequence, value ):
        """ given: a sequence of parameterized symbols using expressions
            of the variable x and a value for x
            substitute the value for x and evaluate the expressions
        """

        expr = ''
        exprgrab = False

        outsequence = ''

        for c in sequence:

            # parameter expression starts
            if c == '(':
                # set the state variable to True (grabbing the expression)
                exprgrab = True
                expr = ''
                continue

            # parameter expression ends
            elif c == ')':
                exprgrab = False
                # create a function out of the expression
                lambdafunc = eval( 'lambda x: ' + expr )
                # execute the function and put the result in a (string)
                newpar = '(' + str( lambdafunc( value ) ) + ')'
                outsequence += newpar

            # grabbing an expression
            elif exprgrab:
                expr += c

            # not grabbing an expression and not a parenthesis
            else:
                outsequence += c 

        return outsequence

    def insertmod(self, sequence, modstring, symbol):
        """ given: a sequence, a parameter string, a symbol 
            inserts the parameter, with parentheses, 
            before each
            instance of the symbol in the sequence
        """
        tstring = ''
        for c in sequence:
            if c == symbol:
                # add the parameter string in parentheses
                tstring += '(' + modstring + ')'
            tstring += c
        return tstring
            
    def replace(self, istring):
        """ Replace all characters in the istring with strings from the
            right-hand side of the appropriate rule. This version handles
            parameterized rules.
        """
        tstring = ''
        parstring = ''
        parval = None
        pargrab = False

        for c in istring:
            if c == '(':
                # put us into number-parsing-mode
                pargrab = True
                parstring = ''
                continue
            # elif the character is )
            elif c == ')':
                # put us out of number-parsing-mode
                pargrab = False
                parval = float(parstring)
                continue
            # elif we are in number-parsing-mode
            elif pargrab:
                # add this character to the number string
                parstring += c
                continue

            if parval != None:
                key = '(x)' + c
                if key in self.rules:
                    replacement = random.choice(self.rules[key])
                    tstring += self.substitute( replacement, parval )
                else:
                    if c in self.rules:
                        replacement = random.choice(self.rules[c])
                        tstring += self.insertmod( replacement, parstring, c )
                    else:
                        tstring += '(' + parstring + ')' + c
                parval = None
            else:
                if c in self.rules:
                    tstring += random.choice(self.rules[c])
                else:
                    tstring += c

        return tstring
        
        
    def buildString(self, iterations):
        ''' builds the string '''
      # assign to a local variable (e.g. newString) the base field of self
        newString = self.base
      # for the number of iterations
        for i in range(iterations):
          # assign to newstring the result of calling the replace method of self
            newString = self.replace( newString )
      # return newstring
        return newString
        
def main(argv):
    ''' tests if it can read a file '''

    if len(argv) < 4:
        print 'Usage: lsystem.py <filename> <iterations> <output file>'
        exit()

    filename = argv[1]
    iterations = int(argv[2])
    outfile = argv[3]

    lsys = Lsystem()

    lsys.read( filename )

    lstr = lsys.buildString( iterations )

    fp = file( outfile, 'w' )
    fp.write(lstr)
    fp.close()

if __name__ == "__main__":
    main(sys.argv)