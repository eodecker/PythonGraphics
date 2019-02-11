# Eli Decker
# 4/28/17
# shapes.py
# version 5

import turtle_interpreter as ti

class Shape:
    
    def __init__(self, distance = 100, angle = 90, color = (0, 0, 0), istring = '' ):
        ''' creates shape with parameters for distance, angle, color, and string '''
        self.style = 'normal'
        self.jitterSigma = 2
        self.width = 1
        self.dotSize = 10
        # create a field of self called distance and assign it distance
        self.distance = distance
        # create a field of self called angle and assign it angle
        self.angle = angle
        # create a field of self called color and assign it color
        self.color = color
        # create a field of self called string and assign it istring
        self.string = istring
    
    def setStyle( self, style ):
        self.style = style
        
    def setJitter( self, jitterSigma ):
        self.jitterSigma = jitterSigma
        
    def setDotSize( self, dotSize ):
        self.dotSize = dotSize
        
    def setWidth( self, width ):
        self.width = width
        
    def setColor(self, c):
        ''' sets color '''
        self.color = c
        
    def setDistance(self, d):
        ''' sets distance '''
        self.distance = d
        
    def setAngle(self, a):
        ''' sets angle '''
        self.angle = a
        
    def setString(self, s):
        '''sets string'''
        self.string = s
        
    def draw(self, xpos, ypos, scale=1.0, orientation = 0, roll = 0, pitch = 0, zpos = 0):
        ''' uses turtle interpreter to draw object '''
        # create a TurtleInterpreter object
        terp = ti.TurtleInterpreter( )
        terp.setStyle( self.style )
        terp.setJitter( self.jitterSigma )
        terp.setDotSize( self.dotSize )
        terp.width( self.width )
        # have the TurtleInterpreter object place the turtle at (xpos, ypos, orientation)
        terp.place( xpos, ypos, orientation, zpos, pitch, roll )
        
        # have the TurtleInterpreter object set the turtle color to self.color
        terp.color( self.color )
        # have the TurtleInterpreter object draw the string
        terp.drawString( self.string, self.distance*scale, self.angle)
        #    Note: use the distance, angle, and string fields of self
        #    Note: multiply the distance by the scale parameter of the method

class Square(Shape):
    
    def __init__( self, distance=100, color=(0, 0, 0) ):
        ''' makes square '''
        # call the parent's __init__ method with distance,
        Shape.__init__( self, distance, 90, color, 'F-F-F-F-' ) 

class SquareFill(Shape):
    
    def __init__( self, distance=100, color=(0, 0, 0) ):
        ''' makes square '''
        # call the parent's __init__ method with distance,
        Shape.__init__( self, distance, 90, color, '{F-F-F-F-}' ) 
        

class Triangle(Shape):
    
    def __init__( self, distance=100, color=(0, 0, 0) ):
        ''' makes triangle '''
        # call the parent's __init__ method with distance,
        Shape.__init__( self, distance, 120, color, 'F-F-F-' ) 
         
         
class Pentagon(Shape):
    
    def __init__( self, distance=100, color=(0, 0, 0) ):
        ''' makes pentagon '''
        # call the parent's __init__ method with distance,
        Shape.__init__( self, distance, 72, color, 'F-F-F-F-F' )     

class Hexagon(Shape):
    
    def __init__( self, distance=100, color=(0, 0, 0) ):
        ''' makes hexagon '''
        # call the parent's __init__ method with distance,
        Shape.__init__( self, distance, 60, color, 'F-F-F-F-F-F-' ) 
        
class Septagon(Shape):
    
    def __init__( self, distance=100, color=(0, 0, 0) ):
        ''' makes septagon '''
        # call the parent's __init__ method with distance,
        Shape.__init__( self, distance, 51.4286, color, '{F-F-F-F-F-F-F-}' ) 
        
class Octagon(Shape):
    
    def __init__( self, distance=100, color=(0, 0, 0) ):
        ''' makes octagon '''
        # call the parent's __init__ method with distance,
        Shape.__init__( self, distance, 45, color, '{F-F-F-F-F-F-F-F-}' ) 
        
###New Shapes Below (for 3D project)
        
class Line( Shape ):
    
    def __init__( self, distance=100, color=(0, 0, 0), roll = 0, pitch = 0, zpos = 0):
        ''' initializes line object '''
        Shape.__init__(self, distance, 90, color, 'F' )

class Cube( Shape ):
    
    def __init__( self, distance=100, color=(0, 0, 0), roll = 0, pitch = 0, zpos = 0):
        ''' initializes cube object '''
        Shape.__init__(self, distance, 90, color, 'F+[F+[F+[F+(90)^F+F+F+F+](90)^F+F+F+F+](90)^F+F+F+F+](90)^F[+F+F+F+](90)&F+F+F+F+' )
 
class CubeFill( Shape ):
   
    def __init__( self, distance=100, color=(0, 0, 0), roll = 0, pitch = 0, zpos = 0):
        ''' initializes cube with fill object '''
        Shape.__init__(self, distance, 90, color, '{F+[F+[F+[F}+(90)^{F+F+F+F}+](90)^{F+F+F+F}+](90)^{F+F+F+F}+](90)^{F[+F+F+F}+](90)&{F+F+F+F}+' )
        
class Pyramid( Shape ):
   
    def __init__( self, distance=100, color=(0, 0, 0), roll = 0, pitch = 0, zpos = 0):
        ''' initializes pyramid object '''
        Shape.__init__(self, distance, 90, color, 'F[(45)^(135)+F(135)+(45)&F]&F[(45)^(135)+F(135)+(45)&F]&F[(45)^(135)+F(135)+(45)&F]&{F[(45)^(135)+F(135)+(45)&F]' )

class PyramidFill( Shape ):
   
    def __init__( self, distance=100, color=(0, 0, 0), roll = 0, pitch = 0, zpos = 0):
        ''' initializes pyramid with fill '''
        Shape.__init__(self, distance, 90, color, '[{(0)//F(90)+F(90)+F(90)+F}]{F[(45)^(135)+F(135)+(45)&F}]&{F[(45)^(135)+F(135)+(45)&F}]&{F[(45)^(135)+F(135)+(45)&F}]&{F[(45)^(135)+F(135)+(45)&F}]' )

class Circle( Shape ):
   
    def __init__( self, distance=100, color=(0, 0, 0), roll = 0, pitch = 0, zpos = 0):
        ''' initializes Circle object '''
        Shape.__init__(self, distance, 90, color, 'C' )
        
class RectanglePrism( Shape ):
    
    def __init__( self, distance=100, color=(0, 0, 0), roll = 0, pitch = 0, zpos = 0):
        ''' initializes rectangular prism '''
        Shape.__init__(self, distance, 90, color, 'F[+F&FF&F&FF]+F[+F&FF&F&FF]+F[+F&FF&F&FF]+F[+F&FF&F&FF]' )

class RectanglePrismFill( Shape ):
    
    def __init__( self, distance=100, color=(0, 0, 0), roll = 0, pitch = 0, zpos = 0):
        ''' initializes rectangular prism that is filled '''
        Shape.__init__(self, distance, 90, color, '{F+F+F+F}[+{F&FF&F&FF}]+F[+{F&FF&F&FF}]+F[+{F&FF&F&FF}]+F[+{F&FF}&[{F+F+F+F}]{F&FF}]' )
        
class TriangularPrism( Shape ):
    
    def __init__( self, distance=100, color=(0, 0, 0), roll = 0, pitch = 0, zpos = 0):
        ''' initializes tirangular prism '''
        Shape.__init__(self, distance, 120, color, 'F[+F(90)&FF(90)&F(90)&FF]+F[+F(90)&FF(90)&F(90)&FF]+F[+F(90)&FF(90)&[F+F+F]F(90)&FF]' )
        
class TriangularPrismFill( Shape ):
    
    def __init__( self, distance=100, color=(0, 0, 0), roll = 0, pitch = 0, zpos = 0):
        ''' initializes triangular prism that is filled '''
        Shape.__init__(self, distance, 120, color, '{F+F+F}[+{F(90)&FF(90)&F(90)&FF}]+F[+{F(90)&FF(90)&F(90)&FF}]+F[+{F(90)&FF}(90)&[{F+F+F}]{F(90)&FF}]' )

class Petal( Shape ):
    
    def __init__( self, distance=5, color=(0, 0, 0), roll = 0, pitch = 0, zpos = 0):
        ''' initializes petal object '''
        outline = '{FF(10)-FF(10)-FF(10)-FF(10)-FF(10)-FF(10)-FF(10)-FF(10)-FF(10)-F(82)-F(10)-FF(10)-FF(10)-FF(10)-FF(10)-FF(10)-FF(10)-FF(10)-FF(10)-FF(45)-F}'
        depth = '(90)^FF(60)&(45)-'
        istring = outline + depth + outline
        Shape.__init__(self, distance, 120, color, istring )
        
class Dodecahedron(Shape):
    
    def __init__( self, distance=100, color=(0, 0, 0), roll = 0, pitch = 0, zpos = 0 ):
        ''' makes Dodecahedron '''

        pentagons = '[F-F-F-F-f-f[(72)-(116.5605)\F-F-F-F-F]][(0)+(116.5605)\F-F-F-F-F]f-f[(-72)+(116.5605)\F-F-F-F-F]-f[(-72)+(116.5605)\F-F-F-F-F]-f[(-72)+(116.5605)\F-F-F-F-F]'
        connection2 = '(180)+(116.5605)//f(72)^(16.5)+f(19.5)+(72)^f(-72)+(108)//(10)^f(108)^(158)-f'
        connection = '@(180)^(-108)+'
        
        
        istring = pentagons + connection2 + connection + pentagons
        Shape.__init__( self, distance, 72, color, istring=istring )
        
class DodecahedronFill(Shape):
    
    def __init__( self, distance=100, color=(0, 0, 0), roll = 0, pitch = 0, zpos = 0 ):
        ''' makes Dodecahedron that is filled '''

        pentagons = '[{rF-F-F-F-F}-f[(72)-(116.5605)\{rF-F-F-F-F}]][(0)+(116.5605)\{rF-F-F-F-F}]f-f[(-72)+(116.5605)\{rF-F-F-F-F}]-f[(-72)+(116.5605)\{rF-F-F-F-F}]-f[(-72)+(116.5605)\{rF-F-F-F-F}]'
        connection2 = '(180)+(116.5605)//f(72)^(16.5)+f(19.5)+(72)^f(-72)+(108)//(10)^f(108)^(158)-f'
        connection = '@(180)^(-108)+'
        
        
        istring = pentagons + connection2 + connection + pentagons
        Shape.__init__( self, distance, 72, color, istring=istring )

        
def main():
    ''' makes a scene with a triangle, square, pentagon, hexagon,
    and septagon with rainbow colors '''
    
    scale = 0.8
    
    # create a triangle object and draw a bunch of them
    t = Triangle()
    t.setColor( "red" )
    t.draw(-380, -100, scale=scale, orientation=90)
    
    
    # create a square object and draw a bunch of them
    s = Square()
    s.setColor( "orange" )
    s.draw(-260, -100, scale=scale, orientation=90)
        
    p = Pentagon()
    p.setColor( "yellow" )
    p.draw(-140, -100, scale=scale, orientation=90)
    
    h = Hexagon()
    h.setColor( "green" )
    h.draw(20, -100, scale=scale, orientation=90)
    
    sept = Septagon()
    sept.setColor( "blue" )
    sept.draw(190, -100, scale=scale, orientation=90)

    # wait
    ti.TurtleInterpreter().hold()


if __name__ == '__main__':
    main()



