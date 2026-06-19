# # # # # # # # # # # # # # # # # # # # # # # # import datetime

# # # # # # # # # # # # # # # # # # # # # # # # class FarmerAccount:
# # # # # # # # # # # # # # # # # # # # # # # #     def __init__(self, name):
# # # # # # # # # # # # # # # # # # # # # # # #         self.name = name
# # # # # # # # # # # # # # # # # # # # # # # #         self.transactions = []  # قائمة العمليات
# # # # # # # # # # # # # # # # # # # # # # # #         self.balance = 0        # الرصيد المستحق للمزارع

# # # # # # # # # # # # # # # # # # # # # # # #     def add_qat(self, amount, price_per_unit):
# # # # # # # # # # # # # # # # # # # # # # # #         """إضافة كمية قات جديدة"""
# # # # # # # # # # # # # # # # # # # # # # # #         total_price = amount * price_per_unit
# # # # # # # # # # # # # # # # # # # # # # # #         self.balance += total_price
# # # # # # # # # # # # # # # # # # # # # # # #         self.transactions.append({
# # # # # # # # # # # # # # # # # # # # # # # #             "type": "إضافة قات",
# # # # # # # # # # # # # # # # # # # # # # # #             "amount": amount,
# # # # # # # # # # # # # # # # # # # # # # # #             "price": total_price,
# # # # # # # # # # # # # # # # # # # # # # # #             "time": datetime.datetime.now()
# # # # # # # # # # # # # # # # # # # # # # # #         })

# # # # # # # # # # # # # # # # # # # # # # # #     def pay_farmer(self, amount):
# # # # # # # # # # # # # # # # # # # # # # # #         """دفع جزء أو كامل المبلغ للمزارع"""
# # # # # # # # # # # # # # # # # # # # # # # #         if amount > self.balance:
# # # # # # # # # # # # # # # # # # # # # # # #             print("❌ المبلغ المدفوع أكبر من الرصيد المستحق!")
# # # # # # # # # # # # # # # # # # # # # # # #             return
# # # # # # # # # # # # # # # # # # # # # # # #         self.balance -= amount
# # # # # # # # # # # # # # # # # # # # # # # #         self.transactions.append({
# # # # # # # # # # # # # # # # # # # # # # # #             "type": "دفع للمزارع",
# # # # # # # # # # # # # # # # # # # # # # # #             "amount": amount,
# # # # # # # # # # # # # # # # # # # # # # # #             "remaining": self.balance,
# # # # # # # # # # # # # # # # # # # # # # # #             "time": datetime.datetime.now()
# # # # # # # # # # # # # # # # # # # # # # # #         })

# # # # # # # # # # # # # # # # # # # # # # # #     def show_balance(self):
# # # # # # # # # # # # # # # # # # # # # # # #         """عرض الرصيد الحالي"""
# # # # # # # # # # # # # # # # # # # # # # # #         print(f"📌 المزارع: {self.name} | الرصيد المتبقي: {self.balance} ريال")

# # # # # # # # # # # # # # # # # # # # # # # #     def show_transactions(self):
# # # # # # # # # # # # # # # # # # # # # # # #         """عرض سجل العمليات"""
# # # # # # # # # # # # # # # # # # # # # # # #         print(f"\n📜 سجل العمليات للمزارع {self.name}:")
# # # # # # # # # # # # # # # # # # # # # # # #         for t in self.transactions:
# # # # # # # # # # # # # # # # # # # # # # # #             if t["type"] == "إضافة قات":
# # # # # # # # # # # # # # # # # # # # # # # #                 print(f"{t['time']} ➡ {t['type']} | كمية: {t['amount']} | السعر: {t['price']} ريال")
# # # # # # # # # # # # # # # # # # # # # # # #             else:
# # # # # # # # # # # # # # # # # # # # # # # #                 print(f"{t['time']} ➡ {t['type']} | مدفوع: {t['amount']} ريال | متبقي: {t['remaining']} ريال")


# # # # # # # # # # # # # # # # # # # # # # # # # مثال عملي
# # # # # # # # # # # # # # # # # # # # # # # # if __name__ == "__main__":
# # # # # # # # # # # # # # # # # # # # # # # #     farmer1 = FarmerAccount("أحمد")

# # # # # # # # # # # # # # # # # # # # # # # #     # إضافة قات
# # # # # # # # # # # # # # # # # # # # # # # #     farmer1.add_qat(amount=10, price_per_unit=500)  # 10 وحدات × 500 ريال
# # # # # # # # # # # # # # # # # # # # # # # #     farmer1.add_qat(amount=5, price_per_unit=600)   # 5 وحدات × 600 ريال

# # # # # # # # # # # # # # # # # # # # # # # #     # دفع جزء من المبلغ
# # # # # # # # # # # # # # # # # # # # # # # #     farmer1.pay_farmer(3000)

# # # # # # # # # # # # # # # # # # # # # # # #     # عرض الرصيد
# # # # # # # # # # # # # # # # # # # # # # # #     farmer1.show_balance()

# # # # # # # # # # # # # # # # # # # # # # # #     # عرض سجل العمليات
# # # # # # # # # # # # # # # # # # # # # # # #     farmer1.show_transactions()







# # # # # # # # # # # # # # # # # # # # # # # import datetime

# # # # # # # # # # # # # # # # # # # # # # # class FarmerAccount:
# # # # # # # # # # # # # # # # # # # # # # #     def __init__(self, name):
# # # # # # # # # # # # # # # # # # # # # # #         self.name = name
# # # # # # # # # # # # # # # # # # # # # # #         self.transactions = []  # قائمة العمليات
# # # # # # # # # # # # # # # # # # # # # # #         self.balance = 0        # الرصيد المستحق للمزارع

# # # # # # # # # # # # # # # # # # # # # # #     def add_qat(self, quantity, qat_type, price_per_unit):
# # # # # # # # # # # # # # # # # # # # # # #         """إضافة كمية قات جديدة مع النوع والسعر"""
# # # # # # # # # # # # # # # # # # # # # # #         total_price = quantity * price_per_unit
# # # # # # # # # # # # # # # # # # # # # # #         self.balance += total_price
# # # # # # # # # # # # # # # # # # # # # # #         self.transactions.append({
# # # # # # # # # # # # # # # # # # # # # # #             "type": "إضافة قات",
# # # # # # # # # # # # # # # # # # # # # # #             "qat_type": qat_type,
# # # # # # # # # # # # # # # # # # # # # # #             "quantity": quantity,
# # # # # # # # # # # # # # # # # # # # # # #             "price_per_unit": price_per_unit,
# # # # # # # # # # # # # # # # # # # # # # #             "total_price": total_price,
# # # # # # # # # # # # # # # # # # # # # # #             "time": datetime.datetime.now()
# # # # # # # # # # # # # # # # # # # # # # #         })

# # # # # # # # # # # # # # # # # # # # # # #     def pay_farmer(self, amount):
# # # # # # # # # # # # # # # # # # # # # # #         """دفع جزء أو كامل المبلغ للمزارع"""
# # # # # # # # # # # # # # # # # # # # # # #         if amount > self.balance:
# # # # # # # # # # # # # # # # # # # # # # #             print("❌ المبلغ المدفوع أكبر من الرصيد المستحق!")
# # # # # # # # # # # # # # # # # # # # # # #             return
# # # # # # # # # # # # # # # # # # # # # # #         self.balance -= amount
# # # # # # # # # # # # # # # # # # # # # # #         self.transactions.append({
# # # # # # # # # # # # # # # # # # # # # # #             "type": "دفع للمزارع",
# # # # # # # # # # # # # # # # # # # # # # #             "amount": amount,
# # # # # # # # # # # # # # # # # # # # # # #             "remaining": self.balance,
# # # # # # # # # # # # # # # # # # # # # # #             "time": datetime.datetime.now()
# # # # # # # # # # # # # # # # # # # # # # #         })

# # # # # # # # # # # # # # # # # # # # # # #     def show_balance(self):
# # # # # # # # # # # # # # # # # # # # # # #         """عرض الرصيد الحالي"""
# # # # # # # # # # # # # # # # # # # # # # #         print(f"📌 المزارع: {self.name} | الرصيد المتبقي: {self.balance} ريال")

# # # # # # # # # # # # # # # # # # # # # # #     def show_transactions(self):
# # # # # # # # # # # # # # # # # # # # # # #         """عرض سجل العمليات"""
# # # # # # # # # # # # # # # # # # # # # # #         print(f"\n📜 سجل العمليات للمزارع {self.name}:")
# # # # # # # # # # # # # # # # # # # # # # #         for t in self.transactions:
# # # # # # # # # # # # # # # # # # # # # # #             if t["type"] == "إضافة قات":
# # # # # # # # # # # # # # # # # # # # # # #                 print(f"{t['time']} ➡ {t['type']} | النوع: {t['qat_type']} | الكمية: {t['quantity']} حبة | السعر/حبة: {t['price_per_unit']} ريال | الإجمالي: {t['total_price']} ريال")
# # # # # # # # # # # # # # # # # # # # # # #             else:
# # # # # # # # # # # # # # # # # # # # # # #                 print(f"{t['time']} ➡ {t['type']} | مدفوع: {t['amount']} ريال | متبقي: {t['remaining']} ريال")


# # # # # # # # # # # # # # # # # # # # # # # # مثال عملي
# # # # # # # # # # # # # # # # # # # # # # # if __name__ == "__main__":
# # # # # # # # # # # # # # # # # # # # # # #     farmer1 = FarmerAccount("أحمد")

# # # # # # # # # # # # # # # # # # # # # # #     # المزارع يعطي التاجر قات بأنواعه
# # # # # # # # # # # # # # # # # # # # # # #     farmer1.add_qat(quantity=2, qat_type="عوارض", price_per_unit=400)
# # # # # # # # # # # # # # # # # # # # # # #     farmer1.add_qat(quantity=5, qat_type="روس", price_per_unit=600)
# # # # # # # # # # # # # # # # # # # # # # #     farmer1.add_qat(quantity=3, qat_type="نقفة", price_per_unit=350)

# # # # # # # # # # # # # # # # # # # # # # #     # دفع جزء من المبلغ
# # # # # # # # # # # # # # # # # # # # # # #     farmer1.pay_farmer(2000)

# # # # # # # # # # # # # # # # # # # # # # #     # عرض الرصيد
# # # # # # # # # # # # # # # # # # # # # # #     farmer1.show_balance()

# # # # # # # # # # # # # # # # # # # # # # #     # عرض سجل العمليات
# # # # # # # # # # # # # # # # # # # # # # #     farmer1.show_transactions()





# # # # # # # # # # # # # # # # # # # # # # import tkinter as tk
# # # # # # # # # # # # # # # # # # # # # # from tkinter import ttk, messagebox
# # # # # # # # # # # # # # # # # # # # # # import datetime

# # # # # # # # # # # # # # # # # # # # # # class FarmerAccountApp:
# # # # # # # # # # # # # # # # # # # # # #     def __init__(self, root):
# # # # # # # # # # # # # # # # # # # # # #         self.root = root
# # # # # # # # # # # # # # # # # # # # # #         self.root.title("دفتر حسابات تجارة القات")
        
# # # # # # # # # # # # # # # # # # # # # #         # بيانات المزارعين
# # # # # # # # # # # # # # # # # # # # # #         self.farmers = {}

# # # # # # # # # # # # # # # # # # # # # #         # واجهة الإدخال
# # # # # # # # # # # # # # # # # # # # # #         self.name_label = tk.Label(root, text="اسم المزارع:")
# # # # # # # # # # # # # # # # # # # # # #         self.name_label.grid(row=0, column=0)
# # # # # # # # # # # # # # # # # # # # # #         self.name_entry = tk.Entry(root)
# # # # # # # # # # # # # # # # # # # # # #         self.name_entry.grid(row=0, column=1)

# # # # # # # # # # # # # # # # # # # # # #         self.type_label = tk.Label(root, text="نوع القات:")
# # # # # # # # # # # # # # # # # # # # # #         self.type_label.grid(row=1, column=0)
# # # # # # # # # # # # # # # # # # # # # #         self.type_entry = tk.Entry(root)
# # # # # # # # # # # # # # # # # # # # # #         self.type_entry.grid(row=1, column=1)

# # # # # # # # # # # # # # # # # # # # # #         self.qty_label = tk.Label(root, text="عدد الحبات:")
# # # # # # # # # # # # # # # # # # # # # #         self.qty_label.grid(row=2, column=0)
# # # # # # # # # # # # # # # # # # # # # #         self.qty_entry = tk.Entry(root)
# # # # # # # # # # # # # # # # # # # # # #         self.qty_entry.grid(row=2, column=1)

# # # # # # # # # # # # # # # # # # # # # #         self.price_label = tk.Label(root, text="السعر للحبة:")
# # # # # # # # # # # # # # # # # # # # # #         self.price_label.grid(row=3, column=0)
# # # # # # # # # # # # # # # # # # # # # #         self.price_entry = tk.Entry(root)
# # # # # # # # # # # # # # # # # # # # # #         self.price_entry.grid(row=3, column=1)

# # # # # # # # # # # # # # # # # # # # # #         self.add_button = tk.Button(root, text="إضافة قات", command=self.add_qat)
# # # # # # # # # # # # # # # # # # # # # #         self.add_button.grid(row=4, column=0, columnspan=2)

# # # # # # # # # # # # # # # # # # # # # #         self.pay_label = tk.Label(root, text="دفع للمزارع:")
# # # # # # # # # # # # # # # # # # # # # #         self.pay_label.grid(row=5, column=0)
# # # # # # # # # # # # # # # # # # # # # #         self.pay_entry = tk.Entry(root)
# # # # # # # # # # # # # # # # # # # # # #         self.pay_entry.grid(row=5, column=1)

# # # # # # # # # # # # # # # # # # # # # #         self.pay_button = tk.Button(root, text="دفع", command=self.pay_farmer)
# # # # # # # # # # # # # # # # # # # # # #         self.pay_button.grid(row=6, column=0, columnspan=2)

# # # # # # # # # # # # # # # # # # # # # #         # جدول عرض العمليات
# # # # # # # # # # # # # # # # # # # # # #         self.tree = ttk.Treeview(root, columns=("النوع","الكمية","السعر","الإجمالي","الوقت","الرصيد"), show="headings")
# # # # # # # # # # # # # # # # # # # # # #         self.tree.grid(row=7, column=0, columnspan=2)

# # # # # # # # # # # # # # # # # # # # # #         for col in ("النوع","الكمية","السعر","الإجمالي","الوقت","الرصيد"):
# # # # # # # # # # # # # # # # # # # # # #             self.tree.heading(col, text=col)

# # # # # # # # # # # # # # # # # # # # # #     def add_qat(self):
# # # # # # # # # # # # # # # # # # # # # #         name = self.name_entry.get()
# # # # # # # # # # # # # # # # # # # # # #         qat_type = self.type_entry.get()
# # # # # # # # # # # # # # # # # # # # # #         qty = int(self.qty_entry.get())
# # # # # # # # # # # # # # # # # # # # # #         price = int(self.price_entry.get())
# # # # # # # # # # # # # # # # # # # # # #         total = qty * price
# # # # # # # # # # # # # # # # # # # # # #         time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# # # # # # # # # # # # # # # # # # # # # #         if name not in self.farmers:
# # # # # # # # # # # # # # # # # # # # # #             self.farmers[name] = {"balance":0, "transactions":[]}

# # # # # # # # # # # # # # # # # # # # # #         self.farmers[name]["balance"] += total
# # # # # # # # # # # # # # # # # # # # # #         self.farmers[name]["transactions"].append((qat_type, qty, price, total, time, self.farmers[name]["balance"]))

# # # # # # # # # # # # # # # # # # # # # #         self.tree.insert("", "end", values=(qat_type, qty, price, total, time, self.farmers[name]["balance"]))
# # # # # # # # # # # # # # # # # # # # # #         messagebox.showinfo("تم", f"إضافة {qty} حبة {qat_type} للمزارع {name}")

# # # # # # # # # # # # # # # # # # # # # #     def pay_farmer(self):
# # # # # # # # # # # # # # # # # # # # # #         name = self.name_entry.get()
# # # # # # # # # # # # # # # # # # # # # #         amount = int(self.pay_entry.get())
# # # # # # # # # # # # # # # # # # # # # #         time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# # # # # # # # # # # # # # # # # # # # # #         if name not in self.farmers:
# # # # # # # # # # # # # # # # # # # # # #             messagebox.showerror("خطأ", "المزارع غير موجود")
# # # # # # # # # # # # # # # # # # # # # #             return

# # # # # # # # # # # # # # # # # # # # # #         if amount > self.farmers[name]["balance"]:
# # # # # # # # # # # # # # # # # # # # # #             messagebox.showerror("خطأ", "المبلغ أكبر من الرصيد")
# # # # # # # # # # # # # # # # # # # # # #             return

# # # # # # # # # # # # # # # # # # # # # #         self.farmers[name]["balance"] -= amount
# # # # # # # # # # # # # # # # # # # # # #         self.farmers[name]["transactions"].append(("دفع", "-", "-", amount, time, self.farmers[name]["balance"]))

# # # # # # # # # # # # # # # # # # # # # #         self.tree.insert("", "end", values=("دفع", "-", "-", amount, time, self.farmers[name]["balance"]))
# # # # # # # # # # # # # # # # # # # # # #         messagebox.showinfo("تم", f"دفع {amount} ريال للمزارع {name}")

# # # # # # # # # # # # # # # # # # # # # # # تشغيل البرنامج
# # # # # # # # # # # # # # # # # # # # # # root = tk.Tk()
# # # # # # # # # # # # # # # # # # # # # # app = FarmerAccountApp(root)
# # # # # # # # # # # # # # # # # # # # # # root.mainloop()








# # # # # # # # # # # # # # # # # # # # # # -*- coding: utf-8 -*-
# # # # # # # # # # # # # # # # # # # # # import tkinter as tk
# # # # # # # # # # # # # # # # # # # # # from tkinter import ttk, messagebox
# # # # # # # # # # # # # # # # # # # # # import datetime

# # # # # # # # # # # # # # # # # # # # # class FarmerAccountApp:
# # # # # # # # # # # # # # # # # # # # #     def __init__(self, root):
# # # # # # # # # # # # # # # # # # # # #         self.root = root
# # # # # # # # # # # # # # # # # # # # #         self.root.title("دفتر حسابات تجارة القات")

# # # # # # # # # # # # # # # # # # # # #         # قاعدة بيانات المزارعين
# # # # # # # # # # # # # # # # # # # # #         self.farmers = {}

# # # # # # # # # # # # # # # # # # # # #         # واجهة إدخال اسم المزارع
# # # # # # # # # # # # # # # # # # # # #         self.name_label = tk.Label(root, text="اسم المزارع:")
# # # # # # # # # # # # # # # # # # # # #         self.name_label.grid(row=0, column=0)
# # # # # # # # # # # # # # # # # # # # #         self.name_entry = tk.Entry(root)
# # # # # # # # # # # # # # # # # # # # #         self.name_entry.grid(row=0, column=1)

# # # # # # # # # # # # # # # # # # # # #         self.add_farmer_button = tk.Button(root, text="إضافة مزارع جديد", command=self.add_farmer)
# # # # # # # # # # # # # # # # # # # # #         self.add_farmer_button.grid(row=0, column=2)

# # # # # # # # # # # # # # # # # # # # #         # قائمة اختيار المزارع
# # # # # # # # # # # # # # # # # # # # #         self.select_label = tk.Label(root, text="اختر المزارع:")
# # # # # # # # # # # # # # # # # # # # #         self.select_label.grid(row=1, column=0)
# # # # # # # # # # # # # # # # # # # # #         self.farmer_select = ttk.Combobox(root, values=list(self.farmers.keys()))
# # # # # # # # # # # # # # # # # # # # #         self.farmer_select.grid(row=1, column=1)
# # # # # # # # # # # # # # # # # # # # #         self.farmer_select.bind("<<ComboboxSelected>>", self.show_farmer_data)

# # # # # # # # # # # # # # # # # # # # #         # إدخال بيانات القات
# # # # # # # # # # # # # # # # # # # # #         self.type_label = tk.Label(root, text="نوع القات:")
# # # # # # # # # # # # # # # # # # # # #         self.type_label.grid(row=2, column=0)
# # # # # # # # # # # # # # # # # # # # #         self.type_entry = tk.Entry(root)
# # # # # # # # # # # # # # # # # # # # #         self.type_entry.grid(row=2, column=1)

# # # # # # # # # # # # # # # # # # # # #         self.qty_label = tk.Label(root, text="عدد الحبات:")
# # # # # # # # # # # # # # # # # # # # #         self.qty_label.grid(row=3, column=0)
# # # # # # # # # # # # # # # # # # # # #         self.qty_entry = tk.Entry(root)
# # # # # # # # # # # # # # # # # # # # #         self.qty_entry.grid(row=3, column=1)

# # # # # # # # # # # # # # # # # # # # #         self.price_label = tk.Label(root, text="السعر للحبة:")
# # # # # # # # # # # # # # # # # # # # #         self.price_label.grid(row=4, column=0)
# # # # # # # # # # # # # # # # # # # # #         self.price_entry = tk.Entry(root)
# # # # # # # # # # # # # # # # # # # # #         self.price_entry.grid(row=4, column=1)

# # # # # # # # # # # # # # # # # # # # #         self.add_button = tk.Button(root, text="إضافة قات", command=self.add_qat)
# # # # # # # # # # # # # # # # # # # # #         self.add_button.grid(row=5, column=0, columnspan=2)

# # # # # # # # # # # # # # # # # # # # #         # إدخال الدفع
# # # # # # # # # # # # # # # # # # # # #         self.pay_label = tk.Label(root, text="دفع للمزارع:")
# # # # # # # # # # # # # # # # # # # # #         self.pay_label.grid(row=6, column=0)
# # # # # # # # # # # # # # # # # # # # #         self.pay_entry = tk.Entry(root)
# # # # # # # # # # # # # # # # # # # # #         self.pay_entry.grid(row=6, column=1)

# # # # # # # # # # # # # # # # # # # # #         self.pay_button = tk.Button(root, text="دفع", command=self.pay_farmer)
# # # # # # # # # # # # # # # # # # # # #         self.pay_button.grid(row=7, column=0, columnspan=2)

# # # # # # # # # # # # # # # # # # # # #         # جدول عرض العمليات
# # # # # # # # # # # # # # # # # # # # #         self.tree = ttk.Treeview(root, columns=("النوع","الكمية","السعر","الإجمالي","الوقت","الرصيد"), show="headings")
# # # # # # # # # # # # # # # # # # # # #         self.tree.grid(row=8, column=0, columnspan=3)

# # # # # # # # # # # # # # # # # # # # #         for col in ("النوع","الكمية","السعر","الإجمالي","الوقت","الرصيد"):
# # # # # # # # # # # # # # # # # # # # #             self.tree.heading(col, text=col)

# # # # # # # # # # # # # # # # # # # # #     def add_farmer(self):
# # # # # # # # # # # # # # # # # # # # #         name = self.name_entry.get()
# # # # # # # # # # # # # # # # # # # # #         if not name:
# # # # # # # # # # # # # # # # # # # # #             messagebox.showerror("خطأ", "أدخل اسم المزارع")
# # # # # # # # # # # # # # # # # # # # #             return
# # # # # # # # # # # # # # # # # # # # #         if name in self.farmers:
# # # # # # # # # # # # # # # # # # # # #             messagebox.showerror("خطأ", "المزارع موجود بالفعل")
# # # # # # # # # # # # # # # # # # # # #             return
# # # # # # # # # # # # # # # # # # # # #         self.farmers[name] = {"balance":0, "transactions":[]}
# # # # # # # # # # # # # # # # # # # # #         self.farmer_select["values"] = list(self.farmers.keys())
# # # # # # # # # # # # # # # # # # # # #         messagebox.showinfo("تم", f"تم إضافة المزارع {name}")

# # # # # # # # # # # # # # # # # # # # #     def add_qat(self):
# # # # # # # # # # # # # # # # # # # # #         name = self.farmer_select.get()
# # # # # # # # # # # # # # # # # # # # #         if not name:
# # # # # # # # # # # # # # # # # # # # #             messagebox.showerror("خطأ", "اختر المزارع أولاً")
# # # # # # # # # # # # # # # # # # # # #             return

# # # # # # # # # # # # # # # # # # # # #         qat_type = self.type_entry.get()
# # # # # # # # # # # # # # # # # # # # #         qty = int(self.qty_entry.get())
# # # # # # # # # # # # # # # # # # # # #         price = int(self.price_entry.get())
# # # # # # # # # # # # # # # # # # # # #         total = qty * price
# # # # # # # # # # # # # # # # # # # # #         time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# # # # # # # # # # # # # # # # # # # # #         self.farmers[name]["balance"] += total
# # # # # # # # # # # # # # # # # # # # #         self.farmers[name]["transactions"].append((qat_type, qty, price, total, time, self.farmers[name]["balance"]))

# # # # # # # # # # # # # # # # # # # # #         self.show_farmer_data()

# # # # # # # # # # # # # # # # # # # # #     def pay_farmer(self):
# # # # # # # # # # # # # # # # # # # # #         name = self.farmer_select.get()
# # # # # # # # # # # # # # # # # # # # #         if not name:
# # # # # # # # # # # # # # # # # # # # #             messagebox.showerror("خطأ", "اختر المزارع أولاً")
# # # # # # # # # # # # # # # # # # # # #             return

# # # # # # # # # # # # # # # # # # # # #         amount = int(self.pay_entry.get())
# # # # # # # # # # # # # # # # # # # # #         time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# # # # # # # # # # # # # # # # # # # # #         if amount > self.farmers[name]["balance"]:
# # # # # # # # # # # # # # # # # # # # #             messagebox.showerror("خطأ", "المبلغ أكبر من الرصيد")
# # # # # # # # # # # # # # # # # # # # #             return

# # # # # # # # # # # # # # # # # # # # #         self.farmers[name]["balance"] -= amount
# # # # # # # # # # # # # # # # # # # # #         self.farmers[name]["transactions"].append(("دفع", "-", "-", amount, time, self.farmers[name]["balance"]))

# # # # # # # # # # # # # # # # # # # # #         self.show_farmer_data()

# # # # # # # # # # # # # # # # # # # # #     def show_farmer_data(self, event=None):
# # # # # # # # # # # # # # # # # # # # #         name = self.farmer_select.get()
# # # # # # # # # # # # # # # # # # # # #         if not name:
# # # # # # # # # # # # # # # # # # # # #             return
# # # # # # # # # # # # # # # # # # # # #         # مسح الجدول
# # # # # # # # # # # # # # # # # # # # #         for row in self.tree.get_children():
# # # # # # # # # # # # # # # # # # # # #             self.tree.delete(row)
# # # # # # # # # # # # # # # # # # # # #         # عرض بيانات المزارع
# # # # # # # # # # # # # # # # # # # # #         for t in self.farmers[name]["transactions"]:
# # # # # # # # # # # # # # # # # # # # #             self.tree.insert("", "end", values=t)

            








# # # # # # # # # # # # # # # # # # # # # -*- coding: utf-8 -*-
# # # # # # # # # # # # # # # # # # # # import tkinter as tk
# # # # # # # # # # # # # # # # # # # # from tkinter import ttk, messagebox
# # # # # # # # # # # # # # # # # # # # import datetime

# # # # # # # # # # # # # # # # # # # # class FarmerAccountApp:
# # # # # # # # # # # # # # # # # # # #     def __init__(self, root):
# # # # # # # # # # # # # # # # # # # #         self.root = root
# # # # # # # # # # # # # # # # # # # #         self.root.title("دفتر حسابات تجارة القات")

# # # # # # # # # # # # # # # # # # # #         # قاعدة بيانات المزارعين
# # # # # # # # # # # # # # # # # # # #         self.farmers = {}

# # # # # # # # # # # # # # # # # # # #         # واجهة إدخال اسم المزارع
# # # # # # # # # # # # # # # # # # # #         self.name_label = tk.Label(root, text="اسم المزارع:")
# # # # # # # # # # # # # # # # # # # #         self.name_label.grid(row=0, column=0)
# # # # # # # # # # # # # # # # # # # #         self.name_entry = tk.Entry(root)
# # # # # # # # # # # # # # # # # # # #         self.name_entry.grid(row=0, column=1)

# # # # # # # # # # # # # # # # # # # #         self.add_farmer_button = tk.Button(root, text="إضافة مزارع جديد", command=self.add_farmer)
# # # # # # # # # # # # # # # # # # # #         self.add_farmer_button.grid(row=0, column=2)

# # # # # # # # # # # # # # # # # # # #         # قائمة اختيار المزارع
# # # # # # # # # # # # # # # # # # # #         self.select_label = tk.Label(root, text="اختر المزارع:")
# # # # # # # # # # # # # # # # # # # #         self.select_label.grid(row=1, column=0)
# # # # # # # # # # # # # # # # # # # #         self.farmer_select = ttk.Combobox(root, values=list(self.farmers.keys()))
# # # # # # # # # # # # # # # # # # # #         self.farmer_select.grid(row=1, column=1)
# # # # # # # # # # # # # # # # # # # #         self.farmer_select.bind("<<ComboboxSelected>>", self.show_farmer_data)

# # # # # # # # # # # # # # # # # # # #         # إدخال بيانات القات
# # # # # # # # # # # # # # # # # # # #         self.type_label = tk.Label(root, text="نوع القات:")
# # # # # # # # # # # # # # # # # # # #         self.type_label.grid(row=2, column=0)
# # # # # # # # # # # # # # # # # # # #         self.type_entry = tk.Entry(root)
# # # # # # # # # # # # # # # # # # # #         self.type_entry.grid(row=2, column=1)

# # # # # # # # # # # # # # # # # # # #         self.qty_label = tk.Label(root, text="عدد الحبات:")
# # # # # # # # # # # # # # # # # # # #         self.qty_label.grid(row=3, column=0)
# # # # # # # # # # # # # # # # # # # #         self.qty_entry = tk.Entry(root)
# # # # # # # # # # # # # # # # # # # #         self.qty_entry.grid(row=3, column=1)

# # # # # # # # # # # # # # # # # # # #         self.price_label = tk.Label(root, text="السعر للحبة:")
# # # # # # # # # # # # # # # # # # # #         self.price_label.grid(row=4, column=0)
# # # # # # # # # # # # # # # # # # # #         self.price_entry = tk.Entry(root)
# # # # # # # # # # # # # # # # # # # #         self.price_entry.grid(row=4, column=1)

# # # # # # # # # # # # # # # # # # # #         self.add_button = tk.Button(root, text="إضافة قات", command=self.add_qat)
# # # # # # # # # # # # # # # # # # # #         self.add_button.grid(row=5, column=0, columnspan=2)

# # # # # # # # # # # # # # # # # # # #         # إدخال الدفع
# # # # # # # # # # # # # # # # # # # #         self.pay_label = tk.Label(root, text="دفع للمزارع:")
# # # # # # # # # # # # # # # # # # # #         self.pay_label.grid(row=6, column=0)
# # # # # # # # # # # # # # # # # # # #         self.pay_entry = tk.Entry(root)
# # # # # # # # # # # # # # # # # # # #         self.pay_entry.grid(row=6, column=1)

# # # # # # # # # # # # # # # # # # # #         self.pay_button = tk.Button(root, text="دفع", command=self.pay_farmer)
# # # # # # # # # # # # # # # # # # # #         self.pay_button.grid(row=7, column=0, columnspan=2)

# # # # # # # # # # # # # # # # # # # #         # جدول عرض العمليات
# # # # # # # # # # # # # # # # # # # #         self.tree = ttk.Treeview(root, columns=("النوع","الكمية","السعر","الإجمالي","الوقت","الرصيد"), show="headings")
# # # # # # # # # # # # # # # # # # # #         self.tree.grid(row=8, column=0, columnspan=3)

# # # # # # # # # # # # # # # # # # # #         for col in ("النوع","الكمية","السعر","الإجمالي","الوقت","الرصيد"):
# # # # # # # # # # # # # # # # # # # #             self.tree.heading(col, text=col)

# # # # # # # # # # # # # # # # # # # #     def add_farmer(self):
# # # # # # # # # # # # # # # # # # # #         name = self.name_entry.get()
# # # # # # # # # # # # # # # # # # # #         if not name:
# # # # # # # # # # # # # # # # # # # #             messagebox.showerror("خطأ", "أدخل اسم المزارع")
# # # # # # # # # # # # # # # # # # # #             return
# # # # # # # # # # # # # # # # # # # #         if name in self.farmers:
# # # # # # # # # # # # # # # # # # # #             messagebox.showerror("خطأ", "المزارع موجود بالفعل")
# # # # # # # # # # # # # # # # # # # #             return
# # # # # # # # # # # # # # # # # # # #         self.farmers[name] = {"balance":0, "transactions":[]}
# # # # # # # # # # # # # # # # # # # #         self.farmer_select["values"] = list(self.farmers.keys())
# # # # # # # # # # # # # # # # # # # #         messagebox.showinfo("تم", f"تم إضافة المزارع {name}")

# # # # # # # # # # # # # # # # # # # #     def add_qat(self):
# # # # # # # # # # # # # # # # # # # #         try:
# # # # # # # # # # # # # # # # # # # #             name = self.farmer_select.get()
# # # # # # # # # # # # # # # # # # # #             if not name:
# # # # # # # # # # # # # # # # # # # #                 messagebox.showerror("خطأ", "اختر المزارع أولاً")
# # # # # # # # # # # # # # # # # # # #                 return

# # # # # # # # # # # # # # # # # # # #             qat_type = self.type_entry.get()
# # # # # # # # # # # # # # # # # # # #             qty = int(self.qty_entry.get())
# # # # # # # # # # # # # # # # # # # #             price = int(self.price_entry.get())
# # # # # # # # # # # # # # # # # # # #             total = qty * price
# # # # # # # # # # # # # # # # # # # #             time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# # # # # # # # # # # # # # # # # # # #             self.farmers[name]["balance"] += total
# # # # # # # # # # # # # # # # # # # #             self.farmers[name]["transactions"].append((qat_type, qty, price, total, time, self.farmers[name]["balance"]))

# # # # # # # # # # # # # # # # # # # #             self.show_farmer_data()
# # # # # # # # # # # # # # # # # # # #         except ValueError:
# # # # # # # # # # # # # # # # # # # #             messagebox.showerror("خطأ", "يرجى إدخال أرقام صحيحة في الكمية والسعر")

# # # # # # # # # # # # # # # # # # # #     def pay_farmer(self):
# # # # # # # # # # # # # # # # # # # #         try:
# # # # # # # # # # # # # # # # # # # #             name = self.farmer_select.get()
# # # # # # # # # # # # # # # # # # # #             if not name:
# # # # # # # # # # # # # # # # # # # #                 messagebox.showerror("خطأ", "اختر المزارع أولاً")
# # # # # # # # # # # # # # # # # # # #                 return

# # # # # # # # # # # # # # # # # # # #             amount = int(self.pay_entry.get())
# # # # # # # # # # # # # # # # # # # #             time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# # # # # # # # # # # # # # # # # # # #             if amount > self.farmers[name]["balance"]:
# # # # # # # # # # # # # # # # # # # #                 messagebox.showerror("خطأ", "المبلغ أكبر من الرصيد المتاح")
# # # # # # # # # # # # # # # # # # # #                 return

# # # # # # # # # # # # # # # # # # # #             self.farmers[name]["balance"] -= amount
# # # # # # # # # # # # # # # # # # # #             self.farmers[name]["transactions"].append(("دفع", "-", "-", amount, time, self.farmers[name]["balance"]))

# # # # # # # # # # # # # # # # # # # #             self.show_farmer_data()
# # # # # # # # # # # # # # # # # # # #         except ValueError:
# # # # # # # # # # # # # # # # # # # #             messagebox.showerror("خطأ", "يرجى إدخال رقم صحيح للمبلغ")

# # # # # # # # # # # # # # # # # # # #     def show_farmer_data(self, event=None):
# # # # # # # # # # # # # # # # # # # #         name = self.farmer_select.get()
# # # # # # # # # # # # # # # # # # # #         if not name:
# # # # # # # # # # # # # # # # # # # #             return
# # # # # # # # # # # # # # # # # # # #         # مسح الجدول
# # # # # # # # # # # # # # # # # # # #         for row in self.tree.get_children():
# # # # # # # # # # # # # # # # # # # #             self.tree.delete(row)
# # # # # # # # # # # # # # # # # # # #         # عرض بيانات المزارع
# # # # # # # # # # # # # # # # # # # #         for t in self.farmers[name]["transactions"]:
# # # # # # # # # # # # # # # # # # # #             self.tree.insert("", "end", values=t)

# # # # # # # # # # # # # # # # # # # # # --- تشغيل البرنامج ---
# # # # # # # # # # # # # # # # # # # # if __name__ == "__main__":
# # # # # # # # # # # # # # # # # # # #     root = tk.Tk()
# # # # # # # # # # # # # # # # # # # #     app = FarmerAccountApp(root)
# # # # # # # # # # # # # # # # # # # #     root.mainloop()







# # # # # # # # # # # # # # # # # # # import tkinter as tk
# # # # # # # # # # # # # # # # # # # from tkinter import ttk, messagebox
# # # # # # # # # # # # # # # # # # # import datetime

# # # # # # # # # # # # # # # # # # # class FarmerAccountApp:
# # # # # # # # # # # # # # # # # # #     def __init__(self, root):
# # # # # # # # # # # # # # # # # # #         self.root = root
# # # # # # # # # # # # # # # # # # #         self.root.title("دفتر حسابات تجارة القات")

# # # # # # # # # # # # # # # # # # #         # قاعدة بيانات المزارعين
# # # # # # # # # # # # # # # # # # #         self.farmers = {}

# # # # # # # # # # # # # # # # # # #         # إدخال اسم المزارع
# # # # # # # # # # # # # # # # # # #         self.name_label = tk.Label(root, text="اسم المزارع:")
# # # # # # # # # # # # # # # # # # #         self.name_label.grid(row=0, column=0)
# # # # # # # # # # # # # # # # # # #         self.name_entry = tk.Entry(root)
# # # # # # # # # # # # # # # # # # #         self.name_entry.grid(row=0, column=1)

# # # # # # # # # # # # # # # # # # #         self.add_farmer_button = tk.Button(root, text="إضافة مزارع جديد", command=self.add_farmer)
# # # # # # # # # # # # # # # # # # #         self.add_farmer_button.grid(row=0, column=2)

# # # # # # # # # # # # # # # # # # #         # قائمة اختيار المزارع
# # # # # # # # # # # # # # # # # # #         self.select_label = tk.Label(root, text="اختر المزارع:")
# # # # # # # # # # # # # # # # # # #         self.select_label.grid(row=1, column=0)
# # # # # # # # # # # # # # # # # # #         self.farmer_select = ttk.Combobox(root, values=list(self.farmers.keys()))
# # # # # # # # # # # # # # # # # # #         self.farmer_select.grid(row=1, column=1)

# # # # # # # # # # # # # # # # # # #         # زر إظهار بيانات المزارع
# # # # # # # # # # # # # # # # # # #         self.show_button = tk.Button(root, text="إظهار بيانات المزارع", command=self.show_farmer_data)
# # # # # # # # # # # # # # # # # # #         self.show_button.grid(row=1, column=2)

# # # # # # # # # # # # # # # # # # #         # إدخال بيانات القات
# # # # # # # # # # # # # # # # # # #         self.type_label = tk.Label(root, text="نوع القات:")
# # # # # # # # # # # # # # # # # # #         self.type_label.grid(row=2, column=0)
# # # # # # # # # # # # # # # # # # #         self.type_entry = tk.Entry(root)
# # # # # # # # # # # # # # # # # # #         self.type_entry.grid(row=2, column=1)

# # # # # # # # # # # # # # # # # # #         self.qty_label = tk.Label(root, text="عدد الحبات:")
# # # # # # # # # # # # # # # # # # #         self.qty_label.grid(row=3, column=0)
# # # # # # # # # # # # # # # # # # #         self.qty_entry = tk.Entry(root)
# # # # # # # # # # # # # # # # # # #         self.qty_entry.grid(row=3, column=1)

# # # # # # # # # # # # # # # # # # #         self.price_label = tk.Label(root, text="السعر للحبة:")
# # # # # # # # # # # # # # # # # # #         self.price_label.grid(row=4, column=0)
# # # # # # # # # # # # # # # # # # #         self.price_entry = tk.Entry(root)
# # # # # # # # # # # # # # # # # # #         self.price_entry.grid(row=4, column=1)

# # # # # # # # # # # # # # # # # # #         self.add_button = tk.Button(root, text="إضافة قات", command=self.add_qat)
# # # # # # # # # # # # # # # # # # #         self.add_button.grid(row=5, column=0, columnspan=2)

# # # # # # # # # # # # # # # # # # #         # إدخال الدفع
# # # # # # # # # # # # # # # # # # #         self.pay_label = tk.Label(root, text="دفع للمزارع:")
# # # # # # # # # # # # # # # # # # #         self.pay_label.grid(row=6, column=0)
# # # # # # # # # # # # # # # # # # #         self.pay_entry = tk.Entry(root)
# # # # # # # # # # # # # # # # # # #         self.pay_entry.grid(row=6, column=1)

# # # # # # # # # # # # # # # # # # #         self.pay_button = tk.Button(root, text="دفع", command=self.pay_farmer)
# # # # # # # # # # # # # # # # # # #         self.pay_button.grid(row=7, column=0, columnspan=2)

# # # # # # # # # # # # # # # # # # #         # جدول عرض العمليات
# # # # # # # # # # # # # # # # # # #         self.tree = ttk.Treeview(root, columns=("النوع","الكمية","السعر","الإجمالي","الوقت","الرصيد"), show="headings")
# # # # # # # # # # # # # # # # # # #         self.tree.grid(row=8, column=0, columnspan=3)

# # # # # # # # # # # # # # # # # # #         for col in ("النوع","الكمية","السعر","الإجمالي","الوقت","الرصيد"):
# # # # # # # # # # # # # # # # # # #             self.tree.heading(col, text=col)

# # # # # # # # # # # # # # # # # # #     def add_farmer(self):
# # # # # # # # # # # # # # # # # # #         name = self.name_entry.get()
# # # # # # # # # # # # # # # # # # #         if not name:
# # # # # # # # # # # # # # # # # # #             messagebox.showerror("خطأ", "أدخل اسم المزارع")
# # # # # # # # # # # # # # # # # # #             return
# # # # # # # # # # # # # # # # # # #         if name in self.farmers:
# # # # # # # # # # # # # # # # # # #             messagebox.showerror("خطأ", "المزارع موجود بالفعل")
# # # # # # # # # # # # # # # # # # #             return
# # # # # # # # # # # # # # # # # # #         self.farmers[name] = {"balance":0, "transactions":[]}
# # # # # # # # # # # # # # # # # # #         self.farmer_select["values"] = list(self.farmers.keys())
# # # # # # # # # # # # # # # # # # #         messagebox.showinfo("تم", f"تم إضافة المزارع {name}")

# # # # # # # # # # # # # # # # # # #     def add_qat(self):
# # # # # # # # # # # # # # # # # # #         name = self.farmer_select.get()
# # # # # # # # # # # # # # # # # # #         if not name:
# # # # # # # # # # # # # # # # # # #             messagebox.showerror("خطأ", "اختر المزارع أولاً")
# # # # # # # # # # # # # # # # # # #             return

# # # # # # # # # # # # # # # # # # #         qat_type = self.type_entry.get()
# # # # # # # # # # # # # # # # # # #         qty = int(self.qty_entry.get())
# # # # # # # # # # # # # # # # # # #         price = int(self.price_entry.get())
# # # # # # # # # # # # # # # # # # #         total = qty * price
# # # # # # # # # # # # # # # # # # #         time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# # # # # # # # # # # # # # # # # # #         self.farmers[name]["balance"] += total
# # # # # # # # # # # # # # # # # # #         self.farmers[name]["transactions"].append((qat_type, qty, price, total, time, self.farmers[name]["balance"]))

# # # # # # # # # # # # # # # # # # #         self.show_farmer_data()

# # # # # # # # # # # # # # # # # # #     def pay_farmer(self):
# # # # # # # # # # # # # # # # # # #         name = self.farmer_select.get()
# # # # # # # # # # # # # # # # # # #         if not name:
# # # # # # # # # # # # # # # # # # #             messagebox.showerror("خطأ", "اختر المزارع أولاً")
# # # # # # # # # # # # # # # # # # #             return

# # # # # # # # # # # # # # # # # # #         amount = int(self.pay_entry.get())
# # # # # # # # # # # # # # # # # # #         time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# # # # # # # # # # # # # # # # # # #         if amount > self.farmers[name]["balance"]:
# # # # # # # # # # # # # # # # # # #             messagebox.showerror("خطأ", "المبلغ أكبر من الرصيد")
# # # # # # # # # # # # # # # # # # #             return

# # # # # # # # # # # # # # # # # # #         self.farmers[name]["balance"] -= amount
# # # # # # # # # # # # # # # # # # #         self.farmers[name]["transactions"].append(("دفع", "-", "-", amount, time, self.farmers[name]["balance"]))

# # # # # # # # # # # # # # # # # # #         self.show_farmer_data()

# # # # # # # # # # # # # # # # # # #     def show_farmer_data(self):
# # # # # # # # # # # # # # # # # # #         name = self.farmer_select.get()
# # # # # # # # # # # # # # # # # # #         if not name:
# # # # # # # # # # # # # # # # # # #             messagebox.showerror("خطأ", "اختر المزارع أولاً")
# # # # # # # # # # # # # # # # # # #             return

# # # # # # # # # # # # # # # # # # #         # مسح الجدول
# # # # # # # # # # # # # # # # # # #         for row in self.tree.get_children():
# # # # # # # # # # # # # # # # # # #             self.tree.delete(row)

# # # # # # # # # # # # # # # # # # #         # عرض بيانات المزارع
# # # # # # # # # # # # # # # # # # #         for t in self.farmers[name]["transactions"]:
# # # # # # # # # # # # # # # # # # #             self.tree.insert("", "end", values=t)

# # # # # # # # # # # # # # # # # # #         # إظهار الرصيد في رسالة
# # # # # # # # # # # # # # # # # # #         balance = self.farmers[name]["balance"]
# # # # # # # # # # # # # # # # # # #         messagebox.showinfo("بيانات المزارع", f"📌 المزارع: {name}\n💰 الرصيد الحالي: {balance} ريال")

# # # # # # # # # # # # # # # # # # #         # # --- تشغيل البرنامج ---
# # # # # # # # # # # # # # # # # # # if __name__ == "__main__":
# # # # # # # # # # # # # # # # # # #     root = tk.Tk()
# # # # # # # # # # # # # # # # # # #     app = FarmerAccountApp(root)
# # # # # # # # # # # # # # # # # # #     root.mainloop()




# # # # # # # # # # # # # # # # # # import tkinter as tk
# # # # # # # # # # # # # # # # # # from tkinter import ttk, messagebox
# # # # # # # # # # # # # # # # # # import datetime

# # # # # # # # # # # # # # # # # # class FarmerAccountApp:
# # # # # # # # # # # # # # # # # #     def __init__(self, root):
# # # # # # # # # # # # # # # # # #         self.root = root
# # # # # # # # # # # # # # # # # #         self.root.title("دفتر حسابات تجارة القات")

# # # # # # # # # # # # # # # # # #         # قاعدة بيانات المزارعين
# # # # # # # # # # # # # # # # # #         self.farmers = {}

# # # # # # # # # # # # # # # # # #         # إدخال اسم المزارع
# # # # # # # # # # # # # # # # # #         self.name_label = tk.Label(root, text="اسم المزارع:")
# # # # # # # # # # # # # # # # # #         self.name_label.grid(row=0, column=0)
# # # # # # # # # # # # # # # # # #         self.name_entry = tk.Entry(root)
# # # # # # # # # # # # # # # # # #         self.name_entry.grid(row=0, column=1)

# # # # # # # # # # # # # # # # # #         self.add_farmer_button = tk.Button(root, text="إضافة مزارع جديد", command=self.add_farmer)
# # # # # # # # # # # # # # # # # #         self.add_farmer_button.grid(row=0, column=2)

# # # # # # # # # # # # # # # # # #         # قائمة اختيار المزارع
# # # # # # # # # # # # # # # # # #         self.select_label = tk.Label(root, text="اختر المزارع:")
# # # # # # # # # # # # # # # # # #         self.select_label.grid(row=1, column=0)
# # # # # # # # # # # # # # # # # #         self.farmer_select = ttk.Combobox(root, values=list(self.farmers.keys()))
# # # # # # # # # # # # # # # # # #         self.farmer_select.grid(row=1, column=1)

# # # # # # # # # # # # # # # # # #         self.show_button = tk.Button(root, text="إظهار بيانات المزارع", command=self.show_farmer_data)
# # # # # # # # # # # # # # # # # #         self.show_button.grid(row=1, column=2)

# # # # # # # # # # # # # # # # # #         # إدخال بيانات القات
# # # # # # # # # # # # # # # # # #         self.type_label = tk.Label(root, text="نوع القات (روس/نقفة/عوارض):")
# # # # # # # # # # # # # # # # # #         self.type_label.grid(row=2, column=0)
# # # # # # # # # # # # # # # # # #         self.type_entry = tk.Entry(root)
# # # # # # # # # # # # # # # # # #         self.type_entry.grid(row=2, column=1)

# # # # # # # # # # # # # # # # # #         self.qty_label = tk.Label(root, text="عدد الحبات:")
# # # # # # # # # # # # # # # # # #         self.qty_label.grid(row=3, column=0)
# # # # # # # # # # # # # # # # # #         self.qty_entry = tk.Entry(root)
# # # # # # # # # # # # # # # # # #         self.qty_entry.grid(row=3, column=1)

# # # # # # # # # # # # # # # # # #         self.price_label = tk.Label(root, text="السعر للحبة:")
# # # # # # # # # # # # # # # # # #         self.price_label.grid(row=4, column=0)
# # # # # # # # # # # # # # # # # #         self.price_entry = tk.Entry(root)
# # # # # # # # # # # # # # # # # #         self.price_entry.grid(row=4, column=1)

# # # # # # # # # # # # # # # # # #         self.add_button = tk.Button(root, text="إضافة قات", command=self.add_qat)
# # # # # # # # # # # # # # # # # #         self.add_button.grid(row=5, column=0, columnspan=2)

# # # # # # # # # # # # # # # # # #         # إدخال الدفع
# # # # # # # # # # # # # # # # # #         self.pay_label = tk.Label(root, text="دفع للمزارع:")
# # # # # # # # # # # # # # # # # #         self.pay_label.grid(row=6, column=0)
# # # # # # # # # # # # # # # # # #         self.pay_entry = tk.Entry(root)
# # # # # # # # # # # # # # # # # #         self.pay_entry.grid(row=6, column=1)

# # # # # # # # # # # # # # # # # #         self.pay_button = tk.Button(root, text="دفع", command=self.pay_farmer)
# # # # # # # # # # # # # # # # # #         self.pay_button.grid(row=7, column=0, columnspan=2)

# # # # # # # # # # # # # # # # # #         # جدول عرض العمليات
# # # # # # # # # # # # # # # # # #         self.tree = ttk.Treeview(root, columns=("الرصيد","الوقت","الإجمالي","السعر","الكمية","النوع"), show="headings")
# # # # # # # # # # # # # # # # # #         self.tree.grid(row=8, column=0, columnspan=3)

# # # # # # # # # # # # # # # # # #         for col in ("الرصيد","الوقت","الإجمالي","السعر","الكمية","النوع"):
# # # # # # # # # # # # # # # # # #             self.tree.heading(col, text=col)
# # # # # # # # # # # # # # # # # #             self.tree.column(col, width=100)

# # # # # # # # # # # # # # # # # #     def add_farmer(self):
# # # # # # # # # # # # # # # # # #         name = self.name_entry.get()
# # # # # # # # # # # # # # # # # #         if not name:
# # # # # # # # # # # # # # # # # #             messagebox.showerror("خطأ", "أدخل اسم المزارع")
# # # # # # # # # # # # # # # # # #             return
# # # # # # # # # # # # # # # # # #         if name in self.farmers:
# # # # # # # # # # # # # # # # # #             messagebox.showerror("خطأ", "المزارع موجود بالفعل")
# # # # # # # # # # # # # # # # # #             return
# # # # # # # # # # # # # # # # # #         self.farmers[name] = {"balance":0, "transactions":[]}
# # # # # # # # # # # # # # # # # #         self.farmer_select["values"] = list(self.farmers.keys())
# # # # # # # # # # # # # # # # # #         messagebox.showinfo("تم", f"تم إضافة المزارع {name}")

# # # # # # # # # # # # # # # # # #     def add_qat(self):
# # # # # # # # # # # # # # # # # #         name = self.farmer_select.get()
# # # # # # # # # # # # # # # # # #         if not name:
# # # # # # # # # # # # # # # # # #             messagebox.showerror("خطأ", "اختر المزارع أولاً")
# # # # # # # # # # # # # # # # # #             return

# # # # # # # # # # # # # # # # # #         qat_type = self.type_entry.get()
# # # # # # # # # # # # # # # # # #         qty = int(self.qty_entry.get())
# # # # # # # # # # # # # # # # # #         price = int(self.price_entry.get())
# # # # # # # # # # # # # # # # # #         total = qty * price
# # # # # # # # # # # # # # # # # #         time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# # # # # # # # # # # # # # # # # #         self.farmers[name]["balance"] += total
# # # # # # # # # # # # # # # # # #         self.farmers[name]["transactions"].append((self.farmers[name]["balance"], time, total, price, qty, qat_type))

# # # # # # # # # # # # # # # # # #         self.show_farmer_data()

# # # # # # # # # # # # # # # # # #     def pay_farmer(self):
# # # # # # # # # # # # # # # # # #         name = self.farmer_select.get()
# # # # # # # # # # # # # # # # # #         if not name:
# # # # # # # # # # # # # # # # # #             messagebox.showerror("خطأ", "اختر المزارع أولاً")
# # # # # # # # # # # # # # # # # #             return

# # # # # # # # # # # # # # # # # #         amount = int(self.pay_entry.get())
# # # # # # # # # # # # # # # # # #         time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# # # # # # # # # # # # # # # # # #         if amount > self.farmers[name]["balance"]:
# # # # # # # # # # # # # # # # # #             messagebox.showerror("خطأ", "المبلغ أكبر من الرصيد")
# # # # # # # # # # # # # # # # # #             return

# # # # # # # # # # # # # # # # # #         self.farmers[name]["balance"] -= amount
# # # # # # # # # # # # # # # # # #         self.farmers[name]["transactions"].append((self.farmers[name]["balance"], time, amount, "-", "-", "دفع"))

# # # # # # # # # # # # # # # # # #         self.show_farmer_data()

# # # # # # # # # # # # # # # # # #     def show_farmer_data(self):
# # # # # # # # # # # # # # # # # #         name = self.farmer_select.get()
# # # # # # # # # # # # # # # # # #         if not name:
# # # # # # # # # # # # # # # # # #             return
# # # # # # # # # # # # # # # # # #         # مسح الجدول
# # # # # # # # # # # # # # # # # #         for row in self.tree.get_children():
# # # # # # # # # # # # # # # # # #             self.tree.delete(row)
# # # # # # # # # # # # # # # # # #         # عرض بيانات المزارع
# # # # # # # # # # # # # # # # # #         for t in self.farmers[name]["transactions"]:
# # # # # # # # # # # # # # # # # #             self.tree.insert("", "end", values=t)







# # # # # # # # # # # # # # # # # import tkinter as tk
# # # # # # # # # # # # # # # # # from tkinter import ttk, messagebox
# # # # # # # # # # # # # # # # # import datetime

# # # # # # # # # # # # # # # # # class FarmerAccountApp:
# # # # # # # # # # # # # # # # #     def __init__(self, root):
# # # # # # # # # # # # # # # # #         self.root = root
# # # # # # # # # # # # # # # # #         self.root.title("دفتر حسابات تجارة القات")

# # # # # # # # # # # # # # # # #         # قاعدة بيانات المزارعين
# # # # # # # # # # # # # # # # #         self.farmers = {}

# # # # # # # # # # # # # # # # #         # إدخال اسم المزارع
# # # # # # # # # # # # # # # # #         tk.Label(root, text="اسم المزارع:").grid(row=0, column=0)
# # # # # # # # # # # # # # # # #         self.name_entry = tk.Entry(root)
# # # # # # # # # # # # # # # # #         self.name_entry.grid(row=0, column=1)

# # # # # # # # # # # # # # # # #         tk.Button(root, text="إضافة مزارع جديد", command=self.add_farmer).grid(row=0, column=2)

# # # # # # # # # # # # # # # # #         # قائمة اختيار المزارع
# # # # # # # # # # # # # # # # #         tk.Label(root, text="اختر المزارع:").grid(row=1, column=0)
# # # # # # # # # # # # # # # # #         self.farmer_select = ttk.Combobox(root, values=list(self.farmers.keys()))
# # # # # # # # # # # # # # # # #         self.farmer_select.grid(row=1, column=1)

# # # # # # # # # # # # # # # # #         tk.Button(root, text="إظهار بيانات المزارع", command=self.show_farmer_data).grid(row=1, column=2)

# # # # # # # # # # # # # # # # #         # إدخال بيانات القات
# # # # # # # # # # # # # # # # #         tk.Label(root, text="نوع القات:").grid(row=2, column=0)
# # # # # # # # # # # # # # # # #         self.type_combo = ttk.Combobox(root, values=["روس", "نقفة", "عوارض"], state="readonly")
# # # # # # # # # # # # # # # # #         self.type_combo.grid(row=2, column=1)

# # # # # # # # # # # # # # # # #         tk.Label(root, text="عدد الحبات:").grid(row=3, column=0)
# # # # # # # # # # # # # # # # #         self.qty_entry = tk.Entry(root)
# # # # # # # # # # # # # # # # #         self.qty_entry.grid(row=3, column=1)

# # # # # # # # # # # # # # # # #         tk.Label(root, text="السعر للحبة:").grid(row=4, column=0)
# # # # # # # # # # # # # # # # #         self.price_entry = tk.Entry(root)
# # # # # # # # # # # # # # # # #         self.price_entry.grid(row=4, column=1)

# # # # # # # # # # # # # # # # #         tk.Button(root, text="إضافة قات", command=self.add_qat).grid(row=5, column=0, columnspan=2)

# # # # # # # # # # # # # # # # #         # إدخال الدفع
# # # # # # # # # # # # # # # # #         tk.Label(root, text="دفع للمزارع:").grid(row=6, column=0)
# # # # # # # # # # # # # # # # #         self.pay_entry = tk.Entry(root)
# # # # # # # # # # # # # # # # #         self.pay_entry.grid(row=6, column=1)

# # # # # # # # # # # # # # # # #         tk.Button(root, text="دفع", command=self.pay_farmer).grid(row=7, column=0, columnspan=2)

# # # # # # # # # # # # # # # # #         # جدول عرض العمليات (أعمدة وصفوف)
# # # # # # # # # # # # # # # # #         self.tree = ttk.Treeview(root, columns=("الرصيد","الوقت","الإجمالي","السعر","الكمية","النوع"), show="headings")
# # # # # # # # # # # # # # # # #         self.tree.grid(row=8, column=0, columnspan=3)

# # # # # # # # # # # # # # # # #         for col in ("الرصيد","الوقت","الإجمالي","السعر","الكمية","النوع"):
# # # # # # # # # # # # # # # # #             self.tree.heading(col, text=col)
# # # # # # # # # # # # # # # # #             self.tree.column(col, width=100)

# # # # # # # # # # # # # # # # #     def add_farmer(self):
# # # # # # # # # # # # # # # # #         name = self.name_entry.get()
# # # # # # # # # # # # # # # # #         if not name:
# # # # # # # # # # # # # # # # #             messagebox.showerror("خطأ", "أدخل اسم المزارع")
# # # # # # # # # # # # # # # # #             return
# # # # # # # # # # # # # # # # #         if name in self.farmers:
# # # # # # # # # # # # # # # # #             messagebox.showerror("خطأ", "المزارع موجود بالفعل")
# # # # # # # # # # # # # # # # #             return
# # # # # # # # # # # # # # # # #         self.farmers[name] = {"balance":0, "transactions":[]}
# # # # # # # # # # # # # # # # #         self.farmer_select["values"] = list(self.farmers.keys())
# # # # # # # # # # # # # # # # #         messagebox.showinfo("تم", f"تم إضافة المزارع {name}")

# # # # # # # # # # # # # # # # #     def add_qat(self):
# # # # # # # # # # # # # # # # #         name = self.farmer_select.get()
# # # # # # # # # # # # # # # # #         if not name:
# # # # # # # # # # # # # # # # #             messagebox.showerror("خطأ", "اختر المزارع أولاً")
# # # # # # # # # # # # # # # # #             return

# # # # # # # # # # # # # # # # #         qat_type = self.type_combo.get()
# # # # # # # # # # # # # # # # #         qty = int(self.qty_entry.get())
# # # # # # # # # # # # # # # # #         price = int(self.price_entry.get())
# # # # # # # # # # # # # # # # #         total = qty * price
# # # # # # # # # # # # # # # # #         time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# # # # # # # # # # # # # # # # #         self.farmers[name]["balance"] += total
# # # # # # # # # # # # # # # # #         self.farmers[name]["transactions"].append((self.farmers[name]["balance"], time, total, price, qty, qat_type))

# # # # # # # # # # # # # # # # #         self.show_farmer_data()

# # # # # # # # # # # # # # # # #     def pay_farmer(self):
# # # # # # # # # # # # # # # # #         name = self.farmer_select.get()
# # # # # # # # # # # # # # # # #         if not name:
# # # # # # # # # # # # # # # # #             messagebox.showerror("خطأ", "اختر المزارع أولاً")
# # # # # # # # # # # # # # # # #             return

# # # # # # # # # # # # # # # # #         amount = int(self.pay_entry.get())
# # # # # # # # # # # # # # # # #         time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# # # # # # # # # # # # # # # # #         if amount > self.farmers[name]["balance"]:
# # # # # # # # # # # # # # # # #             messagebox.showerror("خطأ", "المبلغ أكبر من الرصيد")
# # # # # # # # # # # # # # # # #             return

# # # # # # # # # # # # # # # # #         self.farmers[name]["balance"] -= amount
# # # # # # # # # # # # # # # # #         self.farmers[name]["transactions"].append((self.farmers[name]["balance"], time, amount, "-", "-", "دفع"))

# # # # # # # # # # # # # # # # #         self.show_farmer_data()

# # # # # # # # # # # # # # # # #     def show_farmer_data(self):
# # # # # # # # # # # # # # # # #         name = self.farmer_select.get()
# # # # # # # # # # # # # # # # #         if not name:
# # # # # # # # # # # # # # # # #             return
# # # # # # # # # # # # # # # # #         # مسح الجدول
# # # # # # # # # # # # # # # # #         for row in self.tree.get_children():
# # # # # # # # # # # # # # # # #             self.tree.delete(row)
# # # # # # # # # # # # # # # # #         # عرض بيانات المزارع
# # # # # # # # # # # # # # # # #         for t in self.farmers[name]["transactions"]:
# # # # # # # # # # # # # # # # #             self.tree.insert("", "end", values=t)


# # # # # # # # # # # # # # # # # # تشغيل البرنامج
# # # # # # # # # # # # # # # # # root = tk.Tk()
# # # # # # # # # # # # # # # # # app = FarmerAccountApp(root)
# # # # # # # # # # # # # # # # # root.mainloop()


# # # # # # # # # # # # # # # # # #             #         # # --- تشغيل البرنامج ---
# # # # # # # # # # # # # # # # # # if __name__ == "__main__":
# # # # # # # # # # # # # # # # # #     root = tk.Tk()
# # # # # # # # # # # # # # # # # #     app = FarmerAccountApp(root)
# # # # # # # # # # # # # # # # # #     root.mainloop()














# # # # # # # # # # # # # # # # import tkinter as tk
# # # # # # # # # # # # # # # # from tkinter import ttk, messagebox
# # # # # # # # # # # # # # # # import datetime

# # # # # # # # # # # # # # # # class FarmerAccountApp:
# # # # # # # # # # # # # # # #     def __init__(self, root):
# # # # # # # # # # # # # # # #         self.root = root
# # # # # # # # # # # # # # # #         self.root.title("دفتر حسابات تجارة القات")

# # # # # # # # # # # # # # # #         # قاعدة بيانات المزارعين
# # # # # # # # # # # # # # # #         self.farmers = {}

# # # # # # # # # # # # # # # #         # إدخال اسم المزارع
# # # # # # # # # # # # # # # #         tk.Label(root, text="اسم المزارع:").grid(row=0, column=0)
# # # # # # # # # # # # # # # #         self.name_entry = tk.Entry(root)
# # # # # # # # # # # # # # # #         self.name_entry.grid(row=0, column=1)

# # # # # # # # # # # # # # # #         tk.Button(root, text="إضافة مزارع جديد", command=self.add_farmer).grid(row=0, column=2)

# # # # # # # # # # # # # # # #         # قائمة اختيار المزارع
# # # # # # # # # # # # # # # #         tk.Label(root, text="اختر المزارع:").grid(row=1, column=0)
# # # # # # # # # # # # # # # #         self.farmer_select = ttk.Combobox(root, values=list(self.farmers.keys()))
# # # # # # # # # # # # # # # #         self.farmer_select.grid(row=1, column=1)

# # # # # # # # # # # # # # # #         tk.Button(root, text="إظهار بيانات المزارع", command=self.show_farmer_data).grid(row=1, column=2)

# # # # # # # # # # # # # # # #         # إدخال بيانات القات
# # # # # # # # # # # # # # # #         tk.Label(root, text="نوع القات:").grid(row=2, column=0)
# # # # # # # # # # # # # # # #         self.type_combo = ttk.Combobox(root, values=["روس", "نقفة", "عوارض"], state="readonly")
# # # # # # # # # # # # # # # #         self.type_combo.grid(row=2, column=1)

# # # # # # # # # # # # # # # #         tk.Label(root, text="عدد الحبات:").grid(row=3, column=0)
# # # # # # # # # # # # # # # #         self.qty_entry = tk.Entry(root)
# # # # # # # # # # # # # # # #         self.qty_entry.grid(row=3, column=1)

# # # # # # # # # # # # # # # #         tk.Label(root, text="السعر للحبة:").grid(row=4, column=0)
# # # # # # # # # # # # # # # #         self.price_entry = tk.Entry(root)
# # # # # # # # # # # # # # # #         self.price_entry.grid(row=4, column=1)

# # # # # # # # # # # # # # # #         tk.Button(root, text="إضافة قات", command=self.add_qat).grid(row=5, column=0, columnspan=2)

# # # # # # # # # # # # # # # #         # إدخال الدفع
# # # # # # # # # # # # # # # #         tk.Label(root, text="دفع للمزارع:").grid(row=6, column=0)
# # # # # # # # # # # # # # # #         self.pay_entry = tk.Entry(root)
# # # # # # # # # # # # # # # #         self.pay_entry.grid(row=6, column=1)

# # # # # # # # # # # # # # # #         tk.Button(root, text="دفع", command=self.pay_farmer).grid(row=7, column=0, columnspan=2)

# # # # # # # # # # # # # # # #         # جدول عرض العمليات (أعمدة وصفوف)
# # # # # # # # # # # # # # # #         self.tree = ttk.Treeview(root, 
# # # # # # # # # # # # # # # #                                  columns=("الرصيد","الوقت","الإجمالي","السعر","الكمية","النوع"), 
# # # # # # # # # # # # # # # #                                  show="headings", height=10)
# # # # # # # # # # # # # # # #         self.tree.grid(row=8, column=0, columnspan=3, pady=10)

# # # # # # # # # # # # # # # #         # ضبط الأعمدة
# # # # # # # # # # # # # # # #         self.tree.heading("الرصيد", text="الرصيد")
# # # # # # # # # # # # # # # #         self.tree.heading("الوقت", text="الوقت")
# # # # # # # # # # # # # # # #         self.tree.heading("الإجمالي", text="الإجمالي")
# # # # # # # # # # # # # # # #         self.tree.heading("السعر", text="السعر للحبة")
# # # # # # # # # # # # # # # #         self.tree.heading("الكمية", text="الكمية")
# # # # # # # # # # # # # # # #         self.tree.heading("النوع", text="النوع")

# # # # # # # # # # # # # # # #         self.tree.column("الرصيد", width=100, anchor="center")
# # # # # # # # # # # # # # # #         self.tree.column("الوقت", width=150, anchor="center")
# # # # # # # # # # # # # # # #         self.tree.column("الإجمالي", width=100, anchor="center")
# # # # # # # # # # # # # # # #         self.tree.column("السعر", width=100, anchor="center")
# # # # # # # # # # # # # # # #         self.tree.column("الكمية", width=80, anchor="center")
# # # # # # # # # # # # # # # #         self.tree.column("النوع", width=100, anchor="center")

# # # # # # # # # # # # # # # #     def add_farmer(self):
# # # # # # # # # # # # # # # #         name = self.name_entry.get()
# # # # # # # # # # # # # # # #         if not name:
# # # # # # # # # # # # # # # #             messagebox.showerror("خطأ", "أدخل اسم المزارع")
# # # # # # # # # # # # # # # #             return
# # # # # # # # # # # # # # # #         if name in self.farmers:
# # # # # # # # # # # # # # # #             messagebox.showerror("خطأ", "المزارع موجود بالفعل")
# # # # # # # # # # # # # # # #             return
# # # # # # # # # # # # # # # #         self.farmers[name] = {"balance":0, "transactions":[]}
# # # # # # # # # # # # # # # #         self.farmer_select["values"] = list(self.farmers.keys())
# # # # # # # # # # # # # # # #         messagebox.showinfo("تم", f"تم إضافة المزارع {name}")

# # # # # # # # # # # # # # # #     def add_qat(self):
# # # # # # # # # # # # # # # #         name = self.farmer_select.get()
# # # # # # # # # # # # # # # #         if not name:
# # # # # # # # # # # # # # # #             messagebox.showerror("خطأ", "اختر المزارع أولاً")
# # # # # # # # # # # # # # # #             return

# # # # # # # # # # # # # # # #         qat_type = self.type_combo.get()
# # # # # # # # # # # # # # # #         qty = int(self.qty_entry.get())
# # # # # # # # # # # # # # # #         price = int(self.price_entry.get())
# # # # # # # # # # # # # # # #         total = qty * price
# # # # # # # # # # # # # # # #         time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# # # # # # # # # # # # # # # #         self.farmers[name]["balance"] += total
# # # # # # # # # # # # # # # #         self.farmers[name]["transactions"].append((self.farmers[name]["balance"], time, total, price, qty, qat_type))

# # # # # # # # # # # # # # # #         self.show_farmer_data()

# # # # # # # # # # # # # # # #     def pay_farmer(self):
# # # # # # # # # # # # # # # #         name = self.farmer_select.get()
# # # # # # # # # # # # # # # #         if not name:
# # # # # # # # # # # # # # # #             messagebox.showerror("خطأ", "اختر المزارع أولاً")
# # # # # # # # # # # # # # # #             return

# # # # # # # # # # # # # # # #         amount = int(self.pay_entry.get())
# # # # # # # # # # # # # # # #         time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# # # # # # # # # # # # # # # #         if amount > self.farmers[name]["balance"]:
# # # # # # # # # # # # # # # #             messagebox.showerror("خطأ", "المبلغ أكبر من الرصيد")
# # # # # # # # # # # # # # # #             return

# # # # # # # # # # # # # # # #         self.farmers[name]["balance"] -= amount
# # # # # # # # # # # # # # # #         self.farmers[name]["transactions"].append((self.farmers[name]["balance"], time, amount, "-", "-", "دفع"))

# # # # # # # # # # # # # # # #         self.show_farmer_data()

# # # # # # # # # # # # # # # #     def show_farmer_data(self):
# # # # # # # # # # # # # # # #         name = self.farmer_select.get()
# # # # # # # # # # # # # # # #         if not name:
# # # # # # # # # # # # # # # #             return
# # # # # # # # # # # # # # # #         # مسح الجدول
# # # # # # # # # # # # # # # #         for row in self.tree.get_children():
# # # # # # # # # # # # # # # #             self.tree.delete(row)
# # # # # # # # # # # # # # # #         # عرض بيانات المزارع
# # # # # # # # # # # # # # # #         for t in self.farmers[name]["transactions"]:
# # # # # # # # # # # # # # # #             self.tree.insert("", "end", values=t)


# # # # # # # # # # # # # # # # # تشغيل البرنامج
# # # # # # # # # # # # # # # # root = tk.Tk()
# # # # # # # # # # # # # # # # app = FarmerAccountApp(root)
# # # # # # # # # # # # # # # # root.mainloop()








# # # # # # # # # # # # # # # import tkinter as tk
# # # # # # # # # # # # # # # from tkinter import ttk, messagebox
# # # # # # # # # # # # # # # import datetime

# # # # # # # # # # # # # # # class FarmerAccountApp:
# # # # # # # # # # # # # # #     def __init__(self, root):
# # # # # # # # # # # # # # #         self.root = root
# # # # # # # # # # # # # # #         self.root.title("دفتر حسابات تجارة القات")

# # # # # # # # # # # # # # #         # قاعدة بيانات المزارعين
# # # # # # # # # # # # # # #         self.farmers = {}

# # # # # # # # # # # # # # #         # إدخال اسم المزارع
# # # # # # # # # # # # # # #         tk.Label(root, text="اسم المزارع:").grid(row=0, column=0)
# # # # # # # # # # # # # # #         self.name_entry = tk.Entry(root)
# # # # # # # # # # # # # # #         self.name_entry.grid(row=0, column=1)

# # # # # # # # # # # # # # #         tk.Button(root, text="إضافة مزارع جديد", command=self.add_farmer).grid(row=0, column=2)

# # # # # # # # # # # # # # #         # قائمة اختيار المزارع
# # # # # # # # # # # # # # #         tk.Label(root, text="اختر المزارع:").grid(row=1, column=0)
# # # # # # # # # # # # # # #         self.farmer_select = ttk.Combobox(root, values=list(self.farmers.keys()))
# # # # # # # # # # # # # # #         self.farmer_select.grid(row=1, column=1)

# # # # # # # # # # # # # # #         tk.Button(root, text="إظهار بيانات المزارع", command=self.show_farmer_data).grid(row=1, column=2)

# # # # # # # # # # # # # # #         # إدخال بيانات القات
# # # # # # # # # # # # # # #         tk.Label(root, text="نوع القات:").grid(row=2, column=0)
# # # # # # # # # # # # # # #         self.type_combo = ttk.Combobox(root, values=["روس", "نقفة", "عوارض"], state="readonly")
# # # # # # # # # # # # # # #         self.type_combo.grid(row=2, column=1)

# # # # # # # # # # # # # # #         tk.Label(root, text="عدد الحبات:").grid(row=3, column=0)
# # # # # # # # # # # # # # #         self.qty_entry = tk.Entry(root)
# # # # # # # # # # # # # # #         self.qty_entry.grid(row=3, column=1)

# # # # # # # # # # # # # # #         tk.Label(root, text="السعر للحبة:").grid(row=4, column=0)
# # # # # # # # # # # # # # #         self.price_entry = tk.Entry(root)
# # # # # # # # # # # # # # #         self.price_entry.grid(row=4, column=1)

# # # # # # # # # # # # # # #         tk.Button(root, text="إضافة قات", command=self.add_qat).grid(row=5, column=0, columnspan=2)

# # # # # # # # # # # # # # #         # إدخال الدفع
# # # # # # # # # # # # # # #         tk.Label(root, text="دفع للمزارع:").grid(row=6, column=0)
# # # # # # # # # # # # # # #         self.pay_entry = tk.Entry(root)
# # # # # # # # # # # # # # #         self.pay_entry.grid(row=6, column=1)

# # # # # # # # # # # # # # #         tk.Button(root, text="دفع", command=self.pay_farmer).grid(row=7, column=0, columnspan=2)

# # # # # # # # # # # # # # #         # جدول عرض العمليات (أعمدة وصفوف مثل إكسل)
# # # # # # # # # # # # # # #         self.tree = ttk.Treeview(root, 
# # # # # # # # # # # # # # #                                  columns=("الرصيد","الوقت","الإجمالي","السعر","روس","نقفة","عوارض"), 
# # # # # # # # # # # # # # #                                  show="headings", height=12)
# # # # # # # # # # # # # # #         self.tree.grid(row=8, column=0, columnspan=3, pady=10)

# # # # # # # # # # # # # # #         # ضبط الأعمدة
# # # # # # # # # # # # # # #         for col in ("الرصيد","الوقت","الإجمالي","السعر","روس","نقفة","عوارض"):
# # # # # # # # # # # # # # #             self.tree.heading(col, text=col)
# # # # # # # # # # # # # # #             self.tree.column(col, width=100, anchor="center")

# # # # # # # # # # # # # # #     def add_farmer(self):
# # # # # # # # # # # # # # #         name = self.name_entry.get()
# # # # # # # # # # # # # # #         if not name:
# # # # # # # # # # # # # # #             messagebox.showerror("خطأ", "أدخل اسم المزارع")
# # # # # # # # # # # # # # #             return
# # # # # # # # # # # # # # #         if name in self.farmers:
# # # # # # # # # # # # # # #             messagebox.showerror("خطأ", "المزارع موجود بالفعل")
# # # # # # # # # # # # # # #             return
# # # # # # # # # # # # # # #         self.farmers[name] = {"balance":0, "transactions":[]}
# # # # # # # # # # # # # # #         self.farmer_select["values"] = list(self.farmers.keys())
# # # # # # # # # # # # # # #         messagebox.showinfo("تم", f"تم إضافة المزارع {name}")

# # # # # # # # # # # # # # #     def add_qat(self):
# # # # # # # # # # # # # # #         name = self.farmer_select.get()
# # # # # # # # # # # # # # #         if not name:
# # # # # # # # # # # # # # #             messagebox.showerror("خطأ", "اختر المزارع أولاً")
# # # # # # # # # # # # # # #             return

# # # # # # # # # # # # # # #         qat_type = self.type_combo.get()
# # # # # # # # # # # # # # #         qty = int(self.qty_entry.get())
# # # # # # # # # # # # # # #         price = int(self.price_entry.get())
# # # # # # # # # # # # # # #         total = qty * price
# # # # # # # # # # # # # # #         time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# # # # # # # # # # # # # # #         self.farmers[name]["balance"] += total

# # # # # # # # # # # # # # #         # توزيع الكمية على العمود المناسب
# # # # # # # # # # # # # # #         ros = qty if qat_type == "روس" else ""
# # # # # # # # # # # # # # #         naqfa = qty if qat_type == "نقفة" else ""
# # # # # # # # # # # # # # #         awarid = qty if qat_type == "عوارض" else ""

# # # # # # # # # # # # # # #         self.farmers[name]["transactions"].append((self.farmers[name]["balance"], time, total, price, ros, naqfa, awarid))

# # # # # # # # # # # # # # #         self.show_farmer_data()

# # # # # # # # # # # # # # #     def pay_farmer(self):
# # # # # # # # # # # # # # #         name = self.farmer_select.get()
# # # # # # # # # # # # # # #         if not name:
# # # # # # # # # # # # # # #             messagebox.showerror("خطأ", "اختر المزارع أولاً")
# # # # # # # # # # # # # # #             return

# # # # # # # # # # # # # # #         amount = int(self.pay_entry.get())
# # # # # # # # # # # # # # #         time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# # # # # # # # # # # # # # #         if amount > self.farmers[name]["balance"]:
# # # # # # # # # # # # # # #             messagebox.showerror("خطأ", "المبلغ أكبر من الرصيد")
# # # # # # # # # # # # # # #             return

# # # # # # # # # # # # # # #         self.farmers[name]["balance"] -= amount
# # # # # # # # # # # # # # #         # عملية دفع بدون نوع قات
# # # # # # # # # # # # # # #         self.farmers[name]["transactions"].append((self.farmers[name]["balance"], time, amount, "-", "", "", ""))

# # # # # # # # # # # # # # #         self.show_farmer_data()

# # # # # # # # # # # # # # #     def show_farmer_data(self):
# # # # # # # # # # # # # # #         name = self.farmer_select.get()
# # # # # # # # # # # # # # #         if not name:
# # # # # # # # # # # # # # #             return
# # # # # # # # # # # # # # #         # مسح الجدول
# # # # # # # # # # # # # # #         for row in self.tree.get_children():
# # # # # # # # # # # # # # #             self.tree.delete(row)
# # # # # # # # # # # # # # #         # عرض بيانات المزارع
# # # # # # # # # # # # # # #         for t in self.farmers[name]["transactions"]:
# # # # # # # # # # # # # # #             self.tree.insert("", "end", values=t)


# # # # # # # # # # # # # # # # تشغيل البرنامج
# # # # # # # # # # # # # # # root = tk.Tk()
# # # # # # # # # # # # # # # app = FarmerAccountApp(root)
# # # # # # # # # # # # # # # root.mainloop()











# # # # # # # # # # # # # # import tkinter as tk
# # # # # # # # # # # # # # from tkinter import ttk, messagebox
# # # # # # # # # # # # # # import datetime

# # # # # # # # # # # # # # class FarmerAccountApp:
# # # # # # # # # # # # # #     def __init__(self, root):
# # # # # # # # # # # # # #         self.root = root
# # # # # # # # # # # # # #         self.root.title("دفتر حسابات تجارة القات")

# # # # # # # # # # # # # #         # قاعدة بيانات المزارعين
# # # # # # # # # # # # # #         self.farmers = {}

# # # # # # # # # # # # # #         # إدخال اسم المزارع
# # # # # # # # # # # # # #         tk.Label(root, text="اسم المزارع:").grid(row=0, column=0)
# # # # # # # # # # # # # #         self.name_entry = tk.Entry(root)
# # # # # # # # # # # # # #         self.name_entry.grid(row=0, column=1)

# # # # # # # # # # # # # #         tk.Button(root, text="إضافة مزارع جديد", command=self.add_farmer).grid(row=0, column=2)

# # # # # # # # # # # # # #         # قائمة اختيار المزارع
# # # # # # # # # # # # # #         tk.Label(root, text="اختر المزارع:").grid(row=1, column=0)
# # # # # # # # # # # # # #         self.farmer_select = ttk.Combobox(root, values=list(self.farmers.keys()))
# # # # # # # # # # # # # #         self.farmer_select.grid(row=1, column=1)

# # # # # # # # # # # # # #         tk.Button(root, text="إظهار بيانات المزارع", command=self.show_farmer_data).grid(row=1, column=2)

# # # # # # # # # # # # # #         # إدخال بيانات القات
# # # # # # # # # # # # # #         tk.Label(root, text="نوع القات:").grid(row=2, column=0)
# # # # # # # # # # # # # #         self.type_combo = ttk.Combobox(root, values=["روس", "نقفة", "عوارض"], state="readonly")
# # # # # # # # # # # # # #         self.type_combo.grid(row=2, column=1)

# # # # # # # # # # # # # #         tk.Label(root, text="عدد الحبات:").grid(row=3, column=0)
# # # # # # # # # # # # # #         self.qty_entry = tk.Entry(root)
# # # # # # # # # # # # # #         self.qty_entry.grid(row=3, column=1)

# # # # # # # # # # # # # #         tk.Label(root, text="السعر للحبة:").grid(row=4, column=0)
# # # # # # # # # # # # # #         self.price_entry = tk.Entry(root)
# # # # # # # # # # # # # #         self.price_entry.grid(row=4, column=1)

# # # # # # # # # # # # # #         tk.Button(root, text="إضافة قات", command=self.add_qat).grid(row=5, column=0, columnspan=2)

# # # # # # # # # # # # # #         # إدخال الدفع
# # # # # # # # # # # # # #         tk.Label(root, text="دفع للمزارع:").grid(row=6, column=0)
# # # # # # # # # # # # # #         self.pay_entry = tk.Entry(root)
# # # # # # # # # # # # # #         self.pay_entry.grid(row=6, column=1)

# # # # # # # # # # # # # #         tk.Button(root, text="دفع", command=self.pay_farmer).grid(row=7, column=0, columnspan=2)

# # # # # # # # # # # # # #         # جدول عرض العمليات (أعمدة وصفوف مثل إكسل)
# # # # # # # # # # # # # #         self.tree = ttk.Treeview(root, 
# # # # # # # # # # # # # #                                  columns=("الرصيد","الوقت","الإجمالي","السعر","روس","نقفة","عوارض"), 
# # # # # # # # # # # # # #                                  show="headings", height=12)
# # # # # # # # # # # # # #         self.tree.grid(row=8, column=0, columnspan=3, pady=10)

# # # # # # # # # # # # # #         # ضبط الأعمدة
# # # # # # # # # # # # # #         self.tree.heading("الرصيد", text="الرصيد")
# # # # # # # # # # # # # #         self.tree.heading("الوقت", text="الوقت")
# # # # # # # # # # # # # #         self.tree.heading("الإجمالي", text="الإجمالي")
# # # # # # # # # # # # # #         self.tree.heading("السعر", text="السعر للحبة")
# # # # # # # # # # # # # #         self.tree.heading("روس", text="روس")
# # # # # # # # # # # # # #         self.tree.heading("نقفة", text="نقفة")
# # # # # # # # # # # # # #         self.tree.heading("عوارض", text="عوارض")

# # # # # # # # # # # # # #         for col in ("الرصيد","الوقت","الإجمالي","السعر","روس","نقفة","عوارض"):
# # # # # # # # # # # # # #             self.tree.column(col, width=100, anchor="center")

# # # # # # # # # # # # # #     def add_farmer(self):
# # # # # # # # # # # # # #         name = self.name_entry.get()
# # # # # # # # # # # # # #         if not name:
# # # # # # # # # # # # # #             messagebox.showerror("خطأ", "أدخل اسم المزارع")
# # # # # # # # # # # # # #             return
# # # # # # # # # # # # # #         if name in self.farmers:
# # # # # # # # # # # # # #             messagebox.showerror("خطأ", "المزارع موجود بالفعل")
# # # # # # # # # # # # # #             return
# # # # # # # # # # # # # #         self.farmers[name] = {"balance":0, "transactions":[]}
# # # # # # # # # # # # # #         self.farmer_select["values"] = list(self.farmers.keys())
# # # # # # # # # # # # # #         messagebox.showinfo("تم", f"تم إضافة المزارع {name}")

# # # # # # # # # # # # # #     def add_qat(self):
# # # # # # # # # # # # # #         name = self.farmer_select.get()
# # # # # # # # # # # # # #         if not name:
# # # # # # # # # # # # # #             messagebox.showerror("خطأ", "اختر المزارع أولاً")
# # # # # # # # # # # # # #             return

# # # # # # # # # # # # # #         qat_type = self.type_combo.get()
# # # # # # # # # # # # # #         qty = int(self.qty_entry.get())
# # # # # # # # # # # # # #         price = int(self.price_entry.get())
# # # # # # # # # # # # # #         total = qty * price
# # # # # # # # # # # # # #         time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# # # # # # # # # # # # # #         self.farmers[name]["balance"] += total

# # # # # # # # # # # # # #         # توزيع الكمية على العمود المناسب
# # # # # # # # # # # # # #         ros = qty if qat_type == "روس" else ""
# # # # # # # # # # # # # #         naqfa = qty if qat_type == "نقفة" else ""
# # # # # # # # # # # # # #         awarid = qty if qat_type == "عوارض" else ""

# # # # # # # # # # # # # #         self.farmers[name]["transactions"].append((self.farmers[name]["balance"], time, total, price, ros, naqfa, awarid))

# # # # # # # # # # # # # #         self.show_farmer_data()

# # # # # # # # # # # # # #     def pay_farmer(self):
# # # # # # # # # # # # # #         name = self.farmer_select.get()
# # # # # # # # # # # # # #         if not name:
# # # # # # # # # # # # # #             messagebox.showerror("خطأ", "اختر المزارع أولاً")
# # # # # # # # # # # # # #             return

# # # # # # # # # # # # # #         amount = int(self.pay_entry.get())
# # # # # # # # # # # # # #         time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# # # # # # # # # # # # # #         if amount > self.farmers[name]["balance"]:
# # # # # # # # # # # # # #             messagebox.showerror("خطأ", "المبلغ أكبر من الرصيد")
# # # # # # # # # # # # # #             return

# # # # # # # # # # # # # #         self.farmers[name]["balance"] -= amount
# # # # # # # # # # # # # #         # عملية دفع بدون نوع قات
# # # # # # # # # # # # # #         self.farmers[name]["transactions"].append((self.farmers[name]["balance"], time, amount, "-", "", "", ""))

# # # # # # # # # # # # # #         self.show_farmer_data()

# # # # # # # # # # # # # #     def show_farmer_data(self):
# # # # # # # # # # # # # #         name = self.farmer_select.get()
# # # # # # # # # # # # # #         if not name:
# # # # # # # # # # # # # #             return
# # # # # # # # # # # # # #         # مسح الجدول
# # # # # # # # # # # # # #         for row in self.tree.get_children():
# # # # # # # # # # # # # #             self.tree.delete(row)
# # # # # # # # # # # # # #         # عرض بيانات المزارع
# # # # # # # # # # # # # #         for t in self.farmers[name]["transactions"]:
# # # # # # # # # # # # # #             self.tree.insert("", "end", values=t)


# # # # # # # # # # # # # # # تشغيل البرنامج
# # # # # # # # # # # # # # root = tk.Tk()
# # # # # # # # # # # # # # app = FarmerAccountApp(root)
# # # # # # # # # # # # # # root.mainloop()




# # # # # # # # # # # # # # -*- coding: utf-8 -*-
# # # # # # # # # # # # # import tkinter as tk
# # # # # # # # # # # # # from tkinter import ttk, messagebox
# # # # # # # # # # # # # import datetime

# # # # # # # # # # # # # class FarmerAccountApp:
# # # # # # # # # # # # #     def __init__(self, root):
# # # # # # # # # # # # #         self.root = root
# # # # # # # # # # # # #         self.root.title("دفتر حسابات تجارة القات")
        
# # # # # # # # # # # # #         # --- إضافة لمسة الإكسل (الخطوط والحدود) ---
# # # # # # # # # # # # #         style = ttk.Style()
# # # # # # # # # # # # #         style.theme_use("clam")  # استخدام ثيم يسمح برسم الحدود
# # # # # # # # # # # # #         style.configure("Treeview", 
# # # # # # # # # # # # #                         background="white", 
# # # # # # # # # # # # #                         foreground="black", 
# # # # # # # # # # # # #                         rowheight=25, 
# # # # # # # # # # # # #                         fieldbackground="white",
# # # # # # # # # # # # #                         borderwidth=1)
# # # # # # # # # # # # #         style.map("Treeview", background=[('selected', '#347083')])
# # # # # # # # # # # # #         # جعل العناوين تبدو بارزة
# # # # # # # # # # # # #         style.configure("Treeview.Heading", font=('Arial', 10, 'bold'))

# # # # # # # # # # # # #         # قاعدة بيانات المزارعين
# # # # # # # # # # # # #         self.farmers = {}

# # # # # # # # # # # # #         # إدخال اسم المزارع
# # # # # # # # # # # # #         tk.Label(root, text="اسم المزارع:").grid(row=0, column=0, padx=5, pady=5)
# # # # # # # # # # # # #         self.name_entry = tk.Entry(root)
# # # # # # # # # # # # #         self.name_entry.grid(row=0, column=1)
# # # # # # # # # # # # #         tk.Button(root, text="إضافة مزارع جديد", command=self.add_farmer).grid(row=0, column=2, padx=5)

# # # # # # # # # # # # #         # قائمة اختيار المزارع
# # # # # # # # # # # # #         tk.Label(root, text="اختر المزارع:").grid(row=1, column=0)
# # # # # # # # # # # # #         self.farmer_select = ttk.Combobox(root, values=list(self.farmers.keys()), state="readonly")
# # # # # # # # # # # # #         self.farmer_select.grid(row=1, column=1)
# # # # # # # # # # # # #         tk.Button(root, text="إظهار البيانات", command=self.show_farmer_data).grid(row=1, column=2)

# # # # # # # # # # # # #         # إدخال بيانات القات
# # # # # # # # # # # # #         tk.Label(root, text="نوع القات:").grid(row=2, column=0)
# # # # # # # # # # # # #         self.type_combo = ttk.Combobox(root, values=["روس", "نقفة", "عوارض"], state="readonly")
# # # # # # # # # # # # #         self.type_combo.grid(row=2, column=1)

# # # # # # # # # # # # #         tk.Label(root, text="عدد الحبات:").grid(row=3, column=0)
# # # # # # # # # # # # #         self.qty_entry = tk.Entry(root)
# # # # # # # # # # # # #         self.qty_entry.grid(row=3, column=1)

# # # # # # # # # # # # #         tk.Label(root, text="السعر للحبة:").grid(row=4, column=0)
# # # # # # # # # # # # #         self.price_entry = tk.Entry(root)
# # # # # # # # # # # # #         self.price_entry.grid(row=4, column=1)

# # # # # # # # # # # # #         tk.Button(root, text="إضافة قات", command=self.add_qat, bg="#e1f5fe").grid(row=5, column=0, columnspan=2, pady=5, sticky="nsew")

# # # # # # # # # # # # #         # إدخال الدفع
# # # # # # # # # # # # #         tk.Label(root, text="دفع للمزارع:").grid(row=6, column=0)
# # # # # # # # # # # # #         self.pay_entry = tk.Entry(root)
# # # # # # # # # # # # #         self.pay_entry.grid(row=6, column=1)
# # # # # # # # # # # # #         tk.Button(root, text="تأكيد الدفع", command=self.pay_farmer, bg="#ffebee").grid(row=7, column=0, columnspan=2, pady=5, sticky="nsew")

# # # # # # # # # # # # #         # --- الجدول (Treeview) مع تفعيل الخطوط ---
# # # # # # # # # # # # #         self.tree = ttk.Treeview(root, 
# # # # # # # # # # # # #                                  columns=("الرصيد","الوقت","الإجمالي","السعر","روس","نقفة","عوارض"), 
# # # # # # # # # # # # #                                  show="headings", height=15)
# # # # # # # # # # # # #         self.tree.grid(row=8, column=0, columnspan=3, pady=10, padx=10)

# # # # # # # # # # # # #         # ضبط العناوين والحدود لكل عمود
# # # # # # # # # # # # #         for col in ("الرصيد","الوقت","الإجمالي","السعر","روس","نقفة","عوارض"):
# # # # # # # # # # # # #             self.tree.heading(col, text=col)
# # # # # # # # # # # # #             self.tree.column(col, width=110, anchor="center")

# # # # # # # # # # # # #     def add_farmer(self):
# # # # # # # # # # # # #         name = self.name_entry.get()
# # # # # # # # # # # # #         if name and name not in self.farmers:
# # # # # # # # # # # # #             self.farmers[name] = {"balance":0, "transactions":[]}
# # # # # # # # # # # # #             self.farmer_select["values"] = list(self.farmers.keys())
# # # # # # # # # # # # #             messagebox.showinfo("تم", f"تمت إضافة {name}")
# # # # # # # # # # # # #         else:
# # # # # # # # # # # # #             messagebox.showwarning("تنبيه", "الاسم فارغ أو موجود مسبقاً")

# # # # # # # # # # # # #     def add_qat(self):
# # # # # # # # # # # # #         try:
# # # # # # # # # # # # #             name = self.farmer_select.get()
# # # # # # # # # # # # #             if not name: return
            
# # # # # # # # # # # # #             qty = int(self.qty_entry.get())
# # # # # # # # # # # # #             price = int(self.price_entry.get())
# # # # # # # # # # # # #             qat_type = self.type_combo.get()
# # # # # # # # # # # # #             total = qty * price
# # # # # # # # # # # # #             time = datetime.datetime.now().strftime("%H:%M %Y-%m-%d")
            
# # # # # # # # # # # # #             self.farmers[name]["balance"] += total
            
# # # # # # # # # # # # #             ros = qty if qat_type == "روس" else ""
# # # # # # # # # # # # #             naqfa = qty if qat_type == "نقفة" else ""
# # # # # # # # # # # # #             awarid = qty if qat_type == "عوارض" else ""
            
# # # # # # # # # # # # #             # إضافة الصف
# # # # # # # # # # # # #             self.farmers[name]["transactions"].append((self.farmers[name]["balance"], time, total, price, ros, naqfa, awarid))
# # # # # # # # # # # # #             self.show_farmer_data()
# # # # # # # # # # # # #         except:
# # # # # # # # # # # # #             messagebox.showerror("خطأ", "تأكد من إدخال الأرقام بشكل صحيح")

# # # # # # # # # # # # #     def pay_farmer(self):
# # # # # # # # # # # # #         try:
# # # # # # # # # # # # #             name = self.farmer_select.get()
# # # # # # # # # # # # #             amount = int(self.pay_entry.get())
# # # # # # # # # # # # #             if amount > self.farmers[name]["balance"]:
# # # # # # # # # # # # #                 messagebox.showwarning("تنبيه", "المبلغ أكبر من الرصيد")
# # # # # # # # # # # # #                 return
            
# # # # # # # # # # # # #             self.farmers[name]["balance"] -= amount
# # # # # # # # # # # # #             time = datetime.datetime.now().strftime("%H:%M %Y-%m-%d")
# # # # # # # # # # # # #             self.farmers[name]["transactions"].append((self.farmers[name]["balance"], time, f"-{amount}", "دفع", "", "", ""))
# # # # # # # # # # # # #             self.show_farmer_data()
# # # # # # # # # # # # #         except:
# # # # # # # # # # # # #             messagebox.showerror("خطأ", "أدخل مبلغاً صحيحاً")

# # # # # # # # # # # # #     def show_farmer_data(self):
# # # # # # # # # # # # #         name = self.farmer_select.get()
# # # # # # # # # # # # #         for row in self.tree.get_children():
# # # # # # # # # # # # #             self.tree.delete(row)
# # # # # # # # # # # # #         for t in self.farmers[name]["transactions"]:
# # # # # # # # # # # # #             self.tree.insert("", "end", values=t)

# # # # # # # # # # # # # if __name__ == "__main__":
# # # # # # # # # # # # #     root = tk.Tk()
# # # # # # # # # # # # #     app = FarmerAccountApp(root)
# # # # # # # # # # # # #     root.mainloop()












# # # # # # # # # # # # # -*- coding: utf-8 -*-
# # # # # # # # # # # # import tkinter as tk
# # # # # # # # # # # # from tkinter import ttk, messagebox
# # # # # # # # # # # # import datetime
# # # # # # # # # # # # import speech_recognition as sr

# # # # # # # # # # # # class FarmerAccountApp:
# # # # # # # # # # # #     def __init__(self, root):
# # # # # # # # # # # #         self.root = root
# # # # # # # # # # # #         self.root.title("دفتر حسابات تجارة القات - النسخة الصوتية")
        
# # # # # # # # # # # #         # تحسين المظهر (Style)
# # # # # # # # # # # #         style = ttk.Style()
# # # # # # # # # # # #         style.theme_use("clam")
# # # # # # # # # # # #         style.configure("Treeview", rowheight=25, borderwidth=1)
# # # # # # # # # # # #         style.configure("Treeview.Heading", font=('Arial', 10, 'bold'))

# # # # # # # # # # # #         self.farmers = {}

# # # # # # # # # # # #         # صف إدخال الاسم
# # # # # # # # # # # #         tk.Label(root, text="اسم المزارع:").grid(row=0, column=0, padx=5, pady=5)
# # # # # # # # # # # #         self.name_entry = tk.Entry(root)
# # # # # # # # # # # #         self.name_entry.grid(row=0, column=1)
# # # # # # # # # # # #         # زر الصوت للاسم
# # # # # # # # # # # #         tk.Button(root, text="🎤", command=lambda: self.listen_voice(self.name_entry)).grid(row=0, column=2)
# # # # # # # # # # # #         tk.Button(root, text="إضافة مزارع", command=self.add_farmer).grid(row=0, column=3, padx=5)

# # # # # # # # # # # #         # اختيار المزارع
# # # # # # # # # # # #         tk.Label(root, text="اختر المزارع:").grid(row=1, column=0)
# # # # # # # # # # # #         self.farmer_select = ttk.Combobox(root, state="readonly")
# # # # # # # # # # # #         self.farmer_select.grid(row=1, column=1)

# # # # # # # # # # # #         # نوع القات
# # # # # # # # # # # #         tk.Label(root, text="نوع القات:").grid(row=2, column=0)
# # # # # # # # # # # #         self.type_combo = ttk.Combobox(root, values=["روس", "نقفة", "عوارض"], state="readonly")
# # # # # # # # # # # #         self.type_combo.grid(row=2, column=1)

# # # # # # # # # # # #         # العدد والسعر مع أزرار صوت
# # # # # # # # # # # #         tk.Label(root, text="عدد الحبات:").grid(row=3, column=0)
# # # # # # # # # # # #         self.qty_entry = tk.Entry(root)
# # # # # # # # # # # #         self.qty_entry.grid(row=3, column=1)
# # # # # # # # # # # #         tk.Button(root, text="🎤", command=lambda: self.listen_voice(self.qty_entry)).grid(row=3, column=2)

# # # # # # # # # # # #         tk.Label(root, text="السعر للحبة:").grid(row=4, column=0)
# # # # # # # # # # # #         self.price_entry = tk.Entry(root)
# # # # # # # # # # # #         self.price_entry.grid(row=4, column=1)
# # # # # # # # # # # #         tk.Button(root, text="🎤", command=lambda: self.listen_voice(self.price_entry)).grid(row=4, column=2)

# # # # # # # # # # # #         tk.Button(root, text="إضافة فاتورة (قات)", command=self.add_qat, bg="#d4edda").grid(row=5, column=0, columnspan=2, pady=5, sticky="ew")

# # # # # # # # # # # #         # الجدول
# # # # # # # # # # # #         self.tree = ttk.Treeview(root, columns=("الرصيد","الوقت","الإجمالي","السعر","روس","نقفة","عوارض"), show="headings", height=10)
# # # # # # # # # # # #         self.tree.grid(row=8, column=0, columnspan=4, pady=10, padx=10)
# # # # # # # # # # # #         for col in ("الرصيد","الوقت","الإجمالي","السعر","روس","نقفة","عوارض"):
# # # # # # # # # # # #             self.tree.heading(col, text=col)
# # # # # # # # # # # #             self.tree.column(col, width=90, anchor="center")

# # # # # # # # # # # #     def listen_voice(self, entry_widget):
# # # # # # # # # # # #         r = sr.Recognizer()
# # # # # # # # # # # #         with sr.Microphone() as source:
# # # # # # # # # # # #             self.root.title("جاري الاستماع... تكلم الآن")
# # # # # # # # # # # #             try:
# # # # # # # # # # # #                 audio = r.listen(source, timeout=3)
# # # # # # # # # # # #                 text = r.recognize_google(audio, language='ar-SA')
# # # # # # # # # # # #                 # تنظيف النص (إذا نطق أرقاماً بالعربي يحولها لأرقام نصية)
# # # # # # # # # # # #                 entry_widget.delete(0, tk.END)
# # # # # # # # # # # #                 entry_widget.insert(0, text)
# # # # # # # # # # # #             except:
# # # # # # # # # # # #                 messagebox.showwarning("تنبيه", "لم أسمعك جيداً")
# # # # # # # # # # # #             finally:
# # # # # # # # # # # #                 self.root.title("دفتر حسابات تجارة القات")

# # # # # # # # # # # #     def add_farmer(self):
# # # # # # # # # # # #         name = self.name_entry.get()
# # # # # # # # # # # #         if name and name not in self.farmers:
# # # # # # # # # # # #             self.farmers[name] = {"balance":0, "transactions":[]}
# # # # # # # # # # # #             self.update_combo()
# # # # # # # # # # # #             messagebox.showinfo("تم", f"المزارع: {name} جاهز")

# # # # # # # # # # # #     def update_combo(self):
# # # # # # # # # # # #         self.farmer_select["values"] = list(self.farmers.keys())

# # # # # # # # # # # #     def add_qat(self):
# # # # # # # # # # # #         try:
# # # # # # # # # # # #             name = self.farmer_select.get()
# # # # # # # # # # # #             qty = int(self.qty_entry.get())
# # # # # # # # # # # #             price = int(self.price_entry.get())
# # # # # # # # # # # #             total = qty * price
# # # # # # # # # # # #             self.farmers[name]["balance"] += total
# # # # # # # # # # # #             res = (self.farmers[name]["balance"], "الآن", total, price, qty if self.type_combo.get()=="روس" else "", "", "")
# # # # # # # # # # # #             self.farmers[name]["transactions"].append(res)
# # # # # # # # # # # #             self.show_data()
# # # # # # # # # # # #         except:
# # # # # # # # # # # #             messagebox.showerror("خطأ", "تأكد من اختيار المزارع وإدخال أرقام")

# # # # # # # # # # # #     def show_data(self):
# # # # # # # # # # # #         name = self.farmer_select.get()
# # # # # # # # # # # #         for r in self.tree.get_children(): self.tree.delete(r)
# # # # # # # # # # # #         for t in self.farmers[name]["transactions"]: self.tree.insert("", "end", values=t)

# # # # # # # # # # # # if __name__ == "__main__":
# # # # # # # # # # # #     root = tk.Tk()
# # # # # # # # # # # #     app = FarmerAccountApp(root)
# # # # # # # # # # # #     root.mainloop()






# # # # # # # # # # # import speech_recognition as sr
# # # # # # # # # # # import tkinter as tk
# # # # # # # # # # # from tkinter import ttk, messagebox
# # # # # # # # # # # import datetime

# # # # # # # # # # # class FarmerAccountApp:
# # # # # # # # # # #     def __init__(self, root):
# # # # # # # # # # #         self.root = root
# # # # # # # # # # #         self.root.title("دفتر حسابات تجارة القات بالصوت")

# # # # # # # # # # #         self.farmers = {}

# # # # # # # # # # #         # زر لإضافة مزارع بالصوت
# # # # # # # # # # #         tk.Button(root, text="🎤 إضافة مزارع بالصوت", command=self.add_farmer_voice).grid(row=0, column=0)

# # # # # # # # # # #         # زر لطلب بيانات مزارع بالصوت
# # # # # # # # # # #         tk.Button(root, text="🎤 طلب بيانات مزارع بالصوت", command=self.show_farmer_voice).grid(row=0, column=1)

# # # # # # # # # # #         # جدول عرض العمليات
# # # # # # # # # # #         self.tree = ttk.Treeview(root, 
# # # # # # # # # # #                                  columns=("الرصيد","الوقت","الإجمالي","السعر","روس","نقفة","عوارض"), 
# # # # # # # # # # #                                  show="headings", height=12)
# # # # # # # # # # #         self.tree.grid(row=1, column=0, columnspan=2, pady=10)

# # # # # # # # # # #         for col in ("الرصيد","الوقت","الإجمالي","السعر","روس","نقفة","عوارض"):
# # # # # # # # # # #             self.tree.heading(col, text=col)
# # # # # # # # # # #             self.tree.column(col, width=100, anchor="center")

# # # # # # # # # # #     def listen_voice(self):
# # # # # # # # # # #         """التقاط الصوت وتحويله إلى نص"""
# # # # # # # # # # #         r = sr.Recognizer()
# # # # # # # # # # #         with sr.Microphone() as source:
# # # # # # # # # # #             print("🎤 تكلم الآن...")
# # # # # # # # # # #             audio = r.listen(source)
# # # # # # # # # # #         try:
# # # # # # # # # # #             text = r.recognize_google(audio, language="ar")
# # # # # # # # # # #             print("✅ النص:", text)
# # # # # # # # # # #             return text
# # # # # # # # # # #         except:
# # # # # # # # # # #             messagebox.showerror("خطأ", "لم أتمكن من فهم الصوت")
# # # # # # # # # # #             return ""

# # # # # # # # # # #     def add_farmer_voice(self):
# # # # # # # # # # #         name = self.listen_voice()
# # # # # # # # # # #         if name:
# # # # # # # # # # #             if name in self.farmers:
# # # # # # # # # # #                 messagebox.showerror("خطأ", "المزارع موجود بالفعل")
# # # # # # # # # # #             else:
# # # # # # # # # # #                 self.farmers[name] = {"balance":0, "transactions":[]}
# # # # # # # # # # #                 messagebox.showinfo("تم", f"تم إضافة المزارع {name}")

# # # # # # # # # # #     def show_farmer_voice(self):
# # # # # # # # # # #         name = self.listen_voice()
# # # # # # # # # # #         if name and name in self.farmers:
# # # # # # # # # # #             # مسح الجدول
# # # # # # # # # # #             for row in self.tree.get_children():
# # # # # # # # # # #                 self.tree.delete(row)
# # # # # # # # # # #             # عرض بيانات المزارع
# # # # # # # # # # #             for t in self.farmers[name]["transactions"]:
# # # # # # # # # # #                 self.tree.insert("", "end", values=t)
# # # # # # # # # # #             messagebox.showinfo("بيانات المزارع", f"📌 المزارع: {name}\n💰 الرصيد الحالي: {self.farmers[name]['balance']} ريال")
# # # # # # # # # # #         else:
# # # # # # # # # # #             messagebox.showerror("خطأ", "المزارع غير موجود")
            
# # # # # # # # # # # if __name__ == "__main__":
# # # # # # # # # # #     root = tk.Tk()
# # # # # # # # # # #     app = FarmerAccountApp(root)
# # # # # # # # # # #     root.mainloop()












# # # # # # # # # # import tkinter as tk
# # # # # # # # # # from tkinter import ttk, messagebox
# # # # # # # # # # import datetime
# # # # # # # # # # import speech_recognition as sr

# # # # # # # # # # class FarmerAccountApp:
# # # # # # # # # #     def __init__(self, root):
# # # # # # # # # #         self.root = root
# # # # # # # # # #         self.root.title("دفتر حسابات تجارة القات بالصوت")

# # # # # # # # # #         # قاعدة بيانات المزارعين
# # # # # # # # # #         self.farmers = {}

# # # # # # # # # #         # إدخال اسم المزارع
# # # # # # # # # #         tk.Label(root, text="اسم المزارع:").grid(row=0, column=0)
# # # # # # # # # #         self.name_entry = tk.Entry(root)
# # # # # # # # # #         self.name_entry.grid(row=0, column=1)

# # # # # # # # # #         tk.Button(root, text="إضافة مزارع جديد", command=self.add_farmer).grid(row=0, column=2)
# # # # # # # # # #         tk.Button(root, text="🎤 إضافة مزارع بالصوت", command=self.add_farmer_voice).grid(row=0, column=3)

# # # # # # # # # #         # قائمة اختيار المزارع
# # # # # # # # # #         tk.Label(root, text="اختر المزارع:").grid(row=1, column=0)
# # # # # # # # # #         self.farmer_select = ttk.Combobox(root, values=list(self.farmers.keys()))
# # # # # # # # # #         self.farmer_select.grid(row=1, column=1)

# # # # # # # # # #         tk.Button(root, text="إظهار بيانات المزارع", command=self.show_farmer_data).grid(row=1, column=2)
# # # # # # # # # #         tk.Button(root, text="🎤 طلب بيانات بالصوت", command=self.show_farmer_voice).grid(row=1, column=3)

# # # # # # # # # #         # إدخال بيانات القات
# # # # # # # # # #         tk.Label(root, text="نوع القات:").grid(row=2, column=0)
# # # # # # # # # #         self.type_combo = ttk.Combobox(root, values=["روس", "نقفة", "عوارض"], state="readonly")
# # # # # # # # # #         self.type_combo.grid(row=2, column=1)

# # # # # # # # # #         tk.Label(root, text="عدد الحبات:").grid(row=3, column=0)
# # # # # # # # # #         self.qty_entry = tk.Entry(root)
# # # # # # # # # #         self.qty_entry.grid(row=3, column=1)

# # # # # # # # # #         tk.Label(root, text="السعر للحبة:").grid(row=4, column=0)
# # # # # # # # # #         self.price_entry = tk.Entry(root)
# # # # # # # # # #         self.price_entry.grid(row=4, column=1)

# # # # # # # # # #         tk.Button(root, text="إضافة قات", command=self.add_qat).grid(row=5, column=0, columnspan=2)
# # # # # # # # # #         tk.Button(root, text="🎤 إضافة قات بالصوت", command=self.add_qat_voice).grid(row=5, column=2)

# # # # # # # # # #         # إدخال الدفع
# # # # # # # # # #         tk.Label(root, text="دفع للمزارع:").grid(row=6, column=0)
# # # # # # # # # #         self.pay_entry = tk.Entry(root)
# # # # # # # # # #         self.pay_entry.grid(row=6, column=1)

# # # # # # # # # #         tk.Button(root, text="دفع", command=self.pay_farmer).grid(row=7, column=0, columnspan=2)

# # # # # # # # # #         # جدول عرض العمليات
# # # # # # # # # #         self.tree = ttk.Treeview(root, 
# # # # # # # # # #                                  columns=("الرصيد","الوقت","الإجمالي","السعر","روس","نقفة","عوارض"), 
# # # # # # # # # #                                  show="headings", height=12)
# # # # # # # # # #         self.tree.grid(row=8, column=0, columnspan=4, pady=10)

# # # # # # # # # #         for col in ("الرصيد","الوقت","الإجمالي","السعر","روس","نقفة","عوارض"):
# # # # # # # # # #             self.tree.heading(col, text=col)
# # # # # # # # # #             self.tree.column(col, width=100, anchor="center")

# # # # # # # # # #     # 🎤 دالة الاستماع للصوت
# # # # # # # # # #     def listen_voice(self):
# # # # # # # # # #         r = sr.Recognizer()
# # # # # # # # # #         with sr.Microphone() as source:
# # # # # # # # # #             messagebox.showinfo("🎤", "تكلم الآن...")
# # # # # # # # # #             audio = r.listen(source)
# # # # # # # # # #         try:
# # # # # # # # # #             text = r.recognize_google(audio, language="ar")
# # # # # # # # # #             return text
# # # # # # # # # #         except:
# # # # # # # # # #             messagebox.showerror("خطأ", "لم أتمكن من فهم الصوت")
# # # # # # # # # #             return ""

# # # # # # # # # #     # إضافة مزارع يدوي
# # # # # # # # # #     def add_farmer(self):
# # # # # # # # # #         name = self.name_entry.get()
# # # # # # # # # #         if not name:
# # # # # # # # # #             messagebox.showerror("خطأ", "أدخل اسم المزارع")
# # # # # # # # # #             return
# # # # # # # # # #         if name in self.farmers:
# # # # # # # # # #             messagebox.showerror("خطأ", "المزارع موجود بالفعل")
# # # # # # # # # #             return
# # # # # # # # # #         self.farmers[name] = {"balance":0, "transactions":[]}
# # # # # # # # # #         self.farmer_select["values"] = list(self.farmers.keys())
# # # # # # # # # #         messagebox.showinfo("تم", f"تم إضافة المزارع {name}")

# # # # # # # # # #     # 🎤 إضافة مزارع بالصوت
# # # # # # # # # #     def add_farmer_voice(self):
# # # # # # # # # #         name = self.listen_voice()
# # # # # # # # # #         if name:
# # # # # # # # # #             if name in self.farmers:
# # # # # # # # # #                 messagebox.showerror("خطأ", "المزارع موجود بالفعل")
# # # # # # # # # #             else:
# # # # # # # # # #                 self.farmers[name] = {"balance":0, "transactions":[]}
# # # # # # # # # #                 self.farmer_select["values"] = list(self.farmers.keys())
# # # # # # # # # #                 messagebox.showinfo("تم", f"تم إضافة المزارع {name}")

# # # # # # # # # #     # إضافة قات يدوي
# # # # # # # # # #     def add_qat(self):
# # # # # # # # # #         name = self.farmer_select.get()
# # # # # # # # # #         if not name:
# # # # # # # # # #             messagebox.showerror("خطأ", "اختر المزارع أولاً")
# # # # # # # # # #             return

# # # # # # # # # #         qat_type = self.type_combo.get()
# # # # # # # # # #         qty = int(self.qty_entry.get())
# # # # # # # # # #         price = int(self.price_entry.get())
# # # # # # # # # #         total = qty * price
# # # # # # # # # #         time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# # # # # # # # # #         self.farmers[name]["balance"] += total
# # # # # # # # # #         ros = qty if qat_type == "روس" else ""
# # # # # # # # # #         naqfa = qty if qat_type == "نقفة" else ""
# # # # # # # # # #         awarid = qty if qat_type == "عوارض" else ""

# # # # # # # # # #         self.farmers[name]["transactions"].append((self.farmers[name]["balance"], time, total, price, ros, naqfa, awarid))
# # # # # # # # # #         self.show_farmer_data()

# # # # # # # # # #     # 🎤 إضافة قات بالصوت (مثال: "أضف 3 روس بسعر 500 لأحمد")
# # # # # # # # # #     def add_qat_voice(self):
# # # # # # # # # #         text = self.listen_voice()
# # # # # # # # # #         if not text: return

# # # # # # # # # #         try:
# # # # # # # # # #             # استخراج البيانات من النص
# # # # # # # # # #             words = text.split()
# # # # # # # # # #             qty = int(words[1])  # العدد بعد كلمة "أضف"
# # # # # # # # # #             qat_type = words[2]  # النوع (روس/نقفة/عوارض)
# # # # # # # # # #             price = int(words[4])  # السعر بعد كلمة "بسعر"
# # # # # # # # # #             name = words[-1]  # اسم المزارع آخر كلمة

# # # # # # # # # #             if name not in self.farmers:
# # # # # # # # # #                 messagebox.showerror("خطأ", "المزارع غير موجود")
# # # # # # # # # #                 return

# # # # # # # # # #             total = qty * price
# # # # # # # # # #             time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
# # # # # # # # # #             self.farmers[name]["balance"] += total

# # # # # # # # # #             ros = qty if qat_type == "روس" else ""
# # # # # # # # # #             naqfa = qty if qat_type == "نقفة" else ""
# # # # # # # # # #             awarid = qty if qat_type == "عوارض" else ""

# # # # # # # # # #             self.farmers[name]["transactions"].append((self.farmers[name]["balance"], time, total, price, ros, naqfa, awarid))
# # # # # # # # # #             self.show_farmer_data()
# # # # # # # # # #             messagebox.showinfo("تم", f"تم إضافة {qty} {qat_type} بسعر {price} للمزارع {name}")

# # # # # # # # # #         except Exception as e:
# # # # # # # # # #             messagebox.showerror("خطأ", f"لم أتمكن من فهم الأمر الصوتي\n{e}")

# # # # # # # # # #     # دفع للمزارع
# # # # # # # # # #     def pay_farmer(self):
# # # # # # # # # #         name = self.farmer_select.get()
# # # # # # # # # #         if not name:
# # # # # # # # # #             messagebox.showerror("خطأ", "اختر المزارع أولاً")
# # # # # # # # # #             return

# # # # # # # # # #         amount = int(self.pay_entry.get())
# # # # # # # # # #         time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# # # # # # # # # #         if amount > self.farmers[name]["balance"]:
# # # # # # # # # #             messagebox.showerror("خطأ", "المبلغ أكبر من الرصيد")
# # # # # # # # # #             return

# # # # # # # # # #         self.farmers[name]["balance"] -= amount
# # # # # # # # # #         self.farmers[name]["transactions"].append((self.farmers[name]["balance"], time, amount, "-", "", "", ""))
# # # # # # # # # #         self.show_farmer_data()

# # # # # # # # # #     # 🎤 طلب بيانات مزارع بالصوت
# # # # # # # # # #     def show_farmer_voice(self):
# # # # # # # # # #         name = self.listen_voice()
# # # # # # # # # #         if name and name in self.farmers:
# # # # # # # # # #             self.show_farmer_data(name)
# # # # # # # # # #         else:
# # # # # # # # # #             messagebox.showerror("خطأ", "المزارع غير موجود")

# # # # # # # # # #     # عرض بيانات المزارع
# # # # # # # # # #     def show_farmer_data(self, name=None):










# # # # # # # # # import tkinter as tk
# # # # # # # # # from tkinter import ttk, messagebox
# # # # # # # # # import datetime
# # # # # # # # # import speech_recognition as sr

# # # # # # # # # class FarmerAccountApp:
# # # # # # # # #     def __init__(self, root):
# # # # # # # # #         self.root = root
# # # # # # # # #         self.root.title("دفتر حسابات تجارة القات بالصوت")

# # # # # # # # #         # قاعدة بيانات المزارعين
# # # # # # # # #         self.farmers = {}

# # # # # # # # #         # إدخال اسم المزارع
# # # # # # # # #         tk.Label(root, text="اسم المزارع:").grid(row=0, column=0)
# # # # # # # # #         self.name_entry = tk.Entry(root)
# # # # # # # # #         self.name_entry.grid(row=0, column=1)

# # # # # # # # #         tk.Button(root, text="إضافة مزارع جديد", command=self.add_farmer).grid(row=0, column=2)
# # # # # # # # #         tk.Button(root, text="🎤 إضافة مزارع بالصوت", command=self.add_farmer_voice).grid(row=0, column=3)

# # # # # # # # #         # قائمة اختيار المزارع
# # # # # # # # #         tk.Label(root, text="اختر المزارع:").grid(row=1, column=0)
# # # # # # # # #         self.farmer_select = ttk.Combobox(root, values=list(self.farmers.keys()))
# # # # # # # # #         self.farmer_select.grid(row=1, column=1)

# # # # # # # # #         tk.Button(root, text="إظهار بيانات المزارع", command=self.show_farmer_data).grid(row=1, column=2)
# # # # # # # # #         tk.Button(root, text="🎤 طلب بيانات بالصوت", command=self.show_farmer_voice).grid(row=1, column=3)

# # # # # # # # #         # إدخال بيانات القات
# # # # # # # # #         tk.Label(root, text="نوع القات:").grid(row=2, column=0)
# # # # # # # # #         self.type_combo = ttk.Combobox(root, values=["روس", "نقفة", "عوارض"], state="readonly")
# # # # # # # # #         self.type_combo.grid(row=2, column=1)

# # # # # # # # #         tk.Label(root, text="عدد الحبات:").grid(row=3, column=0)
# # # # # # # # #         self.qty_entry = tk.Entry(root)
# # # # # # # # #         self.qty_entry.grid(row=3, column=1)

# # # # # # # # #         tk.Label(root, text="السعر للحبة:").grid(row=4, column=0)
# # # # # # # # #         self.price_entry = tk.Entry(root)
# # # # # # # # #         self.price_entry.grid(row=4, column=1)

# # # # # # # # #         tk.Button(root, text="إضافة قات", command=self.add_qat).grid(row=5, column=0, columnspan=2)
# # # # # # # # #         tk.Button(root, text="🎤 إضافة قات بالصوت", command=self.add_qat_voice).grid(row=5, column=2)

# # # # # # # # #         # إدخال الدفع
# # # # # # # # #         tk.Label(root, text="دفع للمزارع:").grid(row=6, column=0)
# # # # # # # # #         self.pay_entry = tk.Entry(root)
# # # # # # # # #         self.pay_entry.grid(row=6, column=1)

# # # # # # # # #         tk.Button(root, text="دفع", command=self.pay_farmer).grid(row=7, column=0, columnspan=2)

# # # # # # # # #         # جدول عرض العمليات
# # # # # # # # #         self.tree = ttk.Treeview(root, 
# # # # # # # # #                                  columns=("الرصيد","الوقت","الإجمالي","السعر","روس","نقفة","عوارض"), 
# # # # # # # # #                                  show="headings", height=12)
# # # # # # # # #         self.tree.grid(row=8, column=0, columnspan=4, pady=10)

# # # # # # # # #         for col in ("الرصيد","الوقت","الإجمالي","السعر","روس","نقفة","عوارض"):
# # # # # # # # #             self.tree.heading(col, text=col)
# # # # # # # # #             self.tree.column(col, width=100, anchor="center")

# # # # # # # # #     # 🎤 دالة الاستماع للصوت
# # # # # # # # #     def listen_voice(self):
# # # # # # # # #         r = sr.Recognizer()
# # # # # # # # #         with sr.Microphone() as source:
# # # # # # # # #             messagebox.showinfo("🎤", "تكلم الآن...")
# # # # # # # # #             audio = r.listen(source)
# # # # # # # # #         try:
# # # # # # # # #             text = r.recognize_google(audio, language="ar")
# # # # # # # # #             return text
# # # # # # # # #         except:
# # # # # # # # #             messagebox.showerror("خطأ", "لم أتمكن من فهم الصوت")
# # # # # # # # #             return ""

# # # # # # # # #     # إضافة مزارع يدوي
# # # # # # # # #     def add_farmer(self):
# # # # # # # # #         name = self.name_entry.get()
# # # # # # # # #         if not name:
# # # # # # # # #             messagebox.showerror("خطأ", "أدخل اسم المزارع")
# # # # # # # # #             return
# # # # # # # # #         if name in self.farmers:
# # # # # # # # #             messagebox.showerror("خطأ", "المزارع موجود بالفعل")
# # # # # # # # #             return
# # # # # # # # #         self.farmers[name] = {"balance":0, "transactions":[]}
# # # # # # # # #         self.farmer_select["values"] = list(self.farmers.keys())
# # # # # # # # #         messagebox.showinfo("تم", f"تم إضافة المزارع {name}")

# # # # # # # # #     # 🎤 إضافة مزارع بالصوت
# # # # # # # # #     def add_farmer_voice(self):
# # # # # # # # #         name = self.listen_voice()
# # # # # # # # #         if name:
# # # # # # # # #             if name in self.farmers:
# # # # # # # # #                 messagebox.showerror("خطأ", "المزارع موجود بالفعل")
# # # # # # # # #             else:
# # # # # # # # #                 self.farmers[name] = {"balance":0, "transactions":[]}
# # # # # # # # #                 self.farmer_select["values"] = list(self.farmers.keys())
# # # # # # # # #                 messagebox.showinfo("تم", f"تم إضافة المزارع {name}")

# # # # # # # # #     # إضافة قات يدوي
# # # # # # # # #     def add_qat(self):
# # # # # # # # #         name = self.farmer_select.get()
# # # # # # # # #         if not name:
# # # # # # # # #             messagebox.showerror("خطأ", "اختر المزارع أولاً")
# # # # # # # # #             return

# # # # # # # # #         qat_type = self.type_combo.get()
# # # # # # # # #         qty = int(self.qty_entry.get())
# # # # # # # # #         price = int(self.price_entry.get())
# # # # # # # # #         total = qty * price
# # # # # # # # #         time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# # # # # # # # #         self.farmers[name]["balance"] += total
# # # # # # # # #         ros = qty if qat_type == "روس" else ""
# # # # # # # # #         naqfa = qty if qat_type == "نقفة" else ""
# # # # # # # # #         awarid = qty if qat_type == "عوارض" else ""

# # # # # # # # #         self.farmers[name]["transactions"].append((self.farmers[name]["balance"], time, total, price, ros, naqfa, awarid))
# # # # # # # # #         self.show_farmer_data()

# # # # # # # # #     # 🎤 إضافة قات بالصوت (مثال: "أضف 3 روس بسعر 500 لأحمد")
# # # # # # # # #     def add_qat_voice(self):
# # # # # # # # #         text = self.listen_voice()
# # # # # # # # #         if not text: return

# # # # # # # # #         try:
# # # # # # # # #             words = text.split()
# # # # # # # # #             qty = int(words[1])  # العدد بعد كلمة "أضف"
# # # # # # # # #             qat_type = words[2]  # النوع (روس/نقفة/عوارض)
# # # # # # # # #             price = int(words[4])  # السعر بعد كلمة "بسعر"
# # # # # # # # #             name = words[-1]  # اسم المزارع آخر كلمة

# # # # # # # # #             if name not in self.farmers:
# # # # # # # # #                 messagebox.showerror("خطأ", "المزارع غير موجود")
# # # # # # # # #                 return

# # # # # # # # #             total = qty * price
# # # # # # # # #             time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
# # # # # # # # #             self.farmers[name]["balance"] += total

# # # # # # # # #             ros = qty if qat_type == "روس" else ""
# # # # # # # # #             naqfa = qty if qat_type == "نقفة" else ""
# # # # # # # # #             awarid = qty if qat_type == "عوارض" else ""

# # # # # # # # #             self.farmers[name]["transactions"].append((self.farmers[name]["balance"], time, total, price, ros, naqfa, awarid))
# # # # # # # # #             self.show_farmer_data()
# # # # # # # # #             messagebox.showinfo("تم", f"تم إضافة {qty} {qat_type} بسعر {price} للمزارع {name}")

# # # # # # # # #         except Exception as e:
# # # # # # # # #             messagebox.showerror("خطأ", f"لم أتمكن من فهم الأمر الصوتي\n{e}")

# # # # # # # # #     # دفع للمزارع
# # # # # # # # #     def pay_farmer(self):
# # # # # # # # #         name = self.farmer_select.get()
# # # # # # # # #         if not name:
# # # # # # # # #             messagebox.showerror("خطأ", "اختر المزارع أولاً")
# # # # # # # # #             return

# # # # # # # # #         amount = int(self.pay_entry.get())
# # # # # # # # #         time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# # # # # # # # #         if amount > self.farmers[name]["balance"]:
# # # # # # # # #             messagebox.showerror("خطأ", "المبلغ أكبر من الرصيد")
# # # # # # # # #             return

# # # # # # # # #         self.farmers[name]["balance"] -= amount
# # # # # # # # #         self.farmers[name]["transactions"].append((self.farmers[name]["balance"], time, amount, "-", "", "", ""))
# # # # # # # # #         self.show_farmer_data()

# # # # # # # # #     # 🎤 طلب بيانات مزارع بالصوت
# # # # # # # # #     def show_farmer_voice(self):
# # # # # # # # #         name = self.listen_voice()
# # # # # # # # #         if name and name in self.farmers:
# # # # # # # # #             self.show_farmer_data(name)
# # # # # # # # #         else:
# # # # # # # # #             messagebox.showerror("خطأ", "المزارع غير موجود")

# # # # # # # # #     # عرض بيانات المزارع
# # # # # # # # #     def show_farmer_data(self, name=None):
# # # # # # # # #         if not name:
# # # # # # # # #             name = self.farmer_select.get()
# # # # # # # # #         if not name:
# # # # # # # # #             return
# # # # # # # # #         # مسح الجدول
# # # # # # # # #         for row in self.tree.get_children():
# # # # # # # # #             self.tree.delete(row)
# # # # # # # # #         # عرض بيانات المزارع
# # # # # # # # #         for t in self.farmers[name]["transactions"]:
# # # # # # # # #             self.tree.insert("", "end", values=t)











# # # # # # # # import tkinter as tk
# # # # # # # # from tkinter import ttk, messagebox
# # # # # # # # import datetime
# # # # # # # # import speech_recognition as sr

# # # # # # # # # 🟢 دالة تحويل الكلمات العربية إلى أرقام (قاموس موسع)
# # # # # # # # def arabic_word_to_number(word):
# # # # # # # #     mapping = {
# # # # # # # #         "صفر": 0, "واحد": 1, "إثنين": 2, "اثنين": 2, "ثلاثة": 3, "أربعة": 4,
# # # # # # # #         "خمسة": 5, "ستة": 6, "سبعة": 7, "ثمانية": 8, "تسعة": 9, "عشرة": 10,
# # # # # # # #         "أحد عشر": 11, "اثنا عشر": 12, "ثلاثة عشر": 13, "أربعة عشر": 14,
# # # # # # # #         "خمسة عشر": 15, "ستة عشر": 16, "سبعة عشر": 17, "ثمانية عشر": 18, "تسعة عشر": 19,
# # # # # # # #         "عشرون": 20, "ثلاثون": 30, "أربعون": 40, "خمسون": 50,
# # # # # # # #         "ستون": 60, "سبعون": 70, "ثمانون": 80, "تسعون": 90,
# # # # # # # #         "مئة": 100, "مائة": 100, "مئتان": 200, "ثلاثمئة": 300, "أربعمئة": 400,
# # # # # # # #         "خمسمئة": 500, "ستمئة": 600, "سبعمئة": 700, "ثمانمئة": 800, "تسعمئة": 900,
# # # # # # # #         "ألف": 1000, "ألفان": 2000, "ثلاثة آلاف": 3000, "أربعة آلاف": 4000,
# # # # # # # #         "خمسة آلاف": 5000, "ستة آلاف": 6000, "سبعة آلاف": 7000,
# # # # # # # #         "ثمانية آلاف": 8000, "تسعة آلاف": 9000, "عشرة آلاف": 10000
# # # # # # # #     }
# # # # # # # #     if word in mapping:
# # # # # # # #         return mapping[word]
# # # # # # # #     if word.isdigit():
# # # # # # # #         return int(word)
# # # # # # # #     return None

# # # # # # # # class FarmerAccountApp:
# # # # # # # #     def __init__(self, root):
# # # # # # # #         self.root = root
# # # # # # # #         self.root.title("دفتر حسابات تجارة القات بالصوت")

# # # # # # # #         self.farmers = {}

# # # # # # # #         # إدخال اسم المزارع
# # # # # # # #         tk.Label(root, text="اسم المزارع:").grid(row=0, column=0)
# # # # # # # #         self.name_entry = tk.Entry(root)
# # # # # # # #         self.name_entry.grid(row=0, column=1)

# # # # # # # #         tk.Button(root, text="إضافة مزارع جديد", command=self.add_farmer).grid(row=0, column=2)
# # # # # # # #         tk.Button(root, text="🎤 إضافة مزارع بالصوت", command=self.add_farmer_voice).grid(row=0, column=3)

# # # # # # # #         # قائمة اختيار المزارع
# # # # # # # #         tk.Label(root, text="اختر المزارع:").grid(row=1, column=0)
# # # # # # # #         self.farmer_select = ttk.Combobox(root, values=list(self.farmers.keys()))
# # # # # # # #         self.farmer_select.grid(row=1, column=1)

# # # # # # # #         tk.Button(root, text="إظهار بيانات المزارع", command=self.show_farmer_data).grid(row=1, column=2)
# # # # # # # #         tk.Button(root, text="🎤 طلب بيانات بالصوت", command=self.show_farmer_voice).grid(row=1, column=3)

# # # # # # # #         # إدخال بيانات القات
# # # # # # # #         tk.Label(root, text="نوع القات:").grid(row=2, column=0)
# # # # # # # #         self.type_combo = ttk.Combobox(root, values=["روس", "نقفة", "عوارض"], state="readonly")
# # # # # # # #         self.type_combo.grid(row=2, column=1)

# # # # # # # #         tk.Label(root, text="عدد الحبات:").grid(row=3, column=0)
# # # # # # # #         self.qty_entry = tk.Entry(root)
# # # # # # # #         self.qty_entry.grid(row=3, column=1)

# # # # # # # #         tk.Label(root, text="السعر للحبة:").grid(row=4, column=0)
# # # # # # # #         self.price_entry = tk.Entry(root)
# # # # # # # #         self.price_entry.grid(row=4, column=1)

# # # # # # # #         tk.Button(root, text="إضافة قات", command=self.add_qat).grid(row=5, column=0, columnspan=2)
# # # # # # # #         tk.Button(root, text="🎤 إضافة قات بالصوت", command=self.add_qat_voice).grid(row=5, column=2)

# # # # # # # #         # إدخال الدفع
# # # # # # # #         tk.Label(root, text="دفع للمزارع:").grid(row=6, column=0)
# # # # # # # #         self.pay_entry = tk.Entry(root)
# # # # # # # #         self.pay_entry.grid(row=6, column=1)

# # # # # # # #         tk.Button(root, text="دفع", command=self.pay_farmer).grid(row=7, column=0, columnspan=2)

# # # # # # # #         # جدول عرض العمليات
# # # # # # # #         self.tree = ttk.Treeview(root, 
# # # # # # # #                                  columns=("الرصيد","الوقت","الإجمالي","السعر","روس","نقفة","عوارض"), 
# # # # # # # #                                  show="headings", height=12)
# # # # # # # #         self.tree.grid(row=8, column=0, columnspan=4, pady=10)

# # # # # # # #         for col in ("الرصيد","الوقت","الإجمالي","السعر","روس","نقفة","عوارض"):
# # # # # # # #             self.tree.heading(col, text=col)
# # # # # # # #             self.tree.column(col, width=100, anchor="center")

# # # # # # # #     # 🎤 دالة الاستماع للصوت
# # # # # # # #     def listen_voice(self):
# # # # # # # #         r = sr.Recognizer()
# # # # # # # #         with sr.Microphone() as source:
# # # # # # # #             messagebox.showinfo("🎤", "تكلم الآن...")
# # # # # # # #             audio = r.listen(source)
# # # # # # # #         try:
# # # # # # # #             text = r.recognize_google(audio, language="ar")
# # # # # # # #             return text
# # # # # # # #         except:
# # # # # # # #             messagebox.showerror("خطأ", "لم أتمكن من فهم الصوت")
# # # # # # # #             return ""

# # # # # # # #     # إضافة مزارع يدوي
# # # # # # # #     def add_farmer(self):
# # # # # # # #         name = self.name_entry.get()
# # # # # # # #         if not name:
# # # # # # # #             messagebox.showerror("خطأ", "أدخل اسم المزارع")
# # # # # # # #             return
# # # # # # # #         if name in self.farmers:
# # # # # # # #             messagebox.showerror("خطأ", "المزارع موجود بالفعل")
# # # # # # # #             return
# # # # # # # #         self.farmers[name] = {"balance":0, "transactions":[]}
# # # # # # # #         self.farmer_select["values"] = list(self.farmers.keys())
# # # # # # # #         messagebox.showinfo("تم", f"تم إضافة المزارع {name}")

# # # # # # # #     # 🎤 إضافة مزارع بالصوت
# # # # # # # #     def add_farmer_voice(self):
# # # # # # # #         name = self.listen_voice()
# # # # # # # #         if name:
# # # # # # # #             if name in self.farmers:
# # # # # # # #                 messagebox.showerror("خطأ", "المزارع موجود بالفعل")
# # # # # # # #             else:
# # # # # # # #                 self.farmers[name] = {"balance":0, "transactions":[]}
# # # # # # # #                 self.farmer_select["values"] = list(self.farmers.keys())
# # # # # # # #                 messagebox.showinfo("تم", f"تم إضافة المزارع {name}")

# # # # # # # #     # إضافة قات يدوي
# # # # # # # #     def add_qat(self):
# # # # # # # #         name = self.farmer_select.get()
# # # # # # # #         if not name:
# # # # # # # #             messagebox.showerror("خطأ", "اختر المزارع أولاً")
# # # # # # # #             return

# # # # # # # #         qat_type = self.type_combo.get()
# # # # # # # #         qty = int(self.qty_entry.get())
# # # # # # # #         price = int(self.price_entry.get())
# # # # # # # #         total = qty * price
# # # # # # # #         time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# # # # # # # #         self.farmers[name]["balance"] += total
# # # # # # # #         ros = qty if qat_type == "روس" else ""
# # # # # # # #         naqfa = qty if qat_type == "نقفة" else ""
# # # # # # # #         awarid = qty if qat_type == "عوارض" else ""

# # # # # # # #         self.farmers[name]["transactions"].append((self.farmers[name]["balance"], time, total, price, ros, naqfa, awarid))
# # # # # # # #         self.show_farmer_data()

# # # # # # # #     # 🎤 إضافة قات بالصوت (مرن مع الكلمات المفتاحية + الأرقام النصية)
# # # # # # # #     def add_qat_voice(self):
# # # # # # # #         text = self.listen_voice()
# # # # # # # #         if not text: return

# # # # # # # #         try:
# # # # # # # #             words = text.split()

# # # # # # # #             # البحث عن الكمية
# # # # # # # #             qty = None
# # # # # # # #             for w in words:
# # # # # # # #                 num = arabic_word_to_number(w)
# # # # # # # #                 if num is not None:
# # # # # # # #                     qty = num
# # # # # # # #                     break

# # # # # # # #             # البحث عن النوع
# # # # # # # #             qat_type = None
# # # # # # # #             for w in words:
# # # # # # # #                 if w in ["روس", "نقفة", "عوارض"]:
# # # # # # # #                     qat_type = w
# # # # # # # #                     break

# # # # # # # #             # البحث عن السعر
# # # # # # # #             price = None
# # # # # # # #             if "بسعر" in words:
# # # # # # # #                 idx = words.index("بسعر")
# # # # # # # #                 if idx+1 < len(words):
# # # # # # # #                     price = arabic_word_to_number(words[idx+1])

# # # # # # # #             # البحث عن اسم المزارع (آخر كلمة عادةً)
# # # # # # # #             name = words[-1]

# # # # # # # #             # تحقق من البيانات
# # # # # # # #             if not (qty and qat_type and price and name):
# # # # # # # #                 messagebox.showerror("خطأ",
# # # # # # # # # # تشغيل البرنامج
# # # # # # # # # root = tk.Tk()
# # # # # # # # # app = FarmerAccountApp(root)
# # # # # # # # # root.mainloop()










# # # # # # # import tkinter as tk
# # # # # # # from tkinter import ttk, messagebox
# # # # # # # import datetime
# # # # # # # import speech_recognition as sr

# # # # # # # # 🟢 دالة تحويل الكلمات العربية إلى أرقام (قاموس موسع)
# # # # # # # def arabic_word_to_number(word):
# # # # # # #     mapping = {
# # # # # # #         "صفر": 0, "واحد": 1, "إثنين": 2, "اثنين": 2, "ثلاثة": 3, "أربعة": 4,
# # # # # # #         "خمسة": 5, "ستة": 6, "سبعة": 7, "ثمانية": 8, "تسعة": 9, "عشرة": 10,
# # # # # # #         "أحد عشر": 11, "اثنا عشر": 12, "ثلاثة عشر": 13, "أربعة عشر": 14,
# # # # # # #         "خمسة عشر": 15, "ستة عشر": 16, "سبعة عشر": 17, "ثمانية عشر": 18, "تسعة عشر": 19,
# # # # # # #         "عشرون": 20, "ثلاثون": 30, "أربعون": 40, "خمسون": 50,
# # # # # # #         "ستون": 60, "سبعون": 70, "ثمانون": 80, "تسعون": 90,
# # # # # # #         "مئة": 100, "مائة": 100, "مئتان": 200, "ثلاثمئة": 300, "أربعمئة": 400,
# # # # # # #         "خمسمئة": 500, "ستمئة": 600, "سبعمئة": 700, "ثمانمئة": 800, "تسعمئة": 900,
# # # # # # #         "ألف": 1000, "ألفان": 2000, "ثلاثة آلاف": 3000, "أربعة آلاف": 4000,
# # # # # # #         "خمسة آلاف": 5000, "ستة آلاف": 6000, "سبعة آلاف": 7000,
# # # # # # #         "ثمانية آلاف": 8000, "تسعة آلاف": 9000, "عشرة آلاف": 10000
# # # # # # #     }
# # # # # # #     if word in mapping:
# # # # # # #         return mapping[word]
# # # # # # #     if word.isdigit():
# # # # # # #         return int(word)
# # # # # # #     return None

# # # # # # # class FarmerAccountApp:
# # # # # # #     def __init__(self, root):
# # # # # # #         self.root = root
# # # # # # #         self.root.title("دفتر حسابات تجارة القات بالصوت")

# # # # # # #         self.farmers = {}

# # # # # # #         # إدخال اسم المزارع
# # # # # # #         tk.Label(root, text="اسم المزارع:").grid(row=0, column=0)
# # # # # # #         self.name_entry = tk.Entry(root)
# # # # # # #         self.name_entry.grid(row=0, column=1)

# # # # # # #         tk.Button(root, text="إضافة مزارع جديد", command=self.add_farmer).grid(row=0, column=2)
# # # # # # #         tk.Button(root, text="🎤 إضافة مزارع بالصوت", command=self.add_farmer_voice).grid(row=0, column=3)

# # # # # # #         # قائمة اختيار المزارع
# # # # # # #         tk.Label(root, text="اختر المزارع:").grid(row=1, column=0)
# # # # # # #         self.farmer_select = ttk.Combobox(root, values=list(self.farmers.keys()))
# # # # # # #         self.farmer_select.grid(row=1, column=1)

# # # # # # #         tk.Button(root, text="إظهار بيانات المزارع", command=self.show_farmer_data).grid(row=1, column=2)
# # # # # # #         tk.Button(root, text="🎤 طلب بيانات بالصوت", command=self.show_farmer_voice).grid(row=1, column=3)

# # # # # # #         # إدخال بيانات القات
# # # # # # #         tk.Label(root, text="نوع القات:").grid(row=2, column=0)
# # # # # # #         self.type_combo = ttk.Combobox(root, values=["روس", "نقفة", "عوارض"], state="readonly")
# # # # # # #         self.type_combo.grid(row=2, column=1)

# # # # # # #         tk.Label(root, text="عدد الحبات:").grid(row=3, column=0)
# # # # # # #         self.qty_entry = tk.Entry(root)
# # # # # # #         self.qty_entry.grid(row=3, column=1)

# # # # # # #         tk.Label(root, text="السعر للحبة:").grid(row=4, column=0)
# # # # # # #         self.price_entry = tk.Entry(root)
# # # # # # #         self.price_entry.grid(row=4, column=1)

# # # # # # #         tk.Button(root, text="إضافة قات", command=self.add_qat).grid(row=5, column=0, columnspan=2)
# # # # # # #         tk.Button(root, text="🎤 إضافة قات بالصوت", command=self.add_qat_voice).grid(row=5, column=2)

# # # # # # #         # إدخال الدفع
# # # # # # #         tk.Label(root, text="دفع للمزارع:").grid(row=6, column=0)
# # # # # # #         self.pay_entry = tk.Entry(root)
# # # # # # #         self.pay_entry.grid(row=6, column=1)

# # # # # # #         tk.Button(root, text="دفع", command=self.pay_farmer).grid(row=7, column=0, columnspan=2)

# # # # # # #         # جدول عرض العمليات
# # # # # # #         self.tree = ttk.Treeview(root, 
# # # # # # #                                  columns=("الرصيد","الوقت","الإجمالي","السعر","روس","نقفة","عوارض"), 
# # # # # # #                                  show="headings", height=12)
# # # # # # #         self.tree.grid(row=8, column=0, columnspan=4, pady=10)

# # # # # # #         for col in ("الرصيد","الوقت","الإجمالي","السعر","روس","نقفة","عوارض"):
# # # # # # #             self.tree.heading(col, text=col)
# # # # # # #             self.tree.column(col, width=100, anchor="center")

# # # # # # #     # 🎤 دالة الاستماع للصوت
# # # # # # #     def listen_voice(self):
# # # # # # #         r = sr.Recognizer()
# # # # # # #         with sr.Microphone() as source:
# # # # # # #             messagebox.showinfo("🎤", "تكلم الآن...")
# # # # # # #             audio = r.listen(source)
# # # # # # #         try:
# # # # # # #             text = r.recognize_google(audio, language="ar")
# # # # # # #             return text
# # # # # # #         except:
# # # # # # #             messagebox.showerror("خطأ", "لم أتمكن من فهم الصوت")
# # # # # # #             return ""

# # # # # # #     # إضافة مزارع يدوي
# # # # # # #     def add_farmer(self):
# # # # # # #         name = self.name_entry.get()
# # # # # # #         if not name:
# # # # # # #             messagebox.showerror("خطأ", "أدخل اسم المزارع")
# # # # # # #             return
# # # # # # #         if name in self.farmers:
# # # # # # #             messagebox.showerror("خطأ", "المزارع موجود بالفعل")
# # # # # # #             return
# # # # # # #         self.farmers[name] = {"balance":0, "transactions":[]}
# # # # # # #         self.farmer_select["values"] = list(self.farmers.keys())
# # # # # # #         messagebox.showinfo("تم", f"تم إضافة المزارع {name}")

# # # # # # #     # 🎤 إضافة مزارع بالصوت
# # # # # # #     def add_farmer_voice(self):
# # # # # # #         name = self.listen_voice()
# # # # # # #         if name:
# # # # # # #             if name in self.farmers:
# # # # # # #                 messagebox.showerror("خطأ", "المزارع موجود بالفعل")
# # # # # # #             else:
# # # # # # #                 self.farmers[name] = {"balance":0, "transactions":[]}
# # # # # # #                 self.farmer_select["values"] = list(self.farmers.keys())
# # # # # # #                 messagebox.showinfo("تم", f"تم إضافة المزارع {name}")

# # # # # # #     # إضافة قات يدوي
# # # # # # #     def add_qat(self):
# # # # # # #         name = self.farmer_select.get()
# # # # # # #         if not name:
# # # # # # #             messagebox.showerror("خطأ", "اختر المزارع أولاً")
# # # # # # #             return

# # # # # # #         qat_type = self.type_combo.get()
# # # # # # #         qty = int(self.qty_entry.get())
# # # # # # #         price = int(self.price_entry.get())
# # # # # # #         total = qty * price
# # # # # # #         time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# # # # # # #         self.farmers[name]["balance"] += total
# # # # # # #         ros = qty if qat_type == "روس" else ""
# # # # # # #         naqfa = qty if qat_type == "نقفة" else ""
# # # # # # #         awarid = qty if qat_type == "عوارض" else ""

# # # # # # #         self.farmers[name]["transactions"].append((self.farmers[name]["balance"], time, total, price, ros, naqfa, awarid))
# # # # # # #         self.show_farmer_data()

# # # # # # #     # 🎤 إضافة قات بالصوت (مرن مع الكلمات المفتاحية + الأرقام النصية)
# # # # # # #     def add_qat_voice(self):
# # # # # # #         text = self.listen_voice()
# # # # # # #         if not text: return

# # # # # # #         try:
# # # # # # #             words = text.split()

# # # # # # #             # البحث عن الكمية
# # # # # # #             qty = None
# # # # # # #             for w in words:
# # # # # # #                 num = arabic_word_to_number(w)
# # # # # # #                 if num is not None:
# # # # # # #                     qty = num
# # # # # # #                     break

# # # # # # #             # البحث عن النوع
# # # # # # #             qat_type = None
# # # # # # #             for w in words:
# # # # # # #                 if w in ["روس", "نقفة", "عوارض"]:
# # # # # # #                     qat_type = w
# # # # # # #                     break

# # # # # # #             # البحث عن السعر
# # # # # # #             price = None
# # # # # # #             if "بسعر" in words:
# # # # # # #                 idx = words.index("بسعر")
# # # # # # #                 if idx+1 < len(words):
# # # # # # #                     price = arabic_word_to_number(words[idx+1])

# # # # # # #             # البحث عن اسم المزارع (آخر كلمة عادةً)
# # # # # # #             name = words[-1]

# # # # # # #             # تحقق من البيانات
# # # # # # #             if not (qty and qat_type and price and name):
# # # # # # #                 messagebox.showerror("خطأ", "لم أتمكن من استخراج البيانات من الصوت")
# # # # # # #                 return

# # # # # # #             if name not in self.farmers:
# # # # # # #                 messagebox.showerror("خطأ", f"المزارع {name} غير موجود")
# # # # # # #                 return

# # # # # # #             total = qty * price
# # # # # # #             time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
# # # # # # #             self.farmers[name]["balance"] += total

# # # # # # #             ros = qty if qat_type == "روس" else ""
# # # # # # #             naqfa = qty if qat_type == "نقفة" else ""
# # # # # # #             awarid = qty if qat_type == "عوارض" else ""

# # # # # # #             self.farmers[name]["transactions"].append(
# # # # # # #                 (self.farmers[name]["balance"], time, total, price, ros, naqfa, awarid)
# # # # # # #             )
# # # # # # #             self.show_farmer_data()
# # # # # # #             messagebox.showinfo("تم", f"تم إضافة {qty} {qat_type} بسعر {price} للمزارع {name}")

# # # # # # #         except Exception as e:
# # # # # # #             messagebox.showerror("خطأ", f"لم أتمكن من فهم الأمر الصوتي\n{e}")

# # # # # # #     # دفع للمزارع
# # # # # # #     def pay_farmer(self):
# # # # # # #         name = self.farmer_select.get()
# # # # # # #         if not name:
# # # # # # #             messagebox.showerror("خطأ", "اختر المزارع أولاً")
# # # # # # #             return

# # # # # # #         amount = int(self.pay_entry.get())
# # # # # # #         time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# # # # # # #         if amount > self.farmers[name]["balance"]:
# # # # # # #             messagebox.showerror("خطأ", "المبلغ أكبر من الرصيد")
# # # # # # #             return

# # # # # # #         self.farmers[name]["balance"] -= amount
# # # # # # #         self.farmers[name]["transactions"].append((self.farmers[name]["balance"], time, amount, "-", "", "", ""))
# # # # # # #         self.show_farmer_data()

# # # # # # #     # 🎤 طلب بيانات مزارع بالصوت
# # # # # # #     def show_farmer_voice(self):
# # # # # # #         name = self.listen_voice()
# # # # # # #         if name and name in self.farmers:
# # # # # # #             self.show_farmer_data(name)
# # # # # # #         else:
# # # # # # #             messagebox.showerror("خطأ", "المزارع غير موجود")

# # # # # # #     # عرض بيانات المزارع
# # # # # # #     def show_farmer_data(self, name=None):
# # # # # # #         if not name:
# # # # # # #             name = self.farmer_select.get()
# # # # # # #         if not name:
# # # # # # #             return
# # # # # # #         # مسح الجدول
# # # # # # #         for row in self.tree.get_children():
# # # # # # #             self.tree.delete(row)
# # # # # # #         # عرض بيانات المزارع
# # # # # # #         for t in self.farmers[name]["transactions"]:
# # # # # # #             self.tree.insert("", "end", values=t)

# # # # # # # # تشغيل البرنامج
# # # # # # # root = tk.Tk()
# # # # # # # app = FarmerAccountApp(root)
# # # # # # # root.mainloop()








# # # # # # import tkinter as tk
# # # # # # from tkinter import ttk, messagebox
# # # # # # import datetime
# # # # # # import speech_recognition as sr

# # # # # # # ===================== أدوات مساعدة =====================

# # # # # # def normalize_words(words):
# # # # # #     return [w.replace("،", "").replace(".", "") for w in words]

# # # # # # def arabic_words_to_number(words):
# # # # # #     mapping = {
# # # # # #         "صفر":0, "واحد":1, "اثنين":2, "اثنان":2, "ثلاثة":3, "أربعة":4,
# # # # # #         "خمسة":5, "ستة":6, "سبعة":7, "ثمانية":8, "تسعة":9,
# # # # # #         "عشرة":10, "عشرين":20, "ثلاثين":30, "أربعين":40,
# # # # # #         "خمسين":50, "ستين":60, "سبعين":70, "ثمانين":80,
# # # # # #         "تسعين":90,
# # # # # #         "مئة":100, "مائة":100, "مئتين":200,
# # # # # #         "ألف":1000
# # # # # #     }
# # # # # #     total = 0
# # # # # #     for w in words:
# # # # # #         if w in mapping:
# # # # # #             total += mapping[w]
# # # # # #     return total if total > 0 else None

# # # # # # # ===================== التطبيق =====================

# # # # # # class FarmerAccountApp:
# # # # # #     def __init__(self, root):
# # # # # #         self.root = root
# # # # # #         self.root.title("نظام حسابات المزارعين (فاتورة ذكية)")

# # # # # #         self.farmers = {
# # # # # #             "أحمد": {"balance": 0, "transactions": []},
# # # # # #             "محمد": {"balance": 0, "transactions": []},
# # # # # #             "علي": {"balance": 0, "transactions": []},
# # # # # #         }

# # # # # #         self.build_ui()

# # # # # #     # ===================== الواجهة =====================
# # # # # #     def build_ui(self):
# # # # # #         top = tk.Frame(self.root)
# # # # # #         top.pack(pady=10)

# # # # # #         tk.Label(top, text="اختر المزارع").pack(side="left")
# # # # # #         self.farmer_select = ttk.Combobox(top, values=list(self.farmers.keys()))
# # # # # #         self.farmer_select.pack(side="left", padx=5)

# # # # # #         tk.Button(top, text="🎤 إدخال بالصوت", command=self.add_by_voice).pack(side="left", padx=5)
# # # # # #         tk.Button(top, text="🎤 عرض حساب", command=self.show_farmer_voice).pack(side="left", padx=5)

# # # # # #         pay = tk.Frame(self.root)
# # # # # #         pay.pack(pady=5)

# # # # # #         tk.Label(pay, text="دفع مبلغ").pack(side="left")
# # # # # #         self.pay_entry = tk.Entry(pay, width=10)
# # # # # #         self.pay_entry.pack(side="left", padx=5)
# # # # # #         tk.Button(pay, text="💵 دفع", command=self.pay_farmer).pack(side="left")

# # # # # #         cols = ("الوقت", "النوع", "الكمية", "السعر", "الإجمالي", "الرصيد بعد العملية")
# # # # # #         self.tree = ttk.Treeview(self.root, columns=cols, show="headings")
# # # # # #         for c in cols:
# # # # # #             self.tree.heading(c, text=c)
# # # # # #             self.tree.column(c, width=120)
# # # # # #         self.tree.pack(pady=10)

# # # # # #     # ===================== الصوت =====================
# # # # # #     def listen_voice(self):
# # # # # #         r = sr.Recognizer()
# # # # # #         with sr.Microphone() as source:
# # # # # #             messagebox.showinfo("تحدث", "تحدث الآن...")
# # # # # #             audio = r.listen(source)
# # # # # #         try:
# # # # # #             text = r.recognize_google(audio, language="ar")
# # # # # #             return text
# # # # # #         except:
# # # # # #             messagebox.showerror("خطأ", "لم يتم التعرف على الصوت")
# # # # # #             return None

# # # # # #     # ===================== إضافة بالصوت =====================
# # # # # #     def add_by_voice(self):
# # # # # #         try:
# # # # # #             text = self.listen_voice()
# # # # # #             if not text:
# # # # # #                 return

# # # # # #             words = normalize_words(text.split())

# # # # # #             # --- الكمية ---
# # # # # #             qty = None
# # # # # #             for i, w in enumerate(words):
# # # # # #                 q = arabic_words_to_number([w])
# # # # # #                 if q:
# # # # # #                     qty = q
# # # # # #                     break

# # # # # #             # --- النوع ---
# # # # # #             qat_type = None
# # # # # #             for w in words:
# # # # # #                 if w in ["روس", "نقفة", "عوارض"]:
# # # # # #                     qat_type = w
# # # # # #                     break

# # # # # #             # --- السعر ---
# # # # # #             price = None
# # # # # #             if "بسعر" in words:
# # # # # #                 idx = words.index("بسعر")
# # # # # #                 price = arabic_words_to_number(words[idx+1:])

# # # # # #             # --- اسم المزارع ---
# # # # # #             name = None
# # # # # #             if "المزارع" in words:
# # # # # #                 name = words[words.index("المزارع")+1]
# # # # # #             elif "ل" in words:
# # # # # #                 name = words[words.index("ل")+1]
# # # # # #             else:
# # # # # #                 name = words[-1]

# # # # # #             # --- تحقق ---
# # # # # #             if not (qty and qat_type and price and name):
# # # # # #                 messagebox.showerror("خطأ", "فشل فهم الأمر الصوتي")
# # # # # #                 return

# # # # # #             if name not in self.farmers:
# # # # # #                 messagebox.showerror("خطأ", f"المزارع {name} غير موجود")
# # # # # #                 return

# # # # # #             total = qty * price
# # # # # #             self.farmers[name]["balance"] += total
# # # # # #             time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# # # # # #             invoice = {
# # # # # #                 "time": time,
# # # # # #                 "type": qat_type,
# # # # # #                 "qty": qty,
# # # # # #                 "price": price,
# # # # # #                 "total": total,
# # # # # #                 "balance": self.farmers[name]["balance"]
# # # # # #             }

# # # # # #             self.farmers[name]["transactions"].append(invoice)
# # # # # #             self.show_farmer_data(name)

# # # # # #             messagebox.showinfo(
# # # # # #                 "تم",
# # # # # #                 f"تم تسجيل فاتورة\n{qty} {qat_type}\nبسعر {price}\nالإجمالي {total}"
# # # # # #             )

# # # # # #         except Exception as e:
# # # # # #             messagebox.showerror("خطأ", str(e))

# # # # # #     # ===================== الدفع =====================
# # # # # #     def pay_farmer(self):
# # # # # #         name = self.farmer_select.get()
# # # # # #         if not name:
# # # # # #             messagebox.showerror("خطأ", "اختر المزارع")
# # # # # #             return
# # # # # #         try:
# # # # # #             amount = int(self.pay_entry.get())
# # # # # #             if amount <= 0:
# # # # # #                 raise ValueError
# # # # # #         except:
# # # # # #             messagebox.showerror("خطأ", "مبلغ غير صحيح")
# # # # # #             return

# # # # # #         if amount > self.farmers[name]["balance"]:
# # # # # #             messagebox.showerror("خطأ", "المبلغ أكبر من الرصيد")
# # # # # #             return

# # # # # #         self.farmers[name]["balance"] -= amount
# # # # # #         time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# # # # # #         self.farmers[name]["transactions"].append({
# # # # # #             "time": time,
# # # # # #             "type": "دفع",
# # # # # #             "qty": "",
# # # # # #             "price": "",
# # # # # #             "total": -amount,
# # # # # #             "balance": self.farmers[name]["balance"]
# # # # # #         })

# # # # # #         self.show_farmer_data(name)

# # # # # #     # ===================== عرض =====================
# # # # # #     def show_farmer_voice(self):
# # # # # #         name = self.listen_voice()
# # # # # #         if name in self.farmers:
# # # # # #             self.show_farmer_data(name)
# # # # # #         else:
# # # # # #             messagebox.showerror("خطأ", "المزارع غير موجود")

# # # # # #     def show_farmer_data(self, name=None):
# # # # # #         if not name:
# # # # # #             name = self.farmer_select.get()
# # # # # #         if not name:
# # # # # #             return

# # # # # #         for row in self.tree.get_children():
# # # # # #             self.tree.delete(row)

# # # # # #         for t in self.farmers[name]["transactions"]:
# # # # # #             self.tree.insert("", "end", values=(
# # # # # #                 t["time"], t["type"], t["qty"],
# # # # # #                 t["price"], t["total"], t["balance"]
# # # # # #             ))

# # # # # # # ===================== تشغيل =====================
# # # # # # root = tk.Tk()
# # # # # # app = FarmerAccountApp(root)
# # # # # # root.mainloop()



# # # # # import speech_recognition as sr

# # # # # r = sr.Recognizer()
# # # # # with sr.Microphone() as source:
# # # # #     print("تحدث الآن...")
# # # # #     audio = r.listen(source)

# # # # # try:
# # # # #     print("النص:", r.recognize_google(audio, language="ar"))
# # # # # except Exception as e:
# # # # #     print("خطأ:", e)














# # import tkinter as tk
# # from tkinter import ttk, messagebox
# # import datetime
# # import os
# # import queue
# # import json
# # import sounddevice as sd
# # from vosk import Model, KaldiRecognizer

# # # ------------------ إعداد نموذج VOSK ------------------
# # MODEL_PATH = r"C:\vosk_models\vosk-model-ar-mgb2-0.4"  # ضع مسار المجلد بعد فك الضغط
# # if not os.path.exists(MODEL_PATH):
# #     messagebox.showerror("خطأ", f"لم يتم العثور على النموذج في {MODEL_PATH}")
# #     exit()

# # model = Model(MODEL_PATH)

# # # ------------------ التطبيق ------------------
# # class FarmerAccountApp:
# #     def __init__(self, root):
# #         self.root = root
# #         self.root.title("دفتر حسابات المزارعين")
# #         self.farmers = {}  # بيانات المزارعين
        
# #         # واجهة المستخدم
# #         tk.Label(root, text="اختر المزارع:").grid(row=0, column=0, padx=5, pady=5)
# #         self.farmer_select = ttk.Combobox(root, values=[])
# #         self.farmer_select.grid(row=0, column=1, padx=5, pady=5)

# #         tk.Label(root, text="دفع مبلغ:").grid(row=1, column=0, padx=5, pady=5)
# #         self.pay_entry = tk.Entry(root)
# #         self.pay_entry.grid(row=1, column=1, padx=5, pady=5)
# #         tk.Button(root, text="دفع", command=self.pay_farmer).grid(row=1, column=2, padx=5, pady=5)

# #         tk.Button(root, text="إضافة عبر الصوت", command=self.add_farmer_voice).grid(row=2, column=0, columnspan=3, pady=10)
# #         tk.Button(root, text="عرض بيانات المزارع", command=self.show_farmer_data).grid(row=3, column=0, columnspan=3, pady=10)

# #         # الجدول
# #         columns = ("balance", "time", "total", "price", "روس", "نقفة", "عوارض")
# #         self.tree = ttk.Treeview(root, columns=columns, show="headings")
# #         for col in columns:
# #             self.tree.heading(col, text=col)
# #         self.tree.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

# #         # مثال: إضافة بعض المزارعين
# #         self.farmers = {
# #             "محمد": {"balance": 0, "transactions": []},
# #             "أحمد": {"balance": 0, "transactions": []},
# #             "علي": {"balance": 0, "transactions": []},
# #         }
# #         self.farmer_select['values'] = list(self.farmers.keys())

# #         # صف الانتظار للصوت
# #         self.q = queue.Queue()

# #     # ------------------ تسجيل الصوت ------------------
# #     def listen_voice(self, duration=5):
# #         """استماع للصوت ومعالجته"""
# #         rec = KaldiRecognizer(model, 16000)
# #         self.q.queue.clear()
# #         text = ""

# #         def callback(indata, frames, time, status):
# #             self.q.put(bytes(indata))

# #         with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype="int16",
# #                                channels=1, callback=callback):
# #             messagebox.showinfo("استماع", f"تحدث الآن لمدة {duration} ثواني")
# #             import time as t
# #             start = t.time()
# #             while t.time() - start < duration:
# #                 if not self.q.empty():
# #                     data = self.q.get()
# #                     if rec.AcceptWaveform(data):
# #                         result = json.loads(rec.Result())
# #                         text += result.get("text", "") + " "
# #             # آخر جزء لم يتم الانتهاء منه
# #             final = json.loads(rec.FinalResult())
# #             text += final.get("text", "")
# #         return text.strip()

# #     # ------------------ إضافة مزارع بالصوت ------------------
# #     def add_farmer_voice(self):
# #         try:
# #             voice_text = self.listen_voice()
# #             if not voice_text:
# #                 messagebox.showerror("خطأ", "لم يتم التعرف على الصوت")
# #                 return

# #             words = voice_text.split()
# #             qty = None
# #             for w in words:
# #                 if w.isdigit():
# #                     qty = int(w)
# #                     break

# #             qat_type = None
# #             for w in words:
# #                 if w in ["روس", "نقفة", "عوارض"]:
# #                     qat_type = w
# #                     break

# #             price = None
# #             if "بسعر" in words:
# #                 idx = words.index("بسعر")
# #                 if idx + 1 < len(words) and words[idx+1].isdigit():
# #                     price = int(words[idx+1])

# #             # اسم المزارع آخر كلمة عادةً
# #             name = words[-1] if words else None

# #             # تحقق من البيانات
# #             if not (qty and qat_type and price and name):
# #                 messagebox.showerror("خطأ", f"لم أتمكن من استخراج البيانات من الصوت:\n{voice_text}")
# #                 return

# #             if name not in self.farmers:
# #                 messagebox.showerror("خطأ", f"المزارع {name} غير موجود")
# #                 return

# #             total = qty * price
# #             time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
# #             self.farmers[name]["balance"] += total

# #             ros = qty if qat_type == "روس" else ""
# #             naqfa = qty if qat_type == "نقفة" else ""
# #             awarid = qty if qat_type == "عوارض" else ""

# #             self.farmers[name]["transactions"].append(
# #                 (self.farmers[name]["balance"], time_now, total, price, ros, naqfa, awarid)
# #             )
# #             self.show_farmer_data()
# #             messagebox.showinfo("تم", f"تم إضافة {qty} {qat_type} بسعر {price} للمزارع {name}")

# #         except Exception as e:
# #             messagebox.showerror("خطأ", f"لم أتمكن من فهم الأمر الصوتي\n{e}")

# #     # ------------------ دفع للمزارع ------------------
# #     def pay_farmer(self):
# #         name = self.farmer_select.get()
# #         if not name:
# #             messagebox.showerror("خطأ", "اختر المزارع أولاً")
# #             return

# #         try:
# #             amount = int(self.pay_entry.get())
# #         except ValueError:
# #             messagebox.showerror("خطأ", "أدخل مبلغ صحيح")
# #             return

# #         if amount > self.farmers[name]["balance"]:
# #             messagebox.showerror("خطأ", "المبلغ أكبر من الرصيد")
# #             return

# #         time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
# #         self.farmers[name]["balance"] -= amount
# #         self.farmers[name]["transactions"].append((self.farmers[name]["balance"], time_now, amount, "-", "", "", ""))
# #         self.show_farmer_data()

# #     # ------------------ عرض بيانات المزارع ------------------
# #     def show_farmer_data(self, name=None):
# #         if not name:
# #             name = self.farmer_select.get()
# #         if not name:
# #             return
# #         # مسح الجدول
# #         for row in self.tree.get_children():
# #             self.tree.delete(row)
# #         # عرض بيانات المزارع
# #         for t in self.farmers[name]["transactions"]:
# #             self.tree.insert("", "end", values=t)


# # # ------------------ تشغيل التطبيق ------------------
# # root = tk.Tk()
# # app = FarmerAccountApp(root)
# # root.mainloop()








# # # from vosk import Model, KaldiRecognizer
# # # import sounddevice as sd
# # # import json

# # # # تحميل الموديل
# # # model = Model(r"C:\vosk_models\vosk-model-ar-mgb2-0.4")

# # # # ضبط التعرف الصوتي
# # # rec = KaldiRecognizer(model, 16000)

# # # def callback(indata, frames, time, status):
# # #     if rec.AcceptWaveform(indata):
# # #         result = json.loads(rec.Result())
# # #         print(result['text'])

# # # # التسجيل من المايكروفون
# # # with sd.InputStream(samplerate=16000, channels=1, callback=callback):
# # #     print("ابدأ التكلم… اضغط Ctrl+C للإيقاف")
# # #     import time
# # #     while True:
# # #         time.sleep(1)



# # # # import sounddevice as sd
# # # # from vosk import Model, KaldiRecognizer
# # # # import json

# # # # model = Model("C:/vosk_models/vosk-model-ar-mgb2-0.4")
# # # # rec = KaldiRecognizer(model, 16000)

# # # # print("🎤 تحدث الآن ... Ctrl+C للخروج")

# # # # with sd.RawInputStream(
# # # #     dtype='int16',
# # # #     channels=1
# # # # ) as stream:    
# # # #      while True:
# # # #         data, _ = stream.read(4000)
# # # #         if rec.AcceptWaveform(bytes(data)):
# # # #             result = json.loads(rec.Result())
# # # #             print("✔️", result.get("text", ""))
# # # #         else:
# # # #             partial = json.loads(rec.PartialResult())
# # # #             print("…", partial.get("partial", ""))










# # # import sounddevice as sd
# # # from vosk import Model, KaldiRecognizer
# # # import json

# # # model = Model("C:/vosk_models/vosk-model-ar-mgb2-0.4")

# # # device_info = sd.query_devices(None, 'input')
# # # samplerate = int(device_info['default_samplerate'])

# # # rec = KaldiRecognizer(model, samplerate)

# # # def callback(indata, frames, time, status):
# # #     if status:
# # #         print(status)

# # #     data = bytes(indata)  # ← الحل هنا ✔️

# # #     if rec.AcceptWaveform(data):
# # #         result = json.loads(rec.Result())
# # #         if result.get("text"):
# # #             print("✔️", result["text"])
# # #     else:
# # #         partial = json.loads(rec.PartialResult())
# # #         if partial.get("partial"):
# # #             print("…", partial["partial"])

# # # print("🎤 تحدث الآن ... Ctrl+C للخروج")

# # # with sd.RawInputStream(
# # #     samplerate=samplerate,
# # #     blocksize=8000,
# # #     dtype='int16',
# # #     channels=1,
# # #     callback=callback
# # # ):
# # #     while True:
# # #         sd.sleep(1000)













# import sounddevice as sd
# import json
# from vosk import Model, KaldiRecognizer

# MODEL_PATH = "C:/vosk_models/vosk-model-ar-mgb2-0.4"
# SAMPLE_RATE = 16000

# model = Model(MODEL_PATH)
# rec = KaldiRecognizer(model, SAMPLE_RATE)

# def callback(indata, frames, time, status):
#     if status:
#         print(status)

#     data = bytes(indata)  # ⭐ الحل السحري
#     if rec.AcceptWaveform(data):
#         result = json.loads(rec.Result())
#         if result.get("text"):
#             print("📝", result["text"])
#     else:
#         partial = json.loads(rec.PartialResult())
#         if partial.get("partial"):
#             print("…", partial["partial"], end="\r")

# print("🎤 تحدث الآن ... Ctrl+C للخروج")

# with sd.RawInputStream(
#     samplerate=SAMPLE_RATE,
#     blocksize=8000,
#     dtype="int16",
#     channels=1,
#     callback=callback
# ):
#     while True:
#         pass





import sounddevice as sd
import json
import queue
from vosk import Model, KaldiRecognizer

# ================== الإعدادات ==================
MODEL_PATH = r"C:\vosk_models\vosk-model-ar-mgb2-0.4"
SAMPLE_RATE = 16000

# قوائم مسموحة فقط
NAMES = ["أكرم", "سند", "مهند", "يحيى", "عبدالله"]
TYPES = ["روس", "عوارض", "نقفة"]
NUMBERS = {
    "واحد": 1, "اثنين": 2, "ثلاثة": 3, "أربعة": 4, "خمسة": 5,
    "عشرة": 10, "عشرين": 20, "ثلاثين": 30, "خمسين": 50, "مئة": 100
}

q = queue.Queue()

# ================== الصوت ==================
def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))

# ================== التعرف ==================
def listen(grammar_words):
    grammar = json.dumps(grammar_words, ensure_ascii=False)
    rec = KaldiRecognizer(model, SAMPLE_RATE, grammar)
    with sd.RawInputStream(samplerate=SAMPLE_RATE,
                           blocksize=8000,
                           dtype='int16',
                           channels=1,
                           callback=callback):
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                res = json.loads(rec.Result())
                text = res.get("text", "").strip()
                if text:
                    return text

# ================== التشغيل ==================
print("🔄 تحميل النموذج...")
model = Model(MODEL_PATH)

record = {}

print("🎤 اذكر اسم المزارع:")
record["اسم_المزارع"] = listen(NAMES)
print("✔️", record["اسم_المزارع"])

print("🎤 نوع القات (روس / عوارض / نقفة):")
record["النوع"] = listen(TYPES)
print("✔️", record["النوع"])

print("🎤 الكمية:")
qty_word = listen(list(NUMBERS.keys()))
record["الكمية"] = NUMBERS.get(qty_word, qty_word)
print("✔️", record["الكمية"])

print("🎤 القيمة:")
price_word = listen(list(NUMBERS.keys()))
record["القيمة"] = NUMBERS.get(price_word, price_word)
print("✔️", record["القيمة"])

print("\n📝 النتيجة النهائية:")
print(record)
