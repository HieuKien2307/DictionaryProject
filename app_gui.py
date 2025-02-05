import tkinter as tk
from tkinter import messagebox
from word_management import add_word_gui, search_word_gui
from user_management import register_user_gui, login_user_gui

class DictionaryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dictionary Application")
        self.geometry("500x400")  # Điều chỉnh kích thước để vừa với tất cả nút

        # Giao diện chính
        self.create_main_menu()

    def create_main_menu(self):
        """Menu chính của ứng dụng."""
        for widget in self.winfo_children():
            widget.destroy()

        title_label = tk.Label(self, text="Dictionary Application", font=("Arial", 18))
        title_label.pack(pady=20)

        register_btn = tk.Button(self, text="Đăng ký", command=self.register)
        register_btn.pack(pady=5)

        login_btn = tk.Button(self, text="Đăng nhập", command=self.login)
        login_btn.pack(pady=5)

        add_word_btn = tk.Button(self, text="Thêm từ", command=self.add_word)
        add_word_btn.pack(pady=5)

        search_word_btn = tk.Button(self, text="Tìm kiếm từ", command=self.search_word)
        search_word_btn.pack(pady=5)

        exit_btn = tk.Button(self, text="Thoát", command=self.quit)
        exit_btn.pack(pady=5)

    def register(self):
        """Giao diện đăng ký."""
        register_user_gui(self)

    def login(self):
        """Giao diện đăng nhập và chuyển sang menu phụ."""
        login_user_gui(self)

    def add_word(self):
        """Giao diện thêm từ vào từ điển."""
        add_word_gui(self)

    def search_word(self):
        """Giao diện tìm kiếm từ trong từ điển."""
        search_word_gui(self)

if __name__ == "__main__":
    app = DictionaryApp()
    app.mainloop()
