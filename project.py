# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 14:03:16 2023

@author: Théo
"""

# Importing the necessary Modules
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time


# Color order : 
#     U, R, F, D, L, B

dim = 0.5
gap = 0.03

colorsCode = {
    "red" : [1, 0, 0],
    "green" : [0, 1, 0],
    "blue" : [0, 0, 1],
    "yellow" : [1, 1, 0],
    "orange" : [1, 0.5, 0],
    "white" : [1, 1, 1],
    "grey" : [0.2, 0.2, 0.2]
}

idPositions = {
    0 : (1, 1, 1),
    1 : (1, 1, 0),
    2 : (1, 1, -1),
    3 : (0, 1, 1),
    4 : (0, 1, 0),
    5 : (0, 1, -1),
    6 : (-1, 1, 1),
    7 : (-1, 1, 0),
    8 : (-1, 1, -1),
    9 : (1, 0, 1),
    10 : (1, 0, 0),
    11 : (1, 0, -1),
    12 : (0, 0, 1),
    13 : (0, 0, 0),
    14 : (0, 0, -1),
    15 : (-1, 0, 1),
    16 : (-1, 0, 0),
    17 : (-1, 0, -1),
    18 : (1, -1, 1),
    19 : (1, -1, 0),
    20 : (1, -1, -1),
    21 : (0, -1, 1),
    22 : (0, -1, 0),
    23 : (0, -1, -1),
    24 : (-1, -1, 1),
    25 : (-1, -1, 0),
    26 : (-1, -1, -1)
}

def display():
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)
    # Reset background
    glClearColor(0.7, 0.7, 0.7, 0)
    # Reset background
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # Render scene
    render_Scene()
    # Swap buffers
    glutSwapBuffers()
 
def render_Scene(): # Scene render function
    
    drawReferential(20)
    
    drawCube()
    
def reshape(x,y):
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity()
    
    gluPerspective(45, x/y, 1, 100.0)
    
    gluLookAt(5, 5, 5,  # Position de la caméra (eye)
              0, 0, 0,  # Point où la caméra regarde (at)
              0, 1, 0)   # Vecteur d'orientation vers le haut (up)
    
    glViewport(0, 0, x, y) # Use the whole window for rendering 
    
def drawCube() :
    # First layer
    drawPiece(0, ["yellow", "orange", "green", "grey", "grey", "grey"])
    drawPiece(1, ["yellow", "orange", "grey", "grey", "grey", "grey"])
    drawPiece(2, ["yellow", "orange", "grey", "grey", "grey", "blue"])
    drawPiece(3, ["yellow", "grey", "green", "grey", "grey", "grey"])
    drawPiece(4, ["yellow", "grey", "grey", "grey", "grey", "grey"])
    drawPiece(5, ["yellow", "grey", "grey", "grey", "grey", "blue"])
    drawPiece(6, ["yellow", "grey", "green", "grey", "red", "grey"])
    drawPiece(7, ["yellow", "grey", "grey", "grey", "red", "grey"])
    drawPiece(8, ["yellow", "grey", "grey", "grey", "red", "blue"])
    
    # Second layer
    drawPiece(9, ["grey", "orange", "green", "grey", "grey", "grey"])
    drawPiece(10, ["grey", "orange", "grey", "grey", "grey", "grey"])
    drawPiece(11, ["grey", "orange", "grey", "grey", "grey", "blue"])
    drawPiece(12, ["grey", "grey", "green", "grey", "grey", "grey"])
    drawPiece(13, ["grey", "grey", "grey", "grey", "grey", "grey"])
    drawPiece(14, ["grey", "grey", "grey", "grey", "grey", "blue"])
    drawPiece(15, ["grey", "grey", "green", "grey", "red", "grey"])
    drawPiece(16, ["grey", "grey", "grey", "grey", "red", "grey"])
    drawPiece(17, ["grey", "grey", "grey", "grey", "red", "blue"])
    
    # Third layer
    drawPiece(18, ["grey", "orange", "green", "white", "grey", "grey"])
    drawPiece(19, ["grey", "orange", "grey", "white", "grey", "grey"])
    drawPiece(20, ["grey", "orange", "grey", "white", "grey", "blue"])
    drawPiece(21, ["grey", "grey", "green", "white", "grey", "grey"])
    drawPiece(22, ["grey", "grey", "grey", "white", "grey", "grey"])
    drawPiece(23, ["grey", "grey", "grey", "white", "grey", "blue"])
    drawPiece(24, ["grey", "grey", "green", "white", "red", "grey"])
    drawPiece(25, ["grey", "grey", "grey", "white", "red", "grey"])
    drawPiece(26, ["grey", "grey", "grey", "white", "red", "blue"])
    
def drawPiece(idPiece, listColors) :
    (x, y, z) = idPositions[idPiece]
    
    centerx, centery, centerz = x * (dim + gap), y * (dim + gap), z * (dim + gap)
    
    # Up
    glBegin(GL_POLYGON);
    glColor3f(*colorsCode[listColors[0]]);
    glVertex3f( centerx - dim/2, centery + dim/2, centerz - dim/2 )
    glVertex3f( centerx + dim/2, centery + dim/2, centerz - dim/2 )
    glVertex3f( centerx + dim/2, centery + dim/2, centerz + dim/2 )
    glVertex3f( centerx - dim/2, centery + dim/2, centerz + dim/2 )
    glEnd();
    
    # Right
    glBegin(GL_POLYGON);
    glColor3f(*colorsCode[listColors[1]]);
    glVertex3f( centerx + dim/2, centery + dim/2, centerz - dim/2 )
    glVertex3f( centerx + dim/2, centery - dim/2, centerz - dim/2 )
    glVertex3f( centerx + dim/2, centery - dim/2, centerz + dim/2 )
    glVertex3f( centerx + dim/2, centery + dim/2, centerz + dim/2 )
    glEnd();
    
    # Front
    glBegin(GL_POLYGON);
    glColor3f(*colorsCode[listColors[2]]);
    glVertex3f( centerx + dim/2, centery + dim/2, centerz + dim/2 )
    glVertex3f( centerx + dim/2, centery - dim/2, centerz + dim/2 )
    glVertex3f( centerx - dim/2, centery - dim/2, centerz + dim/2 )
    glVertex3f( centerx - dim/2, centery + dim/2, centerz + dim/2 )
    glEnd();
    
    # Down
    glBegin(GL_POLYGON);
    glColor3f(*colorsCode[listColors[3]]);
    glVertex3f( centerx - dim/2, centery - dim/2, centerz - dim/2 )
    glVertex3f( centerx + dim/2, centery - dim/2, centerz - dim/2 )
    glVertex3f( centerx + dim/2, centery - dim/2, centerz + dim/2 )
    glVertex3f( centerx - dim/2, centery - dim/2, centerz + dim/2 )
    glEnd();
    
    # Left
    glBegin(GL_POLYGON);
    glColor3f(*colorsCode[listColors[4]]);
    glVertex3f( centerx - dim/2, centery + dim/2, centerz - dim/2 )
    glVertex3f( centerx - dim/2, centery - dim/2, centerz - dim/2 )
    glVertex3f( centerx - dim/2, centery - dim/2, centerz + dim/2 )
    glVertex3f( centerx - dim/2, centery + dim/2, centerz + dim/2 )
    glEnd();
    
    # Back
    glBegin(GL_POLYGON);
    glColor3f(*colorsCode[listColors[5]]);
    glVertex3f( centerx + dim/2, centery + dim/2, centerz - dim/2 )
    glVertex3f( centerx + dim/2, centery - dim/2, centerz - dim/2 )
    glVertex3f( centerx - dim/2, centery - dim/2, centerz - dim/2 )
    glVertex3f( centerx - dim/2, centery + dim/2, centerz - dim/2 )
    glEnd();
   
def drawReferential(length):
    drawArrow(2, [1, 0, 0], [0, 0, 0], [length, 0, 0], 'x') # axe x
    drawArrow(2, [0, 1, 0], [0, 0, 0], [0, length, 0], 'y') # axe y
    drawArrow(2, [0, 0, 1], [0, 0, 0], [0, 0, length], 'z') # axe z 
    
def drawArrow(size, color, start, end, axe):
    glLineWidth(size)
    
    glBegin(GL_LINES)
    
    glColor3f(color[0], color[1], color[2])
    
    # Arrow
    glVertex3f(start[0], start[1], start[2])
    glVertex3f(end[0], end[1], end[2])
    
    # Arrowhead
    if (axe == 'x') :
        glVertex3f(end[0], end[1], end[2])
        glVertex3f(end[0]-0.1, end[1]+0.03, end[2])
        
        glVertex3f(end[0], end[1], end[2])
        glVertex3f(end[0]-0.1, end[1]-0.03, end[2])
        
        
        glVertex3f(end[0], end[1], end[2])
        glVertex3f(end[0]-0.1, end[1], end[2]+0.03)
        
        glVertex3f(end[0], end[1], end[2])
        glVertex3f(end[0]-0.1, end[1], end[2]-0.03)
    elif (axe == 'y') :
        glVertex3f(end[0], end[1], end[2])
        glVertex3f(end[0]-0.03, end[1]-0.1, end[2])
        
        glVertex3f(end[0], end[1], end[2])
        glVertex3f(end[0]+0.03, end[1]-0.1, end[2])
        
        
        glVertex3f(end[0], end[1], end[2])
        glVertex3f(end[0], end[1]-0.1, end[2]+0.03)
        
        glVertex3f(end[0], end[1], end[2])
        glVertex3f(end[0], end[1]-0.1, end[2]-0.03)
    elif (axe == 'z') :
        glVertex3f(end[0], end[1], end[2])
        glVertex3f(end[0]-0.03, end[1], end[2]-0.1)
        
        glVertex3f(end[0], end[1], end[2])
        glVertex3f(end[0]+0.03, end[1], end[2]-0.1)
        
        
        glVertex3f(end[0], end[1], end[2])
        glVertex3f(end[0], end[1]-0.03, end[2]-0.1)
        
        glVertex3f(end[0], end[1], end[2])
        glVertex3f(end[0], end[1]+0.03, end[2]-0.1)
        
    glEnd()
    
def drawCorner(size, color1, color2, color3, position) :
    # TOP
    glBegin(GL_POLYGON);
    glColor3f(*color1);
    glVertex3f( size - position[0] * 2 * (size + 0.03), size, size );
    glVertex3f( size - position[0] * 2 * (size + 0.03), size, -size );
    glVertex3f( -size - position[0] * 2 * (size + 0.03), size, -size );
    glVertex3f( -size - position[0] * 2 * (size + 0.03), size, size );
    glEnd();
    
    # FRONT
    glBegin(GL_POLYGON);
    glColor3f(*color2);
    glVertex3f( size - position[0] * 2 * (size + 0.03), -size, -size );
    glVertex3f( size - position[0] * 2 * (size + 0.03), size, -size ); 
    glVertex3f( -size - position[0] * 2 * (size + 0.03), size, -size ); 
    glVertex3f( -size - position[0] * 2 * (size + 0.03), -size, -size ); 
    glEnd();
    
    # RIGHT
    glBegin(GL_POLYGON);
    glColor3f(*color3);
    glVertex3f( size - position[0] * 2 * (size + 0.03), -size, -size );
    glVertex3f( size - position[0] * 2 * (size + 0.03), size, -size );
    glVertex3f( size - position[0] * 2 * (size + 0.03), size, size );
    glVertex3f( size - position[0] * 2 * (size + 0.03), -size, size );
    glEnd();
    
    # BACK - Black
    glBegin(GL_POLYGON);
    glColor3f(0, 0, 0);
    glVertex3f( size - position[0] * 2 * (size + 0.03), -size, size );
    glVertex3f( size - position[0] * 2 * (size + 0.03), size, size );
    glVertex3f( -size - position[0] * 2 * (size + 0.03), size, size );
    glVertex3f( -size - position[0] * 2 * (size + 0.03), -size, size );
    glEnd();
     
    # LEFT- Black
    glBegin(GL_POLYGON);
    glColor3f( 0.0, 0, 0);
    glVertex3f( -size - position[0] * 2 * (size + 0.03), -size, size );
    glVertex3f( -size - position[0] * 2 * (size + 0.03), size, size );
    glVertex3f( -size - position[0] * 2 * (size + 0.03), size, -size );
    glVertex3f( -size - position[0] * 2 * (size + 0.03), -size, -size );
    glEnd();
    
    # BOTTOM - Black
    glBegin(GL_POLYGON);
    glColor3f( 0.0, 0.0, 0.0 );
    glVertex3f( size - position[0] * 2 * (size + 0.03), -size, -size );
    glVertex3f( size - position[0] * 2 * (size + 0.03), -size, size );
    glVertex3f( -size - position[0] * 2 * (size + 0.03), -size, size );
    glVertex3f( -size - position[0] * 2 * (size + 0.03), -size, -size );
    glEnd();

 
# Initialize GLUT
glutInit()

# Initialize the window with double buffering and RGB colors
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    
# Set the window size to 500x500 pixels
glutInitWindowSize(600, 600)

# Create the window and give it a title
glutCreateWindow("My First OpenGL Window")

# Set the initial window position to (50, 50)
glutInitWindowPosition(50, 50)

# Define callbacks
glutDisplayFunc(display)
glutReshapeFunc(reshape)


# Begin event loop
glutMainLoop()
