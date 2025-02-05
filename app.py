from user_management import register_user, login_user
from word_management import add_word, update_word, search_word
from report_management import report_most_searched_words

def main_menu():
    while True:
        print("\n--- MENU CHÍNH ---")
        print("1. Đăng ký")
        print("2. Đăng nhập")
        print("3. Tìm kiếm từ")
        print("4. Báo cáo")
        print("5. Thoát")
        choice = input("Chọn một tùy chọn: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            user_id = login_user()
            if user_id:
                print("\nĐăng nhập thành công!")
                while True:
                    print("\n--- MENU PHỤ ---")
                    print("1. Thêm từ")
                    print("2. Cập nhật từ")
                    print("3. Đăng xuất")
                    sub_choice = input("Chọn một tùy chọn: ")

                    if sub_choice == "1":
                        add_word(user_id)
                    elif sub_choice == "2":
                        update_word(user_id)
                    elif sub_choice == "3":
                        print("Đăng xuất thành công!")
                        break
                    else:
                        print("Lựa chọn không hợp lệ.")
        elif choice == "3":
            search_word()
        elif choice == "4":
            report_most_searched_words()
        elif choice == "5":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main_menu()
