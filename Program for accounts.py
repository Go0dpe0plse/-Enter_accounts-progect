import os
import customtkinter as CTk
from pathlib import Path
from PIL import Image
import tkinter as tk

class MyApp(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.first_inspection = None
    
        self.geometry("400x350")
        self.title("Enter account")
        self.resizable(False, False)

        # Список для зберігання введених текстів
        self.ready_accounts = ["Go0dpe0plse",]
        self.ready_login = ["Go0dpe0plse.prog.ua"]
        self.ready_password = ["19112008"]

        self.login_and_password = {}

        # Створення головного вікна зі списком
        self.create_main_window()
    
    def create_main_window(self):
        self.change_appearance_mode_event("Dark")

        # Фрейм для розміщення елементів
        account_frame = CTk.CTkFrame(master=self)
        account_frame.pack(expand=True, fill=CTk.BOTH)
        main_label = CTk.CTkLabel(master=account_frame, text="Увійдіть в акаунт", text_color="#4d94ff", font=("Comfortaa", 42))
        main_label.pack(anchor="center", side="top", pady=(10, 5))

        enter_frame = CTk.CTkFrame(master=account_frame, bg_color="transparent")
        enter_frame.pack(fill="x")

        main_login_label = CTk.CTkLabel(master=enter_frame, text="Введіить логін:", text_color="white", font=("Comfortaa", 18))
        main_login_label.pack(pady=(5, 0))
        self.main_enter_login = CTk.CTkEntry(master=enter_frame, text_color="white", font=("Comfortaa", 20), width=200, height=2)
        self.main_enter_login.pack()
        main_password_label = CTk.CTkLabel(master=enter_frame, text="Введіить пароль:", text_color="white", font=("Comfortaa", 18))
        main_password_label.pack(pady=(5, 0))
        self.main_enter_password = CTk.CTkEntry(master=enter_frame, text_color="white", show="*", font=("Comfortaa", 20), width=200, height=2)
        self.main_enter_password.pack()

        main_enter_button = CTk.CTkButton(master=enter_frame, text="Увійти", text_color="white", font=("Comfortaa", 18), command=self.inspection_window)
        main_enter_button.pack(pady=(5, 0))
    
        
        new_window_button = CTk.CTkButton(master=account_frame, text="Створить новий акаунт", text_color="white", command=self.open_name_window, font=("Comfortaa", 23), height=2)
        new_window_button.pack(anchor="s",padx=(0, 0), side="bottom")
        create_new_account_label = CTk.CTkLabel(master=account_frame, text="Не маєте акаутну?", text_color="#4d94ff", font=("Comfortaa", 18))
        create_new_account_label.pack(anchor="s",padx=(0, 0), side="bottom")
        

        current_file_path = os.path.abspath(__file__)
        image_path = os.path.join(os.path.dirname(current_file_path), "640px-Infobox_info_icon.svg.png")
        self.image_info = CTk.CTkImage(dark_image=Image.open(image_path), size=(50, 50))



        main_button_info = CTk.CTkButton(master=self, image=self.image_info, text="", width=40, height=50, command=self.open_info_window)
        main_button_info.pack(anchor="se")


    def open_info_window(self):
        self.info_window = CTk.CTkToplevel(self)

        self.info_window.geometry("800x400")
        self.info_window.title("Information")
        self.info_window.resizable(False, False)

        info_frame = CTk.CTkFrame(master=self.info_window)
        info_frame.pack(expand=True, fill=CTk.BOTH)

        first_info_label = CTk.CTkLabel(master=info_frame, text="Для того щоб створити акаунт вам потрібно створити:", text_color="white", font=("Comfortaa", 24))
        first_info_label.pack(anchor="center", pady=(5, 0))

        one_label_to_image = CTk.CTkLabel(master=info_frame, text="1.Ім'я\n по якому до вас будуть звератися", text_color="white", font=("Comfortaa", 24))
        one_label_to_image.pack(anchor="center", pady=(10, 0))

        two_label_to_image = CTk.CTkLabel(master=info_frame, text="1.Логін\n в нашому середовищі логін повинен обовязково мати: \n назву, приписку .prog та .ua\n Напиклад: vladnakonechny.prog.ua", text_color="white", font=("Comfortaa", 24))
        two_label_to_image.pack(anchor="center", pady=(10, 0))
        
        one_label_to_image = CTk.CTkLabel(master=info_frame, text="1.Пароль\n в нашому середовищі пароль повинен містити в собі\n не меньше ніж 7 елементів\n й при цьому не допускаєтья використання !@#$%^&*?", text_color="white", font=("Comfortaa", 24))
        one_label_to_image.pack(anchor="center", pady=(10, 0))

        


    def change_appearance_mode_event(self, new_appearance_mode):
        CTk.set_appearance_mode(new_appearance_mode)

    def inspection_window(self):
        first_inspection = self.list_item(self.ready_login, self.main_enter_login.get())
        self.first_inspection = first_inspection
        second_inspection = self.list_item(self.ready_password, self.main_enter_password.get())
        if first_inspection == second_inspection:
            if first_inspection and second_inspection != "error":
                self.open_enter_accounts_window()
        if first_inspection == "error":
            self.open_error_window()



    def open_enter_accounts_window(self):
        self.enter_accounts_window = CTk.CTkToplevel(self)

        self.enter_accounts_window.geometry("360x160")
        self.enter_accounts_window.title("You accounts")

        open_accounts_frame = CTk.CTkFrame(master=self.enter_accounts_window)
        open_accounts_frame.pack(expand=True, fill=CTk.BOTH)

        text = ("Ви увійшли в акунт: ", self.first_inspection)

        open_accounts_label = CTk.CTkLabel(master=open_accounts_frame, text=text, text_color="white", font=("Comfortaa", 24))
        open_accounts_label.pack(anchor="center", pady=(60, 0))



    def open_error_window(self):
        self.error_window = CTk.CTkToplevel(self)

        self.error_window.geometry("150x50")
        self.error_window.title("ERROR")

        font = CTk.CTkFont(family="Comfortaa", size=23)
        font = ("Comfortaa", 23)

        error_frame = CTk.CTkFrame(master=self.error_window)
        error_frame.pack(expand=True, fill=CTk.BOTH)

        error_label = CTk.CTkLabel(master=error_frame, text="ERROR", text_color="red", font=("Comfortaa", 40))
        error_label.pack(anchor="center")

    def list_item(self, input_list, target_element):
        if target_element in input_list:
            index = input_list.index(target_element)
            return self.ready_accounts[index]

        else:
            return "error"

    def open_name_window(self):
        # Створення нового вікна
        self.name_window = CTk.CTkToplevel(self)

        self.name_window.geometry("450x225")
        self.name_window.title("Create name")

        font = CTk.CTkFont(family="Comfortaa", size=23)
        font = ("Comfortaa", 23)

        # Фрейм для розміщення елементів
        create_name_frame = CTk.CTkFrame(master=self.name_window)
        self.create_name_frame = create_name_frame
        create_name_frame.pack(expand=True, fill=CTk.BOTH)

        label_name = CTk.CTkLabel(master=create_name_frame, text="Create accounts name", text_color="#4d94ff", font=("Comfortaa", 25))
        label_name.pack(pady=10)

        # Текстове поле для введення тексту
        create_name = CTk.CTkEntry(master=create_name_frame, font=("Comfortaa", 15))
        create_name.pack(pady=10,)

        # Кнопка для додавання тексту до списку в головному вікні
        addName_button = CTk.CTkButton(master=create_name_frame, text="Enter", command=lambda: self.add_name(create_name.get()))
        addName_button.pack()

    def add_name(self, text):
        # Додавання тексту до списку
        if "" != text:
            if " " != text:
                self.ready_accounts.append(text)
                self.name_window.destroy()
                self.open_login_window()
        else:
            self.name_window.destroy()
            self.open_name_window()
            Syntax_error = CTk.CTkLabel(master=self.create_name_frame, text="Введіть ваше ім'я", text_color="red", font=("Comfortaa", 20))
            Syntax_error.pack(pady=10)


    def open_login_window(self):
        # Створення нового вікна
        self.create_login_func()
    def create_login_func(self):
        self.login_window = CTk.CTkToplevel(self)

        self.login_window.geometry("450x225")
        self.login_window.title("Create login")

        font = CTk.CTkFont(family="Comfortaa", size=23)
        font = ("Comfortaa", 23)

        # Фрейм для розміщення елементів
        create_login_frame = CTk.CTkFrame(master=self.login_window)
        self.create_login_frame = create_login_frame
        create_login_frame.pack(expand=True, fill=CTk.BOTH)

        label_login = CTk.CTkLabel(master=create_login_frame, text="Create your login", text_color="#4d94ff", font=("Comfortaa", 25))
        label_login.pack(pady=10)

        # Текстове поле для введення тексту
        create_login = CTk.CTkEntry(master=create_login_frame, font=("Comfortaa", 15), width=250)
        create_login.pack(pady=10,)

        addLogin_button = CTk.CTkButton(master=create_login_frame, text="Enter", command=lambda: self.add_login(create_login.get()))
        addLogin_button.pack()

    def add_login(self, text):
        if ".prog" in text:
            if ".ua" in text:
                if "" != text:
                    if " " != text:
                        self.ready_login.append(text)
                        self.login_window.destroy()
                        self.open_password_window()
        else:
            self.login_window.destroy()
            self.create_login_func()
            Syntax_error = CTk.CTkLabel(master=self.create_login_frame, text="Введіть ім'я логіну\n та добавте приписку '.prog.ua'\n Наприклад: vladnakonecny.prog.ua", text_color="red", font=("Comfortaa", 20))
            Syntax_error.pack(pady=10)

    def open_password_window(self):
        
        self.password_window = CTk.CTkToplevel(self)

        self.password_window.geometry("450x225")
        self.password_window.title("Create password")
        font = CTk.CTkFont(family="Comfortaa", size=23)
        font = ("Comfortaa", 23)

        # Фрейм для розміщення елементів
        create_password_frame = CTk.CTkFrame(master=self.password_window)
        self.create_password_frame = create_password_frame
        create_password_frame.pack(expand=True, fill=CTk.BOTH)

        label_password = CTk.CTkLabel(master=create_password_frame, text="Create your password", text_color="#4d94ff", font=("Comfortaa", 25))
        label_password.pack(pady=10)

        # Текстове поле для введення тексту
        create_password = CTk.CTkEntry(master=create_password_frame, show = "*", font=("Comfortaa", 15))
        create_password.pack(pady=10)

        # Кнопка для додавання тексту до списку в головному вікні
        addPassword_button = CTk.CTkButton(master=create_password_frame, text="Enter", command=lambda: self.add_password(create_password.get()))
        addPassword_button.pack()

    def add_password(self, text):
        if len(text) >= 7:
            if " " != text:
                if "" != text:
                    self.password = text
                    self.ready_password.append(text)  
                    self.password_window.destroy()  
                    self.сonfirmation_password()    
        else:
            self.password_window.destroy()
            self.open_password_window()
            Syntax_error = CTk.CTkLabel(master=self.create_password_frame, text="Пароль повинен бути не меньше ніж 7 символів\n та не повинен включати символи !@#$%^&*?", text_color="red", font=("Comfortaa", 20))
            Syntax_error.pack(pady=10)
    def сonfirmation_password(self):
        self.confirm_password_window = CTk.CTkToplevel(self)

        self.confirm_password_window.geometry("450x225")
        self.confirm_password_window.title("Confirm password")
        font = CTk.CTkFont(family="Comfortaa", size=23)
        font = ("Comfortaa", 23)

        # Фрейм для розміщення елементів
        create_confirm_password_frame = CTk.CTkFrame(master=self.confirm_password_window)
        self.create_confirm_password_frame = create_confirm_password_frame
        create_confirm_password_frame.pack(expand=True, fill=CTk.BOTH)

        label_confirm_password = CTk.CTkLabel(master=create_confirm_password_frame, text="Confirm your password", text_color="#4d94ff", font=("Comfortaa", 25))
        label_confirm_password.pack(pady=10)

        # Текстове поле для введення тексту
        create_confirm_password = CTk.CTkEntry(master=create_confirm_password_frame, show = "*", font=("Comfortaa", 15))
        create_confirm_password.pack(pady=10)

        # Кнопка для додавання тексту до списку в головному вікні
        addconfirm_Password_button = CTk.CTkButton(master=create_confirm_password_frame, text="Enter", command=lambda: self.add_confirm_password(create_confirm_password.get()))
        addconfirm_Password_button.pack()

    def add_confirm_password(self, text):
        if self.password == text:
            self.ready_password.append(text)
            self.confirm_password_window.destroy()
        else:
            self.confirm_password_window.destroy()
            self.сonfirmation_password()
            Syntax_error = CTk.CTkLabel(master=self.create_confirm_password_frame, text="Паролі не співпадають, спорбуйте ще раз або\n натисність на 'повторно створить пароль'", text_color="red", font=("Comfortaa", 20))
            Syntax_error.pack(pady=10)
            return_create_passwrod_button = CTk.CTkButton(master=self.create_confirm_password_frame, text="повторно створить пароль", command=self.return_to_create_password,text_color="white", font=("Comfortaa", 20))
            return_create_passwrod_button.pack()

    def return_to_create_password(self):
        self.confirm_password_window.destroy()
        self.open_password_window()
                
                    

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
