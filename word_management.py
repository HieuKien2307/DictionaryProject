from database import get_connection
from tkinter import messagebox
import tkinter as tk
import pyodbc

def add_word(user_id):
    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()

    word = input("Nhập từ: ")
    definition = input("Nhập nghĩa: ")

    if not word.strip():
        print("Từ không được để trống.")
        return

    try:
        cursor.execute("INSERT INTO Words (word, definition) VALUES (?, ?)", (word, definition))
        word_id = cursor.execute("SELECT SCOPE_IDENTITY()").fetchone()[0]
        cursor.execute("INSERT INTO UserDictionary (user_id, word_id) VALUES (?, ?)", (user_id, word_id))
        conn.commit()
        print("Thêm từ thành công!")
    except Exception as e:
        print(f"Lỗi: {e}")
    finally:
        conn.close()

def update_word(user_id):
    """Cập nhật thông tin của một từ trong từ điển."""
    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()

    word = input("Nhập từ cần cập nhật: ")
    cursor.execute("SELECT word_id FROM Words WHERE word = ?", (word,))
    word_data = cursor.fetchone()

    if not word_data:
        print("Không tìm thấy từ.")
        return

    word_id = word_data[0]
    new_definition = input("Nhập nghĩa mới (hoặc để trống để giữ nguyên): ")
    new_example = input("Nhập ví dụ mới (hoặc để trống để giữ nguyên): ")

    try:
        if new_definition.strip():
            cursor.execute("UPDATE Words SET definition = ? WHERE word_id = ?", (new_definition, word_id))
        if new_example.strip():
            cursor.execute("UPDATE Words SET example = ? WHERE word_id = ?", (new_example, word_id))
        conn.commit()
        print("Cập nhật thành công!")
    except Exception as e:
        print(f"Lỗi: {e}")
    finally:
        conn.close()


# Trong word_management.py
def search_word(search_term):
    """Hàm tìm kiếm từ trong cơ sở dữ liệu."""
    conn = get_connection()
    if not conn:
        return None
    cursor = conn.cursor()
    cursor.execute("SELECT definition FROM Words WHERE word = ?", (search_term,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]  # Trả về nghĩa của từ
    return None  # Không tìm thấy từ


def add_word_gui(root):
    """Giao diện thêm từ vào từ điển."""
    add_window = tk.Toplevel(root)
    add_window.title("Thêm từ mới")

    tk.Label(add_window, text="Từ:").grid(row=0, column=0)
    word_entry = tk.Entry(add_window)
    word_entry.grid(row=0, column=1)

    tk.Label(add_window, text="Nghĩa:").grid(row=1, column=0)
    definition_entry = tk.Entry(add_window)
    definition_entry.grid(row=1, column=1)

    def submit_word():
        word = word_entry.get().strip()
        definition = definition_entry.get().strip()

        if not word or not definition:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin.")
            return

        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO Words (word, definition) VALUES (?, ?)", (word, definition))
            conn.commit()
            messagebox.showinfo("Thành công", "Thêm từ thành công!")
            add_window.destroy()
        except pyodbc.Error as e:
            messagebox.showerror("Lỗi", f"Lỗi khi thêm từ: {e}")
        finally:
            conn.close()

    tk.Button(add_window, text="Thêm", command=submit_word).grid(row=2, columnspan=2)

# Trong word_management.py
# Trong word_management.py
def search_word_gui(root):
    """Giao diện tìm kiếm từ trong từ điển."""
    search_window = tk.Toplevel(root)
    search_window.title("Tìm kiếm từ")

    tk.Label(search_window, text="Từ cần tìm:").grid(row=0, column=0)
    search_entry = tk.Entry(search_window)
    search_entry.grid(row=0, column=1)

    # Cập nhật command để truyền search_entry vào submit_search
    def submit_search():
        search_term = search_entry.get().strip()
        if not search_term:
            messagebox.showerror("Lỗi", "Vui lòng nhập từ cần tìm.")
            return

        # Gọi hàm search_word và truyền vào search_term
        meaning = search_word(search_term)

        if meaning:
            messagebox.showinfo("Kết quả tìm kiếm", f"Nghĩa của từ '{search_term}': {meaning}")
        else:
            messagebox.showerror("Lỗi", "Không tìm thấy từ này trong từ điển.")

    tk.Button(search_window, text="Tìm kiếm", command=submit_search).grid(row=1, columnspan=2)



