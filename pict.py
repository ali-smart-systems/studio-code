import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def main():
    # 1. تهيئة pygame أولاً
    pygame.init()
    
    # 2. تهيئة GLUT قبل إنشاء النافذة (خطوة حاسمة لتجنب خطأ Access Violation)
    glutInit(sys.argv)
    
    # 3. إنشاء النافذة
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("المشروع الثاني: 3D Solid Cone")

    # 4. إعداد الكاميرا والمنظور
    glMatrixMode(GL_PROJECTION) # تحديد أننا نعدل مصفوفة الإسقاط
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    
    glMatrixMode(GL_MODELVIEW) # العودة لمصفوفة الرؤية
    glTranslatef(0.0, 0.0, -10)
    
    # تفعيل الإضاءة والعمق
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glLightfv(GL_LIGHT0, GL_POSITION, (5, 5, 5, 1)) # وضع الإضاءة في مكان واضح

    angle = 0
    clock = pygame.time.Clock() # استخدام Clock للتحكم في السرعة بشكل أفضل

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        
        # تدوير الشكل
        glRotatef(angle, 1, 1, 1)
        
        # رسم المخروط
        glColor3f(0.0, 0.7, 1.0) # لون أزرق فاتح
        # تعديل اتجاه المخروط ليظهر بشكل أفضل
        glPushMatrix() 
        glRotatef(-90, 1, 0, 0)
        glutSolidCone(2, 4, 40, 40)
        glPopMatrix()
        
        glPopMatrix()
        
        angle += 1
        pygame.display.flip()
        clock.tick(60) # تحديد الإطارات بـ 60 إطار في الثانية

if __name__ == "__main__":
    main()
