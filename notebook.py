# # # import datetime

# # # class FarmerAccount:
# # #     def __init__(self, name):
# # #         self.name = name
# # #         self.transactions = []  # قائمة العمليات
# # #         self.balance = 0        # الرصيد المستحق للمزارع

# # #     def add_qat(self, amount, price_per_unit):
# # #         """إضافة كمية قات جديدة"""
# # #         total_price = amount * price_per_unit
# # #         self.balance += total_price
# # #         self.transactions.append({
# # #             "type": "إضافة قات",
# # #             "amount": amount,
# # #             "price": total_price,
# # #             "time": datetime.datetime.now()
# # #         })

# # #     def pay_farmer(self, amount):
# # #         """دفع جزء أو كامل المبلغ للمزارع"""
# # #         if amount > self.balance:
# # #             print("❌ المبلغ المدفوع أكبر من الرصيد المستحق!")
# # #             return
# # #         self.balance -= amount
# # #         self.transactions.append({
# # #             "type": "دفع للمزارع",
# # #             "amount": amount,
# # #             "remaining": self.balance,
# # #             "time": datetime.datetime.now()
# # #         })

# # #     def show_balance(self):
# # #         """عرض الرصيد الحالي"""
# # #         print(f"📌 المزارع: {self.name} | الرصيد المتبقي: {self.balance} ريال")

# # #     def show_transactions(self):
# # #         """عرض سجل العمليات"""
# # #         print(f"\n📜 سجل العمليات للمزارع {self.name}:")
# # #         for t in self.transactions:
# # #             if t["type"] == "إضافة قات":
# # #                 print(f"{t['time']} ➡ {t['type']} | كمية: {t['amount']} | السعر: {t['price']} ريال")
# # #             else:
# # #                 print(f"{t['time']} ➡ {t['type']} | مدفوع: {t['amount']} ريال | متبقي: {t['remaining']} ريال")


# # # # مثال عملي
# # # if __name__ == "__main__":
# # #     farmer1 = FarmerAccount("أحمد")

# # #     # إضافة قات
# # #     farmer1.add_qat(amount=10, price_per_unit=500)  # 10 وحدات × 500 ريال
# # #     farmer1.add_qat(amount=5, price_per_unit=600)   # 5 وحدات × 600 ريال

# # #     # دفع جزء من المبلغ
# # #     farmer1.pay_farmer(3000)

# # #     # عرض الرصيد
# # #     farmer1.show_balance()

# # #     # عرض سجل العمليات
# # #     farmer1.show_transactions()







# # import datetime

# # class FarmerAccount:
# #     def __init__(self, name):
# #         self.name = name
# #         self.transactions = []  # قائمة العمليات
# #         self.balance = 0        # الرصيد المستحق للمزارع

# #     def add_qat(self, quantity, qat_type, price_per_unit):
# #         """إضافة كمية قات جديدة مع النوع والسعر"""
# #         total_price = quantity * price_per_unit
# #         self.balance += total_price
# #         self.transactions.append({
# #             "type": "إضافة قات",
# #             "qat_type": qat_type,
# #             "quantity": quantity,
# #             "price_per_unit": price_per_unit,
# #             "total_price": total_price,
# #             "time": datetime.datetime.now()
# #         })

# #     def pay_farmer(self, amount):
# #         """دفع جزء أو كامل المبلغ للمزارع"""
# #         if amount > self.balance:
# #             print("❌ المبلغ المدفوع أكبر من الرصيد المستحق!")
# #             return
# #         self.balance -= amount
# #         self.transactions.append({
# #             "type": "دفع للمزارع",
# #             "amount": amount,
# #             "remaining": self.balance,
# #             "time": datetime.datetime.now()
# #         })

# #     def show_balance(self):
# #         """عرض الرصيد الحالي"""
# #         print(f"📌 المزارع: {self.name} | الرصيد المتبقي: {self.balance} ريال")

# #     def show_transactions(self):
# #         """عرض سجل العمليات"""
# #         print(f"\n📜 سجل العمليات للمزارع {self.name}:")
# #         for t in self.transactions:
# #             if t["type"] == "إضافة قات":
# #                 print(f"{t['time']} ➡ {t['type']} | النوع: {t['qat_type']} | الكمية: {t['quantity']} حبة | السعر/حبة: {t['price_per_unit']} ريال | الإجمالي: {t['total_price']} ريال")
# #             else:
# #                 print(f"{t['time']} ➡ {t['type']} | مدفوع: {t['amount']} ريال | متبقي: {t['remaining']} ريال")


# # # مثال عملي
# # if __name__ == "__main__":
# #     farmer1 = FarmerAccount("أحمد")

# #     # المزارع يعطي التاجر قات بأنواعه
# #     farmer1.add_qat(quantity=2, qat_type="عوارض", price_per_unit=400)
# #     farmer1.add_qat(quantity=5, qat_type="روس", price_per_unit=600)
# #     farmer1.add_qat(quantity=3, qat_type="نقفة", price_per_unit=350)

# #     # دفع جزء من المبلغ
# #     farmer1.pay_farmer(2000)

# #     # عرض الرصيد
# #     farmer1.show_balance()

# #     # عرض سجل العمليات
# #     farmer1.show_transactions()





# import tkinter as tk
# from tkinter import ttk, messagebox
# import datetime

# class FarmerAccountApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("دفتر حسابات تجارة القات")
        
#         # بيانات المزارعين
#         self.farmers = {}

#         # واجهة الإدخال
#         self.name_label = tk.Label(root, text="اسم المزارع:")
#         self.name_label.grid(row=0, column=0)
#         self.name_entry = tk.Entry(root)
#         self.name_entry.grid(row=0, column=1)

#         self.type_label = tk.Label(root, text="نوع القات:")
#         self.type_label.grid(row=1, column=0)
#         self.type_entry = tk.Entry(root)
#         self.type_entry.grid(row=1, column=1)

#         self.qty_label = tk.Label(root, text="عدد الحبات:")
#         self.qty_label.grid(row=2, column=0)
#         self.qty_entry = tk.Entry(root)
#         self.qty_entry.grid(row=2, column=1)

#         self.price_label = tk.Label(root, text="السعر للحبة:")
#         self.price_label.grid(row=3, column=0)
#         self.price_entry = tk.Entry(root)
#         self.price_entry.grid(row=3, column=1)

#         self.add_button = tk.Button(root, text="إضافة قات", command=self.add_qat)
#         self.add_button.grid(row=4, column=0, columnspan=2)

#         self.pay_label = tk.Label(root, text="دفع للمزارع:")
#         self.pay_label.grid(row=5, column=0)
#         self.pay_entry = tk.Entry(root)
#         self.pay_entry.grid(row=5, column=1)

#         self.pay_button = tk.Button(root, text="دفع", command=self.pay_farmer)
#         self.pay_button.grid(row=6, column=0, columnspan=2)

#         # جدول عرض العمليات
#         self.tree = ttk.Treeview(root, columns=("النوع","الكمية","السعر","الإجمالي","الوقت","الرصيد"), show="headings")
#         self.tree.grid(row=7, column=0, columnspan=2)

#         for col in ("النوع","الكمية","السعر","الإجمالي","الوقت","الرصيد"):
#             self.tree.heading(col, text=col)

#     def add_qat(self):
#         name = self.name_entry.get()
#         qat_type = self.type_entry.get()
#         qty = int(self.qty_entry.get())
#         price = int(self.price_entry.get())
#         total = qty * price
#         time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

#         if name not in self.farmers:
#             self.farmers[name] = {"balance":0, "transactions":[]}

#         self.farmers[name]["balance"] += total
#         self.farmers[name]["transactions"].append((qat_type, qty, price, total, time, self.farmers[name]["balance"]))

#         self.tree.insert("", "end", values=(qat_type, qty, price, total, time, self.farmers[name]["balance"]))
#         messagebox.showinfo("تم", f"إضافة {qty} حبة {qat_type} للمزارع {name}")

#     def pay_farmer(self):
#         name = self.name_entry.get()
#         amount = int(self.pay_entry.get())
#         time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

#         if name not in self.farmers:
#             messagebox.showerror("خطأ", "المزارع غير موجود")
#             return

#         if amount > self.farmers[name]["balance"]:
#             messagebox.showerror("خطأ", "المبلغ أكبر من الرصيد")
#             return

#         self.farmers[name]["balance"] -= amount
#         self.farmers[name]["transactions"].append(("دفع", "-", "-", amount, time, self.farmers[name]["balance"]))

#         self.tree.insert("", "end", values=("دفع", "-", "-", amount, time, self.farmers[name]["balance"]))
#         messagebox.showinfo("تم", f"دفع {amount} ريال للمزارع {name}")

# # تشغيل البرنامج
# root = tk.Tk()
# app = FarmerAccountApp(root)
# root.mainloop()








# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk, messagebox
import datetime

class FarmerAccountApp:
    def __init__(self, root):
        self.root = root
        self.root.title("دفتر حسابات تجارة القات")

        # قاعدة بيانات المزارعين
        self.farmers = {}

        # واجهة إدخال اسم المزارع
        self.name_label = tk.Label(root, text="اسم المزارع:")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        self.add_farmer_button = tk.Button(root, text="إضافة مزارع جديد", command=self.add_farmer)
        self.add_farmer_button.grid(row=0, column=2)

        # قائمة اختيار المزارع
        self.select_label = tk.Label(root, text="اختر المزارع:")
        self.select_label.grid(row=1, column=0)
        self.farmer_select = ttk.Combobox(root, values=list(self.farmers.keys()))
        self.farmer_select.grid(row=1, column=1)
        self.farmer_select.bind("<<ComboboxSelected>>", self.show_farmer_data)

        # إدخال بيانات القات
        self.type_label = tk.Label(root, text="نوع القات:")
        self.type_label.grid(row=2, column=0)
        self.type_entry = tk.Entry(root)
        self.type_entry.grid(row=2, column=1)

        self.qty_label = tk.Label(root, text="عدد الحبات:")
        self.qty_label.grid(row=3, column=0)
        self.qty_entry = tk.Entry(root)
        self.qty_entry.grid(row=3, column=1)

        self.price_label = tk.Label(root, text="السعر للحبة:")
        self.price_label.grid(row=4, column=0)
        self.price_entry = tk.Entry(root)
        self.price_entry.grid(row=4, column=1)

        self.add_button = tk.Button(root, text="إضافة قات", command=self.add_qat)
        self.add_button.grid(row=5, column=0, columnspan=2)

        # إدخال الدفع
        self.pay_label = tk.Label(root, text="دفع للمزارع:")
        self.pay_label.grid(row=6, column=0)
        self.pay_entry = tk.Entry(root)
        self.pay_entry.grid(row=6, column=1)

        self.pay_button = tk.Button(root, text="دفع", command=self.pay_farmer)
        self.pay_button.grid(row=7, column=0, columnspan=2)

        # جدول عرض العمليات
        self.tree = ttk.Treeview(root, columns=("النوع","الكمية","السعر","الإجمالي","الوقت","الرصيد"), show="headings")
        self.tree.grid(row=8, column=0, columnspan=3)

        for col in ("النوع","الكمية","السعر","الإجمالي","الوقت","الرصيد"):
            self.tree.heading(col, text=col)

    def add_farmer(self):
        name = self.name_entry.get()
        if not name:
            messagebox.showerror("خطأ", "أدخل اسم المزارع")
            return
        if name in self.farmers:
            messagebox.showerror("خطأ", "المزارع موجود بالفعل")
            return
        self.farmers[name] = {"balance":0, "transactions":[]}
        self.farmer_select["values"] = list(self.farmers.keys())
        messagebox.showinfo("تم", f"تم إضافة المزارع {name}")

    def add_qat(self):
        name = self.farmer_select.get()
        if not name:
            messagebox.showerror("خطأ", "اختر المزارع أولاً")
            return

        qat_type = self.type_entry.get()
        qty = int(self.qty_entry.get())
        price = int(self.price_entry.get())
        total = qty * price
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

        self.farmers[name]["balance"] += total
        self.farmers[name]["transactions"].append((qat_type, qty, price, total, time, self.farmers[name]["balance"]))

        self.show_farmer_data()

    def pay_farmer(self):
        name = self.farmer_select.get()
        if not name:
            messagebox.showerror("خطأ", "اختر المزارع أولاً")
            return

        amount = int(self.pay_entry.get())
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

        if amount > self.farmers[name]["balance"]:
            messagebox.showerror("خطأ", "المبلغ أكبر من الرصيد")
            return

        self.farmers[name]["balance"] -= amount
        self.farmers[name]["transactions"].append(("دفع", "-", "-", amount, time, self.farmers[name]["balance"]))

        self.show_farmer_data()

    def show_farmer_data(self, event=None):
        name = self.farmer_select.get()
        if not name:
            return
        # مسح الجدول
        for row in self.tree.get_children():
            self.tree.delete(row)
        # عرض بيانات المزارع
        for t in self.farmers[name]["transactions"]:
            self.tree.insert("", "end", values=t)