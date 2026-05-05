import customtkinter as ctk
import sqlite3
import hashlib
from tkinter import messagebox
import pandas as pd
from tkinter import filedialog

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

def hash_password(p):
    return hashlib.sha256(p.encode()).hexdigest()

# ===== APP =====
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Hệ thống phân tích")
        self.geometry("700x500")

        self.show_login()

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()

    # ===== LOGIN =====
    def show_login(self):
        self.clear()

        frame = ctk.CTkFrame(self)
        frame.pack(expand=True)

        ctk.CTkLabel(frame, text="Đăng nhập", font=("Arial", 20)).pack(pady=10)

        self.user_entry = ctk.CTkEntry(frame, placeholder_text="Username")
        self.user_entry.pack(pady=5)

        self.pass_entry = ctk.CTkEntry(frame, placeholder_text="Password", show="*")
        self.pass_entry.pack(pady=5)

        ctk.CTkButton(frame, text="Đăng nhập", command=self.login).pack(pady=10)
        ctk.CTkButton(frame, text="Đăng ký", command=self.show_register).pack()

    # ===== REGISTER =====
    def show_register(self):
        self.clear()

        frame = ctk.CTkFrame(self)
        frame.pack(expand=True)

        ctk.CTkLabel(frame, text="Đăng ký", font=("Arial", 20)).pack(pady=10)

        self.reg_user = ctk.CTkEntry(frame, placeholder_text="Username")
        self.reg_user.pack(pady=5)

        self.reg_pass = ctk.CTkEntry(frame, placeholder_text="Password", show="*")
        self.reg_pass.pack(pady=5)

        self.role = ctk.StringVar(value="staff")

        ctk.CTkRadioButton(frame, text="Nhân viên", variable=self.role, value="staff").pack()
        ctk.CTkRadioButton(frame, text="Admin", variable=self.role, value="admin").pack()

        ctk.CTkButton(frame, text="Đăng ký", command=self.register).pack(pady=10)
        ctk.CTkButton(frame, text="Quay lại", command=self.show_login).pack()

    def register(self):
        try:
            cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                           (self.reg_user.get(), hash_password(self.reg_pass.get()), self.role.get()))
            conn.commit()
            messagebox.showinfo("OK", "Đăng ký thành công")
            self.show_login()
        except:
            messagebox.showerror("Lỗi", "User đã tồn tại")











    def login(self):
        cursor.execute("SELECT role FROM users WHERE username=? AND password=?",
                       (self.user_entry.get(), hash_password(self.pass_entry.get())))
        result = cursor.fetchone()

        if result:
            self.show_dashboard(result[0])
        else:
            messagebox.showerror("Sai", "Sai tài khoản")

    # ===== DASHBOARD =====
    def show_dashboard(self, role):
        self.clear()

        sidebar = ctk.CTkFrame(self, width=150)
        sidebar.pack(side="left", fill="y")

        main = ctk.CTkFrame(self)
        main.pack(side="right", expand=True, fill="both")

        ctk.CTkLabel(sidebar, text="Menu").pack(pady=10)

        ctk.CTkButton(sidebar, text="Dashboard").pack(pady=5)

        if role == "admin":
            ctk.CTkButton(sidebar, text="Quản lý User", command=self.user_manager).pack(pady=5)
            ctk.CTkButton(sidebar, text="Upload CSV", command=lambda: self.upload_csv(main)).pack(pady=5)

        ctk.CTkButton(sidebar, text="Đăng xuất", command=self.show_login).pack(side="bottom", pady=10)

        ctk.CTkLabel(main, text=f"Xin chào ({role})", font=("Arial", 18)).pack(pady=20)

    # ===== USER MANAGER =====
    def user_manager(self):
        top = ctk.CTkToplevel(self)
        top.title("User Manager")

        users = cursor.execute("SELECT username, role FROM users").fetchall()

        for u in users:
            ctk.CTkLabel(top, text=f"{u[0]} - {u[1]}").pack()

    # ===== UPLOAD CSV =====
    def upload_csv(self, parent_frame):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

        if not file_path:
            return

        try:
            df = pd.read_csv(file_path)
            self.show_table(parent_frame, df)
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    # ===== SHOW TABLE =====
    def show_table(self, parent_frame, df):
        for widget in parent_frame.winfo_children():
            widget.destroy()

        frame = ctk.CTkScrollableFrame(parent_frame)
        frame.pack(expand=True, fill="both")

        # Header
        for col_index, col_name in enumerate(df.columns):
            label = ctk.CTkLabel(frame, text=col_name, font=("Arial", 12, "bold"))
            label.grid(row=0, column=col_index, padx=5, pady=5)

        # Data
        for row_index, row in df.iterrows():
            for col_index, value in enumerate(row):
                label = ctk.CTkLabel(frame, text=str(value))
                label.grid(row=row_index + 1, column=col_index, padx=5, pady=5)

# ===== RUN =====
app = App()
app.mainloop()