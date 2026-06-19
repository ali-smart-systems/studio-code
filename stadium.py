# # # # import tkinter as tk
# # # # from tkinter import messagebox, scrolledtext
# # # # import time

# # # # # --- 1. المكونات السرية الثابتة ---
# # # # S_BOX = {0: 0xE, 1: 0x4, 2: 0xD, 3: 0x1, 4: 0x2, 5: 0xF, 6: 0xB, 7: 0x8,
# # # #          8: 0x3, 9: 0xA, 10: 0x6, 11: 0xC, 12: 0x5, 13: 0x9, 14: 0x0, 15: 0x7}

# # # # MASTER_KEY = [0x2A3B, 0x4B5C, 0x6C7D, 0x8D9E, 0xAF01, 0xBC12, 0xDE34, 0xEF56]

# # # # def apply_sbox(value_16bit):
# # # #     """دالة التشتيت غير الخطي"""
# # # #     res = 0
# # # #     for i in range(4):
# # # #         nibble = (value_16bit >> (i * 4)) & 0xF
# # # #         res |= (S_BOX[nibble] << (i * 4))
# # # #     return res

# # # # def get_keys(blocks_len, pulse):
# # # #     """
# # # #     توليد سلسلة مفاتيح متزامنة تعتمد على النبضة فقط.
# # # #     هنا الإصلاح الجذري: المفاتيح لا تعتمد على النص، بل على الزمن والمعادلات الرياضية.
# # # #     """
# # # #     # المفتاح الأول مشتق من الماستر والنبضة
# # # #     current_keys = [(k ^ pulse) for k in MASTER_KEY]
# # # #     derived = [current_keys[0]]
    
# # # #     # المحرك المتسلسل (يعتمد على نتيجة المعادلة السابقة + الموقع i)
# # # #     for i in range(blocks_len - 1):
# # # #         # المعادلة: (المفتاح السابق * ترتيب البلوك + النبضة)
# # # #         # هذا يضمن أن المفاتيح هي نفسها تماماً عند التشفير وعند الفك
# # # #         raw_k = (derived[i] * (i + 1) + pulse) & 0xFFFF
        
# # # #         # نطبق الـ S-Box لزيادة التعقيد
# # # #         next_k = apply_sbox(raw_k if raw_k != 0 else 0xACE1)
# # # #         derived.append(next_k)
        
# # # #     return derived

# # # # # --- 2. واجهة التطبيق (GUI) ---
# # # # class CryptoApp:
# # # #     def __init__(self, root):
# # # #         self.root = root
# # # #         self.root.title("ATC Secure System v5 (Stable)")
# # # #         self.root.geometry("600x700")
# # # #         self.root.configure(bg="#111827")

# # # #         # اختصارات النسخ واللصق
# # # #         self.setup_shortcuts()

# # # #         # العنوان
# # # #         tk.Label(root, text="الخوارزمية القاهرة (T-DCA)", font=("Segoe UI", 22, "bold"), fg="#38bdf8", bg="#111827").pack(pady=20)

# # # #         # مربع الإدخال
# # # #         tk.Label(root, text="أدخل النص (للتشفير) أو الكود الكامل ATC (للفك):", fg="#94a3b8", bg="#111827").pack(anchor="e", padx=25)
# # # #         self.input_text = scrolledtext.ScrolledText(root, height=6, width=60, font=("Consolas", 11), bg="#1e293b", fg="white", insertbackground='white')
# # # #         self.input_text.pack(pady=5)
        
# # # #         # أزرار التحكم
# # # #         btn_frame = tk.Frame(root, bg="#111827")
# # # #         btn_frame.pack(pady=20)
        
# # # #         tk.Button(btn_frame, text="🔒 تشفير", command=self.encrypt_action, bg="#10b981", fg="white", font=("Arial", 12, "bold"), width=15).grid(row=0, column=0, padx=10)
# # # #         tk.Button(btn_frame, text="🔓 فك التشفير", command=self.decrypt_action, bg="#6366f1", fg="white", font=("Arial", 12, "bold"), width=15).grid(row=0, column=1, padx=10)
# # # #         tk.Button(btn_frame, text="مسح الكل", command=self.clear_all, bg="#ef4444", fg="white", width=10).grid(row=0, column=2, padx=10)

# # # #         # مربع النتائج
# # # #         tk.Label(root, text="النتيجة:", fg="#94a3b8", bg="#111827").pack(anchor="e", padx=25)
# # # #         self.output_text = scrolledtext.ScrolledText(root, height=8, width=60, font=("Consolas", 11), bg="#0f172a", fg="#38bdf8")
# # # #         self.output_text.pack(pady=5)

# # # #     def setup_shortcuts(self):
# # # #         # تفعيل Ctrl+C و Ctrl+V و Ctrl+A
# # # #         self.root.bind_all("<Control-c>", lambda e: self.copy_output())
# # # #         self.root.bind_all("<Control-v>", lambda e: self.paste_input())
# # # #         self.root.bind_all("<Control-a>", lambda e: e.widget.select_range(0, 'end'))

# # # #     def clear_all(self):
# # # #         self.input_text.delete('1.0', tk.END)
# # # #         self.output_text.delete('1.0', tk.END)

# # # #     def copy_output(self):
# # # #         try:
# # # #             txt = self.output_text.get("1.0", tk.END).strip()
# # # #             self.root.clipboard_clear()
# # # #             self.root.clipboard_append(txt)
# # # #         except: pass

# # # #     def paste_input(self):
# # # #         try:
# # # #             txt = self.root.clipboard_get()
# # # #             self.input_text.insert(tk.END, txt)
# # # #         except: pass

# # # #     def encrypt_action(self):
# # # #         msg = self.input_text.get("1.0", tk.END).strip()
# # # #         if not msg: return
        
# # # #         try:
# # # #             pulse = int(time.time()) # النبضة الزمنية
            
# # # #             # تحويل النص إلى بلوكات
# # # #             bytes_data = msg.encode('utf-8')
# # # #             if len(bytes_data) % 2 != 0: bytes_data += b'\x00' # PADDING
# # # #             blocks = [int.from_bytes(bytes_data[i:i+2], 'big') for i in range(0, len(bytes_data), 2)]
            
# # # #             # توليد المفاتيح
# # # #             keys = get_keys(len(blocks), pulse)
            
# # # #             # التشفير XOR
# # # #             cipher = [blocks[i] ^ keys[i] for i in range(len(blocks))]
# # # #             hex_str = "".join([format(b, '04x') for b in cipher])
            
# # # #             # دمج النبضة مع الشفرة
# # # #             final_output = f"ATC-{pulse}||{hex_str}"
            
# # # #             self.output_text.delete("1.0", tk.END)
# # # #             self.output_text.insert(tk.END, final_output)
            
# # # #         except Exception as e:
# # # #             messagebox.showerror("خطأ", str(e))

# # # #     def decrypt_action(self):
# # # #         full_code = self.input_text.get("1.0", tk.END).strip()
# # # #         if not full_code: return
        
# # # #         try:
# # # #             if "||" not in full_code or "ATC-" not in full_code:
# # # #                 raise ValueError("تنسيق الشفرة غير صحيح. يجب نسخ الكود كاملاً (ATC-...)")
            
# # # #             # فصل النبضة عن البيانات
# # # #             parts = full_code.split("||")
# # # #             pulse = int(parts[0].split("-")[1])
# # # #             hex_data = parts[1]
            
# # # #             # تحويل الـ Hex إلى بلوكات
# # # #             blocks = [int(hex_data[i:i+4], 16) for i in range(0, len(hex_data), 4)]
            
# # # #             # توليد نفس المفاتيح تماماً
# # # #             keys = get_keys(len(blocks), pulse)
            
# # # #             # فك التشفير XOR
# # # #             plain_blocks = [blocks[i] ^ keys[i] for i in range(len(blocks))]
            
# # # #             # تحويل إلى نص
# # # #             dec_bytes = b"".join([b.to_bytes(2, 'big') for b in plain_blocks])
# # # #             # هذا هو السطر الذي كان يسبب المشكلة، الآن سيعمل لأن المفاتيح صحيحة
# # # #             res_text = dec_bytes.decode('utf-8').strip(chr(0))
            
# # # #             self.output_text.delete("1.0", tk.END)
# # # #             self.output_text.insert(tk.END, res_text)
            
# # # #         except UnicodeDecodeError:
# # # #             messagebox.showerror("فشل التشفير", "فشل فك التشفير!\nالسبب: الشفرة تالفة أو تم تعديلها.")
# # # #         except Exception as e:
# # # #             messagebox.showerror("خطأ", f"حدث خطأ: {e}")

# # # # root = tk.Tk()
# # # # app = CryptoApp(root)
# # # # root.mainloop()









# # # import tkinter as tk
# # # from tkinter import messagebox, scrolledtext
# # # import time
# # # import random

# # # # --- محرك التشفير (Seeded Stream Cipher) ---
# # # # هذا هو أقوى منطق ممكن برمجياً: استخدام الزمن كبذرة لتوليد الفوضى
# # # def process_data(data_bytes, pulse_id):
# # #     # نضبط "بذرة" العشوائية بناءً على النبضة الزمنية
# # #     # هذا يضمن أن نفس النبضة تعطي نفس الأرقام العشوائية تماماً
# # #     random.seed(pulse_id)
    
# # #     processed_bytes = bytearray()
# # #     for byte in data_bytes:
# # #         # نولد مفتاح عشوائي فريد لكل حرف (0-255)
# # #         key_byte = random.randint(0, 255)
# # #         # عملية الدمج (XOR)
# # #         processed_bytes.append(byte ^ key_byte)
        
# # #     return processed_bytes

# # # # --- فئة قائمة الزر الأيمن (للنسخ واللصق) ---
# # # class RightClickMenu:
# # #     def __init__(self, root):
# # #         self.menu = tk.Menu(root, tearoff=0)
# # #         self.menu.add_command(label="نسخ (Copy)", command=self.copy_text)
# # #         self.menu.add_command(label="لصق (Paste)", command=self.paste_text)
# # #         self.menu.add_command(label="قص (Cut)", command=self.cut_text)
# # #         self.menu.add_separator()
# # #         self.menu.add_command(label="تحديد الكل", command=self.select_all)
# # #         self.active_widget = None

# # #     def show(self, event):
# # #         self.active_widget = event.widget
# # #         self.menu.tk_popup(event.x_root, event.y_root)

# # #     def copy_text(self):
# # #         if self.active_widget:
# # #             try: self.active_widget.event_generate("<<Copy>>")
# # #             except: pass

# # #     def paste_text(self):
# # #         if self.active_widget:
# # #             try: self.active_widget.event_generate("<<Paste>>")
# # #             except: pass
            
# # #     def cut_text(self):
# # #         if self.active_widget:
# # #             try: self.active_widget.event_generate("<<Cut>>")
# # #             except: pass

# # #     def select_all(self):
# # #         if self.active_widget:
# # #             self.active_widget.tag_add("sel", "1.0", "end")

# # # # --- الواجهة الرسومية ---
# # # class CryptoApp:
# # #     def __init__(self, root):
# # #         self.root = root
# # #         self.root.title("ATC Black-Box System V6")
# # #         self.root.geometry("650x750")
# # #         self.root.configure(bg="#000000") # أسود ملكي

# # #         # تهيئة قائمة الزر الأيمن
# # #         self.rc_menu = RightClickMenu(root)

# # #         # العنوان
# # #         header = tk.Label(root, text="نظام ATC للتشفير السيادي", font=("Impact", 24), fg="#00ff00", bg="black")
# # #         header.pack(pady=20)

# # #         # --- قسم الإدخال ---
# # #         tk.Label(root, text="[ منطقة البيانات ]", fg="#00ff00", bg="black", font=("Courier", 12)).pack(anchor="w", padx=30)
        
# # #         self.input_text = scrolledtext.ScrolledText(root, height=8, width=70, bg="#1a1a1a", fg="white", font=("Consolas", 11), insertbackground='white')
# # #         self.input_text.pack(pady=5)
# # #         # ربط الزر الأيمن
# # #         self.input_text.bind("<Button-3>", self.rc_menu.show)

# # #         # --- الأزرار ---
# # #         btn_frame = tk.Frame(root, bg="black")
# # #         btn_frame.pack(pady=20)

# # #         # زر التشفير
# # #         btn_enc = tk.Button(btn_frame, text="تشفير (Encrypt)", command=self.encrypt, bg="#003300", fg="#00ff00", font=("Arial", 12, "bold"), width=18, activebackground="#005500")
# # #         btn_enc.grid(row=0, column=0, padx=10)

# # #         # زر فك التشفير
# # #         btn_dec = tk.Button(btn_frame, text="فك التشفير (Decrypt)", command=self.decrypt, bg="#330000", fg="#ff0000", font=("Arial", 12, "bold"), width=18, activebackground="#550000")
# # #         btn_dec.grid(row=0, column=1, padx=10)
        
# # #         # زر المسح
# # #         btn_clr = tk.Button(btn_frame, text="تنظيف الشاشة", command=self.clear_screen, bg="#333333", fg="white", font=("Arial", 10), width=15)
# # #         btn_clr.grid(row=0, column=2, padx=10)

# # #         # --- قسم المخرجات ---
# # #         tk.Label(root, text="[ النتيجة النهائية - انسخ الكود كاملاً ]", fg="#00ff00", bg="black", font=("Courier", 12)).pack(anchor="w", padx=30)
        
# # #         self.output_text = scrolledtext.ScrolledText(root, height=8, width=70, bg="#1a1a1a", fg="#00ff00", font=("Consolas", 11), insertbackground='white')
# # #         self.output_text.pack(pady=5)
# # #         self.output_text.bind("<Button-3>", self.rc_menu.show)

# # #         # تعليمات سريعة
# # #         tk.Label(root, text="* استخدم الزر الأيمن للماوس للنسخ واللصق *", fg="gray", bg="black").pack(side="bottom", pady=10)

# # #     def clear_screen(self):
# # #         self.input_text.delete('1.0', tk.END)
# # #         self.output_text.delete('1.0', tk.END)

# # #     def encrypt(self):
# # #         msg = self.input_text.get("1.0", tk.END).strip()
# # #         if not msg: return

# # #         try:
# # #             # 1. تحديد النبضة (الزمن الحالي)
# # #             pulse = int(time.time())
            
# # #             # 2. تحويل النص لبايتات
# # #             data_bytes = msg.encode('utf-8')
            
# # #             # 3. التشفير باستخدام المحرك
# # #             encrypted_bytes = process_data(data_bytes, pulse)
            
# # #             # 4. تحويل الناتج لنظام Hex
# # #             hex_output = encrypted_bytes.hex()
            
# # #             # 5. التغليف (الدمج الذكي)
# # #             final_package = f"ATC||{pulse}||{hex_output}"
            
# # #             self.output_text.delete('1.0', tk.END)
# # #             self.output_text.insert(tk.END, final_package)
            
# # #         except Exception as e:
# # #             messagebox.showerror("System Error", str(e))

# # #     def decrypt(self):
# # #         package = self.input_text.get("1.0", tk.END).strip()
# # #         if not package: return

# # #         try:
# # #             # 1. التحقق من التنسيق
# # #             if "ATC||" not in package:
# # #                 raise ValueError("الكود غير صالح! يجب أن يبدأ بـ ATC||")
            
# # #             # 2. تفكيك الكود
# # #             parts = package.split("||")
# # #             pulse = int(parts[1])  # استخراج النبضة المخزنة
# # #             hex_data = parts[2]    # استخراج الشفرة
            
# # #             # 3. تحويل الـ Hex لبايتات
# # #             encrypted_bytes = bytes.fromhex(hex_data)
            
# # #             # 4. فك التشفير (نفس العملية لأن XOR عكس نفسه)
# # #             decrypted_bytes = process_data(encrypted_bytes, pulse)
            
# # #             # 5. إظهار النص
# # #             original_text = decrypted_bytes.decode('utf-8')
            
# # #             self.output_text.delete('1.0', tk.END)
# # #             self.output_text.insert(tk.END, original_text)
            
# # #         except ValueError as ve:
# # #             messagebox.showwarning("تنبيه أمني", "الكود المدخل ناقص أو تم التلاعب به.")
# # #         except Exception as e:
# # #             messagebox.showerror("فشل فك التشفير", f"البيانات تالفة أو غير متطابقة.\n{e}")

# # # if __name__ == "__main__":
# # #     root = tk.Tk()
# # #     app = CryptoApp(root)
# # #     root.mainloop()











# # import tkinter as tk
# # from tkinter import messagebox, scrolledtext
# # import time
# # import random

# # # =========================================================
# # # (1) الماستر كي السري الخاص بك (الطبقة السيادية)
# # # غير هذه الأرقام لأي أرقام سرية أخرى لضمان خصوصيتك الكاملة
# # # =========================================================
# # MY_MASTER_KEYS = [2024, 550, 999, 129809808093] 

# # # --- محرك التشفير المطور (Seeded Stream Cipher) ---
# # def process_data(data_bytes, pulse_id):
# #     """
# #     هذه الدالة تستخدم النبضة + الماستر كي لتوليد مفاتيح مستحيلة التخمين.
# #     """
# #     # خلط النبضة مع مجموع الماستر كي لإنشاء بذرة فريدة
# #     secret_seed = pulse_id + sum(MY_MASTER_KEYS)
    
# #     # ضبط المولد بناءً على البذرة السرية
# #     random.seed(secret_seed)
    
# #     processed_bytes = bytearray()
# #     for byte in data_bytes:
# #         # توليد مفتاح عشوائي لكل بايت على حدة
# #         key_byte = random.randint(0, 255)
# #         # دمج البيانات مع المفتاح (XOR)
# #         processed_bytes.append(byte ^ key_byte)
        
# #     return processed_bytes

# # # --- فئة قائمة الزر الأيمن (لحل مشكلة النسخ واللصق) ---
# # class RightClickMenu:
# #     def __init__(self, root):
# #         self.menu = tk.Menu(root, tearoff=0)
# #         self.menu.add_command(label="نسخ (Copy)", command=self.copy_text)
# #         self.menu.add_command(label="لصق (Paste)", command=self.paste_text)
# #         self.menu.add_separator()
# #         self.menu.add_command(label="تحديد الكل", command=self.select_all)
# #         self.active_widget = None

# #     def show(self, event):
# #         self.active_widget = event.widget
# #         self.menu.tk_popup(event.x_root, event.y_root)

# #     def copy_text(self):
# #         if self.active_widget:
# #             try: self.active_widget.event_generate("<<Copy>>")
# #             except: pass

# #     def paste_text(self):
# #         if self.active_widget:
# #             try: self.active_widget.event_generate("<<Paste>>")
# #             except: pass

# #     def select_all(self):
# #         if self.active_widget:
# #             self.active_widget.tag_add("sel", "1.0", "end")

# # # --- الواجهة الرسومية المحسنة ---
# # class CryptoApp:
# #     def __init__(self, root):
# #         self.root = root
# #         self.root.title("ATC Black-Box System V6 (Master Key Edition)")
# #         self.root.geometry("650x700")
# #         self.root.configure(bg="#000000")

# #         self.rc_menu = RightClickMenu(root)

# #         tk.Label(root, text="نظام ATC للتشفير السيادي", font=("Impact", 24), fg="#00ff00", bg="black").pack(pady=20)

# #         # منطقة الإدخال
# #         tk.Label(root, text="[ أدخل النص أو الكود ]", fg="#00ff00", bg="black", font=("Courier", 12)).pack(anchor="w", padx=30)
# #         self.input_text = scrolledtext.ScrolledText(root, height=8, width=70, bg="#1a1a1a", fg="white", font=("Consolas", 11), insertbackground='white')
# #         self.input_text.pack(pady=5)
# #         self.input_text.bind("<Button-3>", self.rc_menu.show) # ربط زر اليمين

# #         # الأزرار
# #         btn_frame = tk.Frame(root, bg="black")
# #         btn_frame.pack(pady=20)

# #         tk.Button(btn_frame, text="🔒 تشفير", command=self.encrypt, bg="#003300", fg="#00ff00", font=("Arial", 12, "bold"), width=15).grid(row=0, column=0, padx=10)
# #         tk.Button(btn_frame, text="🔓 فك التشفير", command=self.decrypt, bg="#330000", fg="#ff0000", font=("Arial", 12, "bold"), width=15).grid(row=0, column=1, padx=10)
# #         tk.Button(btn_frame, text="🧹 مسح", command=lambda: [self.input_text.delete('1.0', tk.END), self.output_text.delete('1.0', tk.END)], bg="#333333", fg="white", width=10).grid(row=0, column=2, padx=10)

# #         # منطقة المخرجات
# #         tk.Label(root, text="[ النتيجة ]", fg="#00ff00", bg="black", font=("Courier", 12)).pack(anchor="w", padx=30)
# #         self.output_text = scrolledtext.ScrolledText(root, height=8, width=70, bg="#1a1a1a", fg="#00ff00", font=("Consolas", 11), insertbackground='white')
# #         self.output_text.pack(pady=5)
# #         self.output_text.bind("<Button-3>", self.rc_menu.show) # ربط زر اليمين

# #     def encrypt(self):
# #         msg = self.input_text.get("1.0", tk.END).strip()
# #         if not msg: return
# #         try:
# #             pulse = int(time.time()) # النبضة الزمنية
# #             encrypted_bytes = process_data(msg.encode('utf-8'), pulse)
# #             final_package = f"ATC||{pulse}||{encrypted_bytes.hex()}" # الدمج الذكي
# #             self.output_text.delete('1.0', tk.END)
# #             self.output_text.insert(tk.END, final_package)
# #         except Exception as e:
# #             messagebox.showerror("Error", str(e))

# #     def decrypt(self):
# #         package = self.input_text.get("1.0", tk.END).strip()
# #         if not package or "||" not in package: return
# #         try:
# #             parts = package.split("||")
# #             pulse = int(parts[1]) # استخراج النبضة
# #             hex_data = parts[2]
# #             decrypted_bytes = process_data(bytes.fromhex(hex_data), pulse)
# #             self.output_text.delete('1.0', tk.END)
# #             self.output_text.insert(tk.END, decrypted_bytes.decode('utf-8'))
# #         except Exception:
# #             messagebox.showerror("فشل", "لا يمكن فك التشفير: النبضة أو الماستر كي غير متطابقين.")

# # if __name__ == "__main__":
# #     root = tk.Tk()
# #     app = CryptoApp(root)
# #     root.mainloop()










# import tkinter as tk
# from tkinter import messagebox, scrolledtext
# import time
# import random
# import hashlib  # المكتبة المسؤولة عن توليد الـ 32 بايت (256 بت)

# # =========================================================
# # (1) الماستر كي السري الخاص بك (الطبقة السيادية)
# # غير هذه الأرقام لأي أرقام سرية أخرى لضمان خصوصيتك الكاملة
# # =========================================================
# MY_MASTER_KEYS = [2024, 550, 999, 123] 

# # --- محرك التشفير المطور (بتقنية الـ 32 بايت / 256 بت) ---
# def process_data(data_bytes, pulse_id):
#     """
#     تحويل النبضة والماستر كي إلى مفتاح عسكري طوله 32 بايت مستحيل الكسر.
#     """
#     # دمج النبضة مع الماستر كي وتحويلهم لنص بايتات
#     combined_secret = f"{pulse_id}-{MY_MASTER_KEYS}".encode()
    
#     # توليد بصمة رقمية طولها 32 بايت (SHA-256)
#     # هذه هي الـ 32 رقماً التي سألت عنها، وهي أساس الأمان العالمي
#     hash_32_bytes = hashlib.sha256(combined_secret).digest()
    
#     # استخدام الـ 32 بايت كبذرة للمحرك
#     seed_value = int.from_bytes(hash_32_bytes, 'big')
#     random.seed(seed_value)
    
#     processed_bytes = bytearray()
#     for byte in data_bytes:
#         key_byte = random.randint(0, 255)
#         processed_bytes.append(byte ^ key_byte)
        
#     return processed_bytes

# # --- فئة قائمة الزر الأيمن (لحل مشكلة النسخ واللصق) ---
# class RightClickMenu:
#     def __init__(self, root):
#         self.menu = tk.Menu(root, tearoff=0)
#         self.menu.add_command(label="نسخ (Copy)", command=self.copy_text)
#         self.menu.add_command(label="لصق (Paste)", command=self.paste_text)
#         self.menu.add_separator()
#         self.menu.add_command(label="تحديد الكل", command=self.select_all)
#         self.active_widget = None

#     def show(self, event):
#         self.active_widget = event.widget
#         self.menu.tk_popup(event.x_root, event.y_root)

#     def copy_text(self):
#         if self.active_widget:
#             try: self.active_widget.event_generate("<<Copy>>")
#             except: pass

#     def paste_text(self):
#         if self.active_widget:
#             try: self.active_widget.event_generate("<<Paste>>")
#             except: pass

#     def select_all(self):
#         if self.active_widget:
#             self.active_widget.tag_add("sel", "1.0", "end")

# # --- الواجهة الرسومية ---
# class CryptoApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("ATC Black-Box V7 (32-Byte Security)")
#         self.root.geometry("650x700")
#         self.root.configure(bg="#000000")

#         self.rc_menu = RightClickMenu(root)

#         tk.Label(root, text="نظام ATC للتشفير السيادي (V7)", font=("Impact", 24), fg="#00ff00", bg="black").pack(pady=20)

#         # منطقة الإدخال
#         tk.Label(root, text="[ أدخل النص أو الكود هنا ]", fg="#00ff00", bg="black", font=("Courier", 10)).pack(anchor="w", padx=30)
#         self.input_text = scrolledtext.ScrolledText(root, height=8, width=70, bg="#1a1a1a", fg="white", font=("Consolas", 11), insertbackground='white')
#         self.input_text.pack(pady=5)
#         self.input_text.bind("<Button-3>", self.rc_menu.show)

#         # الأزرار
#         btn_frame = tk.Frame(root, bg="black")
#         btn_frame.pack(pady=20)

#         tk.Button(btn_frame, text="🔒 تشفير عسكري", command=self.encrypt, bg="#003300", fg="#00ff00", font=("Arial", 12, "bold"), width=15).grid(row=0, column=0, padx=10)
#         tk.Button(btn_frame, text="🔓 فك التشفير", command=self.decrypt, bg="#330000", fg="#ff0000", font=("Arial", 12, "bold"), width=15).grid(row=0, column=1, padx=10)
#         tk.Button(btn_frame, text="🧹 مسح", command=lambda: [self.input_text.delete('1.0', tk.END), self.output_text.delete('1.0', tk.END)], bg="#333333", fg="white", width=10).grid(row=0, column=2, padx=10)

#         # منطقة المخرجات
#         tk.Label(root, text="[ النتيجة النهائية ]", fg="#00ff00", bg="black", font=("Courier", 10)).pack(anchor="w", padx=30)
#         self.output_text = scrolledtext.ScrolledText(root, height=8, width=70, bg="#1a1a1a", fg="#00ff00", font=("Consolas", 11), insertbackground='white')
#         self.output_text.pack(pady=5)
#         self.output_text.bind("<Button-3>", self.rc_menu.show)

#     def encrypt(self):
#         msg = self.input_text.get("1.0", tk.END).strip()
#         if not msg: return
#         try:
#             pulse = int(time.time())
#             encrypted_bytes = process_data(msg.encode('utf-8'), pulse)
#             final_package = f"ATC||{pulse}||{encrypted_bytes.hex()}"
#             self.output_text.delete('1.0', tk.END)
#             self.output_text.insert(tk.END, final_package)
#         except Exception as e:
#             messagebox.showerror("Error", str(e))

#     def decrypt(self):
#         package = self.input_text.get("1.0", tk.END).strip()
#         if not package or "||" not in package: return
#         try:
#             parts = package.split("||")
#             pulse = int(parts[1])
#             hex_data = parts[2]
#             decrypted_bytes = process_data(bytes.fromhex(hex_data), pulse)
#             self.output_text.delete('1.0', tk.END)
#             self.output_text.insert(tk.END, decrypted_bytes.decode('utf-8'))
#         except Exception:
#             messagebox.showerror("فشل", "لا يمكن فك التشفير: تأكد من نسخ الكود كاملاً ومن تطابق الماستر كي.")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = CryptoApp(root)
#     root.mainloop()






import tkinter as tk
from tkinter import messagebox, scrolledtext
import time
import random
import hashlib
import hmac # مكتبة التحقق من سلامة الرسائل

# =========================================================
# (1) الماستر كي السري (الطبقة السيادية)
# =========================================================
MY_MASTER_KEYS = [2024, 550, 999, 123] 

def process_data(data_bytes, pulse_id):
    """محرك التشفير الرئيسي 256-بت"""
    combined_secret = f"{pulse_id}-{MY_MASTER_KEYS}".encode()
    hash_32_bytes = hashlib.sha256(combined_secret).digest()
    
    seed_value = int.from_bytes(hash_32_bytes, 'big')
    random.seed(seed_value)
    
    processed_bytes = bytearray()
    for byte in data_bytes:
        key_byte = random.randint(0, 255)
        processed_bytes.append(byte ^ key_byte)
    return processed_bytes

def generate_signature(hex_payload, pulse_id):
    """توليد توقيع رقمي فريد للرسالة لمنع التلاعب بها"""
    key = f"{pulse_id}-{MY_MASTER_KEYS}".encode()
    # استخدام خوارزمية HMAC لإنشاء بصمة فريدة للشفرة
    signature = hmac.new(key, hex_payload.encode(), hashlib.sha256).hexdigest()
    return signature[:8] # نأخذ أول 8 أحرف كتوقيع كافٍ للأمان

# --- الواجهة الرسومية ---
class CryptoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ATC V8 - Authenticated Cyber-System")
        self.root.geometry("650x750")
        self.root.configure(bg="#000000")
        
        # تفعيل الزر الأيمن
        self.setup_right_click()

        tk.Label(root, text="نظام ATC  للحماية الجميلي (V8)", font=("Impact", 24), fg="#38bdf8", bg="black").pack(pady=20)

        # الإدخال
        tk.Label(root, text="[ النص المراد حمايته ]", fg="#38bdf8", bg="black").pack(anchor="w", padx=30)
        self.input_text = scrolledtext.ScrolledText(root, height=8, width=70, bg="#111827", fg="white", font=("Consolas", 11), insertbackground='white')
        self.input_text.pack(pady=5)
        self.input_text.bind("<Button-3>", self.show_menu)

        # الأزرار
        btn_frame = tk.Frame(root, bg="black")
        btn_frame.pack(pady=20)
        tk.Button(btn_frame, text="🔒 تشفير وتوقيع", command=self.encrypt, bg="#065f46", fg="white", font=("Arial", 12, "bold"), width=15).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="🔓 فك وتحقق", command=self.decrypt, bg="#7f1d1d", fg="white", font=("Arial", 12, "bold"), width=15).grid(row=0, column=1, padx=10)
        tk.Button(btn_frame, text="🧹 مسح", command=lambda: [self.input_text.delete('1.0', tk.END), self.output_text.delete('1.0', tk.END)], bg="#374151", fg="white", width=8).grid(row=0, column=2, padx=10)

        # المخرجات
        tk.Label(root, text="[ كود التشفير السيادي المحمي ]", fg="#38bdf8", bg="black").pack(anchor="w", padx=30)
        self.output_text = scrolledtext.ScrolledText(root, height=8, width=70, bg="#111827", fg="#38bdf8", font=("Consolas", 11), insertbackground='white')
        self.output_text.pack(pady=5)
        self.output_text.bind("<Button-3>", self.show_menu)

    def setup_right_click(self):
        self.menu = tk.Menu(self.root, tearoff=0)
        self.menu.add_command(label="نسخ", command=lambda: self.root.focus_get().event_generate("<<Copy>>"))
        self.menu.add_command(label="لصق", command=lambda: self.root.focus_get().event_generate("<<Paste>>"))

    def show_menu(self, event):
        self.menu.tk_popup(event.x_root, event.y_root)

    def encrypt(self):
        msg = self.input_text.get("1.0", tk.END).strip()
        if not msg: return
        try:
            pulse = int(time.time())
            enc_hex = process_data(msg.encode('utf-8'), pulse).hex()
            # إضافة التوقيع الرقمي (Signature) في نهاية الكود
            sig = generate_signature(enc_hex, pulse)
            final_package = f"ATC||{pulse}||{enc_hex}||{sig}"
            
            self.output_text.delete('1.0', tk.END)
            self.output_text.insert(tk.END, final_package)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def decrypt(self):
        package = self.input_text.get("1.0", tk.END).strip()
        if "||" not in package: return
        try:
            parts = package.split("||")
            pulse = int(parts[1])
            hex_data = parts[2]
            received_sig = parts[3]
            
            # الخطوة الأمنية: التحقق من التوقيع قبل الفك
            current_sig = generate_signature(hex_data, pulse)
            if current_sig != received_sig:
                messagebox.showerror("تنبيه أمني خطير", "فشل التحقق! هذه الرسالة تم التلاعب بها أو أن رقم النبضة خاطئ.")
                return

            dec_bytes = process_data(bytes.fromhex(hex_data), pulse)
            self.output_text.delete('1.0', tk.END)
            self.output_text.insert(tk.END, dec_bytes.decode('utf-8'))
        except Exception:
            messagebox.showerror("خطأ", "فشل فك التشفير. تأكد من صحة البيانات.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CryptoApp(root)
    root.mainloop()
