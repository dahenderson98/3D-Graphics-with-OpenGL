import sys
import math

try:
    from OpenGL.GLUT import *
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from OpenGL.GL import glOrtho
    from OpenGL.GLU import gluPerspective
    from OpenGL.GL import glRotated
    from OpenGL.GL import glTranslated
    from OpenGL.GL import glLoadIdentity
    from OpenGL.GL import glMatrixMode
    from OpenGL.GL import GL_MODELVIEW
    from OpenGL.GL import GL_PROJECTION
except:
    print("ERROR: PyOpenGL not installed properly. ")

DISPLAY_WIDTH = 500.0
DISPLAY_HEIGHT = 500.0
CAM_X = 0.0
CAM_Y = 3.0
CAM_Z = 20.0
angle = 0.0
ortho = False

def init(): 
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glShadeModel (GL_FLAT)

def drawHouse ():
    glLineWidth(2.5)
    glColor3f(1.0, 0.0, 0.0)
    #Floor
    glBegin(GL_LINES)
    glVertex3f(-5.0, 0.0, -5.0)
    glVertex3f(5, 0, -5)
    glVertex3f(5, 0, -5)
    glVertex3f(5, 0, 5)
    glVertex3f(5, 0, 5)
    glVertex3f(-5, 0, 5)
    glVertex3f(-5, 0, 5)
    glVertex3f(-5, 0, -5)
    #Ceiling
    glVertex3f(-5, 5, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(5, 5, 5)
    glVertex3f(5, 5, 5)
    glVertex3f(-5, 5, 5)
    glVertex3f(-5, 5, 5)
    glVertex3f(-5, 5, -5)
    #Walls
    glVertex3f(-5, 0, -5)
    glVertex3f(-5, 5, -5)
    glVertex3f(5, 0, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(5, 0, 5)
    glVertex3f(5, 5, 5)
    glVertex3f(-5, 0, 5)
    glVertex3f(-5, 5, 5)
    #Door
    glVertex3f(-1, 0, 5)
    glVertex3f(-1, 3, 5)
    glVertex3f(-1, 3, 5)
    glVertex3f(1, 3, 5)
    glVertex3f(1, 3, 5)
    glVertex3f(1, 0, 5)
    #Roof
    glVertex3f(-5, 5, -5)
    glVertex3f(0, 8, -5)
    glVertex3f(0, 8, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(-5, 5, 5)
    glVertex3f(0, 8, 5)
    glVertex3f(0, 8, 5)
    glVertex3f(5, 5, 5)
    glVertex3f(0, 8, 5)
    glVertex3f(0, 8, -5)
    glEnd()

def display():
    glClear (GL_COLOR_BUFFER_BIT)
    glColor3f (1.0, 1.0, 1.0)
    # viewing transformation
    global DISPLAY_WIDTH, DISPLAY_HEIGHT, CAM_Z, CAM_X, CAM_Y, angle, ortho

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslated(-CAM_X, -CAM_Y, -CAM_Z)
    glRotated(angle, 0.0, 1.0, 0.0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if ortho:
        # glOrtho(0.0, DISPLAY_WIDTH, 0, DISPLAY_HEIGHT, 0.0, 1.0)
        glOrtho(-10,10,-10,10,-100,100)
    else:
        gluPerspective(60.0,1.0,0.0,100.0)

    drawHouse()

    glFlush()
    

def keyboard(key, x, y):
    global CAM_X, CAM_Y, CAM_Z, angle, ortho

    if key == chr(27):
        import sys
        sys.exit(0)
  
    elif key == b'w':
        # print("key pressed")
        # CAM_Z += math.sin(angle)
        # CAM_X += math.cos(angle)
        CAM_Z -= 1

    elif key == b's':
        # print("key pressed")
        # CAM_Z -= math.sin(angle)
        # CAM_X -= math.cos(angle)
        CAM_Z += 1

    elif key == b'a':
        # print("key pressed")
        # CAM_X -= math.cos(angle)
        # CAM_Z -= math.sin(angle)
        CAM_X -= 1

    elif key == b'd':
        # print("key pressed")
        # CAM_X += math.cos(angle)
        # CAM_Z += math.cos(angle)
        CAM_X += 1

    elif key == b'r':
        # print("key pressed")
        CAM_Y += 1

    elif key == b'f':
        # print("key pressed")
        CAM_Y -= 1

    elif key == b'q':
        # print("key pressed")
        angle -= 5

    elif key == b'e':
        # print("key pressed")
        angle += 5

    elif key == b'h':
        # print("key pressed")
        CAM_X = 0.0
        CAM_Y = 3.0
        CAM_Z = 20.0
        angle = 0.0
        ortho = False

    elif key == b'o':
        # print("key pressed")
        ortho = True

    elif key == b'p':
        # print("key pressed")
        ortho = False
  
    #Your Code Here
  
    glutPostRedisplay()


glutInit(sys.argv)
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize (int(DISPLAY_WIDTH), int(DISPLAY_HEIGHT))
glutInitWindowPosition (100, 100)
glutCreateWindow (b'OpenGL Lab')
init ()
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glutMainLoop()
