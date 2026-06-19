# # # # # import pygame
# # # # # import sys
# # # # # import math

# # # # # # إعداد نافذة العرض
# # # # # pygame.init()
# # # # # WIDTH, HEIGHT = 600, 600
# # # # # screen = pygame.display.set_mode((WIDTH, HEIGHT))
# # # # # pygame.display.set_caption("Wheel Simulation")

# # # # # clock = pygame.time.Clock()

# # # # # # إعداد العجلة
# # # # # wheel_radius = 100
# # # # # wheel_center = (WIDTH // 2, HEIGHT // 2)
# # # # # wheel_angle = 0.0
# # # # # angular_velocity = 0.0
# # # # # friction = 0.99  # معامل الاحتكاك لتقليل السرعة تدريجياً

# # # # # dragging = False
# # # # # last_mouse_x = None

# # # # # # حلقة اللعبة
# # # # # while True:
# # # # #     for event in pygame.event.get():
# # # # #         if event.type == pygame.QUIT:
# # # # #             pygame.quit()
# # # # #             sys.exit()

# # # # #         # بداية السحب بالماوس
# # # # #         if event.type == pygame.MOUSEBUTTONDOWN:
# # # # #             dragging = True
# # # # #             last_mouse_x = event.pos[0]

# # # # #         # نهاية السحب
# # # # #         if event.type == pygame.MOUSEBUTTONUP:
# # # # #             dragging = False

# # # # #     if dragging:
# # # # #         mouse_x = pygame.mouse.get_pos()[0]
# # # # #         delta_x = mouse_x - last_mouse_x
# # # # #         angular_velocity += delta_x * 0.01  # قوة السحب تتحول لسرعة دوران
# # # # #         last_mouse_x = mouse_x

# # # # #     # تحديث زاوية العجلة
# # # # #     wheel_angle += angular_velocity
# # # # #     angular_velocity *= friction  # تقليل السرعة تدريجياً (احتكاك)

# # # # #     # رسم الخلفية
# # # # #     screen.fill((30, 30, 30))

# # # # #     # رسم العجلة (دائرة)
# # # # #     pygame.draw.circle(screen, (200, 200, 200), wheel_center, wheel_radius, 5)

# # # # #     # رسم خط يوضح اتجاه الدوران
# # # # #     line_x = wheel_center[0] + wheel_radius * math.cos(math.radians(wheel_angle))
# # # # #     line_y = wheel_center[1] + wheel_radius * math.sin(math.radians(wheel_angle))
# # # # #     pygame.draw.line(screen, (255, 0, 0), wheel_center, (line_x, line_y), 5)

# # # # #     pygame.display.flip()
# # # # #     clock.tick(60)








# # # # import pygame
# # # # import sys
# # # # import math

# # # # # إعداد نافذة العرض
# # # # pygame.init()
# # # # WIDTH, HEIGHT = 600, 600
# # # # screen = pygame.display.set_mode((WIDTH, HEIGHT))
# # # # pygame.display.set_caption("Realistic Bicycle Wheel")

# # # # clock = pygame.time.Clock()

# # # # # إعداد العجلة
# # # # wheel_radius = 120
# # # # wheel_center = (WIDTH // 2, HEIGHT // 2)
# # # # wheel_angle = 0.0
# # # # angular_velocity = 0.05
# # # # friction = 0.999

# # # # dragging = False
# # # # last_mouse_x = None

# # # # # إعداد الأسلاك (spokes)
# # # # num_spokes = 32

# # # # def draw_wheel(angle):
# # # #     # إطار خارجي (الإطار المطاطي)
# # # #     pygame.draw.circle(screen, (20, 20, 20), wheel_center, wheel_radius, 20)

# # # #     # إطار معدني داخلي
# # # #     pygame.draw.circle(screen, (180, 180, 180), wheel_center, wheel_radius - 10, 5)

# # # #     # المحور
# # # #     pygame.draw.circle(screen, (100, 100, 100), wheel_center, 10)

# # # #     # رسم الأسلاك
# # # #     for i in range(num_spokes):
# # # #         spoke_angle = math.radians(angle + (360 / num_spokes) * i)
# # # #         x = wheel_center[0] + (wheel_radius - 15) * math.cos(spoke_angle)
# # # #         y = wheel_center[1] + (wheel_radius - 15) * math.sin(spoke_angle)

# # # #         # اجعل السنارة رقم 0 باللون الأحمر، والباقي فضي
# # # #         color = (255, 0, 0) if i == 0 else (200, 200, 200)
# # # #         pygame.draw.line(screen, color, wheel_center, (x, y), 2)
# # # # # حلقة اللعبة
# # # # while True:
# # # #     for event in pygame.event.get():
# # # #         if event.type == pygame.QUIT:
# # # #             pygame.quit()
# # # #             sys.exit()

# # # #         if event.type == pygame.MOUSEBUTTONDOWN:
# # # #             dragging = True
# # # #             last_mouse_x = event.pos[0]

# # # #         if event.type == pygame.MOUSEBUTTONUP:
# # # #             dragging = False

# # # #     if dragging:
# # # #         mouse_x = pygame.mouse.get_pos()[0]
# # # #         delta_x = mouse_x - last_mouse_x
# # # #         angular_velocity += delta_x * 0.05
# # # #         last_mouse_x = mouse_x

# # # #     wheel_angle += angular_velocity
# # # #     angular_velocity *= friction

# # # #     screen.fill((30, 30, 30))
# # # #     draw_wheel(wheel_angle)
# # # #     pygame.display.flip()
# # # #     clock.tick(60)









# # # import pygame
# # # import sys
# # # import math

# # # # إعداد نافذة العرض
# # # pygame.init()
# # # WIDTH, HEIGHT = 600, 600
# # # screen = pygame.display.set_mode((WIDTH, HEIGHT))
# # # pygame.display.set_caption("Realistic Bicycle Wheel Simulation")

# # # clock = pygame.time.Clock()

# # # # إعداد العجلة
# # # wheel_radius = 120
# # # wheel_center = (WIDTH // 2, HEIGHT // 2)
# # # wheel_angle = 0.0
# # # angular_velocity = 0.0
# # # friction = 0.995   # معامل الاحتكاك (كلما كان أقرب لـ1 العجلة تستمر بالدوران أكثر)

# # # dragging = False
# # # last_mouse_x = None

# # # # عدد الأسلاك
# # # num_spokes = 32

# # # def draw_wheel(angle):
# # #     # إطار خارجي (الإطار المطاطي)
# # #     pygame.draw.circle(screen, (20, 20, 20), wheel_center, wheel_radius, 20)

# # #     # إطار معدني داخلي
# # #     pygame.draw.circle(screen, (180, 180, 180), wheel_center, wheel_radius - 10, 5)

# # #     # المحور
# # #     pygame.draw.circle(screen, (100, 100, 100), wheel_center, 10)

# # #     # رسم الأسلاك
# # #     for i in range(num_spokes):
# # #         spoke_angle = math.radians(angle + (360 / num_spokes) * i)
# # #         x = wheel_center[0] + (wheel_radius - 15) * math.cos(spoke_angle)
# # #         y = wheel_center[1] + (wheel_radius - 15) * math.sin(spoke_angle)

# # #         # اجعل السنارة رقم 0 باللون الأحمر والباقي فضي
# # #         color = (255, 0, 0) if i == 0 else (200, 200, 200)
# # #         pygame.draw.line(screen, color, wheel_center, (x, y), 2)

# # # # حلقة اللعبة
# # # while True:
# # #     for event in pygame.event.get():
# # #         if event.type == pygame.QUIT:
# # #             pygame.quit()
# # #             sys.exit()

# # #         if event.type == pygame.MOUSEBUTTONDOWN:
# # #             dragging = True
# # #             last_mouse_x = event.pos[0]

# # #         if event.type == pygame.MOUSEBUTTONUP:
# # #             dragging = False

# # #     if dragging:
# # #         mouse_x = pygame.mouse.get_pos()[0]
# # #         delta_x = mouse_x - last_mouse_x
# # #         angular_velocity += delta_x * 0.05   # قوة السحب تتحول لسرعة دوران
# # #         last_mouse_x = mouse_x

# # #     # تحديث زاوية العجلة
# # #     wheel_angle += angular_velocity
# # #     angular_velocity *= friction  # تقليل السرعة تدريجياً (احتكاك)

# # #     # رسم الخلفية والعجلة
# # #     screen.fill((30, 30, 30))
# # #     draw_wheel(wheel_angle)
# # #     pygame.display.flip()
# # #     clock.tick(60)






# # import pygame
# # import sys
# # import math

# # # إعداد نافذة العرض
# # pygame.init()
# # WIDTH, HEIGHT = 600, 600
# # screen = pygame.display.set_mode((WIDTH, HEIGHT))
# # pygame.display.set_caption("Wheel with Symbols")

# # clock = pygame.time.Clock()

# # # إعداد العجلة
# # wheel_radius = 120
# # wheel_center = (WIDTH // 2, HEIGHT // 2)
# # wheel_angle = 0.0
# # angular_velocity = 0.0
# # friction = 0.995

# # dragging = False
# # last_mouse_x = None

# # # عدد الأسلاك
# # num_spokes = 32

# # # قائمة الرموز (أرقام + حروف + رموز خاصة)
# # symbols = [
# #     "A","B","C","D","E","F","G","H",
# #     "1","2","3","4","5","6","7","8",
# #     "!","@","#","$","%","^","&","*",
# #     "X","Y","Z","0","+","-","=","?"
# # ]

# # # تأكد أن طول القائمة يساوي عدد الأسلاك
# # assert len(symbols) == num_spokes

# # # خط لكتابة النص في أعلى الشاشة
# # font = pygame.font.SysFont("Arial", 32)
# # selected_symbol = ""

# # def draw_wheel(angle):
# #     # إطار خارجي (الإطار المطاطي)
# #     pygame.draw.circle(screen, (20, 20, 20), wheel_center, wheel_radius, 20)

# #     # إطار معدني داخلي
# #     pygame.draw.circle(screen, (180, 180, 180), wheel_center, wheel_radius - 10, 5)

# #     # المحور
# #     pygame.draw.circle(screen, (100, 100, 100), wheel_center, 10)

# #     # رسم الأسلاك + الرموز
# #     for i in range(num_spokes):
# #         spoke_angle = math.radians(angle + (360 / num_spokes) * i)
# #         x = wheel_center[0] + (wheel_radius - 15) * math.cos(spoke_angle)
# #         y = wheel_center[1] + (wheel_radius - 15) * math.sin(spoke_angle)

# #         # اجعل السنارة رقم 0 باللون الأحمر والباقي فضي
# #         color = (255, 0, 0) if i == 0 else (200, 200, 200)
# #         pygame.draw.line(screen, color, wheel_center, (x, y), 2)

# #         # موقع الرمز خارج العجلة قليلاً
# #         text_x = wheel_center[0] + (wheel_radius + 30) * math.cos(spoke_angle)
# #         text_y = wheel_center[1] + (wheel_radius + 30) * math.sin(spoke_angle)

# #         text_surface = font.render(symbols[i], True, (255, 255, 255))
# #         text_rect = text_surface.get_rect(center=(text_x, text_y))
# #         screen.blit(text_surface, text_rect)

# #     # تحديد الرمز الذي يشير إليه السلك الأحمر
# #     # السلك الأحمر هو i == 0
# #     red_spoke_angle = math.radians(angle)
# #     red_x = wheel_center[0] + (wheel_radius + 30) * math.cos(red_spoke_angle)
# #     red_y = wheel_center[1] + (wheel_radius + 30) * math.sin(red_spoke_angle)

# #     # إيجاد أقرب رمز للسلك الأحمر
# #     min_dist = float("inf")
# #     closest_symbol = ""
# #     for i in range(num_spokes):
# #         spoke_angle = math.radians(angle + (360 / num_spokes) * i)
# #         text_x = wheel_center[0] + (wheel_radius + 30) * math.cos(spoke_angle)
# #         text_y = wheel_center[1] + (wheel_radius + 30) * math.sin(spoke_angle)
# #         dist = math.hypot(red_x - text_x, red_y - text_y)
# #         if dist < min_dist:
# #             min_dist = dist
# #             closest_symbol = symbols[i]

# #     return closest_symbol

# # # حلقة اللعبة
# # while True:
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             pygame.quit()
# #             sys.exit()

# #         if event.type == pygame.MOUSEBUTTONDOWN:
# #             dragging = True
# #             last_mouse_x = event.pos[0]

# #         if event.type == pygame.MOUSEBUTTONUP:
# #             dragging = False

# #     if dragging:
# #         mouse_x = pygame.mouse.get_pos()[0]
# #         delta_x = mouse_x - last_mouse_x
# #         angular_velocity += delta_x * 0.05
# #         last_mouse_x = mouse_x

# #     wheel_angle += angular_velocity
# #     angular_velocity *= friction

# #     screen.fill((30, 30, 30))
# #     selected_symbol = draw_wheel(wheel_angle)

# #     # عرض الرمز في أعلى الشاشة
# #     header_surface = font.render(f"Selected: {selected_symbol}", True, (255, 255, 0))
# #     header_rect = header_surface.get_rect(center=(WIDTH // 2, 40))
# #     screen.blit(header_surface, header_rect)

# #     pygame.display.flip()
# #     clock.tick(60)









# import pygame
# import sys
# import math

# # إعداد نافذة العرض
# pygame.init()
# WIDTH, HEIGHT = 600, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Wheel with Fixed Symbols")

# clock = pygame.time.Clock()

# # إعداد العجلة
# wheel_radius = 120
# wheel_center = (WIDTH // 2, HEIGHT // 2)
# wheel_angle = 0.0
# angular_velocity = 0.0
# friction = 0.995

# dragging = False
# last_mouse_x = None

# # عدد الأسلاك
# num_spokes = 32

# # قائمة الرموز (أرقام + حروف + رموز خاصة)
# symbols = [
#     "A","B","C","D","E","F","G","H",
#     "1","2","3","4","5","6","7","8",
#     "!","@","#","$","%","^","&","*",
#     "X","Y","Z","0","+","-","=","?"
# ]

# assert len(symbols) == num_spokes

# # خط لكتابة النص في أعلى الشاشة
# font = pygame.font.SysFont("Arial", 32)
# selected_symbol = ""

# def draw_wheel(angle):
#     # إطار خارجي (الإطار المطاطي)
#     pygame.draw.circle(screen, (20, 20, 20), wheel_center, wheel_radius, 20)

#     # إطار معدني داخلي
#     pygame.draw.circle(screen, (180, 180, 180), wheel_center, wheel_radius - 10, 5)

#     # المحور
#     pygame.draw.circle(screen, (100, 100, 100), wheel_center, 10)

#     # رسم الأسلاك (تدور مع العجلة)
#     for i in range(num_spokes):
#         spoke_angle = math.radians(angle + (360 / num_spokes) * i)
#         x = wheel_center[0] + (wheel_radius - 15) * math.cos(spoke_angle)
#         y = wheel_center[1] + (wheel_radius - 15) * math.sin(spoke_angle)

#         color = (255, 0, 0) if i == 0 else (200, 200, 200)
#         pygame.draw.line(screen, color, wheel_center, (x, y), 2)

#     # رسم الرموز ثابتة حول العجلة (لا تدور)
#     for i in range(num_spokes):
#         fixed_angle = math.radians((360 / num_spokes) * i)  # زاوية ثابتة
#         text_x = wheel_center[0] + (wheel_radius + 30) * math.cos(fixed_angle)
#         text_y = wheel_center[1] + (wheel_radius + 30) * math.sin(fixed_angle)

#         text_surface = font.render(symbols[i], True, (255, 255, 255))
#         text_rect = text_surface.get_rect(center=(text_x, text_y))
#         screen.blit(text_surface, text_rect)

#     # تحديد الرمز الذي يشير إليه السلك الأحمر
#     red_spoke_angle = math.radians(angle)
#     red_x = wheel_center[0] + (wheel_radius + 30) * math.cos(red_spoke_angle)
#     red_y = wheel_center[1] + (wheel_radius + 30) * math.sin(red_spoke_angle)

#     min_dist = float("inf")
#     closest_symbol = ""
#     for i in range(num_spokes):
#         fixed_angle = math.radians((360 / num_spokes) * i)
#         text_x = wheel_center[0] + (wheel_radius + 30) * math.cos(fixed_angle)
#         text_y = wheel_center[1] + (wheel_radius + 30) * math.sin(fixed_angle)
#         dist = math.hypot(red_x - text_x, red_y - text_y)
#         if dist < min_dist:
#             min_dist = dist
#             closest_symbol = symbols[i]

#     return closest_symbol

# # حلقة اللعبة
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#         if event.type == pygame.MOUSEBUTTONDOWN:
#             dragging = True
#             last_mouse_x = event.pos[0]

#         if event.type == pygame.MOUSEBUTTONUP:
#             dragging = False

#     if dragging:
#         mouse_x = pygame.mouse.get_pos()[0]
#         delta_x = mouse_x - last_mouse_x
#         angular_velocity += delta_x * 0.05
#         last_mouse_x = mouse_x

#     wheel_angle += angular_velocity
#     angular_velocity *= friction

#     screen.fill((30, 30, 30))
#     selected_symbol = draw_wheel(wheel_angle)

#     # عرض الرمز في أعلى الشاشة
#     header_surface = font.render(f"Selected: {selected_symbol}", True, (255, 255, 0))
#     header_rect = header_surface.get_rect(center=(WIDTH // 2, 40))
#     screen.blit(header_surface, header_rect)

#     pygame.display.flip()
#     clock.tick(60)











import pygame
import sys
import math

# إعداد نافذة العرض
pygame.init()
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wheel with Full Symbols")

clock = pygame.time.Clock()

# إعداد العجلة
wheel_radius = 200
wheel_center = (WIDTH // 2, HEIGHT // 2)
wheel_angle = 0.0
angular_velocity = 0.0
friction = 0.995

dragging = False
last_mouse_x = None

# قائمة الرموز الكاملة (حروف + أرقام + رموز)
symbols = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") \
        + list("0123456789") \
        + list("!@#$%^&*()-+=?/")

num_spokes = len(symbols)  # عدد الأسلاك يساوي عدد الرموز

# خط لكتابة النص في أعلى الشاشة
font = pygame.font.SysFont("Arial", 28)
selected_symbol = ""

def draw_wheel(angle):
    # إطار خارجي (الإطار المطاطي)
    pygame.draw.circle(screen, (20, 20, 20), wheel_center, wheel_radius, 20)

    # إطار معدني داخلي
    pygame.draw.circle(screen, (180, 180, 180), wheel_center, wheel_radius - 10, 5)

    # المحور
    pygame.draw.circle(screen, (100, 100, 100), wheel_center, 10)

    # رسم الأسلاك (تدور مع العجلة)
    for i in range(num_spokes):
        spoke_angle = math.radians(angle + (360 / num_spokes) * i)
        x = wheel_center[0] + (wheel_radius - 15) * math.cos(spoke_angle)
        y = wheel_center[1] + (wheel_radius - 15) * math.sin(spoke_angle)

        color = (255, 0, 0) if i == 0 else (200, 200, 200)
        pygame.draw.line(screen, color, wheel_center, (x, y), 2)

    # رسم الرموز ثابتة حول العجلة
    for i in range(num_spokes):
        fixed_angle = math.radians((360 / num_spokes) * i)
        text_x = wheel_center[0] + (wheel_radius + 40) * math.cos(fixed_angle)
        text_y = wheel_center[1] + (wheel_radius + 40) * math.sin(fixed_angle)

        text_surface = font.render(symbols[i], True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(text_x, text_y))
        screen.blit(text_surface, text_rect)

    # تحديد الرمز الذي يشير إليه السلك الأحمر
    red_spoke_angle = math.radians(angle)
    red_x = wheel_center[0] + (wheel_radius + 40) * math.cos(red_spoke_angle)
    red_y = wheel_center[1] + (wheel_radius + 40) * math.sin(red_spoke_angle)

    min_dist = float("inf")
    closest_symbol = ""
    for i in range(num_spokes):
        fixed_angle = math.radians((360 / num_spokes) * i)
        text_x = wheel_center[0] + (wheel_radius + 40) * math.cos(fixed_angle)
        text_y = wheel_center[1] + (wheel_radius + 40) * math.sin(fixed_angle)
        dist = math.hypot(red_x - text_x, red_y - text_y)
        if dist < min_dist:
            min_dist = dist
            closest_symbol = symbols[i]

    return closest_symbol

# حلقة اللعبة
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            dragging = True
            last_mouse_x = event.pos[0]

        if event.type == pygame.MOUSEBUTTONUP:
            dragging = False

    if dragging:
        mouse_x = pygame.mouse.get_pos()[0]
        delta_x = mouse_x - last_mouse_x
        angular_velocity += delta_x * 0.05
        last_mouse_x = mouse_x

    wheel_angle += angular_velocity
    angular_velocity *= friction

    screen.fill((30, 30, 30))
    selected_symbol = draw_wheel(wheel_angle)

    # عرض الرمز في أعلى الشاشة
    header_surface = font.render(f"Selected: {selected_symbol}", True, (255, 255, 0))
    header_rect = header_surface.get_rect(center=(WIDTH // 2, 40))
    screen.blit(header_surface, header_rect)

    pygame.display.flip()
    clock.tick(60)