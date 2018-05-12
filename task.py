from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *
import  Texture_Class

import time
mouse_x = 0
mouse_y = 0
def myinit():
    global back_ground
    glClearColor(1, 1, 1, 1)
    glMatrixMode(GL_MODELVIEW)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 800, 0,800, 0, 100)  # l,r,b,t,n,f
    glMatrixMode(GL_MODELVIEW)
    back_ground =Texture_Class.Texture("123.jpg"  , 0 , 0 , 800)
#################################################################################

def mouse(x,y):
    global mouse_x , mouse_y, cur_y , cur_x, move_bug_X,  move_bug_Y
    move_bug_Y = 0
    move_bug_X = 0
    mouse_y = y
    mouse_y = mouse_y/100
    # mouse_y = min(8-mouse_y , mouse_y)
    mouse_x = x /100
    mouse_y = int(mouse_y)
    mouse_x = int(mouse_x)
    print(mouse_x+1 , mouse_y+1)

    if mouse_y > cur_y:
        mouse_y+=1
    if mouse_x < cur_x:
        mouse_x-=1
trans_x= 0
trans_y = 0
new_x = 0
new_y = 0
cur_x = 0
cur_y = 0
def find_new():
    global mouse_y  , mouse_x  , new_x , new_y
    my_y = 8 - mouse_y
    my_y = my_y * 100 + 65
    my_x = mouse_x * 100
    new_x = my_x
    new_y = my_y

move_bug_X = 0
move_bug_Y = 0

def draw1():
    global  back_ground  , mouse_y , mouse_x , new_y, new_x , cur_x  , cur_y, trans_x , trans_y, move_bug_X, move_bug_Y
    # time.sleep(0.00016)


    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)
    back_ground.render()
    glColor(1,0,0)
    glPushMatrix()
    # trans_x = min(750 , trans_x)
    # trans_x = max(50, trans_x)
    # trans_y= min(765 , trans_y)
    # trans_y = max(65, trans_y)

    if trans_x + 50  < 0:
        trans_x = 0
        move_bug_X = 1

    if trans_y + 765 < 0:
        trans_y = -700
        move_bug_Y= 1
    glTranslate(50 + trans_x, 765+trans_y, 0)
    cur_x = int((trans_x)/100)
    cur_y = int((700+trans_y) /100)
    cur_y = 7- cur_y
    glutSolidSphere(30  , 50 , 50 )

    if (cur_x != mouse_x or cur_y != mouse_y):
        a = 0
        if move_bug_X ==0:
            if cur_x > mouse_x:
                trans_x-= 1
                a=1
            if cur_x < mouse_x :
                trans_x += 1
                a=1
        if a ==0 and move_bug_Y == 0:
            if cur_y > mouse_y :
                trans_y += 1

            if cur_y < mouse_y:
                trans_y -= 1

    glPopMatrix()

    glutSwapBuffers()
###########################

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(800,800)
glutCreateWindow(b"CarOnRoad")
myinit()
glutDisplayFunc(draw1)
glutIdleFunc(draw1)
glutMotionFunc(mouse)
glutMainLoop()

