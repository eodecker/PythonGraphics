# Eli Decker
# 4/28/17
# turtle_interpreter.py
# version 5

import turtleTk3D
import random
import sys

turtle = None

class TurtleInterpreter:
    initialized = False
    

    def __init__(self, dx=800, dy=800):
        ''' initializes screen and set up for turtle '''
        self.style = 'normal'
        self.jitterSigma = 2
        self.dotSize = 5
        
        if TurtleInterpreter.initialized:
            return
        TurtleInterpreter.initialized = True
        
        global turtle
        turtle = turtleTk3D.Turtle3D( dx, dy )
        # call turtle.setup
        turtle.setup( dx, dy)
        turtle.tracer( False )
        
          
    
    def setStyle( self, s):
        self.style = s
    
    def setJitter( self, j ):
        self.jitterSigma = j
        
    def setDotSize( self, d ):
        self.dotSize = d
        
    def forward(self, distance):
    # if self.style is 'normal'
        if self.style == 'normal':
        # have the turtle go foward by distance
            turtle.forward(distance)
    # else if self.style is 'jitter'
        elif self.style == 'jitter':
            # assign to x0 and y0 the result of turtle.position()
            (x0, y0, z0) = turtle.position()
            # pick up the turtle
            turtle.up()
            # have the turtle go forward by distance
            turtle.forward(distance)
            # assign to xf and yf the result of turtle.position()
            (xf, yf, zf) = turtle.position()
            # assign to curwidth the result of turtle.width()
            curwidth = turtle.width()

            # assign to jx the result of random.gauss(0, self.jitterSigma)
            jx = random.gauss( 0, self.jitterSigma )
            # assign to jy the result of random.gauss(0, self.jitterSigma)
            jy = random.gauss( 0, self.jitterSigma )
            jz = random.gauss( 0, self.jitterSigma )
            # assign to kx the result of random.gauss(0, self.jitterSigma)
            kx = random.gauss( 0, self.jitterSigma )
            # assign to ky the result of random.gauss(0, self.jitterSigma)
            ky = random.gauss( 0, self.jitterSigma )
            kz = random.gauss( 0, self.jitterSigma )

            # set the turtle width to (curwidth + random.randint(0, 2))
            turtle.width( curwidth + random.randint( 0, 2 ) )
            # have the turtle go to (x0 + jx, y0 + jy)
            turtle.goto( x0 + jx, y0 + jy, z0 + jz )
            # put the turtle down
            turtle.down()
            # have the turtle go to (xf + kx, yf + ky)
            turtle.goto(xf + kx, yf + ky, zf + kz)
            # pick up the turtle
            turtle.up()
            # have the turtle go to (xf, yf)
            turtle.goto( xf, yf, zf )
            # set the turtle width to curwidth
            turtle.width(curwidth)
            # put the turtle down
            turtle.down()
    
        elif self.style == 'jitter3':
            # assign to x0 and y0 the result of turtle.position()
            (x0, y0) = turtle.position()
            # pick up the turtle
            turtle.up()
            # have the turtle go forward by distance
            turtle.forward(distance)
            # assign to xf and yf the result of turtle.position()
            (xf, yf) = turtle.position()
            # assign to curwidth the result of turtle.width()
            curwidth = turtle.width()

            for i in range(3):
                # assign to jx the result of random.gauss(0, self.jitterSigma)
                jx = random.gauss( 0, self.jitterSigma )
                # assign to jy the result of random.gauss(0, self.jitterSigma)
                jy = random.gauss( 0, self.jitterSigma )
                # assign to kx the result of random.gauss(0, self.jitterSigma)
                kx = random.gauss( 0, self.jitterSigma )
                # assign to ky the result of random.gauss(0, self.jitterSigma)
                ky = random.gauss( 0, self.jitterSigma )
            

                # set the turtle width to (curwidth + random.randint(0, 2))
                turtle.width( curwidth + random.randint( 0, 2 ) )
                # have the turtle go to (x0 + jx, y0 + jy)
                turtle.goto( x0 + jx, y0 + jy )
                # put the turtle down
                turtle.down()
                # have the turtle go to (xf + kx, yf + ky)
                turtle.goto(xf + kx, yf + ky)
                # pick up the turtle
                turtle.up()
                # have the turtle go to (xf, yf)
                turtle.goto( xf, yf )
                # set the turtle width to curwidth
                turtle.width(curwidth)
                # put the turtle down
                turtle.down()
                
        elif self.style == 'dotted':
            for i in range(int(distance / (4*self.dotSize) ) ):
                turtle.circle( self.dotSize )
                turtle.up()
                turtle.forward( 4 * self.dotSize )
                turtle.down()
                
        elif self.style == 'randcolor':
            for i in range(int(distance / 20 ) ):
                turtle.color( ( (random.random()), (random.random()), (random.random()) ) )
                turtle.forward( distance/5 )
                
        elif self.style == 'goldish':
            r = 1.0
            g = 0.81568
            b =  0
            for i in range(int(distance / 20 ) ):
                turtle.color( ( r, g-0.1176*i, b ) )
                turtle.forward( distance/5 )
    
    def drawString( self, dstring, distance, angle):
        """ Interpret the characters in string dstring as a series
        of turtle commands. Distance specifies the distance
        to travel for each forward command. Angle specifies the
        angle (in degrees) for each right or left command. The list of 
        turtle supported turtle commands is:
        F : forward
        - : turn right
        + : turn left
        [ : save position, heading
        ] : restore position, heading
        < : saves color
        > : restores color
        g : makes color green
        d : makes color dark green
        y : makes color yellow
        r : makes color red
        o : makes color orange
        { : begins fill
        } : ends fill
        & : execute the pitch method with a positive angle (down)
        ^ : execute the pitch method with a negative angle (up)
        \ : exectue the roll method with a positive angle (right)
        / : execute the roll method with a negative angle (left )
        """
        # assign to modstring the empty string
        modstring = ''
        # assign to modval the value None
        modval = None
        # assign to modgrab the value False
        modgrab = False


        # assign to a local variable (e.g. stack) the empty list
        stack = []
        colorstack = []
        dstring
        
        
        # for each character c in dstring
        for c in dstring:
                # if c is '('
            if c == '(':
                # assign to modstring the empty string
                modstring = ''
                # assign to modgrab the value True
                modgrab = True
                # continue
                continue
            # else if c is ')'
            elif c == ')':
                # assign to modval the result of casting modstring to a float
                modval = float(modstring)
                # assign to modgrab False
                modgrab = False
                # continue
                continue
            # else if modgrab (is True)
            elif modgrab:
                # add to modstring the character c
                modstring += c
                # continue
                continue
            
            # if c is 'F'
            if c == 'F':
                # if modval is None
                if modval == None:
                    # call self.forward with the argument distance
                    self.forward(distance)
                # else
                else:
                    # call self.forward with the argument distance * modval
                    self.forward(distance * modval )
            if c == 'Z':
                # if modval is None
                if modval == None:
                    # call self.forward with the argument distance
                    self.forward(distance)
                # else
                else:
                    # call self.forward with the argument distance * modval
                    self.forward(distance * modval )
            if c == 'f':
                # if modval is None
                if modval == None:
                    # call self.forward with the argument distance
                    turtle.up()
                    self.forward(distance)
                    turtle.down()
                # else
                else:
                    # call self.forward with the argument distance * modval
                    turtle.up()
                    self.forward(distance * modval )
                    turtle.down()
            # else if c is equal to '-'
            elif c == '-':
                if modval == None:
                    turtle.yaw( -angle )
                else:
                    turtle.yaw( -modval )
            # else if c is equal to '+'
            elif c == '+':
                if modval == None:
                    turtle.yaw( angle )
                else:
                    turtle.yaw( modval )
            elif c == '&':
                if modval == None:
                    turtle.pitch( angle )
                else:
                    turtle.pitch( modval )
            elif c == '^':
                if modval == None:
                    turtle.pitch( -angle )
                else:
                    turtle.pitch( -modval )
            elif c == '\\':
                if modval == None:
                    turtle.roll( angle )
                else:
                    turtle.roll( modval )
            elif c == '/':
                if modval == None:
                    turtle.roll( -angle )
                else:
                    turtle.roll( -modval )
            
                
            # if c is '!'
            elif c == '!':
                # if modval is None
                if modval == None:
                    # assign to w the result of calling turtle.width()
                    w = turtle.width()
                # if w is greater than 1
                    if w > 1:
                    # call turtle.width with w-1 as the argument
                        turtle.width( w-1 )
            # else
                else:
                # call turtle.width with modval as the argument
                    turtle.width( modval )
            
            elif c == '?':
                # if modval is None
                if modval == None:
                    # assign to w the result of calling turtle.width()
                    w = turtle.width()
                # if w is greater than 1
                    if w > 0:
                    # call turtle.width with w-1 as the argument
                        turtle.width( w+1 )
            # else
                else:
                # call turtle.width with modval as the argument
                    turtle.width( modval )
                    
                    
            # else if c is equal to '['
            elif c == '[':
              # append to stack the position of the turtle
                stack.append( turtle.position() )
              # append to stack the heading of the turtle
                stack.append( turtle.heading() )
                stack.append( turtle.width() )
            # else if c is equal to ']'
            elif c == ']':
              # pick up the turtle pen
                turtle.up()
                turtle.width( stack.pop() )
              # set the heading of the turtle to the value popped off stack
                turtle.setheading( stack.pop() )
              # set the position of the turtle to the value popped off stack
                turtle.goto( stack.pop() )
              # put down the turtle pen
                turtle.down()
            elif c == 'q':
                stack.append( turtle.heading() )
            # else if c is equal to ']'
            elif c == 'w':
                turtle.setheading( stack.pop() )
            elif c == '@':
                turtle.setheading( 0 )


            elif c == 'X':
                pass
            elif c == 'L':
                if modval == None:
                    turtle.begin_fill()
                    turtle.forward( 0.8*distance )
                    turtle.right( 60 )
                    turtle.forward( 0.8*distance )
                    turtle.right( 120 )
                    turtle.forward( 0.8*distance )
                    turtle.right( 60 )
                    turtle.forward( 0.8*distance )
                    turtle.right( 120 )
                    turtle.end_fill()
                # else
                else:
                    turtle.begin_fill()
                    turtle.forward( 0.8*distance*modval )
                    turtle.right( 60 )
                    turtle.forward( 0.8*distance*modval )
                    turtle.right( 120 )
                    turtle.forward( 0.8*distance*modval )
                    turtle.right( 60 )
                    turtle.forward( 0.8*distance*modval )
                    turtle.right( 120 )
                    turtle.end_fill()
                
            elif c == '<':
                colorstack.append(turtle.color())
            elif c == '>':
                clrs = colorstack.pop()
                turtle.color(clrs)
            elif c == 'g':
                #turtle.color( (8, 147, 27) )
                turtle.color( (0, 0, 0) )
            elif c == 'd':
                turtle.color( (21, 76, 6) )
            elif c == 'y':
                turtle.color( (239, 224, 16) )
            elif c == 'r':
                turtle.color( (random.randint(200,255), 18, random.randint(50,255)) )
            elif c == 'o':
                turtle.color( (242, 166, 2) )
            elif c == '{':
                turtle.fill(True)
            elif c == '}':
                turtle.fill(False)
            elif c == 'C':
                if modval == None:
                    turtle.circle(distance)
                else:
                    turtle.circle(distance * modval )
            modval = None

        # call turtle.update()
        turtle.update()
    
    
    def hold(self):
        """ holds the screen open until the user clicks or types 'q' """
        turtle.mainloop()

    def place(self, xpos, ypos, angle=None, zpos = 0, pitch = 0, roll = 0):
        """instructs the turtle to move
        to a given spot without drawing lines"""

        turtle.up()
        turtle.goto(xpos, ypos, zpos)
        if angle != None:
            self.orient( angle, roll, pitch )
        turtle.down()
    
    def orient(self, angle, roll = 0, pitch = 0):
        ''' orients the heading of the turtle '''
        turtle.setheading( angle )
        turtle.roll( roll )
        turtle.pitch( pitch )
        turtle.yaw( angle )
    
    def goto(self, xpos, ypos, zpos = 0):
        ''' places the turtle in a position with out drawing a line to that position '''
        turtle.up()
        turtle.goto(xpos, ypos, zpos)
        turtle.down()
        
    def roll( self, r):
        ''' mutator for roll '''
        turtle.roll( r )
        
    def pitch( self, p):
        ''' mutator for pitch '''
        turtle.pitch( p )
        
    def yaw( self, y):
        ''' mutator for yaw '''
        turtle.yaw( y )
        
    def color(self, c):
        ''' sets color '''
        turtle.color( c )
    
    def width(self, w):
        ''' sets width '''
        turtle.width( w )