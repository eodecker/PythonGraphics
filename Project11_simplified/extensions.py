# Eli Decker
# 5/1/17
# task3.py

import shapes as s
import lsystem as ls
import turtle_interpreter as ti

def flower( x, y, z, (r, gc, b), pitch=0, orientation=0, roll=0 ):
    ''' makes a multicolored flower shape '''
    ln = s.Line(distance = 90, color='sienna' )
    ln.setWidth(3) 
    ln.draw( x, y, zpos=z, roll=0, pitch=-90, orientation=0)
    for i in range( 20 ):
        pt = s.Petal( distance = 5 )
        g = gc - (10*i)
        c = (r, g, b)
        pt.setColor( c )
        pt.setDistance( 3-(i/7) )
        pt.draw( x, y, zpos=z+(i*5), roll=0, pitch=0, orientation=i*50+137.5)
        

def pumpkin( x, y, z, i, count, color):   
    ''' makes a pumpkin shape '''
    body = s.Pentagon( distance=20 )
    body.setColor( color )
    body.setWidth( 2 )
    if i > 0:
        body.draw( x, y, zpos=z, pitch=-0 + count, orientation=18)
        body.setColor( 'orange' )
        body.draw( x, y, zpos=z, pitch=-90 + count, orientation=18)
        ln = s.Line(distance = 20, color='sienna' )
        ln.setWidth(6) 
        ln.draw( x, y, zpos=z, roll=0, pitch=0, orientation=45)
        
        
        i = i-1
        count = count + 60
        pumpkin(x, y, z, i, count, color)
        
def main():
    ''' makes an abstract scene with two dodecahedrons, two pumpkins, and two flowers '''

    deca = s.Dodecahedron( distance = 100 )
    deca.setWidth( 5 )
    deca.setStyle( 'goldish' )
    deca.draw( -100, -100, zpos = 0)
    decaFill = s.DodecahedronFill( distance = 50 )
    decaFill.draw( -200, 0, zpos = 100)
    flower( 100, 100, 0, (51, 244, 231) )
    flower( 200, 200, 0, (249, 227, 36) )
    pumpkin( 0, 0, 0, 6, 1, 'tomato' )
    pumpkin( 50, 50, 50, 6, 1, 'peachpuff' )
    
    ti.TurtleInterpreter().hold()


if __name__ == '__main__':
    main()