import pygame
import math
import random
import string

pygame.init()

# ================= إعدادات عامة =================
WIDTH, HEIGHT = 1800, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("8 دوّارات فيزيائية")
clock = pygame.time.Clock()

FONT = pygame.font.SysFont("arial", 22, bold=True)
BIG_FONT = pygame.font.SysFont("arial", 50, bold=True)

BG = (25, 25, 25)
POINTER_COLOR = (255, 255, 255)

RADIUS = 140

# ================= مراكز الدوّارات المضاعفة =================
ORIGINAL_CENTERS = [
    (200, 360),   # أرقام
    (550, 360),   # حروف
    (900, 360),   # رموز
    (1250, 360)   # أقواس واقتباسات
]

# مضاعفة كل مركز على المحور X (+250)
CENTERS = []
for x, y in ORIGINAL_CENTERS:
    CENTERS.append((x, y))          # الأصلية
    CENTERS.append((x+250, y))      # النسخة الثانية

# ================= دالة إنشاء العجلة =================
def new_wheel(center, labels):
    return {
        "center": center,
        "labels": labels,
        "angle": 0,
        "vel": 0,
        "drag": False,
        "last_mouse": 0,
        "result": None,
        "stopped": False
    }

# ================= بيانات الدوّارات =================
labels_list = [
    list(range(10)),                   # أرقام
    list(string.ascii_uppercase),      # كل الحروف
    list("!@#$%^&*?"),                 # رموز
    ['(', ')', '[', ']', '{', '}', '<', '>', '"', "'"]  # أقواس
]

# إنشاء العجلات 8 عجلات
wheels = []
for center, labels in zip(CENTERS, labels_list*2):  # نسخة لكل مركز مضاعف
    wheels.append(new_wheel(center, labels))

COLORS = [
    (255,99,71),(135,206,250),(255,215,0),(144,238,144),
    (221,160,221),(255,182,193),(173,216,230),(240,230,140),
    (255,160,122),(176,196,222)
]

active_wheel = None
results_order = []

# ================= دوال =================
def friction(v):
    return 0.995 - abs(v)*0.0005

def mouse_angle(pos, center):
    dx, dy = pos[0]-center[0], pos[1]-center[1]
    return math.atan2(dy, dx)

def inside_wheel(pos, center):
    dx = pos[0]-center[0]
    dy = pos[1]-center[1]
    return math.hypot(dx, dy) <= RADIUS

def draw_wheel(wheel):
    cx, cy = wheel["center"]
    labels = wheel["labels"]
    sections = len(labels)
    section_angle = 2 * math.pi / sections

    for i in range(sections):
        a1 = wheel["angle"] + i * section_angle
        a2 = a1 + section_angle

        pygame.draw.polygon(
            screen,
            COLORS[i % len(COLORS)],
            [(cx, cy),
             (cx + RADIUS * math.cos(a1), cy + RADIUS * math.sin(a1)),
             (cx + RADIUS * math.cos(a2), cy + RADIUS * math.sin(a2))]
        )

        ta = a1 + section_angle / 2
        tx = cx + (RADIUS - 35) * math.cos(ta)
        ty = cy + (RADIUS - 35) * math.sin(ta)
        txt = FONT.render(str(labels[i]), True, (0,0,0))
        screen.blit(txt, txt.get_rect(center=(tx, ty)))

    pygame.draw.circle(screen, (0,0,0), wheel["center"], RADIUS, 4)

    pygame.draw.polygon(
        screen, POINTER_COLOR,
        [(cx-10, cy-RADIUS-5),
         (cx+10, cy-RADIUS-5),
         (cx, cy-RADIUS-28)]
    )

def get_under_pointer(wheel):
    labels = wheel["labels"]
    sections = len(labels)
    section_angle = 2 * math.pi / sections
    norm = wheel["angle"] % (2 * math.pi)
    pointer = -math.pi / 2
    rel = (pointer - norm) % (2 * math.pi)
    return labels[int(rel // section_angle)]

# ================= الحلقة الرئيسية =================
running = True
while running:
    clock.tick(60)
    screen.fill(BG)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for w in wheels:
                if inside_wheel(pos, w["center"]):
                    active_wheel = w
                    w["drag"] = True
                    w["last_mouse"] = mouse_angle(pos, w["center"])
                    w["vel"] = 0
                    w["result"] = None
                    w["stopped"] = False
                    if w in results_order:
                        results_order.remove(w)

        if event.type == pygame.MOUSEBUTTONUP:
            if active_wheel:
                active_wheel["drag"] = False
                active_wheel["vel"] += random.uniform(-0.02, 0.02)
                active_wheel = None

        if event.type == pygame.MOUSEMOTION and active_wheel and active_wheel["drag"]:
            m = mouse_angle(pygame.mouse.get_pos(), active_wheel["center"])
            delta = m - active_wheel["last_mouse"]
            active_wheel["vel"] += delta * 18
            active_wheel["vel"] = max(-2, min(2, active_wheel["vel"]))
            active_wheel["last_mouse"] = m

    for w in wheels:
        w["angle"] += w["vel"]
        w["vel"] *= friction(w["vel"])

        if abs(w["vel"]) < 0.0005 and not w["drag"] and not w["stopped"]:
            w["vel"] = 0
            w["result"] = str(get_under_pointer(w))
            w["stopped"] = True
            results_order.append(w)

    for w in wheels:
        draw_wheel(w)

    # عرض النتائج أعلى الشاشة حسب ترتيب التوقف
    x_start = WIDTH//2 - 300
    y = 60
    for i, w in enumerate(results_order):
        txt = BIG_FONT.render(w["result"], True, (255,255,0))
        screen.blit(txt, txt.get_rect(center=(x_start + i*80, y)))

    pygame.display.flip()

pygame.quit()