import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

def draw_cone():
    radius = 1.5
    height = 3.0
    slices = 50
    # رسم القاعدة (دائرة)
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0.0, 0.4, 0.8) # لون القاعدة
    glVertex3f(0, 0, 0)
    for i in range(slices + 1):
        theta = i * 2.0 * math.pi / slices
        glVertex3f(radius * math.cos(theta), 0, radius * math.sin(theta))
    glEnd()

    # رسم جوانب المخروط
    glBegin(GL_TRIANGLE_STRIP)
    for i in range(slices + 1):
        theta = i * 2.0 * math.pi / slices
        glColor3f(0.0, 0.6, 1.0) # لون الجوانب
        glVertex3f(0, height, 0) # القمة
        glVertex3f(radius * math.cos(theta), 0, radius * math.sin(theta))
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Project 2: 3D Cone (Stable Version)")

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, -1.0, -10.0)
    glEnable(GL_DEPTH_TEST)

    angle = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        glRotatef(angle, 0, 1, 0) # تدوير حول المحور Y
        glRotatef(20, 1, 0, 0)    # إمالة قليلة لرؤية القاعدة
        
        draw_cone() # استدعاء دالة الرسم اليدوية
        
        glPopMatrix()
        angle += 1
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
