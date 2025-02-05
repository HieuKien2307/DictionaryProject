from database import get_connection

def register_user():
    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()
    
    username = input("Nhập tên đăng nhập: ")
    password = input("Nhập mật khẩu: ")

    try:
        cursor.execute("INSERT INTO Users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("Đăng ký thành công!")
    except Exception as e:
        print(f"Lỗi: {e}")
    finally:
        conn.close()

def login_user():
    conn = get_connection()
    if not conn:
        return None
    cursor = conn.cursor()

    username = input("Nhập tên đăng nhập: ")
    password = input("Nhập mật khẩu: ")

    cursor.execute("SELECT user_id FROM Users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        print("Đăng nhập thành công!")
        return user[0]
    else:
        print("Tên đăng nhập hoặc mật khẩu không đúng.")
        return None
    
import tkinter as tk
from tkinter import messagebox
import pyodbc
from database import get_connection

def register_user_gui(root):
    """Giao diện đăng ký người dùng."""
    register_window = tk.Toplevel(root)
    register_window.title("Đăng ký người dùng")

    tk.Label(register_window, text="Tên đăng nhập:").grid(row=0, column=0)
    username_entry = tk.Entry(register_window)
    username_entry.grid(row=0, column=1)

    tk.Label(register_window, text="Mật khẩu:").grid(row=1, column=0)
    password_entry = tk.Entry(register_window, show="*")
    password_entry.grid(row=1, column=1)

    def submit_registration():
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        if len(password) < 6 or not password.isalnum():
            messagebox.showerror("Lỗi", "Mật khẩu phải có ít nhất 6 ký tự và chỉ chứa chữ hoặc số.")
            return

        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO Users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            messagebox.showinfo("Thành công", "Đăng ký thành công!")
            register_window.destroy()
        except pyodbc.IntegrityError:
            messagebox.showerror("Lỗi", "Tên đăng nhập đã tồn tại.")
        finally:
            conn.close()

    tk.Button(register_window, text="Đăng ký", command=submit_registration).grid(row=2, columnspan=2)

def login_user_gui(root):
    """Giao diện đăng nhập người dùng."""
    login_window = tk.Toplevel(root)
    login_window.title("Đăng nhập")

    tk.Label(login_window, text="Tên đăng nhập:").grid(row=0, column=0)
    username_entry = tk.Entry(login_window)
    username_entry.grid(row=0, column=1)

    tk.Label(login_window, text="Mật khẩu:").grid(row=1, column=0)
    password_entry = tk.Entry(login_window, show="*")
    password_entry.grid(row=1, column=1)

    def submit_login():
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM Users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            messagebox.showinfo("Thành công", "Đăng nhập thành công!")
            login_window.destroy()
        else:
            messagebox.showerror("Lỗi", "Tên đăng nhập hoặc mật khẩu không đúng.")

    tk.Button(login_window, text="Đăng nhập", command=submit_login).grid(row=2, columnspan=2)

