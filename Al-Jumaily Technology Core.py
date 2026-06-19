# # # -*- coding: utf-8 -*-
# # import tkinter as tk
# # import ctypes
# # import time
# # import os
# # import random
# # import base64
# # from tkinter import messagebox

# # class ATCSovereignNexus:
# #     def __init__(self, root):
# #         self.root = root
# #         self.root.title("نظام ATC للسيادة التقنية - الإصدار المستقر")
# #         self.root.geometry("700x750")
# #         self.root.configure(bg="#0a0a0a")

# #         # --- 1. تعريف المحرك (Initialize Engine) ---
# #         # نضع قيمة افتراضية لتجنب خطأ "has no attribute 'engine'"
# #         self.engine = None 
        
# #         self.dll_path = r"C:\Users\ATC\Documents\project\timesecurty\x64\Release\atc_v2.dll"

# #         try:
# #             if os.path.exists(self.dll_path):
# #                 self.engine = ctypes.CDLL(self.dll_path)
# #                 self.engine.ATC_Engine.argtypes = [ctypes.c_char_p, ctypes.c_long, ctypes.c_char_p, ctypes.c_bool, ctypes.c_int]
# #                 print(">>> تم الاتصال بالمحرك بنجاح")
# #             else:
# #                 print(f"تنبيه: الملف غير موجود في {self.dll_path}")
# #         except Exception as e:
# #             print(f"فشل تحميل المحرك: {e}")

# #         # --- 2. واجهة المستخدم ---
# #         tk.Label(root, text="نظام آل جميل للتحكم الأمني", bg="#0a0a0a", fg="#3498db", font=("Arial", 22, "bold")).pack(pady=15)
        
# #         self.lbl_pulse = tk.Label(root, text="نبضة النظام: جاري التحميل...", bg="#0a0a0a", fg="#00ff00", font=("Courier", 12))
# #         self.lbl_pulse.pack()

# #         # إدخال النص
# #         tk.Label(root, text=":أدخل النص المراد معالجته", bg="#0a0a0a", fg="#aaaaaa").pack(pady=(20,0))
# #         self.entry_msg = tk.Entry(root, font=("Arial", 14), width=50, bg="#1a1a1a", fg="#ffffff", insertbackground="white", justify="center")
# #         self.entry_msg.pack(pady=10)
# #         self.add_right_click_menu(self.entry_msg)

# #         # إدخال النبضة
# #         tk.Label(root, text=":النبضة العشوائية", bg="#0a0a0a", fg="#aaaaaa").pack()
# #         self.entry_pulse = tk.Entry(root, font=("Courier", 14), width=25, bg="#1a1a1a", fg="#3498db", insertbackground="white", justify="center")
# #         self.entry_pulse.pack(pady=5)
# #         self.add_right_click_menu(self.entry_pulse)

# #         # الأزرار
# #         btn_frame = tk.Frame(root, bg="#0a0a0a")
# #         btn_frame.pack(pady=20)
        
# #         # التأكد من ربط الدوال بشكل صحيح
# #         tk.Button(btn_frame, text="تشفير البيانات", command=self.encrypt_action, bg="#2980b9", fg="white", width=15, font=("Arial", 12, "bold")).grid(row=0, column=1, padx=10)
# #         tk.Button(btn_frame, text="فك التشفير", command=self.decrypt_action, bg="#27ae60", fg="white", width=15, font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10)

# #         # شاشة النتائج
# #         self.txt_result = tk.Text(root, height=12, width=75, bg="#000000", fg="#00ff00", font=("Courier", 11), padx=10, pady=10)
# #         self.txt_result.pack(pady=10)
# #         self.add_right_click_menu(self.txt_result)

# #         self.update_clock()

# #     # --- 3. الدوال البرمجية (داخل الكلاس) ---

# #     def update_clock(self):
# #         self.current_time = random.randint(100000000, 999999999)
# #         self.lbl_pulse.config(text="نبضة النظام الحية: " + str(self.current_time))
# #         self.root.after(1000, self.update_clock)

# #     def encrypt_action(self):
# #         if self.engine is None:
# #             messagebox.showerror("خطأ في المحرك", "المحرك (DLL) غير محمل. تأكد من تشغيل VS Code كمسؤول.")
# #             return
        
# #         msg = self.entry_msg.get()
# #         if not msg: return
        
# #         try:
# #             pulse = self.current_time
# #             msg_bytes = msg.encode('utf-8')
# #             d_len = len(msg_bytes)
# #             output = ctypes.create_string_buffer(d_len + 1)
            
# #             self.engine.ATC_Engine(msg_bytes, pulse, output, False, d_len)
            
# #             # نظام التشفير السري (حذف علامة الـ =)
# #             res_raw = output.raw[:d_len]
# #             res_secret = base64.b64encode(res_raw).decode('utf-8').replace("=", "")
            
# #             self.txt_result.delete("1.0", tk.END)
# #             self.txt_result.insert(tk.END, f"--- نجاح التشفير السري ---\nالنبضة: {pulse}\nالنتيجة:\n{res_secret}")
# #             self.entry_pulse.delete(0, tk.END)
# #             self.entry_pulse.insert(0, str(pulse))
# #         except Exception as e:
# #             messagebox.showerror("خطأ", f"حدث خطأ: {e}")

# #     def decrypt_action(self):
# #         if self.engine is None: return
        
# #         data_in = self.entry_msg.get().strip()
# #         t_pulse = self.entry_pulse.get().strip()
        
# #         if not data_in or not t_pulse: return
        
# #         try:
# #             # استعادة الحشو (Padding) سرياً لفك التشفير
# #             missing_padding = len(data_in) % 4
# #             if missing_padding:
# #                 data_in += "=" * (4 - missing_padding)
            
# #             c_bytes = base64.b64decode(data_in)
# #             d_len = len(c_bytes)
# #             pulse = int(t_pulse)
# #             output = ctypes.create_string_buffer(d_len + 1)
            
# #             self.engine.ATC_Engine(c_bytes, pulse, output, True, d_len)
            
# #             orig = output.raw[:d_len].decode('utf-8', errors='ignore')
# #             self.txt_result.delete("1.0", tk.END)
# #             self.txt_result.insert(tk.END, f"--- تم فك التشفير بنجاح ---\nالنص الأصلي:\n{orig}")
# #         except Exception as e:
# #             messagebox.showerror("خطأ", "فشل فك التشفير. تأكد من الرموز والنبضة.")

# #     def add_right_click_menu(self, widget):
# #         menu = tk.Menu(self.root, tearoff=0)
# #         menu.add_command(label="قص", command=lambda: widget.event_generate("<<Cut>>"))
# #         menu.add_command(label="نسخ", command=lambda: widget.event_generate("<<Copy>>"))
# #         menu.add_command(label="لصق", command=lambda: widget.event_generate("<<Paste>>"))
# #         menu.add_separator()
# #         menu.add_command(label="تحديد الكل", command=lambda: self.select_all(widget))
# #         widget.bind("<Button-3>", lambda e: menu.post(e.x_root, e.y_root))

# #     def select_all(self, widget):
# #         if isinstance(widget, tk.Entry):
# #             widget.select_range(0, tk.END)
# #         else:
# #             widget.tag_add("sel", "1.0", "end")
# #         return 'break'

# # if __name__ == "__main__":
# #     window = tk.Tk()
# #     app = ATCSovereignNexus(window)
# #     window.mainloop()













# # -*- coding: utf-8 -*-
# import tkinter as tk
# import ctypes, os, random, base64, socket
# from tkinter import messagebox, filedialog
# import threading # لإضافة تعدد المهام

# def encrypt_file_pro(self):
#     path = filedialog.askopenfilename()
#     if not path or not self.engine: return
    
#     # تشغيل التشفير في "خيط" منفصل لكي لا يعلق البرنامج
#     threading.Thread(target=self._process_large_file, args=(path, False)).start()

# def _process_large_file(self, path, is_decrypt):
#     try:
#         pulse = self.current_pulse if not is_decrypt else int(self.entry_pulse.get())
#         file_size = os.path.getsize(path)
#         chunk_size = 1024 * 1024  # تشفير 1 ميجا في كل مرة
        
#         output_path = path + ".atc" if not is_decrypt else path.replace(".atc", "_restored")
        
#         with open(path, "rb") as f_in, open(output_path, "wb") as f_out:
#             bytes_processed = 0
#             while True:
#                 chunk = f_in.read(chunk_size)
#                 if not chunk: break
                
#                 d_len = len(chunk)
#                 out_buff = ctypes.create_string_buffer(d_len)
                
#                 # استدعاء المحرك لكل قطعة
#                 self.engine.ATC_Engine(chunk, pulse, out_buff, is_decrypt, d_len)
#                 f_out.write(out_buff.raw[:d_len])
                
#                 bytes_processed += d_len
#                 # تحديث حالة النظام في الواجهة
#                 percent = (bytes_processed / file_size) * 100
#                 self.lbl_status.config(text=f"[Processing: {percent:.1f}%]")
        
#         self.lbl_status.config(text="[Operation Completed]")
#         messagebox.showinfo("ATC Security", "تمت العملية بنجاح على الملف الكبير!")
#     except Exception as e:
#         messagebox.showerror("Error", str(e))

# class ATCSovereignNexusV3:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("ATC - Al-Jumaily Technology Core V3.1")
#         self.root.geometry("800x850")
#         self.root.configure(bg="#050505")

#         # --- المحرك ---
#         self.dll_path = r"C:\Users\ATC\Documents\project\timesecurty\x64\Release\atc_v2.dll"
#         self.engine = None
#         try:
#             if os.path.exists(self.dll_path):
#                 self.engine = ctypes.CDLL(self.dll_path)
#                 self.engine.ATC_Engine.argtypes = [ctypes.c_char_p, ctypes.c_long, ctypes.c_char_p, ctypes.c_bool, ctypes.c_int]
#         except: print("المحرك غير متصل")

#         # --- الواجهة ---
#         tk.Label(root, text="نظام آل جميل للأمن السيادي", bg="#050505", fg="#00ccff", font=("Terminal", 25, "bold")).pack(pady=20)
        
#         self.lbl_pulse = tk.Label(root, text="Pulse: 000000000", bg="#050505", fg="#ff3300", font=("Courier", 14, "bold"))
#         self.lbl_pulse.pack(pady=10)

#         # خانة النص الأساسية
#         tk.Label(root, text=":أدخل النص أو الشفرة هنا", bg="#050505", fg="#888").pack()
#         self.entry_msg = tk.Entry(root, font=("Arial", 12), width=60, bg="#111", fg="#fff", insertbackground="white", justify="center")
#         self.entry_msg.pack(pady=5)
#         self.apply_tools(self.entry_msg) # تفعيل الأدوات

#         # خانة النبضة
#         tk.Label(root, text=":النبضة المستهدفة", bg="#050505", fg="#888").pack()
#         self.entry_pulse = tk.Entry(root, font=("Courier", 12), width=30, bg="#111", fg="#00ccff", justify="center")
#         self.entry_pulse.pack(pady=5)
#         self.apply_tools(self.entry_pulse) # تفعيل الأدوات

#         # الأزرار
#         frame_btns = tk.Frame(root, bg="#050505")
#         frame_btns.pack(pady=15)
#         tk.Button(frame_btns, text="تشفير نص", command=self.encrypt_text, bg="#004466", fg="white", width=12).grid(row=0, column=0, padx=5)
#         tk.Button(frame_btns, text="فك نص", command=self.decrypt_text, bg="#006633", fg="white", width=12).grid(row=0, column=1, padx=5)
#         tk.Button(frame_btns, text="تشفير ملف", command=self.encrypt_file, bg="#440066", fg="white", width=12).grid(row=0, column=2, padx=5)
#         tk.Button(frame_btns, text="هويتي الرقمية", command=self.network_share, bg="#664400", fg="white", width=12).grid(row=0, column=3, padx=5)
#         tk.Button(frame_btns, text="فك ملف", command=self.decrypt_file, bg="#c0392b", fg="white", width=12).grid(row=0, column=4, padx=5)
#         tk.Button(frame_btns, text="تشفير مجلد", command=self.encrypt_folder, bg="#8e44ad", fg="white", width=12).grid(row=0, column=5, padx=5)
#         tk.Button(frame_btns, text="فك مجلد", command=self.decrypt_folder_trigger, bg="#c0392b", fg="white", width=12).grid(row=0, column=6, padx=5)

#         # شاشة المخرجات
#         self.txt_result = tk.Text(root, height=15, width=85, bg="#000", fg="#00ff00", font=("Courier", 10))
#         self.txt_result.pack(pady=10)
#         self.apply_tools(self.txt_result) # تفعيل الأدوات

#         self.update_pulse()

#     # --- نظام الأدوات (النسخ، القص، اللصق) ---
#     def apply_tools(self, widget):
#         # 1. القائمة اليمينية (الماوس)
#         menu = tk.Menu(self.root, tearoff=0, bg="#222", fg="white")
#         menu.add_command(label="قص", command=lambda: widget.event_generate("<<Cut>>"))
#         menu.add_command(label="نسخ", command=lambda: widget.event_generate("<<Copy>>"))
#         menu.add_command(label="لصق", command=lambda: widget.event_generate("<<Paste>>"))
#         menu.add_separator()
#         menu.add_command(label="تحديد الكل", command=lambda: self.select_all(widget))
        
#         widget.bind("<Button-3>", lambda e: menu.post(e.x_root, e.y_root))
        
#         # 2. اختصارات الكيبورد (تأكيد التفعيل)
#         widget.bind("<Control-a>", lambda e: self.select_all(widget))
#         widget.bind("<Control-A>", lambda e: self.select_all(widget))

#     def select_all(self, widget):
#         if isinstance(widget, tk.Entry):
#             widget.select_range(0, tk.END)
#             widget.icursor(tk.END)
#         else:
#             widget.tag_add("sel", "1.0", "end")
#         return 'break'

#     # --- العمليات المتبقية ---
#     def update_pulse(self):
#         self.current_pulse = random.randint(111111111, 999999999)
#         self.lbl_pulse.config(text=f"SYSTEM PULSE: {self.current_pulse}")
#         self.root.after(1500, self.update_pulse)

#     def encrypt_text(self):
#         msg = self.entry_msg.get()
#         if not msg or not self.engine: return
#         pulse = self.current_pulse
#         b_msg = msg.encode('utf-8')
#         out = ctypes.create_string_buffer(len(b_msg) + 1)
#         self.engine.ATC_Engine(b_msg, pulse, out, False, len(b_msg))
#         res = base64.b64encode(out.raw[:len(b_msg)]).decode('utf-8').replace("=", "")
#         self.txt_result.insert("1.0", f"[Text Encrypted] Pulse: {pulse}\nResult: {res}\n{'-'*30}\n")
#         self.entry_pulse.delete(0, 'end'); self.entry_pulse.insert(0, str(pulse))

#     def decrypt_text(self):
#         try:
#             data = self.entry_msg.get().strip()
#             pulse = int(self.entry_pulse.get())
#             missing = len(data) % 4
#             if missing: data += "=" * (4 - missing)
#             b_data = base64.b64decode(data)
#             out = ctypes.create_string_buffer(len(b_data) + 1)
#             self.engine.ATC_Engine(b_data, pulse, out, True, len(b_data))
#             self.txt_result.insert("1.0", f"[Decrypted]: {out.raw[:len(b_data)].decode('utf-8', 'ignore')}\n")
#         except: messagebox.showerror("خطأ", "تأكد من البيانات والنبضة")

#     # --- [إضافة دالة فك تشفير الملفات] ---
#     def decrypt_file(self):
#         # 1. اختيار الملف المشفر (الذي ينتهي بـ .atc)
#         path = filedialog.askopenfilename(filetypes=[("ATC Encrypted Files", "*.atc")])
#         if not path or not self.engine: return
        
#         # 2. طلب النبضة التي تم التشفير بها
#         t_pulse = self.entry_pulse.get().strip()
#         if not t_pulse:
#             messagebox.showwarning("تنبيه", "يرجى إدخال 'النبضة' الصحيحة في الخانة المخصصة أولاً")
#             return
            
#         try:
#             with open(path, "rb") as f:
#                 data = f.read()
            
#             pulse = int(t_pulse)
#             out = ctypes.create_string_buffer(len(data) + 1)
            
#             # استدعاء المحرك مع ضبط isDecrypt على True
#             self.engine.ATC_Engine(data, pulse, out, True, len(data))
            
#             # 3. حفظ الملف الناتج (بدون امتداد .atc)
#             original_path = path.replace(".atc", "")
#             # إضافة كلمة _restored لتمييزه
#             save_path = filedialog.asksaveasfilename(initialfile="فك_تشفير_" + os.path.basename(original_path))
            
#             if save_path:
#                 with open(save_path, "wb") as f:
#                     f.write(out.raw[:len(data)])
#                 messagebox.showinfo("نجاح", f"تم فك تشفير الملف بنجاح وحفظه في:\n{save_path}")
                
#         except Exception as e:
#             messagebox.showerror("خطأ", f"فشل فك التشفير. تأكد من النبضة أو أن الملف لم يتم التلاعب به.\nالخطأ: {e}")


#     def encrypt_file(self):
#         path = filedialog.askopenfilename()
#         if not path or not self.engine: return
#         with open(path, "rb") as f: data = f.read()
#         pulse = self.current_pulse
#         out = ctypes.create_string_buffer(len(data) + 1)
#         self.engine.ATC_Engine(data, pulse, out, False, len(data))
#         new_path = path + ".atc"
#         with open(new_path, "wb") as f: f.write(out.raw[:len(data)])
#         messagebox.showinfo("ATC File", f"تم التشفير بنجاح!\nالنبضة: {pulse}")
  
#     def encrypt_folder(self):
#         # 1. اختيار المجلد
#         folder_selected = filedialog.askdirectory()
#         if not folder_selected or not self.engine: return
        
#         pulse = self.current_pulse
#         count = 0
        
#         # 2. المرور على كل الملفات داخل المجلد (بما فيها المجلدات الفرعية)
#         for root_path, dirs, files in os.walk(folder_selected):
#             for file in files:
#                 if file.endswith(".atc"): continue # تخطي الملفات المشفرة أصلاً
                
#                 file_path = os.path.join(root_path, file)
#                 try:
#                     with open(file_path, "rb") as f:
#                         data = f.read()
                    
#                     out = ctypes.create_string_buffer(len(data) + 1)
#                     self.engine.ATC_Engine(data, pulse, out, False, len(data))
                    
#                     # حفظ النسخة المشفرة وحذف الأصلية (أو تركها حسب رغبتك)
#                     with open(file_path + ".atc", "wb") as f:
#                         f.write(out.raw[:len(data)])
                    
#                     os.remove(file_path) # حذف الملف الأصلي لضمان "السيادة"
#                     count += 1
#                 except:
#                     continue
        
#         self.txt_result.insert("1.0", f"[Folder Shield] تم تشفير {count} ملف داخل المجلد بنبضة: {pulse}\n")
#         messagebox.showinfo("نجاح", f"تم تشفير المجلد بالكامل!\nعدد الملفات المحمية: {count}")

#     def decrypt_folder_trigger(self):
#         # تشغيل العملية في خيط منفصل لضمان عدم تعليق الواجهة
#         threading.Thread(target=self.decrypt_folder_action).start()

#     def decrypt_folder_action(self):
#       # 1. اختيار المجلد الذي يحتوي على ملفات .atc
#         folder_selected = filedialog.askdirectory()
#         if not folder_selected or not self.engine: return
        
#         # 2. الحصول على النبضة من خانة الإدخال
#         t_pulse = self.entry_pulse.get().strip()
#         if not t_pulse:
#             messagebox.showwarning("تنبيه", "أدخل النبضة (Pulse) المستخدمة في التشفير أولاً!")
#             return
            
#         try:
#             pulse = int(t_pulse)
#             count = 0
#             chunk_size = 1024 * 1024 # معالجة 1 ميجا في المرة (للتعامل مع الفيديوهات)

#             # 3. البحث عن ملفات .atc في المجلد وكل المجلدات الفرعية
#             for root_path, dirs, files in os.walk(folder_selected):
#                 for file in files:
#                     if file.endswith(".atc"):
#                         file_path = os.path.join(root_path, file)
#                         # اسم الملف الأصلي (بدون .atc)
#                         original_file_path = file_path.replace(".atc", "")
                        
#                         self.lbl_status.config(text=f"[فك تشفير: {file}]")
                        
#                         # عملية فك التشفير بالتدفق (Streaming) للملفات الكبيرة
#                         with open(file_path, "rb") as f_in, open(original_file_path, "wb") as f_out:
#                             while True:
#                                 chunk = f_in.read(chunk_size)
#                                 if not chunk: break
                                
#                                 d_len = len(chunk)
#                                 out_buff = ctypes.create_string_buffer(d_len)
#                                 # استدعاء المحرك (isDecrypt = True)
#                                 self.engine.ATC_Engine(chunk, pulse, out_buff, True, d_len)
#                                 f_out.write(out_buff.raw[:d_len])
                        
#                         # حذف النسخة المشفرة بعد استعادة الأصل بنجاح
#                         os.remove(file_path)
#                         count += 1

#             self.lbl_status.config(text="[تم استعادة المجلد بالكامل]")
#             messagebox.showinfo("سيادة ATC", f"تم فك تشفير المجلد بنجاح!\nعدد الملفات المستعادة: {count}")
            
#         except ValueError:
#             messagebox.showerror("خطأ", "النبضة يجب أن تكون أرقاماً فقط!")
#         except Exception as e:
#             messagebox.showerror("خطأ", f"حدثت مشكلة: {e}")



#     def network_share(self):
#         ip = socket.gethostbyname(socket.gethostname())
#         self.txt_result.insert("1.0", f"[Identity] Your IP: {ip}\n")

# if __name__ == "__main__":
#     app = ATCSovereignNexusV3(tk.Tk())
#     app.root.mainloop()








# # -*- coding: utf-8 -*-
# import tkinter as tk
# import ctypes, os, random, base64, socket, time, threading
# from tkinter import messagebox, filedialog

# class ATCSovereignNexusV4:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("ATC - Al-Jumaily Sovereign Core V4")
#         self.root.geometry("850x900")
#         self.root.configure(bg="#050505")

#         # --- المحرك والمسارات ---
#         self.vault_path = os.path.join(os.path.expanduser("~"), "Documents", "atc_vault.log")
#         self.dll_path = r"C:\Users\ATC\Documents\project\timesecurty\x64\Release\atc_v2.dll"
#         self.engine = None
#         try:
#             if os.path.exists(self.dll_path):
#                 self.engine = ctypes.CDLL(self.dll_path)
#                 self.engine.ATC_Engine.argtypes = [ctypes.c_char_p, ctypes.c_long, ctypes.c_char_p, ctypes.c_bool, ctypes.c_int]
#         except: pass

#         # --- الواجهة السينمائية ---
#         tk.Label(root, text="نظام آل جميل للأمن السيادي", bg="#050505", fg="#00ccff", font=("Terminal", 25, "bold")).pack(pady=20)
        
#         # خانة الحالة (إصلاح الخطأ lbl_status)
#         self.lbl_status = tk.Label(root, text="[النظام نشط وجاهز]", bg="#050505", fg="#00ff00", font=("Courier", 10))
#         self.lbl_status.pack()

#         self.lbl_pulse = tk.Label(root, text="Pulse: 000000000", bg="#050505", fg="#ff3300", font=("Courier", 16, "bold"))
#         self.lbl_pulse.pack(pady=10)

#         # الخانات
#         tk.Label(root, text=":أدخل النص أو الشفرة", bg="#050505", fg="#888").pack()
#         self.entry_msg = tk.Entry(root, font=("Arial", 12), width=65, bg="#111", fg="#fff", insertbackground="white", justify="center")
#         self.entry_msg.pack(pady=5)
#         self.apply_tools(self.entry_msg)

#         tk.Label(root, text=":النبضة (Pulse)", bg="#050505", fg="#888").pack()
#         self.entry_pulse = tk.Entry(root, font=("Courier", 14), width=30, bg="#111", fg="#00ccff", justify="center")
#         self.entry_pulse.pack(pady=5)
#         self.apply_tools(self.entry_pulse)

#         # لوحة الأزرار المطورة
#         btn_frame = tk.Frame(root, bg="#050505")
#         btn_frame.pack(pady=20)
        
#         # ألوان سينمائية للأزرار
#         tk.Button(btn_frame, text="تشفير نص", command=self.encrypt_text, bg="#004d4d", fg="white", width=12).grid(row=0, column=0, padx=5, pady=5)
#         tk.Button(btn_frame, text="فك نص", command=self.decrypt_text, bg="#006622", fg="white", width=12).grid(row=0, column=1, padx=5, pady=5)
#         tk.Button(btn_frame, text="تشفير ملف", command=self.encrypt_file_trigger, bg="#4d004d", fg="white", width=12).grid(row=0, column=2, padx=5, pady=5)
#         tk.Button(btn_frame, text="فك ملف", command=self.decrypt_file_trigger, bg="#660000", fg="white", width=12).grid(row=0, column=3, padx=5, pady=5)
#         tk.Button(btn_frame, text="تشفير مجلد", command=self.encrypt_folder_trigger, bg="#2d2d86", fg="white", width=12).grid(row=1, column=0, padx=5, pady=5)
#         tk.Button(btn_frame, text="فك مجلد", command=self.decrypt_folder_trigger, bg="#862d2d", fg="white", width=12).grid(row=1, column=1, padx=5, pady=5)
#         tk.Button(btn_frame, text="الأرشيف السري", command=self.open_vault, bg="#444", fg="gold", width=12).grid(row=1, column=2, padx=5, pady=5)
#         tk.Button(btn_frame, text="هويتي", command=self.show_identity, bg="#664400", fg="white", width=12).grid(row=1, column=3, padx=5, pady=5)

#         # شاشة المخرجات (Matrix Style)
#         self.txt_result = tk.Text(root, height=18, width=90, bg="#000", fg="#00ff00", font=("Courier", 9))
#         self.txt_result.pack(pady=10)
#         self.apply_tools(self.txt_result)

#         self.update_pulse_clock()

#     # --- نظام الأرشفة التلقائي (الخزنة) ---
#     def auto_log(self, type, name, pulse):
#         try:
#             with open(self.vault_path, "a", encoding="utf-8") as f:
#                 f.write(f"[{time.ctime()}] {type}: {name} | Pulse: {pulse}\n")
#         except: pass

#     def open_vault(self):
#         if os.path.exists(self.vault_path):
#             os.startfile(self.vault_path)
#         else:
#             messagebox.showinfo("تنبيه", "الأرشيف فارغ حالياً")

#     # --- أدوات الماوس والاختصارات ---
#     def apply_tools(self, widget):
#         menu = tk.Menu(self.root, tearoff=0, bg="#1a1a1a", fg="white")
#         menu.add_command(label="قص", command=lambda: widget.event_generate("<<Cut>>"))
#         menu.add_command(label="نسخ", command=lambda: widget.event_generate("<<Copy>>"))
#         menu.add_command(label="لصق", command=lambda: widget.event_generate("<<Paste>>"))
#         menu.add_separator()
#         menu.add_command(label="تحديد الكل", command=lambda: widget.tag_add("sel", "1.0", "end") if hasattr(widget, "tag_add") else widget.select_range(0, tk.END))
#         widget.bind("<Button-3>", lambda e: menu.post(e.x_root, e.y_root))

#     def update_pulse_clock(self):
#         self.current_pulse = random.randint(100000000, 999999999)
#         self.lbl_pulse.config(text=f"SYSTEM PULSE: {self.current_pulse}")
#         self.root.after(1500, self.update_pulse_clock)

#     # --- الدوال الأساسية (مع إصلاح الأخطاء) ---
#     def encrypt_text(self):
#         msg = self.entry_msg.get()
#         if not msg or not self.engine: return
#         p = self.current_pulse
#         b_msg = msg.encode('utf-8')
#         out = ctypes.create_string_buffer(len(b_msg) + 1)
#         self.engine.ATC_Engine(b_msg, p, out, False, len(b_msg))
#         res = base64.b64encode(out.raw[:len(b_msg)]).decode('utf-8').replace("=", "")
#         self.txt_result.insert("1.0", f"[Text Encrypted] Pulse: {p} -> {res}\n")
#         self.auto_log("Text", msg[:10], p)
#         self.entry_pulse.delete(0, 'end'); self.entry_pulse.insert(0, str(p))

#     def decrypt_text(self):
#         try:
#             data = self.entry_msg.get().strip()
#             p = int(self.entry_pulse.get())
#             missing = len(data) % 4
#             if missing: data += "=" * (4 - missing)
#             b_data = base64.b64decode(data)
#             out = ctypes.create_string_buffer(len(b_data) + 1)
#             self.engine.ATC_Engine(b_data, p, out, True, len(b_data))
#             self.txt_result.insert("1.0", f"[Decrypted]: {out.raw[:len(b_data)].decode('utf-8', 'ignore')}\n")
#         except: messagebox.showerror("خطأ", "بيانات خاطئة")

#     # --- تشفير الملفات الكبيرة (Streaming) ---
#     def encrypt_file_trigger(self):
#         path = filedialog.askopenfilename()
#         if path: threading.Thread(target=self._file_logic, args=(path, False)).start()

#     def decrypt_file_trigger(self):
#         path = filedialog.askopenfilename(filetypes=[("ATC Files", "*.atc")])
#         if path: threading.Thread(target=self._file_logic, args=(path, True)).start()

#     def _file_logic(self, path, is_dec):
#         try:
#             p = self.current_pulse if not is_dec else int(self.entry_pulse.get())
#             chunk = 1024 * 1024
#             out_p = path + ".atc" if not is_dec else path.replace(".atc", "_restored")
#             with open(path, "rb") as f1, open(out_p, "wb") as f2:
#                 while True:
#                     data = f1.read(chunk)
#                     if not data: break
#                     buf = ctypes.create_string_buffer(len(data))
#                     self.engine.ATC_Engine(data, p, buf, is_dec, len(data))
#                     f2.write(buf.raw[:len(data)])
#             self.lbl_status.config(text="[اكتملت العملية]")
#             self.auto_log("File", os.path.basename(path), p)
#             messagebox.showinfo("نجاح", "تمت العملية بنجاح!")
#         except Exception as e: messagebox.showerror("خطأ", str(e))

#     # --- تشفير/فك المجلدات ---
#     def encrypt_folder_trigger(self):
#         f = filedialog.askdirectory()
#         if f: threading.Thread(target=self._folder_logic, args=(f, False)).start()

#     def decrypt_folder_trigger(self):
#         f = filedialog.askdirectory()
#         if f: threading.Thread(target=self._folder_logic, args=(f, True)).start()

#     # --- نسخة مصلحة لتشفير/فك المجلدات دون توقف ---
#     import gc # مكتبة تنظيف الذاكرة (Garbage Collector)

#     def _folder_logic(self, folder, is_dec):
#         try:
#             p = self.current_pulse if not is_dec else int(self.entry_pulse.get())
#             count = 0
            
#             # جلب قائمة الملفات أولاً لتجنب تغيير حجم القائمة أثناء التنفيذ
#             files_to_process = []
#             for r, d, files in os.walk(folder):
#                 for file in files:
#                     # الفلترة الذكية
#                     if not is_dec and file.lower().endswith(".atc"): continue
#                     if is_dec and not file.lower().endswith(".atc"): continue
#                     files_to_process.append(os.path.join(r, file))

#             for full_path in files_to_process:
#                 try:
#                     filename = os.path.basename(full_path)
#                     self.lbl_status.config(text=f"[جاري المعالجة: {filename}]")
                    
#                     # تنفيذ التشفير
#                     self._process_single_file(full_path, p, is_dec)
                    
#                     count += 1
                    
#                     # --- السر هنا: تنظيف الذاكرة بعد كل ملف ---
#                     gc.collect() # إجبار بايثون على إفراغ الرام فوراً
#                     time.sleep(0.1) # استراحة قصيرة جداً لتبريد المعالج
                    
#                 except Exception as e:
#                     self.txt_result.insert("1.0", f"[فشل] {os.path.basename(full_path)}: {str(e)}\n")
#                     continue
            
#             self.lbl_status.config(text="[اكتملت العملية]")
#             messagebox.showinfo("سيادة ATC", f"تمت معالجة {count} ملف بنجاح!")
                                
#         except Exception as e:
#             messagebox.showerror("خطأ حرج", f"توقف النظام: {str(e)}")

#     def _process_single_file(self, path, p, is_dec):
#         if not is_dec:
#             out_p = path + ".atc"
#         else:
#             # التأكد من حذف .atc بطريقة صحيحة
#             out_p = path[:-4] if path.lower().endswith(".atc") else path + "_fixed"

#         tmp_p = out_p + "_tmp"
#         chunk_size = 512 * 1024 # نصف ميجا (متوازن جداً)
        
#         try:
#             with open(path, "rb") as f_in, open(tmp_p, "wb") as f_out:
#                 while True:
#                     data = f_in.read(chunk_size)
#                     if not data:
#                         break
                    
#                     d_len = len(data)
                    
#                     # 1. إنشاء Buffer بحجم الداتا المقروءة بالضبط (بدون زيادة بايت واحد)
#                     in_buf = ctypes.create_string_buffer(data, d_len)
#                     out_buf = ctypes.create_string_buffer(d_len)
                    
#                     # 2. استدعاء المحرك
#                     self.engine.ATC_Engine(in_buf, p, out_buf, is_dec, d_len)
                    
#                     # 3. كتابة البيانات الخام (raw) بدقة متناهية
#                     f_out.write(out_buf.raw[:d_len])
                    
#                     # 4. تفريغ إجباري للذاكرة لضمان عدم التداخل
#                     del in_buf, out_buf
            
#             time.sleep(0.2)
            
#             # 5. التبديل النهائي مع التأكد من إغلاق الملفات
#             if os.path.exists(path):
#                 os.remove(path)
#             if os.path.exists(out_p):
#                 os.remove(out_p)
#             os.rename(tmp_p, out_p)
            
#         except Exception as e:
#             if os.path.exists(tmp_p): os.remove(tmp_p)
#             raise e

#     def show_identity(self):
#         ip = socket.gethostbyname(socket.gethostname())
#         self.txt_result.insert("1.0", f"[ID] IP: {ip} | Device: {socket.gethostname()}\n")

# if __name__ == "__main__":
#     app = ATCSovereignNexusV4(tk.Tk())
#     app.root.mainloop()










# -*- coding: utf-8 -*-
import tkinter as tk
import ctypes, os, random, base64, time, threading, gc
from tkinter import messagebox, filedialog

class ATCFinalSovereign:
    def __init__(self, root):
        self.root = root
        self.root.title("ATC Sovereign Nexus V6 - Al-Jumaily Edition")
        self.root.geometry("800x850")
        self.root.configure(bg="#0a0a0a")

        # --- الإعدادات والمسارات ---
        self.vault_path = os.path.join(os.path.expanduser("~"), "Documents", "atc_vault.log")
        self.dll_path = r"C:\Users\ATC\Documents\project\timesecurty\x64\Release\atc_v2.dll"
        self.engine = None
        self._load_engine()

        # --- الواجهة السينمائية ---
        tk.Label(root, text="نظام التشفير السيادي - آل جميل", bg="#0a0a0a", fg="#00ffcc", font=("Courier", 22, "bold")).pack(pady=15)
        
        self.lbl_status = tk.Label(root, text="[النظام جاهز ومؤمن]", bg="#0a0a0a", fg="#00ff00", font=("Courier", 10))
        self.lbl_status.pack()

        self.lbl_pulse = tk.Label(root, text="SYSTEM PULSE: 000000000", bg="#0a0a0a", fg="#ff3300", font=("Courier", 14, "bold"))
        self.lbl_pulse.pack(pady=10)

        # خانات الإدخال
        tk.Label(root, text=":النص أو الشفرة", bg="#0a0a0a", fg="#888").pack()
        self.entry_msg = tk.Entry(root, font=("Arial", 12), width=60, bg="#1a1a1a", fg="#fff", insertbackground="white", justify="center")
        self.entry_msg.pack(pady=5)
        self.add_right_click_menu(self.entry_msg)

        tk.Label(root, text=":النبضة المستهدفة (Pulse)", bg="#0a0a0a", fg="#888").pack()
        self.entry_pulse = tk.Entry(root, font=("Courier", 14), width=25, bg="#1a1a1a", fg="#00ccff", justify="center")
        self.entry_pulse.pack(pady=5)
        self.add_right_click_menu(self.entry_pulse)

        # لوحة التحكم
        frame_btns = tk.Frame(root, bg="#0a0a0a")
        frame_btns.pack(pady=20)

        # الأزرار بتصميم احترافي
        btns = [
            ("تشفير شنص", self.encrypt_text, "#004444"), ("فك نص", self.decrypt_text, "#004411"),
            ("تشفير ملف", self.encrypt_file_thread, "#440044"), ("فك ملف", self.decrypt_file_thread, "#440000"),
            ("تشفير مجلد", self.encrypt_folder_thread, "#111144"), ("فك مجلد", self.decrypt_folder_thread, "#442200"),
            ("الخزنة (Logs)", self.open_vault, "#333333")
        ]

        for i, (text, cmd, col) in enumerate(btns):
            r, c = divmod(i, 2)
            tk.Button(frame_btns, text=text, command=cmd, bg=col, fg="white", width=15, font=("Arial", 10, "bold")).grid(row=r, column=c, padx=10, pady=5)

        # شاشة المخرجات (Matrix Mode)
        self.txt_result = tk.Text(root, height=15, width=85, bg="#000", fg="#00ff00", font=("Courier", 9))
        self.txt_result.pack(pady=10)
        self.add_right_click_menu(self.txt_result)

        self.update_pulse_anim()

    def _load_engine(self):
        try:
            if os.path.exists(self.dll_path):
                self.engine = ctypes.CDLL(self.dll_path)
                self.engine.ATC_Engine.argtypes = [ctypes.c_char_p, ctypes.c_long, ctypes.c_char_p, ctypes.c_bool, ctypes.c_int]
        except Exception as e:
            print(f"Engine Load Error: {e}")

    # --- ميزات الماوس (قص، نسخ، لصق، تحديد الكل) ---
    def add_right_click_menu(self, widget):
        menu = tk.Menu(self.root, tearoff=0, bg="#222", fg="white")
        menu.add_command(label="قص (Cut)", command=lambda: widget.event_generate("<<Cut>>"))
        menu.add_command(label="نسخ (Copy)", command=lambda: widget.event_generate("<<Copy>>"))
        menu.add_command(label="لصق (Paste)", command=lambda: widget.event_generate("<<Paste>>"))
        menu.add_separator()
        menu.add_command(label="تحديد الكل (Select All)", command=lambda: self.select_all(widget))
        
        widget.bind("<Button-3>", lambda e: menu.post(e.x_root, e.y_root))
        widget.bind("<Control-a>", lambda e: self.select_all(widget))
        widget.bind("<Control-A>", lambda e: self.select_all(widget))

    def select_all(self, widget):
        if isinstance(widget, tk.Text):
            widget.tag_add("sel", "1.0", "end")
        else:
            widget.select_range(0, tk.END)
            widget.icursor(tk.END)
        return 'break'

    def update_pulse_anim(self):
        self.current_pulse = random.randint(111111111, 999999999)
        self.lbl_pulse.config(text=f"SYSTEM PULSE: {self.current_pulse}")
        self.root.after(2000, self.update_pulse_anim)

    def log_to_vault(self, action, name, pulse):
        try:
            with open(self.vault_path, "a", encoding="utf-8") as f:
                f.write(f"[{time.ctime()}] {action} | {name} | Pulse: {pulse}\n")
        except: pass

    def open_vault(self):
        if os.path.exists(self.vault_path): os.startfile(self.vault_path)
        else: messagebox.showinfo("الخزنة", "لا توجد سجلات حالياً")

    # --- عمليات النص ---
    def encrypt_text(self):
        msg = self.entry_msg.get().strip()
        if not msg or not self.engine: return
        p = self.current_pulse
        b_msg = msg.encode('utf-8')
        out = ctypes.create_string_buffer(len(b_msg))
        self.engine.ATC_Engine(b_msg, p, out, False, len(b_msg))
        res = base64.b64encode(out.raw[:len(b_msg)]).decode()
        self.txt_result.insert("1.0", f"[Encrypted Text] Pulse: {p} -> {res}\n")
        self.entry_pulse.delete(0, tk.END); self.entry_pulse.insert(0, str(p))
        self.log_to_vault("TEXT", msg[:15], p)

    def decrypt_text(self):
        try:
            data = self.entry_msg.get().strip()
            p = int(self.entry_pulse.get())
            b_data = base64.b64decode(data)
            out = ctypes.create_string_buffer(len(b_data))
            self.engine.ATC_Engine(b_data, p, out, True, len(b_data))
            self.txt_result.insert("1.0", f"[Decrypted Text]: {out.raw[:len(b_data)].decode('utf-8', 'ignore')}\n")
        except: messagebox.showerror("خطأ", "تأكد من الشفرة والنبضة")

    # --- عمليات الملفات والمجلدات (Threading) ---
    def encrypt_file_thread(self):
        p = filedialog.askopenfilename()
        if p: threading.Thread(target=self._proc_file, args=(p, False), daemon=True).start()

    def decrypt_file_thread(self):
        p = filedialog.askopenfilename(filetypes=[("ATC Files", "*.atc")])
        if p: threading.Thread(target=self._proc_file, args=(p, True), daemon=True).start()

    def encrypt_folder_thread(self):
        f = filedialog.askdirectory()
        if f: threading.Thread(target=self._proc_folder, args=(f, False), daemon=True).start()

    def decrypt_folder_thread(self):
        f = filedialog.askdirectory()
        if f: threading.Thread(target=self._proc_folder, args=(f, True), daemon=True).start()

    def _proc_file(self, path, is_dec):
        try:
            p = int(self.entry_pulse.get()) if is_dec else self.current_pulse
            self.lbl_status.config(text=f"[جاري معالجة: {os.path.basename(path)}]")
            self._core_engine(path, p, is_dec)
            self.log_to_vault("FILE", os.path.basename(path), p)
            messagebox.showinfo("نجاح", "تمت معالجة الملف بنجاح")
        except Exception as e: messagebox.showerror("خطأ", str(e))
        finally: self.lbl_status.config(text="[النظام جاهز]")

    def _proc_folder(self, folder, is_dec):
        try:
            p = int(self.entry_pulse.get()) if is_dec else self.current_pulse
            count = 0
            for r, d, files in os.walk(folder):
                for file in files:
                    if not is_dec and file.lower().endswith(".atc"): continue
                    if is_dec and not file.lower().endswith(".atc"): continue
                    
                    full_path = os.path.join(r, file)
                    self.lbl_status.config(text=f"[Processing: {file}]")
                    self._core_engine(full_path, p, is_dec)
                    count += 1
                    gc.collect() # تنظيف الذاكرة بعد كل ملف لضمان عدم الانهيار
            
            self.log_to_vault("FOLDER", folder, p)
            messagebox.showinfo("نجاح", f"اكتمل المجلد! عدد الملفات: {count}")
        except Exception as e: messagebox.showerror("خطأ", str(e))
        finally: self.lbl_status.config(text="[النظام جاهز]")

    # --- قلب المحرك: معالجة البيانات بدقة 100% ---
    def _core_engine(self, path, pulse, is_dec):
        out_path = path + ".atc" if not is_dec else path.replace(".atc", "")
        tmp_path = out_path + "_tmp"
        
        # حجم قطعة متوازن لضمان سلامة الفيديوهات والـ PDF
        chunk_size = 256 * 1024 
        
        with open(path, "rb") as f_in, open(tmp_path, "wb") as f_out:
            while True:
                chunk = f_in.read(chunk_size)
                if not chunk: break
                
                c_len = len(chunk)
                in_buf = ctypes.create_string_buffer(chunk, c_len)
                out_buf = ctypes.create_string_buffer(c_len)
                
                self.engine.ATC_Engine(in_buf, pulse, out_buf, is_dec, c_len)
                f_out.write(out_buf.raw[:c_len])
                del in_buf, out_buf # تصفير الذاكرة

        time.sleep(0.1)
        if os.path.exists(path): os.remove(path)
        if os.path.exists(out_path): os.remove(out_path)
        os.rename(tmp_path, out_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = ATCFinalSovereign(root)
    root.mainloop()


