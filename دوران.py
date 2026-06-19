# # # # # # # # # # # # # # # # # # import pygame
# # # # # # # # # # # # # # # # # # import math
# # # # # # # # # # # # # # # # # # import random

# # # # # # # # # # # # # # # # # # pygame.init()
# # # # # # # # # # # # # # # # # # WIDTH, HEIGHT = 1000, 700
# # # # # # # # # # # # # # # # # # screen = pygame.display.set_mode((WIDTH, HEIGHT))
# # # # # # # # # # # # # # # # # # pygame.display.set_caption("أربع عجلات دوّارة فيزيائية - النتائج بالترتيب")

# # # # # # # # # # # # # # # # # # clock = pygame.time.Clock()

# # # # # # # # # # # # # # # # # # # مراكز العجلات الأربع
# # # # # # # # # # # # # # # # # # centers = [
# # # # # # # # # # # # # # # # # #     (250, 250),
# # # # # # # # # # # # # # # # # #     (750, 250),
# # # # # # # # # # # # # # # # # #     (250, 550),
# # # # # # # # # # # # # # # # # #     (750, 550)
# # # # # # # # # # # # # # # # # # ]

# # # # # # # # # # # # # # # # # # # محتوى كل عجلة
# # # # # # # # # # # # # # # # # # wheels_content = [
# # # # # # # # # # # # # # # # # #     [str(i) for i in range(10)],                         # الأرقام
# # # # # # # # # # # # # # # # # #     [chr(ord('A') + i) for i in range(26)],             # الحروف
# # # # # # # # # # # # # # # # # #     list("!@#$%^&*()_+{}[]"),                           # الرموز
# # # # # # # # # # # # # # # # # #     ["★", "☀", "☂", "♠", "♥", "♦", "♣", "☻"]           # العلامات
# # # # # # # # # # # # # # # # # # ]

# # # # # # # # # # # # # # # # # # NUM_SECTIONS = [len(c) for c in wheels_content]
# # # # # # # # # # # # # # # # # # angles = [0]*4
# # # # # # # # # # # # # # # # # # angular_velocities = [0]*4
# # # # # # # # # # # # # # # # # # max_velocity = 2.0
# # # # # # # # # # # # # # # # # # dragging = [False]*4
# # # # # # # # # # # # # # # # # # last_mouse_angles = [0]*4

# # # # # # # # # # # # # # # # # # font = pygame.font.SysFont("arial", 32, bold=True)
# # # # # # # # # # # # # # # # # # win_font = pygame.font.SysFont("arial", 50, bold=True)
# # # # # # # # # # # # # # # # # # COLORS = [
# # # # # # # # # # # # # # # # # #     (255, 99, 71), (135, 206, 250), (255, 215, 0), (144, 238, 144),
# # # # # # # # # # # # # # # # # #     (221, 160, 221), (255, 182, 193), (173, 216, 230), (240, 230, 140),
# # # # # # # # # # # # # # # # # #     (255, 160, 122), (176, 196, 222)
# # # # # # # # # # # # # # # # # # ]

# # # # # # # # # # # # # # # # # # # النتيجة النهائية بأربع خانات
# # # # # # # # # # # # # # # # # # final_result = [None]*4
# # # # # # # # # # # # # # # # # # # مؤشر لتحديد الخانة التالية التي ستملأ حسب توقيف العجلات
# # # # # # # # # # # # # # # # # # next_result_index = 0

# # # # # # # # # # # # # # # # # # def friction(v):
# # # # # # # # # # # # # # # # # #     return 0.995 - (abs(v)*0.0005)

# # # # # # # # # # # # # # # # # # def get_mouse_angle(pos, center):
# # # # # # # # # # # # # # # # # #     dx = pos[0]-center[0]
# # # # # # # # # # # # # # # # # #     dy = pos[1]-center[1]
# # # # # # # # # # # # # # # # # #     return math.atan2(dy, dx)

# # # # # # # # # # # # # # # # # # def draw_wheel(center, angle, content):
# # # # # # # # # # # # # # # # # #     radius = 150
# # # # # # # # # # # # # # # # # #     sections = len(content)
# # # # # # # # # # # # # # # # # #     section_angle = 2*math.pi / sections

# # # # # # # # # # # # # # # # # #     for i in range(sections):
# # # # # # # # # # # # # # # # # #         start = angle + i*section_angle
# # # # # # # # # # # # # # # # # #         end = start + section_angle
# # # # # # # # # # # # # # # # # #         color = COLORS[i % len(COLORS)]
# # # # # # # # # # # # # # # # # #         pygame.draw.polygon(screen, color, [
# # # # # # # # # # # # # # # # # #             center,
# # # # # # # # # # # # # # # # # #             (center[0]+radius*math.cos(start), center[1]+radius*math.sin(start)),
# # # # # # # # # # # # # # # # # #             (center[0]+radius*math.cos(end), center[1]+radius*math.sin(end))
# # # # # # # # # # # # # # # # # #         ])
# # # # # # # # # # # # # # # # # #         text_angle = start + section_angle/2
# # # # # # # # # # # # # # # # # #         text_x = center[0] + (radius-50)*math.cos(text_angle)
# # # # # # # # # # # # # # # # # #         text_y = center[1] + (radius-50)*math.sin(text_angle)
# # # # # # # # # # # # # # # # # #         txt = font.render(str(content[i]), True, (0,0,0))
# # # # # # # # # # # # # # # # # #         rect = txt.get_rect(center=(text_x,text_y))
# # # # # # # # # # # # # # # # # #         screen.blit(txt,rect)

# # # # # # # # # # # # # # # # # #     pygame.draw.circle(screen, (0,0,0), center, radius, 4)
# # # # # # # # # # # # # # # # # #     # المؤشر العلوي
# # # # # # # # # # # # # # # # # #     pygame.draw.polygon(screen, (255,255,255), [
# # # # # # # # # # # # # # # # # #         (center[0]-10, center[1]-radius-5),
# # # # # # # # # # # # # # # # # #         (center[0]+10, center[1]-radius-5),
# # # # # # # # # # # # # # # # # #         (center[0], center[1]-radius-30)
# # # # # # # # # # # # # # # # # #     ])

# # # # # # # # # # # # # # # # # # def get_element_under_pointer(angle, sections):
# # # # # # # # # # # # # # # # # #     normalized = angle % (2*math.pi)
# # # # # # # # # # # # # # # # # #     pointer = -math.pi/2  # المؤشر العلوي
# # # # # # # # # # # # # # # # # #     relative = (pointer - normalized) % (2*math.pi)
# # # # # # # # # # # # # # # # # #     return int(relative // (2*math.pi/sections))

# # # # # # # # # # # # # # # # # # running = True
# # # # # # # # # # # # # # # # # # while running:
# # # # # # # # # # # # # # # # # #     clock.tick(60)
# # # # # # # # # # # # # # # # # #     screen.fill((30,30,30))
# # # # # # # # # # # # # # # # # #     mouse_pos = pygame.mouse.get_pos()

# # # # # # # # # # # # # # # # # #     # أحداث الماوس
# # # # # # # # # # # # # # # # # #     for event in pygame.event.get():
# # # # # # # # # # # # # # # # # #         if event.type == pygame.QUIT:
# # # # # # # # # # # # # # # # # #             running = False
# # # # # # # # # # # # # # # # # #         elif event.type == pygame.MOUSEBUTTONDOWN:
# # # # # # # # # # # # # # # # # #             for i, c in enumerate(centers):
# # # # # # # # # # # # # # # # # #                 dx = mouse_pos[0]-c[0]
# # # # # # # # # # # # # # # # # #                 dy = mouse_pos[1]-c[1]
# # # # # # # # # # # # # # # # # #                 if dx*dx + dy*dy <= 150*150:
# # # # # # # # # # # # # # # # # #                     dragging[i] = True
# # # # # # # # # # # # # # # # # #                     last_mouse_angles[i] = get_mouse_angle(mouse_pos, c)
# # # # # # # # # # # # # # # # # #         elif event.type == pygame.MOUSEBUTTONUP:
# # # # # # # # # # # # # # # # # #             for i in range(4):
# # # # # # # # # # # # # # # # # #                 if dragging[i]:
# # # # # # # # # # # # # # # # # #                     dragging[i] = False
# # # # # # # # # # # # # # # # # #                     angular_velocities[i] += random.uniform(-0.02,0.02)  # اهتزاز خفيف عند إطلاق
# # # # # # # # # # # # # # # # # #         elif event.type == pygame.MOUSEMOTION:
# # # # # # # # # # # # # # # # # #             for i, c in enumerate(centers):
# # # # # # # # # # # # # # # # # #                 if dragging[i]:
# # # # # # # # # # # # # # # # # #                     mouse_angle = get_mouse_angle(mouse_pos, c)
# # # # # # # # # # # # # # # # # #                     delta = mouse_angle - last_mouse_angles[i]
# # # # # # # # # # # # # # # # # #                     angular_velocities[i] += delta*20
# # # # # # # # # # # # # # # # # #                     angular_velocities[i] = max(-max_velocity, min(max_velocity, angular_velocities[i]))
# # # # # # # # # # # # # # # # # #                     last_mouse_angles[i] = mouse_angle

# # # # # # # # # # # # # # # # # #     # تحديث كل عجلة
# # # # # # # # # # # # # # # # # #     for i in range(4):
# # # # # # # # # # # # # # # # # #         angles[i] += angular_velocities[i]
# # # # # # # # # # # # # # # # # #         angular_velocities[i] *= friction(angular_velocities[i])

# # # # # # # # # # # # # # # # # #         # إذا توقفت العجلة وتمت تعبئة الخانة التالية
# # # # # # # # # # # # # # # # # #         if abs(angular_velocities[i]) < 0.001 and not dragging[i] and (i not in final_result):
# # # # # # # # # # # # # # # # # #             angular_velocities[i] = 0
# # # # # # # # # # # # # # # # # #             if final_result[i] is None:
# # # # # # # # # # # # # # # # # #                 element_index = get_element_under_pointer(angles[i], NUM_SECTIONS[i])
# # # # # # # # # # # # # # # # # #                 final_result[i] = wheels_content[i][element_index]
# # # # # # # # # # # # # # # # # #                 print(f"🏆 العجلة {i+1} توقفت على: {final_result[i]}")

# # # # # # # # # # # # # # # # # #         draw_wheel(centers[i], angles[i], wheels_content[i])

# # # # # # # # # # # # # # # # # #     # رسم الخانات الأربع في الأعلى للنتيجة
# # # # # # # # # # # # # # # # # #     for idx, val in enumerate(final_result):
# # # # # # # # # # # # # # # # # #         display_val = val if val is not None else "_"
# # # # # # # # # # # # # # # # # #         txt = win_font.render(str(display_val), True, (255,255,0))
# # # # # # # # # # # # # # # # # #         rect = txt.get_rect(center=(WIDTH//5*(idx+1), 50))
# # # # # # # # # # # # # # # # # #         screen.blit(txt, rect)

# # # # # # # # # # # # # # # # # #     pygame.display.flip()

# # # # # # # # # # # # # # # # # # pygame.quit()













# # # # # # # # # # # # # # # # # import pygame
# # # # # # # # # # # # # # # # # import math
# # # # # # # # # # # # # # # # # import random

# # # # # # # # # # # # # # # # # pygame.init()
# # # # # # # # # # # # # # # # # WIDTH, HEIGHT = 600, 600
# # # # # # # # # # # # # # # # # screen = pygame.display.set_mode((WIDTH, HEIGHT))
# # # # # # # # # # # # # # # # # pygame.display.set_caption("عجلة دوّارة فيزيائية مع رقم فائز")

# # # # # # # # # # # # # # # # # clock = pygame.time.Clock()

# # # # # # # # # # # # # # # # # CENTER = (WIDTH // 2, HEIGHT // 2)
# # # # # # # # # # # # # # # # # RADIUS = 220

# # # # # # # # # # # # # # # # # angle = 0
# # # # # # # # # # # # # # # # # angular_velocity = 0
# # # # # # # # # # # # # # # # # max_angular_velocity = 2.0

# # # # # # # # # # # # # # # # # dragging = False
# # # # # # # # # # # # # # # # # last_mouse_angle = 0

# # # # # # # # # # # # # # # # # font = pygame.font.SysFont("arial", 32, bold=True)
# # # # # # # # # # # # # # # # # win_font = pygame.font.SysFont("arial", 60, bold=True)

# # # # # # # # # # # # # # # # # COLORS = [
# # # # # # # # # # # # # # # # #     (255, 99, 71), (135, 206, 250), (255, 215, 0), (144, 238, 144), 
# # # # # # # # # # # # # # # # #     (221, 160, 221), (255, 182, 193), (173, 216, 230), (240, 230, 140), 
# # # # # # # # # # # # # # # # #     (255, 160, 122), (176, 196, 222)
# # # # # # # # # # # # # # # # # ]

# # # # # # # # # # # # # # # # # NUM_SECTIONS = 10
# # # # # # # # # # # # # # # # # SECTION_ANGLE = 2 * math.pi / NUM_SECTIONS

# # # # # # # # # # # # # # # # # def friction_force(velocity):
# # # # # # # # # # # # # # # # #     return 0.995 - (abs(velocity) * 0.0005)

# # # # # # # # # # # # # # # # # def get_mouse_angle(pos):
# # # # # # # # # # # # # # # # #     dx = pos[0] - CENTER[0]
# # # # # # # # # # # # # # # # #     dy = pos[1] - CENTER[1]
# # # # # # # # # # # # # # # # #     return math.atan2(dy, dx)

# # # # # # # # # # # # # # # # # def draw_wheel(angle, winning_number=None):
# # # # # # # # # # # # # # # # #     screen.fill((25, 25, 25))
# # # # # # # # # # # # # # # # #     for i in range(NUM_SECTIONS):
# # # # # # # # # # # # # # # # #         start_angle = angle + i * SECTION_ANGLE
# # # # # # # # # # # # # # # # #         end_angle = start_angle + SECTION_ANGLE

# # # # # # # # # # # # # # # # #         pygame.draw.polygon(
# # # # # # # # # # # # # # # # #             screen,
# # # # # # # # # # # # # # # # #             COLORS[i],
# # # # # # # # # # # # # # # # #             [
# # # # # # # # # # # # # # # # #                 CENTER,
# # # # # # # # # # # # # # # # #                 (CENTER[0] + RADIUS * math.cos(start_angle),
# # # # # # # # # # # # # # # # #                  CENTER[1] + RADIUS * math.sin(start_angle)),
# # # # # # # # # # # # # # # # #                 (CENTER[0] + RADIUS * math.cos(end_angle),
# # # # # # # # # # # # # # # # #                  CENTER[1] + RADIUS * math.sin(end_angle))
# # # # # # # # # # # # # # # # #             ]
# # # # # # # # # # # # # # # # #         )

# # # # # # # # # # # # # # # # #         text_angle = start_angle + SECTION_ANGLE / 2
# # # # # # # # # # # # # # # # #         text_x = CENTER[0] + (RADIUS - 50) * math.cos(text_angle)
# # # # # # # # # # # # # # # # #         text_y = CENTER[1] + (RADIUS - 50) * math.sin(text_angle)
# # # # # # # # # # # # # # # # #         number = font.render(str(i), True, (0, 0, 0))
# # # # # # # # # # # # # # # # #         text_rect = number.get_rect(center=(text_x, text_y))
# # # # # # # # # # # # # # # # #         screen.blit(number, text_rect)

# # # # # # # # # # # # # # # # #     pygame.draw.circle(screen, (0, 0, 0), CENTER, RADIUS, 4)
# # # # # # # # # # # # # # # # #     pygame.draw.polygon(
# # # # # # # # # # # # # # # # #         screen,
# # # # # # # # # # # # # # # # #         (255, 255, 255),
# # # # # # # # # # # # # # # # #         [
# # # # # # # # # # # # # # # # #             (CENTER[0] - 10, CENTER[1] - RADIUS - 5),
# # # # # # # # # # # # # # # # #             (CENTER[0] + 10, CENTER[1] - RADIUS - 5),
# # # # # # # # # # # # # # # # #             (CENTER[0], CENTER[1] - RADIUS - 30)
# # # # # # # # # # # # # # # # #         ]
# # # # # # # # # # # # # # # # #     )

# # # # # # # # # # # # # # # # #     # عرض الرقم الفائز في الوسط إذا موجود
# # # # # # # # # # # # # # # # #     if winning_number is not None:
# # # # # # # # # # # # # # # # #         win_text = win_font.render(f"🏆 الرقم الفائز: {winning_number} 🏆", True, (255, 255, 0))
# # # # # # # # # # # # # # # # #         win_rect = win_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
# # # # # # # # # # # # # # # # #         screen.blit(win_text, win_rect)

# # # # # # # # # # # # # # # # #     pygame.display.flip()

# # # # # # # # # # # # # # # # # def get_winning_number(angle):
# # # # # # # # # # # # # # # # #     normalized_angle = angle % (2 * math.pi)
# # # # # # # # # # # # # # # # #     pointer_angle = -math.pi / 2
# # # # # # # # # # # # # # # # #     relative_angle = (pointer_angle - normalized_angle) % (2 * math.pi)
# # # # # # # # # # # # # # # # #     section_index = int(relative_angle // SECTION_ANGLE)
# # # # # # # # # # # # # # # # #     return section_index

# # # # # # # # # # # # # # # # # running = True
# # # # # # # # # # # # # # # # # winning_number_shown = False
# # # # # # # # # # # # # # # # # winning_number = None

# # # # # # # # # # # # # # # # # while running:
# # # # # # # # # # # # # # # # #     clock.tick(60)

# # # # # # # # # # # # # # # # #     for event in pygame.event.get():
# # # # # # # # # # # # # # # # #         if event.type == pygame.QUIT:
# # # # # # # # # # # # # # # # #             running = False

# # # # # # # # # # # # # # # # #         elif event.type == pygame.MOUSEBUTTONDOWN:
# # # # # # # # # # # # # # # # #             dragging = True
# # # # # # # # # # # # # # # # #             last_mouse_angle = get_mouse_angle(pygame.mouse.get_pos())
# # # # # # # # # # # # # # # # #             winning_number_shown = False
# # # # # # # # # # # # # # # # #             winning_number = None

# # # # # # # # # # # # # # # # #         elif event.type == pygame.MOUSEBUTTONUP:
# # # # # # # # # # # # # # # # #             dragging = False
# # # # # # # # # # # # # # # # #             angular_velocity += random.uniform(-0.02, 0.02)  # اهتزاز بسيط

# # # # # # # # # # # # # # # # #         elif event.type == pygame.MOUSEMOTION and dragging:
# # # # # # # # # # # # # # # # #             mouse_angle = get_mouse_angle(pygame.mouse.get_pos())
# # # # # # # # # # # # # # # # #             delta = mouse_angle - last_mouse_angle
# # # # # # # # # # # # # # # # #             angular_velocity += delta * 20
# # # # # # # # # # # # # # # # #             angular_velocity = max(-max_angular_velocity, min(max_angular_velocity, angular_velocity))
# # # # # # # # # # # # # # # # #             last_mouse_angle = mouse_angle

# # # # # # # # # # # # # # # # #     # تحديث الحركة الفيزيائية
# # # # # # # # # # # # # # # # #     angle += angular_velocity
# # # # # # # # # # # # # # # # #     angular_velocity *= friction_force(angular_velocity)

# # # # # # # # # # # # # # # # #     # التوقف وعرض الرقم الفائز
# # # # # # # # # # # # # # # # #     if abs(angular_velocity) < 0.0005 and not dragging:
# # # # # # # # # # # # # # # # #         angular_velocity = 0
# # # # # # # # # # # # # # # # #         if not winning_number_shown:
# # # # # # # # # # # # # # # # #             winning_number = get_winning_number(angle)
# # # # # # # # # # # # # # # # #             winning_number_shown = True
# # # # # # # # # # # # # # # # #             print(f"🏆 الرقم الفائز هو: {winning_number}")

# # # # # # # # # # # # # # # # #     draw_wheel(angle, winning_number)

# # # # # # # # # # # # # # # # # pygame.quit()





# # # # # # # # # # # # # # # # import pygame
# # # # # # # # # # # # # # # # import math
# # # # # # # # # # # # # # # # import random

# # # # # # # # # # # # # # # # pygame.init()
# # # # # # # # # # # # # # # # WIDTH, HEIGHT = 800, 500
# # # # # # # # # # # # # # # # screen = pygame.display.set_mode((WIDTH, HEIGHT))
# # # # # # # # # # # # # # # # pygame.display.set_caption("عجلة الحروف الواقعية")

# # # # # # # # # # # # # # # # clock = pygame.time.Clock()

# # # # # # # # # # # # # # # # CENTER = (WIDTH // 2 - 150, HEIGHT // 2)
# # # # # # # # # # # # # # # # RADIUS = 200

# # # # # # # # # # # # # # # # angle = 0
# # # # # # # # # # # # # # # # angular_velocity = 0
# # # # # # # # # # # # # # # # max_angular_velocity = 2.0

# # # # # # # # # # # # # # # # dragging = False
# # # # # # # # # # # # # # # # last_mouse_angle = 0

# # # # # # # # # # # # # # # # font = pygame.font.SysFont("arial", 32, bold=True)
# # # # # # # # # # # # # # # # win_font = pygame.font.SysFont("arial", 60, bold=True)

# # # # # # # # # # # # # # # # COLORS = [
# # # # # # # # # # # # # # # #     (255, 99, 71), (135, 206, 250), (255, 215, 0), (144, 238, 144), 
# # # # # # # # # # # # # # # #     (221, 160, 221), (255, 182, 193), (173, 216, 230), (240, 230, 140), 
# # # # # # # # # # # # # # # #     (255, 160, 122), (176, 196, 222)
# # # # # # # # # # # # # # # # ]

# # # # # # # # # # # # # # # # letters = [chr(ord('A') + i) for i in range(26)]
# # # # # # # # # # # # # # # # NUM_SECTIONS = len(letters)
# # # # # # # # # # # # # # # # SECTION_ANGLE = 2 * math.pi / NUM_SECTIONS

# # # # # # # # # # # # # # # # def friction_force(velocity):
# # # # # # # # # # # # # # # #     return 0.995 - (abs(velocity) * 0.0005)

# # # # # # # # # # # # # # # # def get_mouse_angle(pos):
# # # # # # # # # # # # # # # #     dx = pos[0] - CENTER[0]
# # # # # # # # # # # # # # # #     dy = pos[1] - CENTER[1]
# # # # # # # # # # # # # # # #     return math.atan2(dy, dx)

# # # # # # # # # # # # # # # # def draw_wheel(angle, winning_letter=None):
# # # # # # # # # # # # # # # #     screen.fill((25, 25, 25))
# # # # # # # # # # # # # # # #     for i in range(NUM_SECTIONS):
# # # # # # # # # # # # # # # #         start_angle = angle + i * SECTION_ANGLE
# # # # # # # # # # # # # # # #         end_angle = start_angle + SECTION_ANGLE

# # # # # # # # # # # # # # # #         pygame.draw.polygon(
# # # # # # # # # # # # # # # #             screen,
# # # # # # # # # # # # # # # #             COLORS[i % len(COLORS)],
# # # # # # # # # # # # # # # #             [
# # # # # # # # # # # # # # # #                 CENTER,
# # # # # # # # # # # # # # # #                 (CENTER[0] + RADIUS * math.cos(start_angle),
# # # # # # # # # # # # # # # #                  CENTER[1] + RADIUS * math.sin(start_angle)),
# # # # # # # # # # # # # # # #                 (CENTER[0] + RADIUS * math.cos(end_angle),
# # # # # # # # # # # # # # # #                  CENTER[1] + RADIUS * math.sin(end_angle))
# # # # # # # # # # # # # # # #             ]
# # # # # # # # # # # # # # # #         )

# # # # # # # # # # # # # # # #         text_angle = start_angle + SECTION_ANGLE / 2
# # # # # # # # # # # # # # # #         text_x = CENTER[0] + (RADIUS - 50) * math.cos(text_angle)
# # # # # # # # # # # # # # # #         text_y = CENTER[1] + (RADIUS - 50) * math.sin(text_angle)
# # # # # # # # # # # # # # # #         letter = font.render(letters[i], True, (0, 0, 0))
# # # # # # # # # # # # # # # #         text_rect = letter.get_rect(center=(text_x, text_y))
# # # # # # # # # # # # # # # #         screen.blit(letter, text_rect)

# # # # # # # # # # # # # # # #     pygame.draw.circle(screen, (0, 0, 0), CENTER, RADIUS, 4)
# # # # # # # # # # # # # # # #     pygame.draw.polygon(
# # # # # # # # # # # # # # # #         screen,
# # # # # # # # # # # # # # # #         (255, 255, 255),
# # # # # # # # # # # # # # # #         [
# # # # # # # # # # # # # # # #             (CENTER[0] - 10, CENTER[1] - RADIUS - 5),
# # # # # # # # # # # # # # # #             (CENTER[0] + 10, CENTER[1] - RADIUS - 5),
# # # # # # # # # # # # # # # #             (CENTER[0], CENTER[1] - RADIUS - 30)
# # # # # # # # # # # # # # # #         ]
# # # # # # # # # # # # # # # #     )

# # # # # # # # # # # # # # # #     # عرض الحرف الفائز بجانب العجلة
# # # # # # # # # # # # # # # #     if winning_letter is not None:
# # # # # # # # # # # # # # # #         letter_text = win_font.render(f"{winning_letter}", True, (255, 255, 0))
# # # # # # # # # # # # # # # #         letter_rect = letter_text.get_rect(center=(CENTER[0] + RADIUS + 100, CENTER[1]))
# # # # # # # # # # # # # # # #         screen.blit(letter_text, letter_rect)

# # # # # # # # # # # # # # # #     pygame.display.flip()

# # # # # # # # # # # # # # # # def get_winning_letter(angle):
# # # # # # # # # # # # # # # #     normalized_angle = angle % (2 * math.pi)
# # # # # # # # # # # # # # # #     pointer_angle = -math.pi / 2
# # # # # # # # # # # # # # # #     relative_angle = (pointer_angle - normalized_angle) % (2 * math.pi)
# # # # # # # # # # # # # # # #     section_index = int(relative_angle // SECTION_ANGLE)
# # # # # # # # # # # # # # # #     return letters[section_index]

# # # # # # # # # # # # # # # # running = True
# # # # # # # # # # # # # # # # winning_letter_shown = False
# # # # # # # # # # # # # # # # winning_letter = None

# # # # # # # # # # # # # # # # while running:
# # # # # # # # # # # # # # # #     clock.tick(60)
# # # # # # # # # # # # # # # #     mouse_pos = pygame.mouse.get_pos()

# # # # # # # # # # # # # # # #     for event in pygame.event.get():
# # # # # # # # # # # # # # # #         if event.type == pygame.QUIT:
# # # # # # # # # # # # # # # #             running = False

# # # # # # # # # # # # # # # #         elif event.type == pygame.MOUSEBUTTONDOWN:
# # # # # # # # # # # # # # # #             dragging = True
# # # # # # # # # # # # # # # #             last_mouse_angle = get_mouse_angle(mouse_pos)
# # # # # # # # # # # # # # # #             winning_letter_shown = False
# # # # # # # # # # # # # # # #             winning_letter = None

# # # # # # # # # # # # # # # #         elif event.type == pygame.MOUSEBUTTONUP:
# # # # # # # # # # # # # # # #             dragging = False
# # # # # # # # # # # # # # # #             angular_velocity += random.uniform(-0.02, 0.02)

# # # # # # # # # # # # # # # #         elif event.type == pygame.MOUSEMOTION and dragging:
# # # # # # # # # # # # # # # #             mouse_angle = get_mouse_angle(mouse_pos)
# # # # # # # # # # # # # # # #             delta = mouse_angle - last_mouse_angle
# # # # # # # # # # # # # # # #             angular_velocity += delta * 20
# # # # # # # # # # # # # # # #             angular_velocity = max(-max_angular_velocity, min(max_angular_velocity, angular_velocity))
# # # # # # # # # # # # # # # #             last_mouse_angle = mouse_angle

# # # # # # # # # # # # # # # #     angle += angular_velocity
# # # # # # # # # # # # # # # #     angular_velocity *= friction_force(angular_velocity)

# # # # # # # # # # # # # # # #     # توقف العجلة وعرض الحرف
# # # # # # # # # # # # # # # #     if abs(angular_velocity) < 0.0005 and not dragging:
# # # # # # # # # # # # # # # #         angular_velocity = 0
# # # # # # # # # # # # # # # #         if not winning_letter_shown:
# # # # # # # # # # # # # # # #             winning_letter = get_winning_letter(angle)
# # # # # # # # # # # # # # # #             winning_letter_shown = True
# # # # # # # # # # # # # # # #             print(f"🏆 الحرف الفائز هو: {winning_letter}")

# # # # # # # # # # # # # # # #     draw_wheel(angle, winning_letter)

# # # # # # # # # # # # # # # # pygame.quit()




# # # # # # # # # # # # # # # import pygame
# # # # # # # # # # # # # # # import math
# # # # # # # # # # # # # # # import random

# # # # # # # # # # # # # # # pygame.init()
# # # # # # # # # # # # # # # WIDTH, HEIGHT = 1000, 500
# # # # # # # # # # # # # # # screen = pygame.display.set_mode((WIDTH, HEIGHT))
# # # # # # # # # # # # # # # pygame.display.set_caption("عجلتان واقعيّتان: الأرقام والحروف")

# # # # # # # # # # # # # # # clock = pygame.time.Clock()

# # # # # # # # # # # # # # # # مراكز العجلتين
# # # # # # # # # # # # # # # CENTER_NUM = (250, HEIGHT//2)
# # # # # # # # # # # # # # # CENTER_LETTER = (750, HEIGHT//2)
# # # # # # # # # # # # # # # RADIUS = 200

# # # # # # # # # # # # # # # # محتوى العجلات
# # # # # # # # # # # # # # # numbers = [str(i) for i in range(10)]
# # # # # # # # # # # # # # # letters = [chr(ord('A') + i) for i in range(26)]

# # # # # # # # # # # # # # # # الإعدادات الفيزيائية
# # # # # # # # # # # # # # # angles = [0, 0]  # [الأرقام، الحروف]
# # # # # # # # # # # # # # # angular_velocities = [0, 0]
# # # # # # # # # # # # # # # max_velocity = 2.0
# # # # # # # # # # # # # # # dragging = [False, False]
# # # # # # # # # # # # # # # last_mouse_angles = [0, 0]

# # # # # # # # # # # # # # # font = pygame.font.SysFont("arial", 32, bold=True)
# # # # # # # # # # # # # # # win_font = pygame.font.SysFont("arial", 60, bold=True)

# # # # # # # # # # # # # # # COLORS = [
# # # # # # # # # # # # # # #     (255, 99, 71), (135, 206, 250), (255, 215, 0), (144, 238, 144),
# # # # # # # # # # # # # # #     (221, 160, 221), (255, 182, 193), (173, 216, 230), (240, 230, 140),
# # # # # # # # # # # # # # #     (255, 160, 122), (176, 196, 222)
# # # # # # # # # # # # # # # ]

# # # # # # # # # # # # # # # final_result = [None, None]  # [الرقم، الحرف]

# # # # # # # # # # # # # # # def friction(v):
# # # # # # # # # # # # # # #     return 0.995 - (abs(v) * 0.0005)

# # # # # # # # # # # # # # # def get_mouse_angle(pos, center):
# # # # # # # # # # # # # # #     dx = pos[0]-center[0]
# # # # # # # # # # # # # # #     dy = pos[1]-center[1]
# # # # # # # # # # # # # # #     return math.atan2(dy, dx)

# # # # # # # # # # # # # # # def draw_wheel(center, angle, content):
# # # # # # # # # # # # # # #     sections = len(content)
# # # # # # # # # # # # # # #     section_angle = 2 * math.pi / sections

# # # # # # # # # # # # # # #     for i in range(sections):
# # # # # # # # # # # # # # #         start = angle + i*section_angle
# # # # # # # # # # # # # # #         end = start + section_angle
# # # # # # # # # # # # # # #         color = COLORS[i % len(COLORS)]
# # # # # # # # # # # # # # #         pygame.draw.polygon(screen, color, [
# # # # # # # # # # # # # # #             center,
# # # # # # # # # # # # # # #             (center[0]+RADIUS*math.cos(start), center[1]+RADIUS*math.sin(start)),
# # # # # # # # # # # # # # #             (center[0]+RADIUS*math.cos(end), center[1]+RADIUS*math.sin(end))
# # # # # # # # # # # # # # #         ])
# # # # # # # # # # # # # # #         text_angle = start + section_angle/2
# # # # # # # # # # # # # # #         text_x = center[0] + (RADIUS-50) * math.cos(text_angle)
# # # # # # # # # # # # # # #         text_y = center[1] + (RADIUS-50) * math.sin(text_angle)
# # # # # # # # # # # # # # #         txt = font.render(str(content[i]), True, (0,0,0))
# # # # # # # # # # # # # # #         rect = txt.get_rect(center=(text_x,text_y))
# # # # # # # # # # # # # # #         screen.blit(txt, rect)

# # # # # # # # # # # # # # #     pygame.draw.circle(screen, (0,0,0), center, RADIUS, 4)
# # # # # # # # # # # # # # #     # المؤشر العلوي
# # # # # # # # # # # # # # #     pygame.draw.polygon(screen, (255,255,255), [
# # # # # # # # # # # # # # #         (center[0]-10, center[1]-RADIUS-5),
# # # # # # # # # # # # # # #         (center[0]+10, center[1]-RADIUS-5),
# # # # # # # # # # # # # # #         (center[0], center[1]-RADIUS-30)
# # # # # # # # # # # # # # #     ])

# # # # # # # # # # # # # # #     # عرض العنصر الفائز بجانب العجلة
# # # # # # # # # # # # # # #     index = 0 if center==CENTER_NUM else 1
# # # # # # # # # # # # # # #     if final_result[index] is not None:
# # # # # # # # # # # # # # #         text = win_font.render(str(final_result[index]), True, (255,255,0))
# # # # # # # # # # # # # # #         rect = text.get_rect(center=(center[0]+RADIUS+100, center[1]))
# # # # # # # # # # # # # # #         screen.blit(text, rect)

# # # # # # # # # # # # # # # def get_element_under_pointer(angle, num_sections, content):
# # # # # # # # # # # # # # #     normalized = angle % (2*math.pi)
# # # # # # # # # # # # # # #     pointer = -math.pi/2
# # # # # # # # # # # # # # #     relative = (pointer - normalized) % (2*math.pi)
# # # # # # # # # # # # # # #     section_index = int(relative // (2*math.pi/num_sections))
# # # # # # # # # # # # # # #     return content[section_index]

# # # # # # # # # # # # # # # running = True
# # # # # # # # # # # # # # # while running:
# # # # # # # # # # # # # # #     clock.tick(60)
# # # # # # # # # # # # # # #     screen.fill((30,30,30))
# # # # # # # # # # # # # # #     mouse_pos = pygame.mouse.get_pos()

# # # # # # # # # # # # # # #     # الأحداث
# # # # # # # # # # # # # # #     for event in pygame.event.get():
# # # # # # # # # # # # # # #         if event.type == pygame.QUIT:
# # # # # # # # # # # # # # #             running = False
# # # # # # # # # # # # # # #         elif event.type == pygame.MOUSEBUTTONDOWN:
# # # # # # # # # # # # # # #             for i, c in enumerate([CENTER_NUM, CENTER_LETTER]):
# # # # # # # # # # # # # # #                 dx = mouse_pos[0]-c[0]
# # # # # # # # # # # # # # #                 dy = mouse_pos[1]-c[1]
# # # # # # # # # # # # # # #                 if dx*dx+dy*dy <= RADIUS*RADIUS:
# # # # # # # # # # # # # # #                     dragging[i] = True
# # # # # # # # # # # # # # #                     last_mouse_angles[i] = get_mouse_angle(mouse_pos, c)
# # # # # # # # # # # # # # #                     final_result[i] = None
# # # # # # # # # # # # # # #         elif event.type == pygame.MOUSEBUTTONUP:
# # # # # # # # # # # # # # #             for i in range(2):
# # # # # # # # # # # # # # #                 if dragging[i]:
# # # # # # # # # # # # # # #                     dragging[i] = False
# # # # # # # # # # # # # # #                     angular_velocities[i] += random.uniform(-0.02,0.02)
# # # # # # # # # # # # # # #         elif event.type == pygame.MOUSEMOTION:
# # # # # # # # # # # # # # #             for i, c in enumerate([CENTER_NUM, CENTER_LETTER]):
# # # # # # # # # # # # # # #                 if dragging[i]:
# # # # # # # # # # # # # # #                     mouse_angle = get_mouse_angle(mouse_pos, c)
# # # # # # # # # # # # # # #                     delta = mouse_angle - last_mouse_angles[i]
# # # # # # # # # # # # # # #                     angular_velocities[i] += delta*20
# # # # # # # # # # # # # # #                     angular_velocities[i] = max(-max_velocity, min(max_velocity, angular_velocities[i]))
# # # # # # # # # # # # # # #                     last_mouse_angles[i] = mouse_angle

# # # # # # # # # # # # # # #     # تحديث الحركة الفيزيائية
# # # # # # # # # # # # # # #     angles[0] += angular_velocities[0]
# # # # # # # # # # # # # # #     angles[1] += angular_velocities[1]
# # # # # # # # # # # # # # #     angular_velocities[0] *= friction(angular_velocities[0])
# # # # # # # # # # # # # # #     angular_velocities[1] *= friction(angular_velocities[1])

# # # # # # # # # # # # # # #     # التوقف وتسجيل العنصر تحت المؤشر
# # # # # # # # # # # # # # #     if abs(angular_velocities[0]) < 0.001 and not dragging[0] and final_result[0] is None:
# # # # # # # # # # # # # # #         angular_velocities[0] = 0
# # # # # # # # # # # # # # #         final_result[0] = get_element_under_pointer(angles[0], len(numbers), numbers)
# # # # # # # # # # # # # # #         print(f"🏆 الرقم الفائز: {final_result[0]}")
# # # # # # # # # # # # # # #     if abs(angular_velocities[1]) < 0.001 and not dragging[1] and final_result[1] is None:
# # # # # # # # # # # # # # #         angular_velocities[1] = 0
# # # # # # # # # # # # # # #         final_result[1] = get_element_under_pointer(angles[1], len(letters), letters)
# # # # # # # # # # # # # # #         print(f"🏆 الحرف الفائز: {final_result[1]}")

# # # # # # # # # # # # # # #     # رسم العجلات
# # # # # # # # # # # # # # #     draw_wheel(CENTER_NUM, angles[0], numbers)
# # # # # # # # # # # # # # #     draw_wheel(CENTER_LETTER, angles[1], letters)

# # # # # # # # # # # # # # #     pygame.display.flip()

# # # # # # # # # # # # # # # pygame.quit()







# # # # # # # # # # # # # # import pygame
# # # # # # # # # # # # # # import math
# # # # # # # # # # # # # # import random
# # # # # # # # # # # # # # import string

# # # # # # # # # # # # # # pygame.init()

# # # # # # # # # # # # # # # ================== إعدادات عامة ==================
# # # # # # # # # # # # # # WIDTH, HEIGHT = 1000, 600
# # # # # # # # # # # # # # screen = pygame.display.set_mode((WIDTH, HEIGHT))
# # # # # # # # # # # # # # pygame.display.set_caption("دوّارتان فيزيائيتان (أرقام + حروف)")
# # # # # # # # # # # # # # clock = pygame.time.Clock()

# # # # # # # # # # # # # # FONT = pygame.font.SysFont("arial", 26, bold=True)
# # # # # # # # # # # # # # BIG_FONT = pygame.font.SysFont("arial", 60, bold=True)

# # # # # # # # # # # # # # BG = (25, 25, 25)
# # # # # # # # # # # # # # POINTER_COLOR = (255, 255, 255)

# # # # # # # # # # # # # # RADIUS = 180
# # # # # # # # # # # # # # NUM_SECTIONS = 10
# # # # # # # # # # # # # # SECTION_ANGLE = 2 * math.pi / NUM_SECTIONS

# # # # # # # # # # # # # # # ================== مراكز الدوارات ==================
# # # # # # # # # # # # # # CENTER_NUM = (300, 320)
# # # # # # # # # # # # # # CENTER_LET = (700, 320)

# # # # # # # # # # # # # # # ================== بيانات الدوارة ==================
# # # # # # # # # # # # # # def new_wheel(center):
# # # # # # # # # # # # # #     return {
# # # # # # # # # # # # # #         "center": center,
# # # # # # # # # # # # # #         "angle": 0,
# # # # # # # # # # # # # #         "vel": 0,
# # # # # # # # # # # # # #         "drag": False,
# # # # # # # # # # # # # #         "last_mouse": 0,
# # # # # # # # # # # # # #         "result": None,
# # # # # # # # # # # # # #         "stopped": False
# # # # # # # # # # # # # #     }

# # # # # # # # # # # # # # wheel_num = new_wheel(CENTER_NUM)
# # # # # # # # # # # # # # wheel_let = new_wheel(CENTER_LET)

# # # # # # # # # # # # # # letters = list(string.ascii_uppercase[:10])

# # # # # # # # # # # # # # COLORS = [
# # # # # # # # # # # # # #     (255,99,71),(135,206,250),(255,215,0),(144,238,144),
# # # # # # # # # # # # # #     (221,160,221),(255,182,193),(173,216,230),(240,230,140),
# # # # # # # # # # # # # #     (255,160,122),(176,196,222)
# # # # # # # # # # # # # # ]

# # # # # # # # # # # # # # first_stopped = None

# # # # # # # # # # # # # # # ================== دوال ==================
# # # # # # # # # # # # # # def friction(v):
# # # # # # # # # # # # # #     return 0.995 - abs(v)*0.0005

# # # # # # # # # # # # # # def mouse_angle(pos, center):
# # # # # # # # # # # # # #     dx, dy = pos[0]-center[0], pos[1]-center[1]
# # # # # # # # # # # # # #     return math.atan2(dy, dx)

# # # # # # # # # # # # # # def draw_wheel(wheel, labels):
# # # # # # # # # # # # # #     cx, cy = wheel["center"]
# # # # # # # # # # # # # #     for i in range(NUM_SECTIONS):
# # # # # # # # # # # # # #         a1 = wheel["angle"] + i*SECTION_ANGLE
# # # # # # # # # # # # # #         a2 = a1 + SECTION_ANGLE

# # # # # # # # # # # # # #         pygame.draw.polygon(
# # # # # # # # # # # # # #             screen,
# # # # # # # # # # # # # #             COLORS[i],
# # # # # # # # # # # # # #             [(cx,cy),
# # # # # # # # # # # # # #              (cx+RADIUS*math.cos(a1), cy+RADIUS*math.sin(a1)),
# # # # # # # # # # # # # #              (cx+RADIUS*math.cos(a2), cy+RADIUS*math.sin(a2))]
# # # # # # # # # # # # # #         )

# # # # # # # # # # # # # #         ta = a1 + SECTION_ANGLE/2
# # # # # # # # # # # # # #         tx = cx + (RADIUS-40)*math.cos(ta)
# # # # # # # # # # # # # #         ty = cy + (RADIUS-40)*math.sin(ta)
# # # # # # # # # # # # # #         txt = FONT.render(str(labels[i]), True, (0,0,0))
# # # # # # # # # # # # # #         screen.blit(txt, txt.get_rect(center=(tx,ty)))

# # # # # # # # # # # # # #     pygame.draw.circle(screen, (0,0,0), wheel["center"], RADIUS, 4)

# # # # # # # # # # # # # #     # المؤشر
# # # # # # # # # # # # # #     pygame.draw.polygon(
# # # # # # # # # # # # # #         screen, POINTER_COLOR,
# # # # # # # # # # # # # #         [(cx-10, cy-RADIUS-5),
# # # # # # # # # # # # # #          (cx+10, cy-RADIUS-5),
# # # # # # # # # # # # # #          (cx, cy-RADIUS-30)]
# # # # # # # # # # # # # #     )

# # # # # # # # # # # # # # def get_under_pointer(wheel):
# # # # # # # # # # # # # #     norm = wheel["angle"] % (2*math.pi)
# # # # # # # # # # # # # #     pointer = -math.pi/2
# # # # # # # # # # # # # #     rel = (pointer - norm) % (2*math.pi)
# # # # # # # # # # # # # #     return int(rel // SECTION_ANGLE)

# # # # # # # # # # # # # # # ================== الحلقة الرئيسية ==================
# # # # # # # # # # # # # # running = True
# # # # # # # # # # # # # # while running:
# # # # # # # # # # # # # #     clock.tick(60)
# # # # # # # # # # # # # #     screen.fill(BG)

# # # # # # # # # # # # # #     for event in pygame.event.get():
# # # # # # # # # # # # # #         if event.type == pygame.QUIT:
# # # # # # # # # # # # # #             running = False

# # # # # # # # # # # # # #         if event.type == pygame.MOUSEBUTTONDOWN:
# # # # # # # # # # # # # #             for w in (wheel_num, wheel_let):
# # # # # # # # # # # # # #                 w["drag"] = True
# # # # # # # # # # # # # #                 w["last_mouse"] = mouse_angle(pygame.mouse.get_pos(), w["center"])
# # # # # # # # # # # # # #                 w["vel"] = 0
# # # # # # # # # # # # # #                 w["result"] = None
# # # # # # # # # # # # # #                 w["stopped"] = False
# # # # # # # # # # # # # #             first_stopped = None

# # # # # # # # # # # # # #         if event.type == pygame.MOUSEBUTTONUP:
# # # # # # # # # # # # # #             for w in (wheel_num, wheel_let):
# # # # # # # # # # # # # #                 w["drag"] = False
# # # # # # # # # # # # # #                 w["vel"] += random.uniform(-0.02,0.02)

# # # # # # # # # # # # # #         if event.type == pygame.MOUSEMOTION:
# # # # # # # # # # # # # #             for w in (wheel_num, wheel_let):
# # # # # # # # # # # # # #                 if w["drag"]:
# # # # # # # # # # # # # #                     m = mouse_angle(pygame.mouse.get_pos(), w["center"])
# # # # # # # # # # # # # #                     delta = m - w["last_mouse"]
# # # # # # # # # # # # # #                     w["vel"] += delta * 18
# # # # # # # # # # # # # #                     w["vel"] = max(-2, min(2, w["vel"]))
# # # # # # # # # # # # # #                     w["last_mouse"] = m

# # # # # # # # # # # # # #     # تحديث الفيزياء
# # # # # # # # # # # # # #     for w in (wheel_num, wheel_let):
# # # # # # # # # # # # # #         w["angle"] += w["vel"]
# # # # # # # # # # # # # #         w["vel"] *= friction(w["vel"])

# # # # # # # # # # # # # #         if abs(w["vel"]) < 0.0005 and not w["drag"] and not w["stopped"]:
# # # # # # # # # # # # # #             w["vel"] = 0
# # # # # # # # # # # # # #             idx = get_under_pointer(w)
# # # # # # # # # # # # # #             if w is wheel_num:
# # # # # # # # # # # # # #                 w["result"] = str(idx)
# # # # # # # # # # # # # #                 if first_stopped is None:
# # # # # # # # # # # # # #                     first_stopped = "number"
# # # # # # # # # # # # # #             else:
# # # # # # # # # # # # # #                 w["result"] = letters[idx]
# # # # # # # # # # # # # #                 if first_stopped is None:
# # # # # # # # # # # # # #                     first_stopped = "letter"
# # # # # # # # # # # # # #             w["stopped"] = True

# # # # # # # # # # # # # #     # رسم الدوارات
# # # # # # # # # # # # # #     draw_wheel(wheel_num, list(range(10)))
# # # # # # # # # # # # # #     draw_wheel(wheel_let, letters)

# # # # # # # # # # # # # #     # عرض النتائج أعلى الشاشة
# # # # # # # # # # # # # #     if wheel_num["result"] and wheel_let["result"]:
# # # # # # # # # # # # # #         if first_stopped == "number":
# # # # # # # # # # # # # #             right = wheel_num["result"]
# # # # # # # # # # # # # #             left = wheel_let["result"]
# # # # # # # # # # # # # #         else:
# # # # # # # # # # # # # #             right = wheel_let["result"]
# # # # # # # # # # # # # #             left = wheel_num["result"]

# # # # # # # # # # # # # #         r = BIG_FONT.render(right, True, (255,255,0))
# # # # # # # # # # # # # #         l = BIG_FONT.render(left, True, (255,255,0))

# # # # # # # # # # # # # #         screen.blit(r, r.get_rect(center=(WIDTH//2+40, 60)))
# # # # # # # # # # # # # #         screen.blit(l, l.get_rect(center=(WIDTH//2-40, 60)))

# # # # # # # # # # # # # #     pygame.display.flip()

# # # # # # # # # # # # # # pygame.quit()











# # # # # # # # # # # # # import pygame
# # # # # # # # # # # # # import math
# # # # # # # # # # # # # import random
# # # # # # # # # # # # # import string

# # # # # # # # # # # # # pygame.init()

# # # # # # # # # # # # # WIDTH, HEIGHT = 1000, 600
# # # # # # # # # # # # # screen = pygame.display.set_mode((WIDTH, HEIGHT))
# # # # # # # # # # # # # pygame.display.set_caption("دوّارتان مستقلتان (أرقام + حروف)")
# # # # # # # # # # # # # clock = pygame.time.Clock()

# # # # # # # # # # # # # FONT = pygame.font.SysFont("arial", 26, bold=True)
# # # # # # # # # # # # # BIG_FONT = pygame.font.SysFont("arial", 60, bold=True)

# # # # # # # # # # # # # BG = (25, 25, 25)
# # # # # # # # # # # # # POINTER_COLOR = (255, 255, 255)

# # # # # # # # # # # # # RADIUS = 180
# # # # # # # # # # # # # NUM_SECTIONS = 10
# # # # # # # # # # # # # SECTION_ANGLE = 2 * math.pi / NUM_SECTIONS

# # # # # # # # # # # # # CENTER_NUM = (300, 320)
# # # # # # # # # # # # # CENTER_LET = (700, 320)

# # # # # # # # # # # # # def new_wheel(center):
# # # # # # # # # # # # #     return {
# # # # # # # # # # # # #         "center": center,
# # # # # # # # # # # # #         "angle": 0,
# # # # # # # # # # # # #         "vel": 0,
# # # # # # # # # # # # #         "drag": False,
# # # # # # # # # # # # #         "last_mouse": 0,
# # # # # # # # # # # # #         "result": None,
# # # # # # # # # # # # #         "stopped": False
# # # # # # # # # # # # #     }

# # # # # # # # # # # # # wheel_num = new_wheel(CENTER_NUM)
# # # # # # # # # # # # # wheel_let = new_wheel(CENTER_LET)

# # # # # # # # # # # # # letters = list(string.ascii_uppercase[:10])

# # # # # # # # # # # # # COLORS = [
# # # # # # # # # # # # #     (255,99,71),(135,206,250),(255,215,0),(144,238,144),
# # # # # # # # # # # # #     (221,160,221),(255,182,193),(173,216,230),(240,230,140),
# # # # # # # # # # # # #     (255,160,122),(176,196,222)
# # # # # # # # # # # # # ]

# # # # # # # # # # # # # first_stopped = None
# # # # # # # # # # # # # active_wheel = None

# # # # # # # # # # # # # def friction(v):
# # # # # # # # # # # # #     return 0.995 - abs(v)*0.0005

# # # # # # # # # # # # # def mouse_angle(pos, center):
# # # # # # # # # # # # #     dx, dy = pos[0]-center[0], pos[1]-center[1]
# # # # # # # # # # # # #     return math.atan2(dy, dx)

# # # # # # # # # # # # # def inside_wheel(pos, center):
# # # # # # # # # # # # #     dx = pos[0]-center[0]
# # # # # # # # # # # # #     dy = pos[1]-center[1]
# # # # # # # # # # # # #     return math.hypot(dx, dy) <= RADIUS

# # # # # # # # # # # # # def draw_wheel(wheel, labels):
# # # # # # # # # # # # #     cx, cy = wheel["center"]
# # # # # # # # # # # # #     for i in range(NUM_SECTIONS):
# # # # # # # # # # # # #         a1 = wheel["angle"] + i*SECTION_ANGLE
# # # # # # # # # # # # #         a2 = a1 + SECTION_ANGLE

# # # # # # # # # # # # #         pygame.draw.polygon(
# # # # # # # # # # # # #             screen,
# # # # # # # # # # # # #             COLORS[i],
# # # # # # # # # # # # #             [(cx,cy),
# # # # # # # # # # # # #              (cx+RADIUS*math.cos(a1), cy+RADIUS*math.sin(a1)),
# # # # # # # # # # # # #              (cx+RADIUS*math.cos(a2), cy+RADIUS*math.sin(a2))]
# # # # # # # # # # # # #         )

# # # # # # # # # # # # #         ta = a1 + SECTION_ANGLE/2
# # # # # # # # # # # # #         tx = cx + (RADIUS-40)*math.cos(ta)
# # # # # # # # # # # # #         ty = cy + (RADIUS-40)*math.sin(ta)
# # # # # # # # # # # # #         txt = FONT.render(str(labels[i]), True, (0,0,0))
# # # # # # # # # # # # #         screen.blit(txt, txt.get_rect(center=(tx,ty)))

# # # # # # # # # # # # #     pygame.draw.circle(screen, (0,0,0), wheel["center"], RADIUS, 4)

# # # # # # # # # # # # #     pygame.draw.polygon(
# # # # # # # # # # # # #         screen, POINTER_COLOR,
# # # # # # # # # # # # #         [(cx-10, cy-RADIUS-5),
# # # # # # # # # # # # #          (cx+10, cy-RADIUS-5),
# # # # # # # # # # # # #          (cx, cy-RADIUS-30)]
# # # # # # # # # # # # #     )

# # # # # # # # # # # # # def get_under_pointer(wheel):
# # # # # # # # # # # # #     norm = wheel["angle"] % (2*math.pi)
# # # # # # # # # # # # #     pointer = -math.pi/2
# # # # # # # # # # # # #     rel = (pointer - norm) % (2*math.pi)
# # # # # # # # # # # # #     return int(rel // SECTION_ANGLE)

# # # # # # # # # # # # # running = True
# # # # # # # # # # # # # while running:
# # # # # # # # # # # # #     clock.tick(60)
# # # # # # # # # # # # #     screen.fill(BG)

# # # # # # # # # # # # #     for event in pygame.event.get():
# # # # # # # # # # # # #         if event.type == pygame.QUIT:
# # # # # # # # # # # # #             running = False

# # # # # # # # # # # # #         if event.type == pygame.MOUSEBUTTONDOWN:
# # # # # # # # # # # # #             pos = pygame.mouse.get_pos()
# # # # # # # # # # # # #             if inside_wheel(pos, wheel_num["center"]):
# # # # # # # # # # # # #                 active_wheel = wheel_num
# # # # # # # # # # # # #             elif inside_wheel(pos, wheel_let["center"]):
# # # # # # # # # # # # #                 active_wheel = wheel_let

# # # # # # # # # # # # #             if active_wheel:
# # # # # # # # # # # # #                 active_wheel["drag"] = True
# # # # # # # # # # # # #                 active_wheel["last_mouse"] = mouse_angle(pos, active_wheel["center"])
# # # # # # # # # # # # #                 active_wheel["vel"] = 0
# # # # # # # # # # # # #                 active_wheel["result"] = None
# # # # # # # # # # # # #                 active_wheel["stopped"] = False
# # # # # # # # # # # # #                 first_stopped = None

# # # # # # # # # # # # #         if event.type == pygame.MOUSEBUTTONUP:
# # # # # # # # # # # # #             if active_wheel:
# # # # # # # # # # # # #                 active_wheel["drag"] = False
# # # # # # # # # # # # #                 active_wheel["vel"] += random.uniform(-0.02,0.02)
# # # # # # # # # # # # #                 active_wheel = None

# # # # # # # # # # # # #         if event.type == pygame.MOUSEMOTION and active_wheel and active_wheel["drag"]:
# # # # # # # # # # # # #             m = mouse_angle(pygame.mouse.get_pos(), active_wheel["center"])
# # # # # # # # # # # # #             delta = m - active_wheel["last_mouse"]
# # # # # # # # # # # # #             active_wheel["vel"] += delta * 18
# # # # # # # # # # # # #             active_wheel["vel"] = max(-2, min(2, active_wheel["vel"]))
# # # # # # # # # # # # #             active_wheel["last_mouse"] = m

# # # # # # # # # # # # #     for w in (wheel_num, wheel_let):
# # # # # # # # # # # # #         w["angle"] += w["vel"]
# # # # # # # # # # # # #         w["vel"] *= friction(w["vel"])

# # # # # # # # # # # # #         if abs(w["vel"]) < 0.0005 and not w["drag"] and not w["stopped"]:
# # # # # # # # # # # # #             w["vel"] = 0
# # # # # # # # # # # # #             idx = get_under_pointer(w)
# # # # # # # # # # # # #             if w is wheel_num:
# # # # # # # # # # # # #                 w["result"] = str(idx)
# # # # # # # # # # # # #                 if first_stopped is None:
# # # # # # # # # # # # #                     first_stopped = "number"
# # # # # # # # # # # # #             else:
# # # # # # # # # # # # #                 w["result"] = letters[idx]
# # # # # # # # # # # # #                 if first_stopped is None:
# # # # # # # # # # # # #                     first_stopped = "letter"
# # # # # # # # # # # # #             w["stopped"] = True

# # # # # # # # # # # # #     draw_wheel(wheel_num, list(range(10)))
# # # # # # # # # # # # #     draw_wheel(wheel_let, letters)

# # # # # # # # # # # # #     if wheel_num["result"] and wheel_let["result"]:
# # # # # # # # # # # # #         if first_stopped == "number":
# # # # # # # # # # # # #             right = wheel_num["result"]
# # # # # # # # # # # # #             left = wheel_let["result"]
# # # # # # # # # # # # #         else:
# # # # # # # # # # # # #             right = wheel_let["result"]
# # # # # # # # # # # # #             left = wheel_num["result"]

# # # # # # # # # # # # #         r = BIG_FONT.render(right, True, (255,255,0))
# # # # # # # # # # # # #         l = BIG_FONT.render(left, True, (255,255,0))
# # # # # # # # # # # # #         screen.blit(r, r.get_rect(center=(WIDTH//2+40, 60)))
# # # # # # # # # # # # #         screen.blit(l, l.get_rect(center=(WIDTH//2-40, 60)))

# # # # # # # # # # # # #     pygame.display.flip()

# # # # # # # # # # # # # pygame.quit()










# # # # # # # # # # # # import pygame
# # # # # # # # # # # # import math
# # # # # # # # # # # # import random
# # # # # # # # # # # # import string

# # # # # # # # # # # # pygame.init()

# # # # # # # # # # # # # ================= إعدادات عامة =================
# # # # # # # # # # # # WIDTH, HEIGHT = 1200, 600
# # # # # # # # # # # # screen = pygame.display.set_mode((WIDTH, HEIGHT))
# # # # # # # # # # # # pygame.display.set_caption("3 دوّارات فيزيائية (أرقام - حروف - رموز)")
# # # # # # # # # # # # clock = pygame.time.Clock()

# # # # # # # # # # # # FONT = pygame.font.SysFont("arial", 24, bold=True)
# # # # # # # # # # # # BIG_FONT = pygame.font.SysFont("arial", 55, bold=True)

# # # # # # # # # # # # BG = (25, 25, 25)
# # # # # # # # # # # # POINTER_COLOR = (255, 255, 255)

# # # # # # # # # # # # RADIUS = 150

# # # # # # # # # # # # # ================= مراكز الدوّارات =================
# # # # # # # # # # # # CENTER_NUM = (250, 330)
# # # # # # # # # # # # CENTER_LET = (600, 330)
# # # # # # # # # # # # CENTER_SYM = (950, 330)

# # # # # # # # # # # # # ================= بيانات الدوّارات =================
# # # # # # # # # # # # def new_wheel(center, labels):
# # # # # # # # # # # #     return {
# # # # # # # # # # # #         "center": center,
# # # # # # # # # # # #         "labels": labels,
# # # # # # # # # # # #         "angle": 0,
# # # # # # # # # # # #         "vel": 0,
# # # # # # # # # # # #         "drag": False,
# # # # # # # # # # # #         "last_mouse": 0,
# # # # # # # # # # # #         "result": None,
# # # # # # # # # # # #         "stopped": False
# # # # # # # # # # # #     }

# # # # # # # # # # # # wheel_num = new_wheel(CENTER_NUM, list(range(10)))
# # # # # # # # # # # # wheel_let = new_wheel(CENTER_LET, list(string.ascii_uppercase[:10]))
# # # # # # # # # # # # wheel_sym = new_wheel(CENTER_SYM, list("!@#$%^&*?"))

# # # # # # # # # # # # wheels = [wheel_num, wheel_let, wheel_sym]

# # # # # # # # # # # # COLORS = [
# # # # # # # # # # # #     (255,99,71),(135,206,250),(255,215,0),(144,238,144),
# # # # # # # # # # # #     (221,160,221),(255,182,193),(173,216,230),(240,230,140),
# # # # # # # # # # # #     (255,160,122),(176,196,222)
# # # # # # # # # # # # ]

# # # # # # # # # # # # active_wheel = None
# # # # # # # # # # # # results_order = []

# # # # # # # # # # # # # ================= دوال =================
# # # # # # # # # # # # def friction(v):
# # # # # # # # # # # #     return 0.995 - abs(v)*0.0005

# # # # # # # # # # # # def mouse_angle(pos, center):
# # # # # # # # # # # #     dx, dy = pos[0]-center[0], pos[1]-center[1]
# # # # # # # # # # # #     return math.atan2(dy, dx)

# # # # # # # # # # # # def inside_wheel(pos, center):
# # # # # # # # # # # #     dx = pos[0]-center[0]
# # # # # # # # # # # #     dy = pos[1]-center[1]
# # # # # # # # # # # #     return math.hypot(dx, dy) <= RADIUS

# # # # # # # # # # # # def draw_wheel(wheel):
# # # # # # # # # # # #     cx, cy = wheel["center"]
# # # # # # # # # # # #     labels = wheel["labels"]
# # # # # # # # # # # #     sections = len(labels)
# # # # # # # # # # # #     section_angle = 2 * math.pi / sections

# # # # # # # # # # # #     for i in range(sections):
# # # # # # # # # # # #         a1 = wheel["angle"] + i * section_angle
# # # # # # # # # # # #         a2 = a1 + section_angle

# # # # # # # # # # # #         pygame.draw.polygon(
# # # # # # # # # # # #             screen,
# # # # # # # # # # # #             COLORS[i % len(COLORS)],
# # # # # # # # # # # #             [(cx, cy),
# # # # # # # # # # # #              (cx + RADIUS * math.cos(a1), cy + RADIUS * math.sin(a1)),
# # # # # # # # # # # #              (cx + RADIUS * math.cos(a2), cy + RADIUS * math.sin(a2))]
# # # # # # # # # # # #         )

# # # # # # # # # # # #         ta = a1 + section_angle / 2
# # # # # # # # # # # #         tx = cx + (RADIUS - 35) * math.cos(ta)
# # # # # # # # # # # #         ty = cy + (RADIUS - 35) * math.sin(ta)
# # # # # # # # # # # #         txt = FONT.render(str(labels[i]), True, (0,0,0))
# # # # # # # # # # # #         screen.blit(txt, txt.get_rect(center=(tx, ty)))

# # # # # # # # # # # #     pygame.draw.circle(screen, (0,0,0), wheel["center"], RADIUS, 4)

# # # # # # # # # # # #     pygame.draw.polygon(
# # # # # # # # # # # #         screen, POINTER_COLOR,
# # # # # # # # # # # #         [(cx-10, cy-RADIUS-5),
# # # # # # # # # # # #          (cx+10, cy-RADIUS-5),
# # # # # # # # # # # #          (cx, cy-RADIUS-28)]
# # # # # # # # # # # #     )

# # # # # # # # # # # # def get_under_pointer(wheel):
# # # # # # # # # # # #     labels = wheel["labels"]
# # # # # # # # # # # #     sections = len(labels)
# # # # # # # # # # # #     section_angle = 2 * math.pi / sections
# # # # # # # # # # # #     norm = wheel["angle"] % (2 * math.pi)
# # # # # # # # # # # #     pointer = -math.pi / 2
# # # # # # # # # # # #     rel = (pointer - norm) % (2 * math.pi)
# # # # # # # # # # # #     return labels[int(rel // section_angle)]

# # # # # # # # # # # # # ================= الحلقة الرئيسية =================
# # # # # # # # # # # # running = True
# # # # # # # # # # # # while running:
# # # # # # # # # # # #     clock.tick(60)
# # # # # # # # # # # #     screen.fill(BG)

# # # # # # # # # # # #     for event in pygame.event.get():
# # # # # # # # # # # #         if event.type == pygame.QUIT:
# # # # # # # # # # # #             running = False

# # # # # # # # # # # #         if event.type == pygame.MOUSEBUTTONDOWN:
# # # # # # # # # # # #             pos = pygame.mouse.get_pos()
# # # # # # # # # # # #             for w in wheels:
# # # # # # # # # # # #                 if inside_wheel(pos, w["center"]):
# # # # # # # # # # # #                     active_wheel = w
# # # # # # # # # # # #                     w["drag"] = True
# # # # # # # # # # # #                     w["last_mouse"] = mouse_angle(pos, w["center"])
# # # # # # # # # # # #                     w["vel"] = 0
# # # # # # # # # # # #                     w["result"] = None
# # # # # # # # # # # #                     w["stopped"] = False
# # # # # # # # # # # #                     if w in results_order:
# # # # # # # # # # # #                         results_order.remove(w)

# # # # # # # # # # # #         if event.type == pygame.MOUSEBUTTONUP:
# # # # # # # # # # # #             if active_wheel:
# # # # # # # # # # # #                 active_wheel["drag"] = False
# # # # # # # # # # # #                 active_wheel["vel"] += random.uniform(-0.02, 0.02)
# # # # # # # # # # # #                 active_wheel = None

# # # # # # # # # # # #         if event.type == pygame.MOUSEMOTION and active_wheel and active_wheel["drag"]:
# # # # # # # # # # # #             m = mouse_angle(pygame.mouse.get_pos(), active_wheel["center"])
# # # # # # # # # # # #             delta = m - active_wheel["last_mouse"]
# # # # # # # # # # # #             active_wheel["vel"] += delta * 18
# # # # # # # # # # # #             active_wheel["vel"] = max(-2, min(2, active_wheel["vel"]))
# # # # # # # # # # # #             active_wheel["last_mouse"] = m

# # # # # # # # # # # #     for w in wheels:
# # # # # # # # # # # #         w["angle"] += w["vel"]
# # # # # # # # # # # #         w["vel"] *= friction(w["vel"])

# # # # # # # # # # # #         if abs(w["vel"]) < 0.0005 and not w["drag"] and not w["stopped"]:
# # # # # # # # # # # #             w["vel"] = 0
# # # # # # # # # # # #             w["result"] = str(get_under_pointer(w))
# # # # # # # # # # # #             w["stopped"] = True
# # # # # # # # # # # #             results_order.append(w)

# # # # # # # # # # # #     for w in wheels:
# # # # # # # # # # # #         draw_wheel(w)

# # # # # # # # # # # #     # عرض النتائج أعلى الشاشة حسب ترتيب التوقف
# # # # # # # # # # # #     x_start = WIDTH//2 - 80
# # # # # # # # # # # #     y = 60
# # # # # # # # # # # #     for i, w in enumerate(results_order):
# # # # # # # # # # # #         txt = BIG_FONT.render(w["result"], True, (255,255,0))
# # # # # # # # # # # #         screen.blit(txt, txt.get_rect(center=(x_start + i*80, y)))

# # # # # # # # # # # #     pygame.display.flip()

# # # # # # # # # # # # pygame.quit()












# # # # # # # # # # # import pygame
# # # # # # # # # # # import math
# # # # # # # # # # # import random
# # # # # # # # # # # import string

# # # # # # # # # # # pygame.init()

# # # # # # # # # # # # ================= إعدادات عامة =================
# # # # # # # # # # # WIDTH, HEIGHT = 1500, 650
# # # # # # # # # # # screen = pygame.display.set_mode((WIDTH, HEIGHT))
# # # # # # # # # # # pygame.display.set_caption("4 دوّارات فيزيائية")
# # # # # # # # # # # clock = pygame.time.Clock()

# # # # # # # # # # # FONT = pygame.font.SysFont("arial", 22, bold=True)
# # # # # # # # # # # BIG_FONT = pygame.font.SysFont("arial", 50, bold=True)

# # # # # # # # # # # BG = (25, 25, 25)
# # # # # # # # # # # POINTER_COLOR = (255, 255, 255)

# # # # # # # # # # # RADIUS = 140

# # # # # # # # # # # # ================= مراكز الدوّارات =================
# # # # # # # # # # # CENTERS = [
# # # # # # # # # # #     (200, 360),   # أرقام
# # # # # # # # # # #     (550, 360),   # حروف
# # # # # # # # # # #     (900, 360),   # رموز
# # # # # # # # # # #     (1250, 360)   # أقواس واقتباسات
# # # # # # # # # # # ]

# # # # # # # # # # # # ================= بيانات الدوّارة =================
# # # # # # # # # # # def new_wheel(center, labels):
# # # # # # # # # # #     return {
# # # # # # # # # # #         "center": center,
# # # # # # # # # # #         "labels": labels,
# # # # # # # # # # #         "angle": 0,
# # # # # # # # # # #         "vel": 0,
# # # # # # # # # # #         "drag": False,
# # # # # # # # # # #         "last_mouse": 0,
# # # # # # # # # # #         "result": None,
# # # # # # # # # # #         "stopped": False
# # # # # # # # # # #     }

# # # # # # # # # # # wheel_num = new_wheel(CENTERS[0], list(range(10)))
# # # # # # # # # # # wheel_let = new_wheel(CENTERS[1], list(string.ascii_uppercase[:10]))
# # # # # # # # # # # wheel_sym = new_wheel(CENTERS[2], list("!@#$%^&*?"))
# # # # # # # # # # # wheel_brk = new_wheel(
# # # # # # # # # # #     CENTERS[3],
# # # # # # # # # # #     ['(', ')', '[', ']', '{', '}', '<', '>', '"', "'"]
# # # # # # # # # # # )

# # # # # # # # # # # wheels = [wheel_num, wheel_let, wheel_sym, wheel_brk]

# # # # # # # # # # # COLORS = [
# # # # # # # # # # #     (255,99,71),(135,206,250),(255,215,0),(144,238,144),
# # # # # # # # # # #     (221,160,221),(255,182,193),(173,216,230),(240,230,140),
# # # # # # # # # # #     (255,160,122),(176,196,222)
# # # # # # # # # # # ]

# # # # # # # # # # # active_wheel = None
# # # # # # # # # # # results_order = []

# # # # # # # # # # # # ================= دوال =================
# # # # # # # # # # # def friction(v):
# # # # # # # # # # #     return 0.995 - abs(v)*0.0005

# # # # # # # # # # # def mouse_angle(pos, center):
# # # # # # # # # # #     dx, dy = pos[0]-center[0], pos[1]-center[1]
# # # # # # # # # # #     return math.atan2(dy, dx)

# # # # # # # # # # # def inside_wheel(pos, center):
# # # # # # # # # # #     dx = pos[0]-center[0]
# # # # # # # # # # #     dy = pos[1]-center[1]
# # # # # # # # # # #     return math.hypot(dx, dy) <= RADIUS

# # # # # # # # # # # def draw_wheel(wheel):
# # # # # # # # # # #     cx, cy = wheel["center"]
# # # # # # # # # # #     labels = wheel["labels"]
# # # # # # # # # # #     sections = len(labels)
# # # # # # # # # # #     section_angle = 2 * math.pi / sections

# # # # # # # # # # #     for i in range(sections):
# # # # # # # # # # #         a1 = wheel["angle"] + i * section_angle
# # # # # # # # # # #         a2 = a1 + section_angle

# # # # # # # # # # #         pygame.draw.polygon(
# # # # # # # # # # #             screen,
# # # # # # # # # # #             COLORS[i % len(COLORS)],
# # # # # # # # # # #             [(cx, cy),
# # # # # # # # # # #              (cx + RADIUS * math.cos(a1), cy + RADIUS * math.sin(a1)),
# # # # # # # # # # #              (cx + RADIUS * math.cos(a2), cy + RADIUS * math.sin(a2))]
# # # # # # # # # # #         )

# # # # # # # # # # #         ta = a1 + section_angle / 2
# # # # # # # # # # #         tx = cx + (RADIUS - 35) * math.cos(ta)
# # # # # # # # # # #         ty = cy + (RADIUS - 35) * math.sin(ta)
# # # # # # # # # # #         txt = FONT.render(str(labels[i]), True, (0,0,0))
# # # # # # # # # # #         screen.blit(txt, txt.get_rect(center=(tx, ty)))

# # # # # # # # # # #     pygame.draw.circle(screen, (0,0,0), wheel["center"], RADIUS, 4)

# # # # # # # # # # #     pygame.draw.polygon(
# # # # # # # # # # #         screen, POINTER_COLOR,
# # # # # # # # # # #         [(cx-10, cy-RADIUS-5),
# # # # # # # # # # #          (cx+10, cy-RADIUS-5),
# # # # # # # # # # #          (cx, cy-RADIUS-28)]
# # # # # # # # # # #     )

# # # # # # # # # # # def get_under_pointer(wheel):
# # # # # # # # # # #     labels = wheel["labels"]
# # # # # # # # # # #     sections = len(labels)
# # # # # # # # # # #     section_angle = 2 * math.pi / sections
# # # # # # # # # # #     norm = wheel["angle"] % (2 * math.pi)
# # # # # # # # # # #     pointer = -math.pi / 2
# # # # # # # # # # #     rel = (pointer - norm) % (2 * math.pi)
# # # # # # # # # # #     return labels[int(rel // section_angle)]

# # # # # # # # # # # # ================= الحلقة الرئيسية =================
# # # # # # # # # # # running = True
# # # # # # # # # # # while running:
# # # # # # # # # # #     clock.tick(60)
# # # # # # # # # # #     screen.fill(BG)

# # # # # # # # # # #     for event in pygame.event.get():
# # # # # # # # # # #         if event.type == pygame.QUIT:
# # # # # # # # # # #             running = False

# # # # # # # # # # #         if event.type == pygame.MOUSEBUTTONDOWN:
# # # # # # # # # # #             pos = pygame.mouse.get_pos()
# # # # # # # # # # #             for w in wheels:
# # # # # # # # # # #                 if inside_wheel(pos, w["center"]):
# # # # # # # # # # #                     active_wheel = w
# # # # # # # # # # #                     w["drag"] = True
# # # # # # # # # # #                     w["last_mouse"] = mouse_angle(pos, w["center"])
# # # # # # # # # # #                     w["vel"] = 0
# # # # # # # # # # #                     w["result"] = None
# # # # # # # # # # #                     w["stopped"] = False
# # # # # # # # # # #                     if w in results_order:
# # # # # # # # # # #                         results_order.remove(w)

# # # # # # # # # # #         if event.type == pygame.MOUSEBUTTONUP:
# # # # # # # # # # #             if active_wheel:
# # # # # # # # # # #                 active_wheel["drag"] = False
# # # # # # # # # # #                 active_wheel["vel"] += random.uniform(-0.02, 0.02)
# # # # # # # # # # #                 active_wheel = None

# # # # # # # # # # #         if event.type == pygame.MOUSEMOTION and active_wheel and active_wheel["drag"]:
# # # # # # # # # # #             m = mouse_angle(pygame.mouse.get_pos(), active_wheel["center"])
# # # # # # # # # # #             delta = m - active_wheel["last_mouse"]
# # # # # # # # # # #             active_wheel["vel"] += delta * 18
# # # # # # # # # # #             active_wheel["vel"] = max(-2, min(2, active_wheel["vel"]))
# # # # # # # # # # #             active_wheel["last_mouse"] = m

# # # # # # # # # # #     for w in wheels:
# # # # # # # # # # #         w["angle"] += w["vel"]
# # # # # # # # # # #         w["vel"] *= friction(w["vel"])

# # # # # # # # # # #         if abs(w["vel"]) < 0.0005 and not w["drag"] and not w["stopped"]:
# # # # # # # # # # #             w["vel"] = 0
# # # # # # # # # # #             w["result"] = str(get_under_pointer(w))
# # # # # # # # # # #             w["stopped"] = True
# # # # # # # # # # #             results_order.append(w)

# # # # # # # # # # #     for w in wheels:
# # # # # # # # # # #         draw_wheel(w)

# # # # # # # # # # #     # عرض النتائج أعلى الشاشة حسب ترتيب التوقف
# # # # # # # # # # #     x_start = WIDTH//2 - 120
# # # # # # # # # # #     y = 60
# # # # # # # # # # #     for i, w in enumerate(results_order):
# # # # # # # # # # #         txt = BIG_FONT.render(w["result"], True, (255,255,0))
# # # # # # # # # # #         screen.blit(txt, txt.get_rect(center=(x_start + i*80, y)))

# # # # # # # # # # #     pygame.display.flip()

# # # # # # # # # # # pygame.quit()





# # # # # # # # # # import pygame
# # # # # # # # # # import math
# # # # # # # # # # import random
# # # # # # # # # # import string

# # # # # # # # # # pygame.init()

# # # # # # # # # # # ================= إعدادات عامة =================
# # # # # # # # # # WIDTH, HEIGHT = 1800, 650
# # # # # # # # # # screen = pygame.display.set_mode((WIDTH, HEIGHT))
# # # # # # # # # # pygame.display.set_caption("8 دوّارات فيزيائية")
# # # # # # # # # # clock = pygame.time.Clock()

# # # # # # # # # # FONT = pygame.font.SysFont("arial", 22, bold=True)
# # # # # # # # # # BIG_FONT = pygame.font.SysFont("arial", 50, bold=True)

# # # # # # # # # # BG = (25, 25, 25)
# # # # # # # # # # POINTER_COLOR = (255, 255, 255)

# # # # # # # # # # RADIUS = 140

# # # # # # # # # # # ================= مراكز الدوّارات المضاعفة =================
# # # # # # # # # # ORIGINAL_CENTERS = [
# # # # # # # # # #     (200, 360),   # أرقام
# # # # # # # # # #     (550, 360),   # حروف
# # # # # # # # # #     (900, 360),   # رموز
# # # # # # # # # #     (1250, 360)   # أقواس واقتباسات
# # # # # # # # # # ]

# # # # # # # # # # # مضاعفة كل مركز على المحور X (+250)
# # # # # # # # # # CENTERS = []
# # # # # # # # # # for x, y in ORIGINAL_CENTERS:
# # # # # # # # # #     CENTERS.append((x, y))          # الأصلية
# # # # # # # # # #     CENTERS.append((x+250, y))      # النسخة الثانية

# # # # # # # # # # # ================= دالة إنشاء العجلة =================
# # # # # # # # # # def new_wheel(center, labels):
# # # # # # # # # #     return {
# # # # # # # # # #         "center": center,
# # # # # # # # # #         "labels": labels,
# # # # # # # # # #         "angle": 0,
# # # # # # # # # #         "vel": 0,
# # # # # # # # # #         "drag": False,
# # # # # # # # # #         "last_mouse": 0,
# # # # # # # # # #         "result": None,
# # # # # # # # # #         "stopped": False
# # # # # # # # # #     }

# # # # # # # # # # # ================= بيانات الدوّارات =================
# # # # # # # # # # labels_list = [
# # # # # # # # # #     list(range(10)),                   # أرقام
# # # # # # # # # #     list(string.ascii_uppercase[:10]), # حروف
# # # # # # # # # #     list("!@#$%^&*?"),                 # رموز
# # # # # # # # # #     ['(', ')', '[', ']', '{', '}', '<', '>', '"', "'"]  # أقواس
# # # # # # # # # # ]

# # # # # # # # # # # إنشاء العجلات 8 عجلات
# # # # # # # # # # wheels = []
# # # # # # # # # # for center, labels in zip(CENTERS, labels_list*2):  # تكرار الرموز لكل نسخة
# # # # # # # # # #     wheels.append(new_wheel(center, labels))

# # # # # # # # # # COLORS = [
# # # # # # # # # #     (255,99,71),(135,206,250),(255,215,0),(144,238,144),
# # # # # # # # # #     (221,160,221),(255,182,193),(173,216,230),(240,230,140),
# # # # # # # # # #     (255,160,122),(176,196,222)
# # # # # # # # # # ]

# # # # # # # # # # active_wheel = None
# # # # # # # # # # results_order = []

# # # # # # # # # # # ================= دوال =================
# # # # # # # # # # def friction(v):
# # # # # # # # # #     return 0.995 - abs(v)*0.0005

# # # # # # # # # # def mouse_angle(pos, center):
# # # # # # # # # #     dx, dy = pos[0]-center[0], pos[1]-center[1]
# # # # # # # # # #     return math.atan2(dy, dx)

# # # # # # # # # # def inside_wheel(pos, center):
# # # # # # # # # #     dx = pos[0]-center[0]
# # # # # # # # # #     dy = pos[1]-center[1]
# # # # # # # # # #     return math.hypot(dx, dy) <= RADIUS

# # # # # # # # # # def draw_wheel(wheel):
# # # # # # # # # #     cx, cy = wheel["center"]
# # # # # # # # # #     labels = wheel["labels"]
# # # # # # # # # #     sections = len(labels)
# # # # # # # # # #     section_angle = 2 * math.pi / sections

# # # # # # # # # #     for i in range(sections):
# # # # # # # # # #         a1 = wheel["angle"] + i * section_angle
# # # # # # # # # #         a2 = a1 + section_angle

# # # # # # # # # #         pygame.draw.polygon(
# # # # # # # # # #             screen,
# # # # # # # # # #             COLORS[i % len(COLORS)],
# # # # # # # # # #             [(cx, cy),
# # # # # # # # # #              (cx + RADIUS * math.cos(a1), cy + RADIUS * math.sin(a1)),
# # # # # # # # # #              (cx + RADIUS * math.cos(a2), cy + RADIUS * math.sin(a2))]
# # # # # # # # # #         )

# # # # # # # # # #         ta = a1 + section_angle / 2
# # # # # # # # # #         tx = cx + (RADIUS - 35) * math.cos(ta)
# # # # # # # # # #         ty = cy + (RADIUS - 35) * math.sin(ta)
# # # # # # # # # #         txt = FONT.render(str(labels[i]), True, (0,0,0))
# # # # # # # # # #         screen.blit(txt, txt.get_rect(center=(tx, ty)))

# # # # # # # # # #     pygame.draw.circle(screen, (0,0,0), wheel["center"], RADIUS, 4)

# # # # # # # # # #     pygame.draw.polygon(
# # # # # # # # # #         screen, POINTER_COLOR,
# # # # # # # # # #         [(cx-10, cy-RADIUS-5),
# # # # # # # # # #          (cx+10, cy-RADIUS-5),
# # # # # # # # # #          (cx, cy-RADIUS-28)]
# # # # # # # # # #     )

# # # # # # # # # # def get_under_pointer(wheel):
# # # # # # # # # #     labels = wheel["labels"]
# # # # # # # # # #     sections = len(labels)
# # # # # # # # # #     section_angle = 2 * math.pi / sections
# # # # # # # # # #     norm = wheel["angle"] % (2 * math.pi)
# # # # # # # # # #     pointer = -math.pi / 2
# # # # # # # # # #     rel = (pointer - norm) % (2 * math.pi)
# # # # # # # # # #     return labels[int(rel // section_angle)]

# # # # # # # # # # # ================= الحلقة الرئيسية =================
# # # # # # # # # # running = True
# # # # # # # # # # while running:
# # # # # # # # # #     clock.tick(60)
# # # # # # # # # #     screen.fill(BG)

# # # # # # # # # #     for event in pygame.event.get():
# # # # # # # # # #         if event.type == pygame.QUIT:
# # # # # # # # # #             running = False

# # # # # # # # # #         if event.type == pygame.MOUSEBUTTONDOWN:
# # # # # # # # # #             pos = pygame.mouse.get_pos()
# # # # # # # # # #             for w in wheels:
# # # # # # # # # #                 if inside_wheel(pos, w["center"]):
# # # # # # # # # #                     active_wheel = w
# # # # # # # # # #                     w["drag"] = True
# # # # # # # # # #                     w["last_mouse"] = mouse_angle(pos, w["center"])
# # # # # # # # # #                     w["vel"] = 0
# # # # # # # # # #                     w["result"] = None
# # # # # # # # # #                     w["stopped"] = False
# # # # # # # # # #                     if w in results_order:
# # # # # # # # # #                         results_order.remove(w)

# # # # # # # # # #         if event.type == pygame.MOUSEBUTTONUP:
# # # # # # # # # #             if active_wheel:
# # # # # # # # # #                 active_wheel["drag"] = False
# # # # # # # # # #                 active_wheel["vel"] += random.uniform(-0.02, 0.02)
# # # # # # # # # #                 active_wheel = None

# # # # # # # # # #         if event.type == pygame.MOUSEMOTION and active_wheel and active_wheel["drag"]:
# # # # # # # # # #             m = mouse_angle(pygame.mouse.get_pos(), active_wheel["center"])
# # # # # # # # # #             delta = m - active_wheel["last_mouse"]
# # # # # # # # # #             active_wheel["vel"] += delta * 18
# # # # # # # # # #             active_wheel["vel"] = max(-2, min(2, active_wheel["vel"]))
# # # # # # # # # #             active_wheel["last_mouse"] = m

# # # # # # # # # #     for w in wheels:
# # # # # # # # # #         w["angle"] += w["vel"]
# # # # # # # # # #         w["vel"] *= friction(w["vel"])

# # # # # # # # # #         if abs(w["vel"]) < 0.0005 and not w["drag"] and not w["stopped"]:
# # # # # # # # # #             w["vel"] = 0
# # # # # # # # # #             w["result"] = str(get_under_pointer(w))
# # # # # # # # # #             w["stopped"] = True
# # # # # # # # # #             results_order.append(w)

# # # # # # # # # #     for w in wheels:
# # # # # # # # # #         draw_wheel(w)

# # # # # # # # # #     # عرض النتائج أعلى الشاشة حسب ترتيب التوقف
# # # # # # # # # #     x_start = WIDTH//2 - 200
# # # # # # # # # #     y = 60
# # # # # # # # # #     for i, w in enumerate(results_order):
# # # # # # # # # #         txt = BIG_FONT.render(w["result"], True, (255,255,0))
# # # # # # # # # #         screen.blit(txt, txt.get_rect(center=(x_start + i*80, y)))

# # # # # # # # # #     pygame.display.flip()

# # # # # # # # # # pygame.quit()






# # # # # # # # # import pygame
# # # # # # # # # import math
# # # # # # # # # import random
# # # # # # # # # import string

# # # # # # # # # pygame.init()

# # # # # # # # # # ================= إعدادات عامة =================
# # # # # # # # # WIDTH, HEIGHT = 1800, 650
# # # # # # # # # screen = pygame.display.set_mode((WIDTH, HEIGHT))
# # # # # # # # # pygame.display.set_caption("8 دوّارات فيزيائية")
# # # # # # # # # clock = pygame.time.Clock()

# # # # # # # # # FONT = pygame.font.SysFont("arial", 22, bold=True)
# # # # # # # # # BIG_FONT = pygame.font.SysFont("arial", 50, bold=True)

# # # # # # # # # BG = (25, 25, 25)
# # # # # # # # # POINTER_COLOR = (255, 255, 255)

# # # # # # # # # RADIUS = 140

# # # # # # # # # # ================= مراكز الدوّارات المضاعفة =================
# # # # # # # # # ORIGINAL_CENTERS = [
# # # # # # # # #     (200, 360),   # أرقام
# # # # # # # # #     (550, 360),   # حروف
# # # # # # # # #     (900, 360),   # رموز
# # # # # # # # #     (1250, 360)   # أقواس واقتباسات
# # # # # # # # # ]

# # # # # # # # # # مضاعفة كل مركز على المحور X (+250)
# # # # # # # # # CENTERS = []
# # # # # # # # # for x, y in ORIGINAL_CENTERS:
# # # # # # # # #     CENTERS.append((x, y))          # الأصلية
# # # # # # # # #     CENTERS.append((x+250, y))      # النسخة الثانية

# # # # # # # # # # ================= دالة إنشاء العجلة =================
# # # # # # # # # def new_wheel(center, labels):
# # # # # # # # #     return {
# # # # # # # # #         "center": center,
# # # # # # # # #         "labels": labels,
# # # # # # # # #         "angle": 0,
# # # # # # # # #         "vel": 0,
# # # # # # # # #         "drag": False,
# # # # # # # # #         "last_mouse": 0,
# # # # # # # # #         "result": None,
# # # # # # # # #         "stopped": False
# # # # # # # # #     }

# # # # # # # # # # ================= بيانات الدوّارات =================
# # # # # # # # # labels_list = [
# # # # # # # # #     list(range(10)),                   # أرقام
# # # # # # # # #     list(string.ascii_uppercase),      # كل الحروف
# # # # # # # # #     list("!@#$%^&*?"),                 # رموز
# # # # # # # # #     ['(', ')', '[', ']', '{', '}', '<', '>', '"', "'"]  # أقواس
# # # # # # # # # ]

# # # # # # # # # # إنشاء العجلات 8 عجلات
# # # # # # # # # wheels = []
# # # # # # # # # for center, labels in zip(CENTERS, labels_list*2):  # نسخة لكل مركز مضاعف
# # # # # # # # #     wheels.append(new_wheel(center, labels))

# # # # # # # # # COLORS = [
# # # # # # # # #     (255,99,71),(135,206,250),(255,215,0),(144,238,144),
# # # # # # # # #     (221,160,221),(255,182,193),(173,216,230),(240,230,140),
# # # # # # # # #     (255,160,122),(176,196,222)
# # # # # # # # # ]

# # # # # # # # # active_wheel = None
# # # # # # # # # results_order = []

# # # # # # # # # # ================= دوال =================
# # # # # # # # # def friction(v):
# # # # # # # # #     return 0.995 - abs(v)*0.0005

# # # # # # # # # def mouse_angle(pos, center):
# # # # # # # # #     dx, dy = pos[0]-center[0], pos[1]-center[1]
# # # # # # # # #     return math.atan2(dy, dx)

# # # # # # # # # def inside_wheel(pos, center):
# # # # # # # # #     dx = pos[0]-center[0]
# # # # # # # # #     dy = pos[1]-center[1]
# # # # # # # # #     return math.hypot(dx, dy) <= RADIUS

# # # # # # # # # def draw_wheel(wheel):
# # # # # # # # #     cx, cy = wheel["center"]
# # # # # # # # #     labels = wheel["labels"]
# # # # # # # # #     sections = len(labels)
# # # # # # # # #     section_angle = 2 * math.pi / sections

# # # # # # # # #     for i in range(sections):
# # # # # # # # #         a1 = wheel["angle"] + i * section_angle
# # # # # # # # #         a2 = a1 + section_angle

# # # # # # # # #         pygame.draw.polygon(
# # # # # # # # #             screen,
# # # # # # # # #             COLORS[i % len(COLORS)],
# # # # # # # # #             [(cx, cy),
# # # # # # # # #              (cx + RADIUS * math.cos(a1), cy + RADIUS * math.sin(a1)),
# # # # # # # # #              (cx + RADIUS * math.cos(a2), cy + RADIUS * math.sin(a2))]
# # # # # # # # #         )

# # # # # # # # #         ta = a1 + section_angle / 2
# # # # # # # # #         tx = cx + (RADIUS - 35) * math.cos(ta)
# # # # # # # # #         ty = cy + (RADIUS - 35) * math.sin(ta)
# # # # # # # # #         txt = FONT.render(str(labels[i]), True, (0,0,0))
# # # # # # # # #         screen.blit(txt, txt.get_rect(center=(tx, ty)))

# # # # # # # # #     pygame.draw.circle(screen, (0,0,0), wheel["center"], RADIUS, 4)

# # # # # # # # #     pygame.draw.polygon(
# # # # # # # # #         screen, POINTER_COLOR,
# # # # # # # # #         [(cx-10, cy-RADIUS-5),
# # # # # # # # #          (cx+10, cy-RADIUS-5),
# # # # # # # # #          (cx, cy-RADIUS-28)]
# # # # # # # # #     )

# # # # # # # # # def get_under_pointer(wheel):
# # # # # # # # #     labels = wheel["labels"]
# # # # # # # # #     sections = len(labels)
# # # # # # # # #     section_angle = 2 * math.pi / sections
# # # # # # # # #     norm = wheel["angle"] % (2 * math.pi)
# # # # # # # # #     pointer = -math.pi / 2
# # # # # # # # #     rel = (pointer - norm) % (2 * math.pi)
# # # # # # # # #     return labels[int(rel // section_angle)]

# # # # # # # # # # ================= الحلقة الرئيسية =================
# # # # # # # # # running = True
# # # # # # # # # while running:
# # # # # # # # #     clock.tick(60)
# # # # # # # # #     screen.fill(BG)

# # # # # # # # #     for event in pygame.event.get():
# # # # # # # # #         if event.type == pygame.QUIT:
# # # # # # # # #             running = False

# # # # # # # # #         if event.type == pygame.MOUSEBUTTONDOWN:
# # # # # # # # #             pos = pygame.mouse.get_pos()
# # # # # # # # #             for w in wheels:
# # # # # # # # #                 if inside_wheel(pos, w["center"]):
# # # # # # # # #                     active_wheel = w
# # # # # # # # #                     w["drag"] = True
# # # # # # # # #                     w["last_mouse"] = mouse_angle(pos, w["center"])
# # # # # # # # #                     w["vel"] = 0
# # # # # # # # #                     w["result"] = None
# # # # # # # # #                     w["stopped"] = False
# # # # # # # # #                     if w in results_order:
# # # # # # # # #                         results_order.remove(w)

# # # # # # # # #         if event.type == pygame.MOUSEBUTTONUP:
# # # # # # # # #             if active_wheel:
# # # # # # # # #                 active_wheel["drag"] = False
# # # # # # # # #                 active_wheel["vel"] += random.uniform(-0.02, 0.02)
# # # # # # # # #                 active_wheel = None

# # # # # # # # #         if event.type == pygame.MOUSEMOTION and active_wheel and active_wheel["drag"]:
# # # # # # # # #             m = mouse_angle(pygame.mouse.get_pos(), active_wheel["center"])
# # # # # # # # #             delta = m - active_wheel["last_mouse"]
# # # # # # # # #             active_wheel["vel"] += delta * 18
# # # # # # # # #             active_wheel["vel"] = max(-2, min(2, active_wheel["vel"]))
# # # # # # # # #             active_wheel["last_mouse"] = m

# # # # # # # # #     for w in wheels:
# # # # # # # # #         w["angle"] += w["vel"]
# # # # # # # # #         w["vel"] *= friction(w["vel"])

# # # # # # # # #         if abs(w["vel"]) < 0.0005 and not w["drag"] and not w["stopped"]:
# # # # # # # # #             w["vel"] = 0
# # # # # # # # #             w["result"] = str(get_under_pointer(w))
# # # # # # # # #             w["stopped"] = True
# # # # # # # # #             results_order.append(w)

# # # # # # # # #     for w in wheels:
# # # # # # # # #         draw_wheel(w)

# # # # # # # # #     # عرض النتائج أعلى الشاشة حسب ترتيب التوقف
# # # # # # # # #     x_start = WIDTH//2 - 300
# # # # # # # # #     y = 60
# # # # # # # # #     for i, w in enumerate(results_order):
# # # # # # # # #         txt = BIG_FONT.render(w["result"], True, (255,255,0))
# # # # # # # # #         screen.blit(txt, txt.get_rect(center=(x_start + i*80, y)))

# # # # # # # # #     pygame.display.flip()

# # # # # # # # # pygame.quit()
















# # # # # # # # import pygame
# # # # # # # # import math
# # # # # # # # import random
# # # # # # # # import string

# # # # # # # # pygame.init()

# # # # # # # # # ================= إعدادات عامة =================
# # # # # # # # WIDTH, HEIGHT = 1500, 800
# # # # # # # # screen = pygame.display.set_mode((WIDTH, HEIGHT))
# # # # # # # # pygame.display.set_caption("8 دوّارات فيزيائية - صفين")
# # # # # # # # clock = pygame.time.Clock()

# # # # # # # # FONT = pygame.font.SysFont("arial", 22, bold=True)
# # # # # # # # BIG_FONT = pygame.font.SysFont("arial", 50, bold=True)

# # # # # # # # BG = (25, 25, 25)
# # # # # # # # POINTER_COLOR = (255, 255, 255)

# # # # # # # # RADIUS = 140

# # # # # # # # # ================= مراكز الدوّارات 4x2 =================
# # # # # # # # X_OFFSETS = [200, 550, 900, 1250]
# # # # # # # # Y_OFFSETS = [250, 600]  # صفين
# # # # # # # # CENTERS = []
# # # # # # # # for y in Y_OFFSETS:
# # # # # # # #     for x in X_OFFSETS:
# # # # # # # #         CENTERS.append((x, y))

# # # # # # # # # ================= دالة إنشاء العجلة =================
# # # # # # # # def new_wheel(center, labels):
# # # # # # # #     return {
# # # # # # # #         "center": center,
# # # # # # # #         "labels": labels,
# # # # # # # #         "angle": 0,
# # # # # # # #         "vel": 0,
# # # # # # # #         "drag": False,
# # # # # # # #         "last_mouse": 0,
# # # # # # # #         "result": None,
# # # # # # # #         "stopped": False
# # # # # # # #     }

# # # # # # # # # ================= بيانات الدوّارات =================
# # # # # # # # labels_list = [
# # # # # # # #     list(range(10)),                   # أرقام
# # # # # # # #     list(string.ascii_uppercase),      # كل الحروف
# # # # # # # #     list("!@#$%^&*?"),                 # رموز
# # # # # # # #     ['(', ')', '[', ']', '{', '}', '<', '>', '"', "'"]  # أقواس
# # # # # # # # ]

# # # # # # # # # إنشاء العجلات 8 عجلات (كل نوع له صفين)
# # # # # # # # wheels = []
# # # # # # # # for labels in labels_list:
# # # # # # # #     wheels.append(new_wheel(CENTERS.pop(0), labels))  # الصف الأول
# # # # # # # #     wheels.append(new_wheel(CENTERS.pop(0), labels))  # الصف الثاني

# # # # # # # # COLORS = [
# # # # # # # #     (255,99,71),(135,206,250),(255,215,0),(144,238,144),
# # # # # # # #     (221,160,221),(255,182,193),(173,216,230),(240,230,140),
# # # # # # # #     (255,160,122),(176,196,222)
# # # # # # # # ]

# # # # # # # # active_wheel = None
# # # # # # # # results_order = []

# # # # # # # # # ================= دوال =================
# # # # # # # # def friction(v):
# # # # # # # #     return 0.995 - abs(v)*0.0005

# # # # # # # # def mouse_angle(pos, center):
# # # # # # # #     dx, dy = pos[0]-center[0], pos[1]-center[1]
# # # # # # # #     return math.atan2(dy, dx)

# # # # # # # # def inside_wheel(pos, center):
# # # # # # # #     dx = pos[0]-center[0]
# # # # # # # #     dy = pos[1]-center[1]
# # # # # # # #     return math.hypot(dx, dy) <= RADIUS

# # # # # # # # def draw_wheel(wheel):
# # # # # # # #     cx, cy = wheel["center"]
# # # # # # # #     labels = wheel["labels"]
# # # # # # # #     sections = len(labels)
# # # # # # # #     section_angle = 2 * math.pi / sections

# # # # # # # #     for i in range(sections):
# # # # # # # #         a1 = wheel["angle"] + i * section_angle
# # # # # # # #         a2 = a1 + section_angle

# # # # # # # #         pygame.draw.polygon(
# # # # # # # #             screen,
# # # # # # # #             COLORS[i % len(COLORS)],
# # # # # # # #             [(cx, cy),
# # # # # # # #              (cx + RADIUS * math.cos(a1), cy + RADIUS * math.sin(a1)),
# # # # # # # #              (cx + RADIUS * math.cos(a2), cy + RADIUS * math.sin(a2))]
# # # # # # # #         )

# # # # # # # #         ta = a1 + section_angle / 2
# # # # # # # #         tx = cx + (RADIUS - 35) * math.cos(ta)
# # # # # # # #         ty = cy + (RADIUS - 35) * math.sin(ta)
# # # # # # # #         txt = FONT.render(str(labels[i]), True, (0,0,0))
# # # # # # # #         screen.blit(txt, txt.get_rect(center=(tx, ty)))

# # # # # # # #     pygame.draw.circle(screen, (0,0,0), wheel["center"], RADIUS, 4)

# # # # # # # #     pygame.draw.polygon(
# # # # # # # #         screen, POINTER_COLOR,
# # # # # # # #         [(cx-10, cy-RADIUS-5),
# # # # # # # #          (cx+10, cy-RADIUS-5),
# # # # # # # #          (cx, cy-RADIUS-28)]
# # # # # # # #     )

# # # # # # # # def get_under_pointer(wheel):
# # # # # # # #     labels = wheel["labels"]
# # # # # # # #     sections = len(labels)
# # # # # # # #     section_angle = 2 * math.pi / sections
# # # # # # # #     norm = wheel["angle"] % (2 * math.pi)
# # # # # # # #     pointer = -math.pi / 2
# # # # # # # #     rel = (pointer - norm) % (2 * math.pi)
# # # # # # # #     return labels[int(rel // section_angle)]

# # # # # # # # # ================= الحلقة الرئيسية =================
# # # # # # # # running = True
# # # # # # # # while running:
# # # # # # # #     clock.tick(60)
# # # # # # # #     screen.fill(BG)

# # # # # # # #     for event in pygame.event.get():
# # # # # # # #         if event.type == pygame.QUIT:
# # # # # # # #             running = False

# # # # # # # #         if event.type == pygame.MOUSEBUTTONDOWN:
# # # # # # # #             pos = pygame.mouse.get_pos()
# # # # # # # #             for w in wheels:
# # # # # # # #                 if inside_wheel(pos, w["center"]):
# # # # # # # #                     active_wheel = w
# # # # # # # #                     w["drag"] = True
# # # # # # # #                     w["last_mouse"] = mouse_angle(pos, w["center"])
# # # # # # # #                     w["vel"] = 0
# # # # # # # #                     w["result"] = None
# # # # # # # #                     w["stopped"] = False
# # # # # # # #                     if w in results_order:
# # # # # # # #                         results_order.remove(w)

# # # # # # # #         if event.type == pygame.MOUSEBUTTONUP:
# # # # # # # #             if active_wheel:
# # # # # # # #                 active_wheel["drag"] = False
# # # # # # # #                 active_wheel["vel"] += random.uniform(-0.02, 0.02)
# # # # # # # #                 active_wheel = None

# # # # # # # #         if event.type == pygame.MOUSEMOTION and active_wheel and active_wheel["drag"]:
# # # # # # # #             m = mouse_angle(pygame.mouse.get_pos(), active_wheel["center"])
# # # # # # # #             delta = m - active_wheel["last_mouse"]
# # # # # # # #             active_wheel["vel"] += delta * 18
# # # # # # # #             active_wheel["vel"] = max(-2, min(2, active_wheel["vel"]))
# # # # # # # #             active_wheel["last_mouse"] = m

# # # # # # # #     for w in wheels:
# # # # # # # #         w["angle"] += w["vel"]
# # # # # # # #         w["vel"] *= friction(w["vel"])

# # # # # # # #         if abs(w["vel"]) < 0.0005 and not w["drag"] and not w["stopped"]:
# # # # # # # #             w["vel"] = 0
# # # # # # # #             w["result"] = str(get_under_pointer(w))
# # # # # # # #             w["stopped"] = True
# # # # # # # #             results_order.append(w)

# # # # # # # #     for w in wheels:
# # # # # # # #         draw_wheel(w)

# # # # # # # #     # عرض النتائج أعلى الشاشة حسب ترتيب التوقف
# # # # # # # #     x_start = WIDTH//2 - 300
# # # # # # # #     y = 60
# # # # # # # #     for i, w in enumerate(results_order):
# # # # # # # #         txt = BIG_FONT.render(w["result"], True, (255,255,0))
# # # # # # # #         screen.blit(txt, txt.get_rect(center=(x_start + i*80, y)))

# # # # # # # #     pygame.display.flip()

# # # # # # # # pygame.quit()











# # # # # # # import pygame
# # # # # # # import math
# # # # # # # import random
# # # # # # # import string

# # # # # # # pygame.init()

# # # # # # # # ================= إعدادات عامة =================
# # # # # # # WIDTH, HEIGHT = 1600, 900
# # # # # # # screen = pygame.display.set_mode((WIDTH, HEIGHT))
# # # # # # # pygame.display.set_caption("16 دوّارة فيزيائية")
# # # # # # # clock = pygame.time.Clock()

# # # # # # # FONT = pygame.font.SysFont("arial", 22, bold=True)
# # # # # # # BIG_FONT = pygame.font.SysFont("arial", 50, bold=True)

# # # # # # # BG = (25, 25, 25)
# # # # # # # POINTER_COLOR = (255, 255, 255)

# # # # # # # RADIUS = 140

# # # # # # # # ================= مراكز الدوّارات 4x4 =================
# # # # # # # X_OFFSETS = [200, 550, 900, 1250]       # 4 أعمدة
# # # # # # # Y_OFFSETS = [150, 350, 550, 750]        # 4 صفوف
# # # # # # # CENTERS = []
# # # # # # # for y in Y_OFFSETS:
# # # # # # #     for x in X_OFFSETS:
# # # # # # #         CENTERS.append((x, y))          # كل مركز للعجلة

# # # # # # # # ================= دالة إنشاء العجلة =================
# # # # # # # def new_wheel(center, labels):
# # # # # # #     return {
# # # # # # #         "center": center,
# # # # # # #         "labels": labels,
# # # # # # #         "angle": 0,
# # # # # # #         "vel": 0,
# # # # # # #         "drag": False,
# # # # # # #         "last_mouse": 0,
# # # # # # #         "result": None,
# # # # # # #         "stopped": False
# # # # # # #     }

# # # # # # # # ================= بيانات الدوّارات =================
# # # # # # # labels_list = [
# # # # # # #     list(range(10)),                   # أرقام
# # # # # # #     list(string.ascii_uppercase),      # كل الحروف
# # # # # # #     list("!@#$%^&*?"),                 # رموز
# # # # # # #     ['(', ')', '[', ']', '{', '}', '<', '>', '"', "'"]  # أقواس
# # # # # # # ]

# # # # # # # # لكل نوع عجلة، نكررها 4 مرات لتصبح 16 عجلة
# # # # # # # wheels = []
# # # # # # # for labels in labels_list:
# # # # # # #     for _ in range(4):
# # # # # # #         wheels.append(new_wheel(CENTERS.pop(0), labels))

# # # # # # # # ================= ألوان للعجلات =================
# # # # # # # COLORS = [
# # # # # # #     (255,99,71),(135,206,250),(255,215,0),(144,238,144),
# # # # # # #     (221,160,221),(255,182,193),(173,216,230),(240,230,140),
# # # # # # #     (255,160,122),(176,196,222)
# # # # # # # ]

# # # # # # # active_wheel = None
# # # # # # # results_order = []

# # # # # # # # ================= دوال =================
# # # # # # # def friction(v):
# # # # # # #     return 0.995 - abs(v)*0.0005

# # # # # # # def mouse_angle(pos, center):
# # # # # # #     dx, dy = pos[0]-center[0], pos[1]-center[1]
# # # # # # #     return math.atan2(dy, dx)

# # # # # # # def inside_wheel(pos, center):
# # # # # # #     dx = pos[0]-center[0]
# # # # # # #     dy = pos[1]-center[1]
# # # # # # #     return math.hypot(dx, dy) <= RADIUS

# # # # # # # def draw_wheel(wheel):
# # # # # # #     cx, cy = wheel["center"]
# # # # # # #     labels = wheel["labels"]
# # # # # # #     sections = len(labels)
# # # # # # #     section_angle = 2 * math.pi / sections

# # # # # # #     for i in range(sections):
# # # # # # #         a1 = wheel["angle"] + i * section_angle
# # # # # # #         a2 = a1 + section_angle

# # # # # # #         pygame.draw.polygon(
# # # # # # #             screen,
# # # # # # #             COLORS[i % len(COLORS)],
# # # # # # #             [(cx, cy),
# # # # # # #              (cx + RADIUS * math.cos(a1), cy + RADIUS * math.sin(a1)),
# # # # # # #              (cx + RADIUS * math.cos(a2), cy + RADIUS * math.sin(a2))]
# # # # # # #         )

# # # # # # #         ta = a1 + section_angle / 2
# # # # # # #         tx = cx + (RADIUS - 35) * math.cos(ta)
# # # # # # #         ty = cy + (RADIUS - 35) * math.sin(ta)
# # # # # # #         txt = FONT.render(str(labels[i]), True, (0,0,0))
# # # # # # #         screen.blit(txt, txt.get_rect(center=(tx, ty)))

# # # # # # #     pygame.draw.circle(screen, (0,0,0), wheel["center"], RADIUS, 4)

# # # # # # #     pygame.draw.polygon(
# # # # # # #         screen, POINTER_COLOR,
# # # # # # #         [(cx-10, cy-RADIUS-5),
# # # # # # #          (cx+10, cy-RADIUS-5),
# # # # # # #          (cx, cy-RADIUS-28)]
# # # # # # #     )

# # # # # # # def get_under_pointer(wheel):
# # # # # # #     labels = wheel["labels"]
# # # # # # #     sections = len(labels)
# # # # # # #     section_angle = 2 * math.pi / sections
# # # # # # #     norm = wheel["angle"] % (2 * math.pi)
# # # # # # #     pointer = -math.pi / 2
# # # # # # #     rel = (pointer - norm) % (2 * math.pi)
# # # # # # #     return labels[int(rel // section_angle)]

# # # # # # # # ================= الحلقة الرئيسية =================
# # # # # # # running = True
# # # # # # # while running:
# # # # # # #     clock.tick(60)
# # # # # # #     screen.fill(BG)

# # # # # # #     for event in pygame.event.get():
# # # # # # #         if event.type == pygame.QUIT:
# # # # # # #             running = False

# # # # # # #         if event.type == pygame.MOUSEBUTTONDOWN:
# # # # # # #             pos = pygame.mouse.get_pos()
# # # # # # #             for w in wheels:
# # # # # # #                 if inside_wheel(pos, w["center"]):
# # # # # # #                     active_wheel = w
# # # # # # #                     w["drag"] = True
# # # # # # #                     w["last_mouse"] = mouse_angle(pos, w["center"])
# # # # # # #                     w["vel"] = 0
# # # # # # #                     w["result"] = None
# # # # # # #                     w["stopped"] = False
# # # # # # #                     if w in results_order:
# # # # # # #                         results_order.remove(w)

# # # # # # #         if event.type == pygame.MOUSEBUTTONUP:
# # # # # # #             if active_wheel:
# # # # # # #                 active_wheel["drag"] = False
# # # # # # #                 active_wheel["vel"] += random.uniform(-0.02, 0.02)
# # # # # # #                 active_wheel = None

# # # # # # #         if event.type == pygame.MOUSEMOTION and active_wheel and active_wheel["drag"]:
# # # # # # #             m = mouse_angle(pygame.mouse.get_pos(), active_wheel["center"])
# # # # # # #             delta = m - active_wheel["last_mouse"]
# # # # # # #             active_wheel["vel"] += delta * 18
# # # # # # #             active_wheel["vel"] = max(-2, min(2, active_wheel["vel"]))
# # # # # # #             active_wheel["last_mouse"] = m

# # # # # # #     for w in wheels:
# # # # # # #         w["angle"] += w["vel"]
# # # # # # #         w["vel"] *= friction(w["vel"])

# # # # # # #         if abs(w["vel"]) < 0.0005 and not w["drag"] and not w["stopped"]:
# # # # # # #             w["vel"] = 0
# # # # # # #             w["result"] = str(get_under_pointer(w))
# # # # # # #             w["stopped"] = True
# # # # # # #             results_order.append(w)

# # # # # # #     for w in wheels:
# # # # # # #         draw_wheel(w)

# # # # # # #     # عرض النتائج أعلى الشاشة حسب ترتيب التوقف
# # # # # # #     x_start = WIDTH//2 - 400
# # # # # # #     y = 60
# # # # # # #     for i, w in enumerate(results_order):
# # # # # # #         txt = BIG_FONT.render(w["result"], True, (255,255,0))
# # # # # # #         screen.blit(txt, txt.get_rect(center=(x_start + i*80, y)))

# # # # # # #     pygame.display.flip()

# # # # # # # pygame.quit()










# # # # # # # import pygame
# # # # # # # import math
# # # # # # # import random
# # # # # # # import string

# # # # # # # pygame.init()

# # # # # # # # ================= إعدادات عامة =================
# # # # # # # WIDTH, HEIGHT = 1400, 800
# # # # # # # screen = pygame.display.set_mode((WIDTH, HEIGHT))
# # # # # # # pygame.display.set_caption("16 دوّارة فيزيائية صغيرة")
# # # # # # # clock = pygame.time.Clock()

# # # # # # # FONT = pygame.font.SysFont("arial", 16, bold=True)
# # # # # # # BIG_FONT = pygame.font.SysFont("arial", 30, bold=True)

# # # # # # # BG = (25, 25, 25)
# # # # # # # POINTER_COLOR = (255, 255, 255)

# # # # # # # RADIUS = 70  # صغر حجم العجلات

# # # # # # # # ================= مراكز الدوّارات 4x4 =================
# # # # # # # X_OFFSETS = [150, 450, 750, 1050]       # أعمدة
# # # # # # # Y_OFFSETS = [150, 300, 450, 600]        # صفوف
# # # # # # # CENTERS = []
# # # # # # # for y in Y_OFFSETS:
# # # # # # #     for x in X_OFFSETS:
# # # # # # #         CENTERS.append((x, y))          # كل مركز للعجلة

# # # # # # # # ================= دالة إنشاء العجلة =================
# # # # # # # def new_wheel(center, labels):
# # # # # # #     return {
# # # # # # #         "center": center,
# # # # # # #         "labels": labels,
# # # # # # #         "angle": 0,
# # # # # # #         "vel": 0,
# # # # # # #         "drag": False,
# # # # # # #         "last_mouse": 0,
# # # # # # #         "result": None,
# # # # # # #         "stopped": False
# # # # # # #     }

# # # # # # # # ================= بيانات الدوّارات =================
# # # # # # # labels_list = [
# # # # # # #     list(range(10)),                   # أرقام
# # # # # # #     list(string.ascii_uppercase),      # كل الحروف
# # # # # # #     list("!@#$%^&*?"),                 # رموز
# # # # # # #     ['(', ')', '[', ']', '{', '}', '<', '>', '"', "'"]  # أقواس
# # # # # # # ]

# # # # # # # # لكل نوع عجلة، نكررها 4 مرات لتصبح 16 عجلة
# # # # # # # wheels = []
# # # # # # # for labels in labels_list:
# # # # # # #     for _ in range(4):
# # # # # # #         wheels.append(new_wheel(CENTERS.pop(0), labels))

# # # # # # # # ================= ألوان للعجلات =================
# # # # # # # COLORS = [
# # # # # # #     (255,99,71),(135,206,250),(255,215,0),(144,238,144),
# # # # # # #     (221,160,221),(255,182,193),(173,216,230),(240,230,140),
# # # # # # #     (255,160,122),(176,196,222)
# # # # # # # ]

# # # # # # # active_wheel = None
# # # # # # # results_order = []

# # # # # # # # ================= دوال =================
# # # # # # # def friction(v):
# # # # # # #     return 0.995 - abs(v)*0.0005

# # # # # # # def mouse_angle(pos, center):
# # # # # # #     dx, dy = pos[0]-center[0], pos[1]-center[1]
# # # # # # #     return math.atan2(dy, dx)

# # # # # # # def inside_wheel(pos, center):
# # # # # # #     dx = pos[0]-center[0]
# # # # # # #     dy = pos[1]-center[1]
# # # # # # #     return math.hypot(dx, dy) <= RADIUS

# # # # # # # def draw_wheel(wheel):
# # # # # # #     cx, cy = wheel["center"]
# # # # # # #     labels = wheel["labels"]
# # # # # # #     sections = len(labels)
# # # # # # #     section_angle = 2 * math.pi / sections

# # # # # # #     for i in range(sections):
# # # # # # #         a1 = wheel["angle"] + i * section_angle
# # # # # # #         a2 = a1 + section_angle

# # # # # # #         pygame.draw.polygon(
# # # # # # #             screen,
# # # # # # #             COLORS[i % len(COLORS)],
# # # # # # #             [(cx, cy),
# # # # # # #              (cx + RADIUS * math.cos(a1), cy + RADIUS * math.sin(a1)),
# # # # # # #              (cx + RADIUS * math.cos(a2), cy + RADIUS * math.sin(a2))]
# # # # # # #         )

# # # # # # #         ta = a1 + section_angle / 2
# # # # # # #         tx = cx + (RADIUS - 20) * math.cos(ta)
# # # # # # #         ty = cy + (RADIUS - 20) * math.sin(ta)
# # # # # # #         txt = FONT.render(str(labels[i]), True, (0,0,0))
# # # # # # #         screen.blit(txt, txt.get_rect(center=(tx, ty)))

# # # # # # #     pygame.draw.circle(screen, (0,0,0), wheel["center"], RADIUS, 3)

# # # # # # #     pygame.draw.polygon(
# # # # # # #         screen, POINTER_COLOR,
# # # # # # #         [(cx-7, cy-RADIUS-3),
# # # # # # #          (cx+7, cy-RADIUS-3),
# # # # # # #          (cx, cy-RADIUS-15)]
# # # # # # #     )

# # # # # # # def get_under_pointer(wheel):
# # # # # # #     labels = wheel["labels"]
# # # # # # #     sections = len(labels)
# # # # # # #     section_angle = 2 * math.pi / sections
# # # # # # #     norm = wheel["angle"] % (2 * math.pi)
# # # # # # #     pointer = -math.pi / 2
# # # # # # #     rel = (pointer - norm) % (2 * math.pi)
# # # # # # #     return labels[int(rel // section_angle)]

# # # # # # # # ================= الحلقة الرئيسية =================
# # # # # # # running = True
# # # # # # # while running:
# # # # # # #     clock.tick(60)
# # # # # # #     screen.fill(BG)

# # # # # # #     for event in pygame.event.get():
# # # # # # #         if event.type == pygame.QUIT:
# # # # # # #             running = False

# # # # # # #         if event.type == pygame.MOUSEBUTTONDOWN:
# # # # # # #             pos = pygame.mouse.get_pos()
# # # # # # #             for w in wheels:
# # # # # # #                 if inside_wheel(pos, w["center"]):
# # # # # # #                     active_wheel = w
# # # # # # #                     w["drag"] = True
# # # # # # #                     w["last_mouse"] = mouse_angle(pos, w["center"])
# # # # # # #                     w["vel"] = 0
# # # # # # #                     w["result"] = None
# # # # # # #                     w["stopped"] = False
# # # # # # #                     if w in results_order:
# # # # # # #                         results_order.remove(w)

# # # # # # #         if event.type == pygame.MOUSEBUTTONUP:
# # # # # # #             if active_wheel:
# # # # # # #                 active_wheel["drag"] = False
# # # # # # #                 active_wheel["vel"] += random.uniform(-0.02, 0.02)
# # # # # # #                 active_wheel = None

# # # # # # #         if event.type == pygame.MOUSEMOTION and active_wheel and active_wheel["drag"]:
# # # # # # #             m = mouse_angle(pygame.mouse.get_pos(), active_wheel["center"])
# # # # # # #             delta = m - active_wheel["last_mouse"]
# # # # # # #             active_wheel["vel"] += delta * 18
# # # # # # #             active_wheel["vel"] = max(-2, min(2, active_wheel["vel"]))
# # # # # # #             active_wheel["last_mouse"] = m

# # # # # # #     for w in wheels:
# # # # # # #         w["angle"] += w["vel"]
# # # # # # #         w["vel"] *= friction(w["vel"])

# # # # # # #         if abs(w["vel"]) < 0.0005 and not w["drag"] and not w["stopped"]:
# # # # # # #             w["vel"] = 0
# # # # # # #             w["result"] = str(get_under_pointer(w))
# # # # # # #             w["stopped"] = True
# # # # # # #             results_order.append(w)

# # # # # # #     for w in wheels:
# # # # # # #         draw_wheel(w)

# # # # # # #     # عرض النتائج أعلى الشاشة حسب ترتيب التوقف
# # # # # # #     x_start = WIDTH//2 - 400
# # # # # # #     y = 50
# # # # # # #     for i, w in enumerate(results_order):
# # # # # # #         txt = BIG_FONT.render(w["result"], True, (255,255,0))
# # # # # # #         screen.blit(txt, txt.get_rect(center=(x_start + i*50, y)))

# # # # # # #     pygame.display.flip()

# # # # # # # pygame.quit()










# # # # # # import pygame
# # # # # # import math
# # # # # # import random
# # # # # # import string

# # # # # # pygame.init()

# # # # # # # ================= إعدادات عامة =================
# # # # # # WIDTH, HEIGHT = 1400, 800
# # # # # # screen = pygame.display.set_mode((WIDTH, HEIGHT))
# # # # # # pygame.display.set_caption("16 دوّارة فيزيائية صغيرة")
# # # # # # clock = pygame.time.Clock()

# # # # # # FONT = pygame.font.SysFont("arial", 16, bold=True)
# # # # # # BIG_FONT = pygame.font.SysFont("arial", 30, bold=True)

# # # # # # BG = (25, 25, 25)
# # # # # # POINTER_COLOR = (255, 255, 255)

# # # # # # RADIUS = 70  # صغر حجم العجلات

# # # # # # # ================= مراكز الدوّارات 4x4 =================
# # # # # # X_OFFSETS = [150, 450, 750, 1050]       # أعمدة
# # # # # # Y_OFFSETS = [150, 300, 450, 600]        # صفوف
# # # # # # CENTERS = []
# # # # # # for y in Y_OFFSETS:
# # # # # #     for x in X_OFFSETS:
# # # # # #         CENTERS.append((x, y))          # كل مركز للعجلة

# # # # # # # ================= دالة إنشاء العجلة =================
# # # # # # def new_wheel(center, labels):
# # # # # #     return {
# # # # # #         "center": center,
# # # # # #         "labels": labels,
# # # # # #         "angle": 0,
# # # # # #         "vel": 0,
# # # # # #         "drag": False,
# # # # # #         "last_mouse": 0,
# # # # # #         "result": None,
# # # # # #         "stopped": False
# # # # # #     }

# # # # # # # ================= بيانات الدوّارات =================
# # # # # # labels_list = [
# # # # # #     list(range(10)),                   # أرقام
# # # # # #     list(string.ascii_uppercase),      # كل الحروف الكبيرة
# # # # # #     list("!@#$%^&*?~+-=/<>"),          # رموز = 17
# # # # # #     ['(', ')', '[', ']', '{', '}', '<', '>', '"', "'", '«', '»', '‹', '›', '`', '´']  # أقواس/اقتباسات = 16
# # # # # # ]

# # # # # # # لكل نوع عجلة، نكررها 4 مرات لتصبح 16 عجلة
# # # # # # wheels = []
# # # # # # for labels in labels_list:
# # # # # #     for _ in range(4):
# # # # # #         wheels.append(new_wheel(CENTERS.pop(0), labels))

# # # # # # # ================= ألوان للعجلات =================
# # # # # # COLORS = [
# # # # # #     (255,99,71),(135,206,250),(255,215,0),(144,238,144),
# # # # # #     (221,160,221),(255,182,193),(173,216,230),(240,230,140),
# # # # # #     (255,160,122),(176,196,222)
# # # # # # ]

# # # # # # active_wheel = None
# # # # # # results_order = []

# # # # # # # ================= دوال =================
# # # # # # def friction(v):
# # # # # #     return 0.995 - abs(v)*0.0005

# # # # # # def mouse_angle(pos, center):
# # # # # #     dx, dy = pos[0]-center[0], pos[1]-center[1]
# # # # # #     return math.atan2(dy, dx)

# # # # # # def inside_wheel(pos, center):
# # # # # #     dx = pos[0]-center[0]
# # # # # #     dy = pos[1]-center[1]
# # # # # #     return math.hypot(dx, dy) <= RADIUS

# # # # # # def draw_wheel(wheel):
# # # # # #     cx, cy = wheel["center"]
# # # # # #     labels = wheel["labels"]
# # # # # #     sections = len(labels)
# # # # # #     section_angle = 2 * math.pi / sections

# # # # # #     for i in range(sections):
# # # # # #         a1 = wheel["angle"] + i * section_angle
# # # # # #         a2 = a1 + section_angle

# # # # # #         pygame.draw.polygon(
# # # # # #             screen,
# # # # # #             COLORS[i % len(COLORS)],
# # # # # #             [(cx, cy),
# # # # # #              (cx + RADIUS * math.cos(a1), cy + RADIUS * math.sin(a1)),
# # # # # #              (cx + RADIUS * math.cos(a2), cy + RADIUS * math.sin(a2))]
# # # # # #         )

# # # # # #         ta = a1 + section_angle / 2
# # # # # #         tx = cx + (RADIUS - 20) * math.cos(ta)
# # # # # #         ty = cy + (RADIUS - 20) * math.sin(ta)
# # # # # #         txt = FONT.render(str(labels[i]), True, (0,0,0))
# # # # # #         screen.blit(txt, txt.get_rect(center=(tx, ty)))

# # # # # #     pygame.draw.circle(screen, (0,0,0), wheel["center"], RADIUS, 3)

# # # # # #     pygame.draw.polygon(
# # # # # #         screen, POINTER_COLOR,
# # # # # #         [(cx-7, cy-RADIUS-3),
# # # # # #          (cx+7, cy-RADIUS-3),
# # # # # #          (cx, cy-RADIUS-15)]
# # # # # #     )

# # # # # # # ================= تعديل get_under_pointer ليكون آمن =================
# # # # # # def get_under_pointer(wheel):
# # # # # #     labels = wheel["labels"]
# # # # # #     sections = len(labels)
# # # # # #     section_angle = 2 * math.pi / sections
# # # # # #     norm = wheel["angle"] % (2 * math.pi)
# # # # # #     pointer = -math.pi / 2
# # # # # #     rel = (pointer - norm) % (2 * math.pi)
# # # # # #     index = int(rel // section_angle) % len(labels)  # ✅ آمن لأي عدد رموز
# # # # # #     return labels[index]

# # # # # # # ================= الحلقة الرئيسية =================
# # # # # # running = True
# # # # # # while running:
# # # # # #     clock.tick(60)
# # # # # #     screen.fill(BG)

# # # # # #     for event in pygame.event.get():
# # # # # #         if event.type == pygame.QUIT:
# # # # # #             running = False

# # # # # #         if event.type == pygame.MOUSEBUTTONDOWN:
# # # # # #             pos = pygame.mouse.get_pos()
# # # # # #             for w in wheels:
# # # # # #                 if inside_wheel(pos, w["center"]):
# # # # # #                     active_wheel = w
# # # # # #                     w["drag"] = True
# # # # # #                     w["last_mouse"] = mouse_angle(pos, w["center"])
# # # # # #                     w["vel"] = 0
# # # # # #                     w["result"] = None
# # # # # #                     w["stopped"] = False
# # # # # #                     if w in results_order:
# # # # # #                         results_order.remove(w)

# # # # # #         if event.type == pygame.MOUSEBUTTONUP:
# # # # # #             if active_wheel:
# # # # # #                 active_wheel["drag"] = False
# # # # # #                 active_wheel["vel"] += random.uniform(-0.02, 0.02)
# # # # # #                 active_wheel = None

# # # # # #         if event.type == pygame.MOUSEMOTION and active_wheel and active_wheel["drag"]:
# # # # # #             m = mouse_angle(pygame.mouse.get_pos(), active_wheel["center"])
# # # # # #             delta = m - active_wheel["last_mouse"]
# # # # # #             active_wheel["vel"] += delta * 18
# # # # # #             active_wheel["vel"] = max(-2, min(2, active_wheel["vel"]))
# # # # # #             active_wheel["last_mouse"] = m

# # # # # #     for w in wheels:
# # # # # #         w["angle"] += w["vel"]
# # # # # #         w["vel"] *= friction(w["vel"])

# # # # # #         if abs(w["vel"]) < 0.0005 and not w["drag"] and not w["stopped"]:
# # # # # #             w["vel"] = 0
# # # # # #             w["result"] = str(get_under_pointer(w))
# # # # # #             w["stopped"] = True
# # # # # #             results_order.append(w)

# # # # # #     for w in wheels:
# # # # # #         draw_wheel(w)

# # # # # #     # عرض النتائج أعلى الشاشة حسب ترتيب التوقف
# # # # # #     x_start = WIDTH//2 - 400
# # # # # #     y = 50
# # # # # #     for i, w in enumerate(results_order):
# # # # # #         txt = BIG_FONT.render(w["result"], True, (255,255,0))
# # # # # #         screen.blit(txt, txt.get_rect(center=(x_start + i*50, y)))

# # # # # #     pygame.display.flip()

# # # # # # pygame.quit()








# # # # # import pygame
# # # # # import math
# # # # # import random
# # # # # import string

# # # # # pygame.init()

# # # # # # ================= إعدادات عامة =================
# # # # # WIDTH, HEIGHT = 1400, 800
# # # # # screen = pygame.display.set_mode((WIDTH, HEIGHT))
# # # # # pygame.display.set_caption("16 دوّارة فيزيائية صغيرة")
# # # # # clock = pygame.time.Clock()

# # # # # FONT = pygame.font.SysFont("arial", 16, bold=True)
# # # # # BIG_FONT = pygame.font.SysFont("arial", 30, bold=True)

# # # # # BG = (25, 25, 25)
# # # # # POINTER_COLOR = (255, 255, 255)

# # # # # RADIUS = 70  # حجم العجلات

# # # # # # ================= مراكز الدوّارات 4x4 =================
# # # # # X_OFFSETS = [150, 450, 750, 1050]
# # # # # Y_OFFSETS = [150, 300, 450, 600]
# # # # # CENTERS = [(x, y) for y in Y_OFFSETS for x in X_OFFSETS]

# # # # # # ================= دالة إنشاء العجلة =================
# # # # # def new_wheel(center, labels):
# # # # #     return {
# # # # #         "center": center,
# # # # #         "labels": labels,
# # # # #         "angle": 0,
# # # # #         "vel": 0,
# # # # #         "drag": False,
# # # # #         "last_mouse": 0,
# # # # #         "result": None,
# # # # #         "stopped": False,
# # # # #         "stop_time": None  # ✅ وقت التوقف
# # # # #     }

# # # # # # ================= بيانات الدوّارات =================
# # # # # labels_list = [
# # # # #     list(range(10)),                   # أرقام
# # # # #     list(string.ascii_uppercase),      # حروف
# # # # #     list("!@#$%^&*?~+-=/<>"),          # رموز = 17
# # # # #     ['(', ')', '[', ']', '{', '}', '<', '>', '"', "'", '«', '»', '‹', '›', '`', '´']  # أقواس =16
# # # # # ]

# # # # # # لكل نوع عجلة، نكررها 4 مرات → 16 عجلة
# # # # # wheels = []
# # # # # for labels in labels_list:
# # # # #     for _ in range(4):
# # # # #         wheels.append(new_wheel(CENTERS.pop(0), labels))

# # # # # # ================= ألوان للعجلات =================
# # # # # COLORS = [
# # # # #     (255,99,71),(135,206,250),(255,215,0),(144,238,144),
# # # # #     (221,160,221),(255,182,193),(173,216,230),(240,230,140),
# # # # #     (255,160,122),(176,196,222)
# # # # # ]

# # # # # active_wheel = None

# # # # # # ================= دوال =================
# # # # # def friction(v):
# # # # #     return 0.995 - abs(v)*0.0005

# # # # # def mouse_angle(pos, center):
# # # # #     dx, dy = pos[0]-center[0], pos[1]-center[1]
# # # # #     return math.atan2(dy, dx)

# # # # # def inside_wheel(pos, center):
# # # # #     dx = pos[0]-center[0]
# # # # #     dy = pos[1]-center[1]
# # # # #     return math.hypot(dx, dy) <= RADIUS

# # # # # def draw_wheel(wheel):
# # # # #     cx, cy = wheel["center"]
# # # # #     labels = wheel["labels"]
# # # # #     sections = len(labels)
# # # # #     section_angle = 2 * math.pi / sections

# # # # #     for i in range(sections):
# # # # #         a1 = wheel["angle"] + i * section_angle
# # # # #         a2 = a1 + section_angle

# # # # #         pygame.draw.polygon(
# # # # #             screen,
# # # # #             COLORS[i % len(COLORS)],
# # # # #             [(cx, cy),
# # # # #              (cx + RADIUS * math.cos(a1), cy + RADIUS * math.sin(a1)),
# # # # #              (cx + RADIUS * math.cos(a2), cy + RADIUS * math.sin(a2))]
# # # # #         )

# # # # #         ta = a1 + section_angle / 2
# # # # #         tx = cx + (RADIUS - 20) * math.cos(ta)
# # # # #         ty = cy + (RADIUS - 20) * math.sin(ta)
# # # # #         txt = FONT.render(str(labels[i]), True, (0,0,0))
# # # # #         screen.blit(txt, txt.get_rect(center=(tx, ty)))

# # # # #     pygame.draw.circle(screen, (0,0,0), wheel["center"], RADIUS, 3)
# # # # #     pygame.draw.polygon(
# # # # #         screen, POINTER_COLOR,
# # # # #         [(cx-7, cy-RADIUS-3),
# # # # #          (cx+7, cy-RADIUS-3),
# # # # #          (cx, cy-RADIUS-15)]
# # # # #     )

# # # # # def get_under_pointer(wheel):
# # # # #     labels = wheel["labels"]
# # # # #     sections = len(labels)
# # # # #     section_angle = 2 * math.pi / sections
# # # # #     norm = wheel["angle"] % (2 * math.pi)
# # # # #     pointer = -math.pi / 2
# # # # #     rel = (pointer - norm) % (2 * math.pi)
# # # # #     index = int(rel // section_angle) % len(labels)
# # # # #     return labels[index]

# # # # # # ================= الحلقة الرئيسية =================
# # # # # running = True
# # # # # while running:
# # # # #     clock.tick(60)
# # # # #     screen.fill(BG)

# # # # #     for event in pygame.event.get():
# # # # #         if event.type == pygame.QUIT:
# # # # #             running = False

# # # # #         if event.type == pygame.MOUSEBUTTONDOWN:
# # # # #             pos = pygame.mouse.get_pos()
# # # # #             for w in wheels:
# # # # #                 if inside_wheel(pos, w["center"]):
# # # # #                     active_wheel = w
# # # # #                     w["drag"] = True
# # # # #                     w["last_mouse"] = mouse_angle(pos, w["center"])
# # # # #                     w["vel"] = 0
# # # # #                     w["result"] = None
# # # # #                     w["stopped"] = False
# # # # #                     w["stop_time"] = None

# # # # #         if event.type == pygame.MOUSEBUTTONUP:
# # # # #             if active_wheel:
# # # # #                 active_wheel["drag"] = False
# # # # #                 active_wheel["vel"] += random.uniform(-0.02, 0.02)
# # # # #                 active_wheel = None

# # # # #         if event.type == pygame.MOUSEMOTION and active_wheel and active_wheel["drag"]:
# # # # #             m = mouse_angle(pygame.mouse.get_pos(), active_wheel["center"])
# # # # #             delta = m - active_wheel["last_mouse"]
# # # # #             active_wheel["vel"] += delta * 18
# # # # #             active_wheel["vel"] = max(-2, min(2, active_wheel["vel"]))
# # # # #             active_wheel["last_mouse"] = m

# # # # #     for w in wheels:
# # # # #         w["angle"] += w["vel"]
# # # # #         w["vel"] *= friction(w["vel"])

# # # # #         # التوقف وتسجيل وقت التوقف
# # # # #         if abs(w["vel"]) < 0.0005 and not w["drag"] and not w["stopped"]:
# # # # #             w["vel"] = 0
# # # # #             w["result"] = str(get_under_pointer(w))
# # # # #             w["stopped"] = True
# # # # #             w["stop_time"] = pygame.time.get_ticks()  # ✅ وقت التوقف

# # # # #     for w in wheels:
# # # # #         draw_wheel(w)

# # # # #     # ================= عرض النتائج حسب زمن التوقف =================
# # # # #     stopped_wheels = [w for w in wheels if w["stopped"]]
# # # # #     stopped_wheels.sort(key=lambda w: w["stop_time"])  # الأسرع أولاً

# # # # #     x_start = WIDTH//2 - 400
# # # # #     y = 50
# # # # #     for i, w in enumerate(stopped_wheels):
# # # # #         txt = BIG_FONT.render(w["result"], True, (255,255,0))
# # # # #         screen.blit(txt, txt.get_rect(center=(x_start + i*50, y)))

# # # # #     pygame.display.flip()

# # # # # pygame.quit()










# # # # import pygame
# # # # import math
# # # # import random
# # # # import string

# # # # pygame.init()

# # # # # ================= إعدادات عامة =================
# # # # WIDTH, HEIGHT = 1400, 800
# # # # screen = pygame.display.set_mode((WIDTH, HEIGHT))
# # # # pygame.display.set_caption("16 دوّارة فيزيائية صغيرة")
# # # # clock = pygame.time.Clock()

# # # # FONT = pygame.font.SysFont("arial", 16, bold=True)
# # # # BIG_FONT = pygame.font.SysFont("arial", 30, bold=True)

# # # # BG = (25, 25, 25)
# # # # POINTER_COLOR = (255, 255, 255)

# # # # RADIUS = 70  # حجم العجلات

# # # # # ================= مراكز الدوّارات 4x4 =================
# # # # X_OFFSETS = [150, 450, 750, 1050]
# # # # Y_OFFSETS = [150, 300, 450, 600]
# # # # CENTERS = [(x, y) for y in Y_OFFSETS for x in X_OFFSETS]

# # # # # ================= دالة إنشاء العجلة =================
# # # # def new_wheel(center, labels):
# # # #     return {
# # # #         "center": center,
# # # #         "labels": labels,
# # # #         "angle": 0,
# # # #         "vel": 0,
# # # #         "drag": False,
# # # #         "last_mouse": 0,
# # # #         "result": None,
# # # #         "stopped": False,
# # # #         "running_time": 0  # ✅ مدة الدوران منذ بدء الحركة
# # # #     }

# # # # # ================= بيانات الدوّارات =================
# # # # labels_list = [
# # # #     list(range(10)),                   # أرقام
# # # #     list(string.ascii_uppercase),      # حروف
# # # #     list("!@#$%^&*?~+-=/<>"),          # رموز = 17
# # # #     ['(', ')', '[', ']', '{', '}', '<', '>', '"', "'", '«', '»', '‹', '›', '`', '´']  # أقواس =16
# # # # ]

# # # # # لكل نوع عجلة، نكررها 4 مرات → 16 عجلة
# # # # wheels = []
# # # # for labels in labels_list:
# # # #     for _ in range(4):
# # # #         wheels.append(new_wheel(CENTERS.pop(0), labels))

# # # # # ================= ألوان للعجلات =================
# # # # COLORS = [
# # # #     (255,99,71),(135,206,250),(255,215,0),(144,238,144),
# # # #     (221,160,221),(255,182,193),(173,216,230),(240,230,140),
# # # #     (255,160,122),(176,196,222)
# # # # ]

# # # # active_wheel = None

# # # # # ================= دوال =================
# # # # def friction(v):
# # # #     return 0.995 - abs(v)*0.0005

# # # # def mouse_angle(pos, center):
# # # #     dx, dy = pos[0]-center[0], pos[1]-center[1]
# # # #     return math.atan2(dy, dx)

# # # # def inside_wheel(pos, center):
# # # #     dx = pos[0]-center[0]
# # # #     dy = pos[1]-center[1]
# # # #     return math.hypot(dx, dy) <= RADIUS

# # # # def draw_wheel(wheel):
# # # #     cx, cy = wheel["center"]
# # # #     labels = wheel["labels"]
# # # #     sections = len(labels)
# # # #     section_angle = 2 * math.pi / sections

# # # #     for i in range(sections):
# # # #         a1 = wheel["angle"] + i * section_angle
# # # #         a2 = a1 + section_angle

# # # #         pygame.draw.polygon(
# # # #             screen,
# # # #             COLORS[i % len(COLORS)],
# # # #             [(cx, cy),
# # # #              (cx + RADIUS * math.cos(a1), cy + RADIUS * math.sin(a1)),
# # # #              (cx + RADIUS * math.cos(a2), cy + RADIUS * math.sin(a2))]
# # # #         )

# # # #         ta = a1 + section_angle / 2
# # # #         tx = cx + (RADIUS - 20) * math.cos(ta)
# # # #         ty = cy + (RADIUS - 20) * math.sin(ta)
# # # #         txt = FONT.render(str(labels[i]), True, (0,0,0))
# # # #         screen.blit(txt, txt.get_rect(center=(tx, ty)))

# # # #     pygame.draw.circle(screen, (0,0,0), wheel["center"], RADIUS, 3)
# # # #     pygame.draw.polygon(
# # # #         screen, POINTER_COLOR,
# # # #         [(cx-7, cy-RADIUS-3),
# # # #          (cx+7, cy-RADIUS-3),
# # # #          (cx, cy-RADIUS-15)]
# # # #     )

# # # # def get_under_pointer(wheel):
# # # #     labels = wheel["labels"]
# # # #     sections = len(labels)
# # # #     section_angle = 2 * math.pi / sections
# # # #     norm = wheel["angle"] % (2 * math.pi)
# # # #     pointer = -math.pi / 2
# # # #     rel = (pointer - norm) % (2 * math.pi)
# # # #     index = int(rel // section_angle) % len(labels)
# # # #     return labels[index]

# # # # # ================= الحلقة الرئيسية =================
# # # # running = True
# # # # while running:
# # # #     dt = clock.tick(60)  # الوقت بالمللي ثانية منذ آخر إطار
# # # #     screen.fill(BG)

# # # #     for event in pygame.event.get():
# # # #         if event.type == pygame.QUIT:
# # # #             running = False

# # # #         if event.type == pygame.MOUSEBUTTONDOWN:
# # # #             pos = pygame.mouse.get_pos()
# # # #             for w in wheels:
# # # #                 if inside_wheel(pos, w["center"]):
# # # #                     active_wheel = w
# # # #                     w["drag"] = True
# # # #                     w["last_mouse"] = mouse_angle(pos, w["center"])
# # # #                     w["vel"] = 0
# # # #                     w["result"] = None
# # # #                     w["stopped"] = False
# # # #                     w["running_time"] = 0  # إعادة ضبط مدة الدوران عند بدء الحركة

# # # #         if event.type == pygame.MOUSEBUTTONUP:
# # # #             if active_wheel:
# # # #                 active_wheel["drag"] = False
# # # #                 active_wheel["vel"] += random.uniform(-0.02, 0.02)
# # # #                 active_wheel = None

# # # #         if event.type == pygame.MOUSEMOTION and active_wheel and active_wheel["drag"]:
# # # #             m = mouse_angle(pygame.mouse.get_pos(), active_wheel["center"])
# # # #             delta = m - active_wheel["last_mouse"]
# # # #             active_wheel["vel"] += delta * 18
# # # #             active_wheel["vel"] = max(-2, min(2, active_wheel["vel"]))
# # # #             active_wheel["last_mouse"] = m

# # # #     for w in wheels:
# # # #         # تحديث زاوية العجلة
# # # #         w["angle"] += w["vel"]
# # # #         w["vel"] *= friction(w["vel"])

# # # #         # تحديث مدة الدوران إذا العجلة تتحرك
# # # #         if w["vel"] != 0:
# # # #             w["running_time"] += dt

# # # #         # التوقف
# # # #         if abs(w["vel"]) < 0.0005 and not w["drag"] and not w["stopped"]:
# # # #             w["vel"] = 0
# # # #             w["result"] = str(get_under_pointer(w))
# # # #             w["stopped"] = True

# # # #     for w in wheels:
# # # #         draw_wheel(w)

# # # #     # ================= عرض النتائج حسب مدة الدوران =================
# # # #     stopped_wheels = [w for w in wheels if w["stopped"]]
# # # #     stopped_wheels.sort(key=lambda w: w["running_time"])  # الأقل مدة أولًا

# # # #     x_start = WIDTH//2 - 400
# # # #     y = 50
# # # #     for i, w in enumerate(stopped_wheels):
# # # #         txt = BIG_FONT.render(w["result"], True, (255,255,0))
# # # #         screen.blit(txt, txt.get_rect(center=(x_start + i*50, y)))

# # # #     pygame.display.flip()

# # # # pygame.quit()






# # # import pygame
# # # import math
# # # import random
# # # import string

# # # pygame.init()

# # # # ================= إعدادات عامة =================
# # # WIDTH, HEIGHT = 1400, 800
# # # screen = pygame.display.set_mode((WIDTH, HEIGHT))
# # # pygame.display.set_caption("16 دوّارة فيزيائية - جولة واحدة")
# # # clock = pygame.time.Clock()

# # # FONT = pygame.font.SysFont("arial", 16, bold=True)
# # # BIG_FONT = pygame.font.SysFont("arial", 30, bold=True)

# # # BG = (25, 25, 25)
# # # POINTER_COLOR = (255, 255, 255)

# # # RADIUS = 70  # حجم العجلات

# # # # ================= مراكز الدوّارات 4x4 =================
# # # X_OFFSETS = [150, 450, 750, 1050]
# # # Y_OFFSETS = [150, 300, 450, 600]
# # # CENTERS = [(x, y) for y in Y_OFFSETS for x in X_OFFSETS]

# # # # ================= دالة إنشاء العجلة =================
# # # def new_wheel(center, labels):
# # #     return {
# # #         "center": center,
# # #         "labels": labels,
# # #         "angle": 0,
# # #         "vel": 0,
# # #         "drag": False,
# # #         "last_mouse": 0,
# # #         "result": None,
# # #         "stopped": False,
# # #         "running_time": 0,  # مدة الدوران
# # #         "used": False       # هل تم تحريكها في الجولة
# # #     }

# # # # ================= بيانات الدوّارات =================
# # # labels_list = [
# # #     list(range(10)),                   # أرقام
# # #     list(string.ascii_uppercase),      # حروف
# # #     list("!@#$%^&*?~+-=/<>"),          # رموز = 17
# # #     ['(', ')', '[', ']', '{', '}', '<', '>', '"', "'", '«', '»', '‹', '›', '`', '´']  # أقواس =16
# # # ]

# # # # لكل نوع عجلة، نكررها 4 مرات → 16 عجلة
# # # wheels = []
# # # for labels in labels_list:
# # #     for _ in range(4):
# # #         wheels.append(new_wheel(CENTERS.pop(0), labels))

# # # # ================= ألوان للعجلات =================
# # # COLORS = [
# # #     (255,99,71),(135,206,250),(255,215,0),(144,238,144),
# # #     (221,160,221),(255,182,193),(173,216,230),(240,230,140),
# # #     (255,160,122),(176,196,222)
# # # ]

# # # active_wheel = None

# # # # ================= دوال =================
# # # def friction(v):
# # #     return 0.995 - abs(v)*0.0005

# # # def mouse_angle(pos, center):
# # #     dx, dy = pos[0]-center[0], pos[1]-center[1]
# # #     return math.atan2(dy, dx)

# # # def inside_wheel(pos, center):
# # #     dx = pos[0]-center[0]
# # #     dy = pos[1]-center[1]
# # #     return math.hypot(dx, dy) <= RADIUS

# # # def draw_wheel(wheel):
# # #     cx, cy = wheel["center"]
# # #     labels = wheel["labels"]
# # #     sections = len(labels)
# # #     section_angle = 2 * math.pi / sections

# # #     for i in range(sections):
# # #         a1 = wheel["angle"] + i * section_angle
# # #         a2 = a1 + section_angle

# # #         pygame.draw.polygon(
# # #             screen,
# # #             COLORS[i % len(COLORS)],
# # #             [(cx, cy),
# # #              (cx + RADIUS * math.cos(a1), cy + RADIUS * math.sin(a1)),
# # #              (cx + RADIUS * math.cos(a2), cy + RADIUS * math.sin(a2))]
# # #         )

# # #         ta = a1 + section_angle / 2
# # #         tx = cx + (RADIUS - 20) * math.cos(ta)
# # #         ty = cy + (RADIUS - 20) * math.sin(ta)
# # #         txt = FONT.render(str(labels[i]), True, (0,0,0))
# # #         screen.blit(txt, txt.get_rect(center=(tx, ty)))

# # #     pygame.draw.circle(screen, (0,0,0), wheel["center"], RADIUS, 3)
# # #     pygame.draw.polygon(
# # #         screen, POINTER_COLOR,
# # #         [(cx-7, cy-RADIUS-3),
# # #          (cx+7, cy-RADIUS-3),
# # #          (cx, cy-RADIUS-15)]
# # #     )

# # # def get_under_pointer(wheel):
# # #     labels = wheel["labels"]
# # #     sections = len(labels)
# # #     section_angle = 2 * math.pi / sections
# # #     norm = wheel["angle"] % (2 * math.pi)
# # #     pointer = -math.pi / 2
# # #     rel = (pointer - norm) % (2 * math.pi)
# # #     index = int(rel // section_angle) % len(labels)
# # #     return labels[index]

# # # # ================= الحلقة الرئيسية =================
# # # running = True
# # # while running:
# # #     dt = clock.tick(60)  # الوقت بالمللي ثانية منذ آخر إطار
# # #     screen.fill(BG)

# # #     for event in pygame.event.get():
# # #         if event.type == pygame.QUIT:
# # #             running = False

# # #         # تحريك العجلة
# # #         if event.type == pygame.MOUSEBUTTONDOWN:
# # #             pos = pygame.mouse.get_pos()
# # #             for w in wheels:
# # #                 if inside_wheel(pos, w["center"]) and not w["used"]:
# # #                     active_wheel = w
# # #                     w["drag"] = True
# # #                     w["last_mouse"] = mouse_angle(pos, w["center"])
# # #                     w["vel"] = 0
# # #                     w["result"] = None
# # #                     w["stopped"] = False
# # #                     w["running_time"] = 0  # إعادة ضبط مدة الدوران

# # #         if event.type == pygame.MOUSEBUTTONUP:
# # #             if active_wheel:
# # #                 active_wheel["drag"] = False
# # #                 active_wheel["vel"] += random.uniform(-0.02, 0.02)
# # #                 active_wheel["used"] = True  # تم استخدامها
# # #                 active_wheel = None

# # #         if event.type == pygame.MOUSEMOTION and active_wheel and active_wheel["drag"]:
# # #             m = mouse_angle(pygame.mouse.get_pos(), active_wheel["center"])
# # #             delta = m - active_wheel["last_mouse"]
# # #             active_wheel["vel"] += delta * 18
# # #             active_wheel["vel"] = max(-2, min(2, active_wheel["vel"]))
# # #             active_wheel["last_mouse"] = m

# # #     # تحديث حركة العجلات
# # #     for w in wheels:
# # #         w["angle"] += w["vel"]
# # #         w["vel"] *= friction(w["vel"])

# # #         # تحديث مدة الدوران إذا تتحرك
# # #         if w["vel"] != 0:
# # #             w["running_time"] += dt

# # #         # التوقف
# # #         if abs(w["vel"]) < 0.0005 and not w["drag"] and not w["stopped"]:
# # #             w["vel"] = 0
# # #             w["result"] = str(get_under_pointer(w))
# # #             w["stopped"] = True

# # #     # رسم العجلات
# # #     for w in wheels:
# # #         draw_wheel(w)

# # #     # ================= عرض النتائج حسب مدة الدوران =================
# # #     stopped_wheels = [w for w in wheels if w["stopped"]]
# # #     stopped_wheels.sort(key=lambda w: w["running_time"])  # الأقل مدة أولًا

# # #     x_start = WIDTH//2 - 400
# # #     y = 50
# # #     for i, w in enumerate(stopped_wheels):
# # #         txt = BIG_FONT.render(w["result"], True, (255,255,0))
# # #         screen.blit(txt, txt.get_rect(center=(x_start + i*50, y)))

# # #     pygame.display.flip()

# # # pygame.quit()












# # import pygame
# # import math
# # import random
# # import string

# # pygame.init()

# # # ================= إعدادات عامة =================
# # WIDTH, HEIGHT = 1400, 800
# # screen = pygame.display.set_mode((WIDTH, HEIGHT))
# # pygame.display.set_caption("16 دوّارة فيزيائية - جولة واحدة")
# # clock = pygame.time.Clock()

# # FONT = pygame.font.SysFont("arial", 16, bold=True)
# # BIG_FONT = pygame.font.SysFont("arial", 30, bold=True)

# # BG = (25, 25, 25)
# # POINTER_COLOR = (255, 255, 255)

# # RADIUS = 70  # حجم العجلات

# # # ================= مراكز الدوّارات 4x4 =================
# # X_OFFSETS = [150, 450, 750, 1050]
# # Y_OFFSETS = [150, 300, 450, 600]
# # CENTERS = [(x, y) for y in Y_OFFSETS for x in X_OFFSETS]

# # # ================= دالة إنشاء العجلة =================
# # def new_wheel(center, labels):
# #     return {
# #         "center": center,
# #         "labels": labels,
# #         "angle": 0,
# #         "vel": 0,
# #         "drag": False,
# #         "last_mouse": 0,
# #         "result": None,
# #         "stopped": False,
# #         "running_time": 0,  # مدة الدوران
# #         "used": False       # هل تم تحريكها في الجولة
# #     }

# # # ================= بيانات الدوّارات =================
# # labels_list = [
# #     list(range(10)),                   # أرقام
# #     list(string.ascii_uppercase),      # حروف
# #     list("!@#$%^&*?~+-=/<>"),          # رموز = 17
# #     ['(', ')', '[', ']', '{', '}', '<', '>', '"', "'", '«', '»', '‹', '›', '`', '´']  # أقواس =16
# # ]

# # # لكل نوع عجلة، نكررها 4 مرات → 16 عجلة
# # wheels = []
# # for labels in labels_list:
# #     for _ in range(4):
# #         wheels.append(new_wheel(CENTERS.pop(0), labels))

# # # ================= ألوان للعجلات =================
# # COLORS = [
# #     (255,99,71),(135,206,250),(255,215,0),(144,238,144),
# #     (221,160,221),(255,182,193),(173,216,230),(240,230,140),
# #     (255,160,122),(176,196,222)
# # ]

# # active_wheel = None

# # # ================= زر جولة جديدة =================
# # BUTTON_RECT = pygame.Rect(WIDTH-180, 10, 160, 40)  # موقع وحجم الزر

# # # ================= دوال =================
# # def friction(v):
# #     return 0.995 - abs(v)*0.0005

# # def mouse_angle(pos, center):
# #     dx, dy = pos[0]-center[0], pos[1]-center[1]
# #     return math.atan2(dy, dx)

# # def inside_wheel(pos, center):
# #     dx = pos[0]-center[0]
# #     dy = pos[1]-center[1]
# #     return math.hypot(dx, dy) <= RADIUS

# # def draw_wheel(wheel):
# #     cx, cy = wheel["center"]
# #     labels = wheel["labels"]
# #     sections = len(labels)
# #     section_angle = 2 * math.pi / sections

# #     for i in range(sections):
# #         a1 = wheel["angle"] + i * section_angle
# #         a2 = a1 + section_angle

# #         pygame.draw.polygon(
# #             screen,
# #             COLORS[i % len(COLORS)],
# #             [(cx, cy),
# #              (cx + RADIUS * math.cos(a1), cy + RADIUS * math.sin(a1)),
# #              (cx + RADIUS * math.cos(a2), cy + RADIUS * math.sin(a2))]
# #         )

# #         ta = a1 + section_angle / 2
# #         tx = cx + (RADIUS - 20) * math.cos(ta)
# #         ty = cy + (RADIUS - 20) * math.sin(ta)
# #         txt = FONT.render(str(labels[i]), True, (0,0,0))
# #         screen.blit(txt, txt.get_rect(center=(tx, ty)))

# #     pygame.draw.circle(screen, (0,0,0), wheel["center"], RADIUS, 3)
# #     pygame.draw.polygon(
# #         screen, POINTER_COLOR,
# #         [(cx-7, cy-RADIUS-3),
# #          (cx+7, cy-RADIUS-3),
# #          (cx, cy-RADIUS-15)]
# #     )

# # def get_under_pointer(wheel):
# #     labels = wheel["labels"]
# #     sections = len(labels)
# #     section_angle = 2 * math.pi / sections
# #     norm = wheel["angle"] % (2 * math.pi)
# #     pointer = -math.pi / 2
# #     rel = (pointer - norm) % (2 * math.pi)
# #     index = int(rel // section_angle) % len(labels)
# #     return labels[index]

# # # ================= الحلقة الرئيسية =================
# # running = True
# # while running:
# #     dt = clock.tick(60)  # الوقت بالمللي ثانية منذ آخر إطار
# #     screen.fill(BG)

# #     # رسم زر الجولة الجديدة
# #     pygame.draw.rect(screen, (50, 50, 50), BUTTON_RECT)
# #     txt_btn = FONT.render("جولة جديدة", True, (255,255,255))
# #     screen.blit(txt_btn, txt_btn.get_rect(center=BUTTON_RECT.center))

# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             running = False

# #         # الضغط على الزر
# #         if event.type == pygame.MOUSEBUTTONDOWN:
# #             pos = pygame.mouse.get_pos()
# #             if BUTTON_RECT.collidepoint(pos):
# #                 for w in wheels:
# #                     w["angle"] = 0
# #                     w["vel"] = 0
# #                     w["drag"] = False
# #                     w["stopped"] = False
# #                     w["used"] = False
# #                     w["running_time"] = 0
# #                     w["result"] = None
# #                 active_wheel = None

# #         # تحريك العجلة
# #         if event.type == pygame.MOUSEBUTTONDOWN:
# #             pos = pygame.mouse.get_pos()
# #             for w in wheels:
# #                 if inside_wheel(pos, w["center"]) and not w["used"]:
# #                     active_wheel = w
# #                     w["drag"] = True
# #                     w["last_mouse"] = mouse_angle(pos, w["center"])
# #                     w["vel"] = 0
# #                     w["result"] = None
# #                     w["stopped"] = False
# #                     w["running_time"] = 0

# #         if event.type == pygame.MOUSEBUTTONUP:
# #             if active_wheel:
# #                 active_wheel["drag"] = False
# #                 active_wheel["vel"] += random.uniform(-0.02, 0.02)
# #                 active_wheel["used"] = True
# #                 active_wheel = None

# #         if event.type == pygame.MOUSEMOTION and active_wheel and active_wheel["drag"]:
# #             m = mouse_angle(pygame.mouse.get_pos(), active_wheel["center"])
# #             delta = m - active_wheel["last_mouse"]
# #             active_wheel["vel"] += delta * 18
# #             active_wheel["vel"] = max(-2, min(2, active_wheel["vel"]))
# #             active_wheel["last_mouse"] = m

# #     # تحديث حركة العجلات
# #     for w in wheels:
# #         w["angle"] += w["vel"]
# #         w["vel"] *= friction(w["vel"])
# #         if w["vel"] != 0:
# #             w["running_time"] += dt
# #         if abs(w["vel"]) < 0.0005 and not w["drag"] and not w["stopped"]:
# #             w["vel"] = 0
# #             w["result"] = str(get_under_pointer(w))
# #             w["stopped"] = True

# #     # رسم العجلات
# #     for w in wheels:
# #         draw_wheel(w)

# #     # ================= عرض النتائج حسب مدة الدوران =================
# #     stopped_wheels = [w for w in wheels if w["stopped"]]
# #     stopped_wheels.sort(key=lambda w: w["running_time"])  # الأقل مدة أولًا

# #     x_start = WIDTH//2 - 400
# #     y = 50
# #     for i, w in enumerate(stopped_wheels):
# #         txt = BIG_FONT.render(w["result"], True, (255,255,0))
# #         screen.blit(txt, txt.get_rect(center=(x_start + i*50, y)))

# #     pygame.display.flip()

# # pygame.quit()














# import pygame
# import math
# import random
# import string

# pygame.init()

# # ================= إعدادات عامة =================
# WIDTH, HEIGHT = 1400, 800
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("16 دوّارة فيزيائية - جولة واحدة مع مؤقت")
# clock = pygame.time.Clock()

# FONT = pygame.font.SysFont("arial", 16, bold=True)
# BIG_FONT = pygame.font.SysFont("arial", 30, bold=True)

# BG = (25, 25, 25)
# POINTER_COLOR = (255, 255, 255)

# RADIUS = 70  # حجم العجلات

# # ================= مراكز الدوّارات 4x4 =================
# X_OFFSETS = [150, 450, 750, 1050]
# Y_OFFSETS = [150, 300, 450, 600]
# CENTERS = [(x, y) for y in Y_OFFSETS for x in X_OFFSETS]

# # ================= دالة إنشاء العجلة =================
# def new_wheel(center, labels):
#     return {
#         "center": center,
#         "labels": labels,
#         "angle": 0,
#         "vel": 0,
#         "drag": False,
#         "last_mouse": 0,
#         "result": None,
#         "stopped": False,
#         "running_time": 0,  # مدة الدوران
#         "used": False       # هل تم تحريكها في الجولة
#     }

# # ================= بيانات الدوّارات =================
# labels_list = [
#     list(range(10)),                   # أرقام
#     list(string.ascii_uppercase),      # حروف
#     list("!@#$%^&*?~+-=/<>"),          # رموز = 17
#     ['(', ')', '[', ']', '{', '}', '<', '>', '"', "'", '«', '»', '‹', '›', '`', '´']  # أقواس =16
# ]

# # لكل نوع عجلة، نكررها 4 مرات → 16 عجلة
# wheels = []
# for labels in labels_list:
#     for _ in range(4):
#         wheels.append(new_wheel(CENTERS.pop(0), labels))

# # ================= ألوان للعجلات =================
# COLORS = [
#     (255,99,71),(135,206,250),(255,215,0),(144,238,144),
#     (221,160,221),(255,182,193),(173,216,230),(240,230,140),
#     (255,160,122),(176,196,222)
# ]

# active_wheel = None

# # ================= زر جولة جديدة =================
# BUTTON_RECT = pygame.Rect(WIDTH-180, 10, 160, 40)  # موقع وحجم الزر

# # ================= دوال =================
# def friction(v):
#     return 0.995 - abs(v)*0.0005

# def mouse_angle(pos, center):
#     dx, dy = pos[0]-center[0], pos[1]-center[1]
#     return math.atan2(dy, dx)

# def inside_wheel(pos, center):
#     dx = pos[0]-center[0]
#     dy = pos[1]-center[1]
#     return math.hypot(dx, dy) <= RADIUS

# def draw_wheel(wheel):
#     cx, cy = wheel["center"]
#     labels = wheel["labels"]
#     sections = len(labels)
#     section_angle = 2 * math.pi / sections

#     for i in range(sections):
#         a1 = wheel["angle"] + i * section_angle
#         a2 = a1 + section_angle

#         pygame.draw.polygon(
#             screen,
#             COLORS[i % len(COLORS)],
#             [(cx, cy),
#              (cx + RADIUS * math.cos(a1), cy + RADIUS * math.sin(a1)),
#              (cx + RADIUS * math.cos(a2), cy + RADIUS * math.sin(a2))]
#         )

#         ta = a1 + section_angle / 2
#         tx = cx + (RADIUS - 20) * math.cos(ta)
#         ty = cy + (RADIUS - 20) * math.sin(ta)
#         txt = FONT.render(str(labels[i]), True, (0,0,0))
#         screen.blit(txt, txt.get_rect(center=(tx, ty)))

#     pygame.draw.circle(screen, (0,0,0), wheel["center"], RADIUS, 3)
#     pygame.draw.polygon(
#         screen, POINTER_COLOR,
#         [(cx-7, cy-RADIUS-3),
#          (cx+7, cy-RADIUS-3),
#          (cx, cy-RADIUS-15)]
#     )

#     # رسم المؤقت أعلى كل عجلة
#     time_sec = wheel["running_time"] / 1000  # تحويل المللي ثانية إلى ثواني
#     timer_text = FONT.render(f"{time_sec:.2f}s", True, (255,255,0))
#     screen.blit(timer_text, timer_text.get_rect(center=(cx, cy - RADIUS - 30)))

# def get_under_pointer(wheel):
#     labels = wheel["labels"]
#     sections = len(labels)
#     section_angle = 2 * math.pi / sections
#     norm = wheel["angle"] % (2 * math.pi)
#     pointer = -math.pi / 2
#     rel = (pointer - norm) % (2 * math.pi)
#     index = int(rel // section_angle) % len(labels)
#     return labels[index]

# # ================= الحلقة الرئيسية =================
# running = True
# while running:
#     dt = clock.tick(60)  # الوقت بالمللي ثانية منذ آخر إطار
#     screen.fill(BG)

#     # رسم زر الجولة الجديدة
#     pygame.draw.rect(screen, (50, 50, 50), BUTTON_RECT)
#     txt_btn = FONT.render("جولة جديدة", True, (255,255,255))
#     screen.blit(txt_btn, txt_btn.get_rect(center=BUTTON_RECT.center))

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#         # الضغط على الزر
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             pos = pygame.mouse.get_pos()
#             if BUTTON_RECT.collidepoint(pos):
#                 for w in wheels:
#                     w["angle"] = 0
#                     w["vel"] = 0
#                     w["drag"] = False
#                     w["stopped"] = False
#                     w["used"] = False
#                     w["running_time"] = 0
#                     w["result"] = None
#                 active_wheel = None

#         # تحريك العجلة
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             pos = pygame.mouse.get_pos()
#             for w in wheels:
#                 if inside_wheel(pos, w["center"]) and not w["used"]:
#                     active_wheel = w
#                     w["drag"] = True
#                     w["last_mouse"] = mouse_angle(pos, w["center"])
#                     w["vel"] = 0
#                     w["result"] = None
#                     w["stopped"] = False
#                     w["running_time"] = 0

#         if event.type == pygame.MOUSEBUTTONUP:
#             if active_wheel:
#                 active_wheel["drag"] = False
#                 active_wheel["vel"] += random.uniform(-0.02, 0.02)
#                 active_wheel["used"] = True
#                 active_wheel = None

#         if event.type == pygame.MOUSEMOTION and active_wheel and active_wheel["drag"]:
#             m = mouse_angle(pygame.mouse.get_pos(), active_wheel["center"])
#             delta = m - active_wheel["last_mouse"]
#             active_wheel["vel"] += delta * 18
#             active_wheel["vel"] = max(-2, min(2, active_wheel["vel"]))
#             active_wheel["last_mouse"] = m

#     # تحديث حركة العجلات
#     for w in wheels:
#         w["angle"] += w["vel"]
#         w["vel"] *= friction(w["vel"])
#         if w["vel"] != 0:
#             w["running_time"] += dt
#         if abs(w["vel"]) < 0.0005 and not w["drag"] and not w["stopped"]:
#             w["vel"] = 0
#             w["result"] = str(get_under_pointer(w))
#             w["stopped"] = True

#     # رسم العجلات مع المؤقت
#     for w in wheels:
#         draw_wheel(w)

#     # ================= عرض النتائج حسب مدة الدوران =================
#     stopped_wheels = [w for w in wheels if w["stopped"]]
#     stopped_wheels.sort(key=lambda w: w["running_time"])  # الأقل مدة أولًا

#     x_start = WIDTH//2 - 400
#     y = 50
#     for i, w in enumerate(stopped_wheels):
#         txt = BIG_FONT.render(w["result"], True, (255,255,0))
#         screen.blit(txt, txt.get_rect(center=(x_start + i*50, y)))

#     pygame.display.flip()

# pygame.quit()









import pygame
import math
import random
import string

pygame.init()

# ================= إعدادات عامة =================
WIDTH, HEIGHT = 1400, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("16 دوّارة فيزيائية - جولة واحدة مع مؤقت على اليمين")
clock = pygame.time.Clock()

FONT = pygame.font.SysFont("arial", 16, bold=True)
BIG_FONT = pygame.font.SysFont("arial", 30, bold=True)

BG = (25, 25, 25)
POINTER_COLOR = (255, 255, 255)

RADIUS = 70  # حجم العجلات

# ================= مراكز الدوّارات 4x4 =================
X_OFFSETS = [150, 450, 750, 1050]
Y_OFFSETS = [150, 300, 450, 600]
CENTERS = [(x, y) for y in Y_OFFSETS for x in X_OFFSETS]

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
        "stopped": False,
        "running_time": 0,  # مدة الدوران
        "used": False       # هل تم تحريكها في الجولة
    }

# ================= بيانات الدوّارات =================
labels_list = [
    list(range(10)),                   # أرقام
    list(string.ascii_uppercase),      # حروف
    list("!@#$%^&*?~+-=/<>"),          # رموز = 17
    ['(', ')', '[', ']', '{', '}', '<', '>', '"', "'", '«', '»', '‹', '›', '`', '´']  # أقواس =16
]

# لكل نوع عجلة، نكررها 4 مرات → 16 عجلة
wheels = []
for labels in labels_list:
    for _ in range(4):
        wheels.append(new_wheel(CENTERS.pop(0), labels))

# ================= ألوان للعجلات =================
COLORS = [
    (255,99,71),(135,206,250),(255,215,0),(144,238,144),
    (221,160,221),(255,182,193),(173,216,230),(240,230,140),
    (255,160,122),(176,196,222)
]

active_wheel = None

# ================= زر جولة جديدة =================
BUTTON_RECT = pygame.Rect(WIDTH-180, 10, 160, 40)  # موقع وحجم الزر

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
        tx = cx + (RADIUS - 20) * math.cos(ta)
        ty = cy + (RADIUS - 20) * math.sin(ta)
        txt = FONT.render(str(labels[i]), True, (0,0,0))
        screen.blit(txt, txt.get_rect(center=(tx, ty)))

    pygame.draw.circle(screen, (0,0,0), wheel["center"], RADIUS, 3)
    pygame.draw.polygon(
        screen, POINTER_COLOR,
        [(cx-7, cy-RADIUS-3),
         (cx+7, cy-RADIUS-3),
         (cx, cy-RADIUS-15)]
    )

    # رسم المؤقت على يمين العجلة
    time_sec = wheel["running_time"] / 1000
    timer_text = FONT.render(f"{time_sec:.2f}s", True, (255,255,0))
    screen.blit(timer_text, timer_text.get_rect(midleft=(cx + RADIUS + 10, cy)))

def get_under_pointer(wheel):
    labels = wheel["labels"]
    sections = len(labels)
    section_angle = 2 * math.pi / sections
    norm = wheel["angle"] % (2 * math.pi)
    pointer = -math.pi / 2
    rel = (pointer - norm) % (2 * math.pi)
    index = int(rel // section_angle) % len(labels)
    return labels[index]

# ================= الحلقة الرئيسية =================
running = True
while running:
    dt = clock.tick(60)  # الوقت بالمللي ثانية منذ آخر إطار
    screen.fill(BG)

    # رسم زر الجولة الجديدة
    pygame.draw.rect(screen, (50, 50, 50), BUTTON_RECT)
    txt_btn = FONT.render("جولة جديدة", True, (255,255,255))
    screen.blit(txt_btn, txt_btn.get_rect(center=BUTTON_RECT.center))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # الضغط على الزر
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if BUTTON_RECT.collidepoint(pos):
                for w in wheels:
                    w["angle"] = 0
                    w["vel"] = 0
                    w["drag"] = False
                    w["stopped"] = False
                    w["used"] = False
                    w["running_time"] = 0
                    w["result"] = None
                active_wheel = None

        # تحريك العجلة
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for w in wheels:
                if inside_wheel(pos, w["center"]) and not w["used"]:
                    active_wheel = w
                    w["drag"] = True
                    w["last_mouse"] = mouse_angle(pos, w["center"])
                    w["vel"] = 0
                    w["result"] = None
                    w["stopped"] = False
                    w["running_time"] = 0

        if event.type == pygame.MOUSEBUTTONUP:
            if active_wheel:
                active_wheel["drag"] = False
                active_wheel["vel"] += random.uniform(-0.02, 0.02)
                active_wheel["used"] = True
                active_wheel = None

        if event.type == pygame.MOUSEMOTION and active_wheel and active_wheel["drag"]:
            m = mouse_angle(pygame.mouse.get_pos(), active_wheel["center"])
            delta = m - active_wheel["last_mouse"]
            active_wheel["vel"] += delta * 18
            active_wheel["vel"] = max(-2, min(2, active_wheel["vel"]))
            active_wheel["last_mouse"] = m

    # تحديث حركة العجلات
    for w in wheels:
        w["angle"] += w["vel"]
        w["vel"] *= friction(w["vel"])
        if w["vel"] != 0:
            w["running_time"] += dt
        if abs(w["vel"]) < 0.0005 and not w["drag"] and not w["stopped"]:
            w["vel"] = 0
            w["result"] = str(get_under_pointer(w))
            w["stopped"] = True

    # رسم العجلات مع المؤقت على اليمين
    for w in wheels:
        draw_wheel(w)

    # ================= عرض النتائج حسب مدة الدوران =================
    stopped_wheels = [w for w in wheels if w["stopped"]]
    stopped_wheels.sort(key=lambda w: w["running_time"])  # الأقل مدة أولًا

    x_start = WIDTH//2 - 400
    y = 50
    for i, w in enumerate(stopped_wheels):
        txt = BIG_FONT.render(w["result"], True, (255,255,0))
        screen.blit(txt, txt.get_rect(center=(x_start + i*50, y)))

    pygame.display.flip()

pygame.quit()