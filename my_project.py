import cv2
import mediapipe as mp
import numpy as np
import pyautogui
import webbrowser
import time
import winsound
import random
import string


mp_hands = mp.solutions.hands
mp_face_mesh = mp.solutions.face_mesh
hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8)
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
canvas = None
xp, yp = 0, 0
already_pressed = False 
video_is_open = False 
closed_eyes_start = 0 
sound_enabled = True 


def generate_dynamic_password():
    length = random.randint(10, 19)
    password_type = random.choice(["letters", "digits", "symbols", "mix"])
    if password_type == "letters": chars = string.ascii_letters
    elif password_type == "digits": chars = string.digits
    elif password_type == "symbols": chars = string.punctuation
    else: chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length)), password_type

print("جاهز فل الفل")

while True:
    success, img = cap.read()
    if not success: break
    img = cv2.flip(img, 1)
    h, w, c = img.shape
    if canvas is None: canvas = np.zeros_like(img)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    hand_results = hands.process(img_rgb)
    face_results = face_mesh.process(img_rgb)

    # --- [أ] منطق الوجه (الابتسام، الحزن، التعب) - موجودة هنا! ---
    if face_results.multi_face_landmarks:
        for face_lms in face_results.multi_face_landmarks:
            # نقاط العين (159، 145) ونقاط الفم (61، 291 للزوايا / 13، 14 للشفاه)
            eye_dist = abs(face_lms.landmark[159].y - face_lms.landmark[145].y) * h
            m_left, m_right = face_lms.landmark[61], face_lms.landmark[291]
            m_top, m_bottom = face_lms.landmark[13], face_lms.landmark[14]
            corners_y = (m_left.y + m_right.y) / 2

            # 1. كشف السعادة (الابتسام)
            if corners_y < m_top.y:
                cv2.putText(img, "HAPPY :)", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            # 2. كشف الحزن
            elif corners_y > m_bottom.y:
                cv2.putText(img, "SAD :(", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                if sound_enabled: winsound.Beep(440, 50)

            # 3. كشف التعب (إغلاق العين)
            if eye_dist < 10:
                if closed_eyes_start == 0: closed_eyes_start = time.time()
                elif time.time() - closed_eyes_start > 1.5:
                    cv2.putText(img, "WAKE UP!", (w//2-100, h//2), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)
                if sound_enabled: winsound.Beep(1000, 100)
            else: closed_eyes_start = 0

    # --- [ب] منطق اليد (التحكم الكامل + توليد كلمات السر) ---
    if hand_results.multi_hand_landmarks:
        for hand_lms in hand_results.multi_hand_landmarks:
            lmList = []
            for id, lm in enumerate(hand_lms.landmark):
                lmList.append([id, int(lm.x * w), int(lm.y * h)])

            if len(lmList) > 20:
                # فحص الأصابع
                thumb_up = lmList[4][1] > lmList[3][1] if lmList[5][1] > lmList[17][1] else lmList[4][1] < lmList[3][1]
                index_up = lmList[8][2] < lmList[6][2]
                middle_up = lmList[12][2] < lmList[10][2]
                ring_up = lmList[16][2] < lmList[14][2]
                pinky_up = lmList[20][2] < lmList[18][2]
                
                sound_enabled = thumb_up

                # 1. حركة توليد كلمة السر (وسطى وبنصر فقط)
                if middle_up and ring_up and not index_up and not pinky_up:
                    if not already_pressed:
                        new_pass, p_type = generate_dynamic_password()
                        cv2.rectangle(canvas, (40, 110), (w-40, 170), (0,0,0), -1)
                        cv2.putText(canvas, f"Type:{p_type} Pass: {new_pass}", (50, 150), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
                        if sound_enabled: winsound.Beep(800, 50)
                        already_pressed = True

                # 2. حركة القبضة (FIST) - تشغيل بـ Enter أو Pause بـ Space
                elif not index_up and not middle_up and not ring_up and not pinky_up:
                    if not already_pressed:
                        if not video_is_open:
                            pyautogui.press('enter'); video_is_open = True
                        else:
                            pyautogui.press('space')
                        already_pressed = True

                # 3. حركة الروك (🤘) - الخروج
                elif index_up and pinky_up and not middle_up and not ring_up:
                    if not already_pressed:
                        pyautogui.hotkey('alt', 'f4'); video_is_open = False; already_pressed = True

                # 4. تقليب الصور (3 أصابع)
                elif index_up and middle_up and ring_up and not pinky_up:
                    x_pos = lmList[8][1]
                    if x_pos < 150 and not already_pressed:
                        pyautogui.press('right'); already_pressed = True
                    elif x_pos > w - 150 and not already_pressed:
                        pyautogui.press('left'); already_pressed = True
                    elif 250 < x_pos < w - 250: already_pressed = False

                # 5. فتح جوجل (الخنصر فقط)
                elif pinky_up and not index_up and not middle_up:
                    if not already_pressed:
                        webbrowser.open("http://www.google.com"); already_pressed = True

                # 6. وضع المسح (سبابة ووسطى معاً) - يمسح الرسم والكلمات المولدة
                elif index_up and middle_up and not ring_up:
                    canvas = np.zeros_like(img); xp, yp = 0, 0
                    already_pressed = False

                # 7. وضع الرسم (سبابة فقط)
                elif index_up and not middle_up:
                    already_pressed = False 
                    x1, y1 = lmList[8][1], lmList[8][2]
                    if xp == 0 and yp == 0: xp, yp = x1, y1
                    cv2.line(canvas, (xp, yp), (x1, y1), (0, 255, 0), 10)
                    xp, yp = x1, y1
                
                else:
                    already_pressed = False; xp, yp = 0, 0

            mp_draw.draw_landmarks(img, hand_lms, mp_hands.HAND_CONNECTIONS)

    img = cv2.addWeighted(img, 1, canvas, 0.8, 0)
    cv2.imshow("The Master System FINAL", img)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()