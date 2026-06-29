import customtkinter as ctk
import sqlite3
import hashlib
from tkinter import messagebox
import pandas as pd
from tkinter import filedialog

# ===== APRIORI =====
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# ===== DB =====
conn = sqlite3.connect("app.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    role TEXT
)
""")
conn.commit()


# ===== HASH PASSWORD =====
def hash_password(p):
    return hashlib.sha256(p.encode()).hexdigest()


# ===== APP =====
class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Hệ thống phân tích giỏ hàng")
        self.geometry("1000x600")

        self.show_login()

    # ===== CLEAR SCREEN =====
    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()

    # ===== LOGIN =====
    def show_login(self):

        self.clear()

        frame = ctk.CTkFrame(self)
        frame.pack(expand=True)

        ctk.CTkLabel(
            frame,
            text="Đăng nhập",
            font=("Arial", 24)
        ).pack(pady=20)

        self.user_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Username",
            width=250
        )
        self.user_entry.pack(pady=10)

        self.pass_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Password",
            show="*",
            width=250
        )
        self.pass_entry.pack(pady=10)

        ctk.CTkButton(
            frame,
            text="Đăng nhập",
            command=self.login
        ).pack(pady=10)

        ctk.CTkButton(
            frame,
            text="Đăng ký",
            command=self.show_register
        ).pack()

    # ===== REGISTER =====
    def show_register(self):

        self.clear()

        frame = ctk.CTkFrame(self)
        frame.pack(expand=True)

        ctk.CTkLabel(
            frame,
            text="Đăng ký",
            font=("Arial", 24)
        ).pack(pady=20)

        self.reg_user = ctk.CTkEntry(
            frame,
            placeholder_text="Username",
            width=250
        )
        self.reg_user.pack(pady=10)

        self.reg_pass = ctk.CTkEntry(
            frame,
            placeholder_text="Password",
            show="*",
            width=250
        )
        self.reg_pass.pack(pady=10)

        self.role = ctk.StringVar(value="staff")

        ctk.CTkRadioButton(
            frame,
            text="Nhân viên",
            variable=self.role,
            value="staff"
        ).pack()

        ctk.CTkRadioButton(
            frame,
            text="Admin",
            variable=self.role,
            value="admin"
        ).pack()

        ctk.CTkButton(
            frame,
            text="Đăng ký",
            command=self.register
        ).pack(pady=10)

        ctk.CTkButton(
            frame,
            text="Quay lại",
            command=self.show_login
        ).pack()

    # ===== REGISTER FUNCTION =====
    def register(self):

        try:

            cursor.execute(
                "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                (
                    self.reg_user.get(),
                    hash_password(self.reg_pass.get()),
                    self.role.get()
                )
            )

            conn.commit()

            messagebox.showinfo(
                "OK",
                "Đăng ký thành công"
            )

            self.show_login()

        except:
            messagebox.showerror(
                "Lỗi",
                "User đã tồn tại"
            )

    # ===== LOGIN FUNCTION =====
    def login(self):

        cursor.execute(
            "SELECT role FROM users WHERE username=? AND password=?",
            (
                self.user_entry.get(),
                hash_password(self.pass_entry.get())
            )
        )

        result = cursor.fetchone()

        if result:
            self.show_dashboard(result[0])

        else:
            messagebox.showerror(
                "Sai",
                "Sai tài khoản"
            )

    # ===== DASHBOARD =====
    def show_dashboard(self, role):

        self.clear()

        # ===== SIDEBAR =====
        sidebar = ctk.CTkFrame(self, width=220)
        sidebar.pack(side="left", fill="y")

        # ===== MAIN =====
        main = ctk.CTkFrame(self)
        main.pack(side="right", expand=True, fill="both")

        ctk.CTkLabel(
            sidebar,
            text="MENU",
            font=("Arial", 20)
        ).pack(pady=20)

        ctk.CTkButton(
            sidebar,
            text="Dashboard"
        ).pack(pady=10)

        # ===== ADMIN =====
        if role == "admin":

            ctk.CTkButton(
                sidebar,
                text="Quản lý User",
                command=self.user_manager
            ).pack(pady=10)

            ctk.CTkButton(
                sidebar,
                text="Upload CSV",
                command=lambda: self.upload_csv(main)
            ).pack(pady=10)

            # ===== NÚT ENCODE =====
            ctk.CTkButton(
                sidebar,
                text="Encode Data",
                command=lambda: self.encode_data(main)
            ).pack(pady=10)

            # ===== THAM SỐ THUẬT TOÁN =====
            ctk.CTkLabel(
                sidebar,
                text="Min Support"
            ).pack(pady=(20, 5))

            self.support_entry = ctk.CTkEntry(sidebar)
            self.support_entry.insert(0, "0.01")
            self.support_entry.pack(pady=5)

            ctk.CTkLabel(
                sidebar,
                text="Min Confidence"
            ).pack(pady=(20, 5))

            self.conf_entry = ctk.CTkEntry(sidebar)
            self.conf_entry.insert(0, "0.2")
            self.conf_entry.pack(pady=5)

            # ===== RUN APRIORI =====
            ctk.CTkButton(
                sidebar,
                text="Chạy Apriori",
                command=lambda: self.run_apriori(main)
            ).pack(pady=20)

        # ===== LOGOUT =====
        ctk.CTkButton(
            sidebar,
            text="Đăng xuất",
            command=self.show_login
        ).pack(side="bottom", pady=20)

        # ===== MAIN TITLE =====
        ctk.CTkLabel(
            main,
            text=f"Xin chào ({role})",
            font=("Arial", 24)
        ).pack(pady=20)

    # ===== USER MANAGER =====
    def user_manager(self):

        top = ctk.CTkToplevel(self)
        top.title("User Manager")
        top.geometry("300x300")

        users = cursor.execute(
            "SELECT username, role FROM users"
        ).fetchall()

        for u in users:

            ctk.CTkLabel(
                top,
                text=f"{u[0]} - {u[1]}"
            ).pack(pady=5)

    # ===== UPLOAD CSV =====
    def upload_csv(self, parent_frame):

        file_path = filedialog.askopenfilename(
            filetypes=[("CSV files", "*.csv")]
        )

        if not file_path:
            return

        try:

            # ===== READ CSV =====
            self.df = pd.read_csv(file_path)

            # ===== SHOW TABLE =====
            self.show_table(parent_frame, self.df)

            messagebox.showinfo(
                "OK",
                "Upload CSV thành công"
            )

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                str(e)
            )

    # ===== SHOW TABLE =====
    def show_table(self, parent_frame, df):

        for widget in parent_frame.winfo_children():
            widget.destroy()

        frame = ctk.CTkScrollableFrame(parent_frame)
        frame.pack(expand=True, fill="both")

        # ===== HEADER =====
        for col_index, col_name in enumerate(df.columns):

            label = ctk.CTkLabel(
                frame,
                text=col_name,
                font=("Arial", 12, "bold")
            )

            label.grid(
                row=0,
                column=col_index,
                padx=10,
                pady=5
            )

        # ===== DATA =====
        for row_index, row in df.iterrows():

            for col_index, value in enumerate(row):

                label = ctk.CTkLabel(
                    frame,
                    text=str(value)
                )

                label.grid(
                    row=row_index + 1,
                    column=col_index,
                    padx=10,
                    pady=5
                )

    # ===== ENCODE DATA =====
    def encode_data(self, parent_frame):

        # ===== CHECK CSV =====
        if not hasattr(self, 'df'):

            messagebox.showerror(
                "Lỗi",
                "Vui lòng upload CSV trước"
            )

            return

        try:

            # ===== LẤY PRODUCTS =====
            transactions = self.df['Products'].apply(eval).tolist()

            # ===== ENCODE =====
            te = TransactionEncoder()

            te_array = te.fit(transactions).transform(transactions)

            df_encoded = pd.DataFrame(
                te_array,
                columns=te.columns_
            )

            # ===== SHOW TABLE =====
            self.show_table(parent_frame, df_encoded)

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                str(e)
            )

    # ===== RUN APRIORI =====
    def run_apriori(self, parent_frame):

        # ===== CHECK CSV =====
        if not hasattr(self, 'df'):

            messagebox.showerror(
                "Lỗi",
                "Vui lòng upload CSV trước"
            )

            return

        try:

            # ===== GET PARAM =====
            min_support = float(self.support_entry.get())
            min_confidence = float(self.conf_entry.get())

            # ===== LẤY PRODUCTS =====
            transactions = self.df['Products'].apply(eval).tolist()

            # ===== ENCODE DATA =====
            te = TransactionEncoder()

            te_array = te.fit(transactions).transform(transactions)

            df_encoded = pd.DataFrame(
                te_array,
                columns=te.columns_
            )

            # ===== APRIORI =====
            frequent_itemsets = apriori(
                df_encoded,
                min_support=min_support,
                use_colnames=True
            )

            # ===== CHECK EMPTY =====
            if frequent_itemsets.empty:

                messagebox.showwarning(
                    "Thông báo",
                    "Không tìm thấy tập phổ biến"
                )

                return

            # ===== ASSOCIATION RULE =====
            rules = association_rules(
                frequent_itemsets,
                metric="confidence",
                min_threshold=min_confidence
            )

            # ===== CHECK RULE EMPTY =====
            if rules.empty:

                messagebox.showwarning(
                    "Thông báo",
                    "Không tìm thấy luật kết hợp"
                )

                return

            # ===== SHOW RESULT =====
            self.show_rules(parent_frame, rules)

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                str(e)
            )

    # ===== SHOW RULES =====
    def show_rules(self, parent_frame, rules):

        for widget in parent_frame.winfo_children():
            widget.destroy()

        frame = ctk.CTkScrollableFrame(parent_frame)
        frame.pack(expand=True, fill="both")

        headers = [
            "Antecedents",
            "Consequents",
            "Support",
            "Confidence",
            "Lift"
        ]

        # ===== HEADER =====
        for col_index, header in enumerate(headers):

            label = ctk.CTkLabel(
                frame,
                text=header,
                font=("Arial", 12, "bold")
            )

            label.grid(
                row=0,
                column=col_index,
                padx=10,
                pady=5
            )

        # ===== DATA =====
        for row_index, row in rules.iterrows():

            antecedent = ', '.join(
                list(row['antecedents'])
            )

            consequent = ', '.join(
                list(row['consequents'])
            )

            data = [
                antecedent,
                consequent,
                round(row['support'], 3),
                round(row['confidence'], 3),
                round(row['lift'], 3)
            ]

            for col_index, value in enumerate(data):

                label = ctk.CTkLabel(
                    frame,
                    text=str(value)
                )

                label.grid(
                    row=row_index + 1,
                    column=col_index,
                    padx=10,
                    pady=5
                )


# ===== RUN APP =====
app = App()
app.mainloop()