import os
from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel, CTkRadioButton,CTkComboBox, CTkScrollableFrame, CTkTabview, CTkOptionMenu, CTkTextbox, CTkCanvas, CTkScrollbar, CTkImage, CTkSwitch, CTkEntry
from tkinter import StringVar
#from settings import selected_language
from converter import start_program, stop_program
from PIL import Image
import customtkinter


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

class LanguageAssistantApp(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500+500+200")
        self.title("Language Assistant")
        self.resizable(False, False)

        self.main_frame = MainFrame(self)
        self.main_frame.pack(side="right", fill="both", expand=True)

        self.menu_frame = MenuFrame(self, self.main_frame)
        self.menu_frame.pack(side="left", fill="y")
        self.menu_frame.configure(width=180, height=600)

        self.mainloop()


class MainFrame(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, corner_radius=0)
        self.pack_propagate(False)


class MenuFrame(CTkFrame):
    def __init__(self, parent, main_frame):
        super().__init__(parent, corner_radius=0)#corner_radius=0
        self.main_frame = main_frame
        self.pack_propagate(False)
        self.rows = []
        self.create_widgets()
        self.create_tabview()

        self.settings = ['Light', 'Green']

    def create_widgets(self):
        self.image_start = CTkImage(Image.open("/Users/annasemenova/Desktop/langAssistant/play-whie.png/Users/annasemenova/Desktop/langAssistant/play-whie.png").resize((35, 35)))
        self.image_stop = CTkImage(Image.open("/Users/annasemenova/Desktop/langAssistant/play-whie.png/Users/annasemenova/Desktop/langAssistant/stop-white.png").resize((35, 35)))

        #logo_image = Image.open("лого.png")
        #logo_image = logo_image.resize((300, 300))
        #self.logo = CTkImage(logo_image)

        #logo_label = CTkLabel(self, image=self.logo, text='')
        #logo_label.place(x=20, y=30)

        general_btn = CTkButton(self, text='Общее', font=('Montserrat', 14),
                                command=self.general_tab)
        general_btn.place(x=20, y=200)


        abbr_btn = CTkButton(self, text='Автозамена', font=('Montserrat', 14),
                             command=self.abbr_tab)
        abbr_btn.place(x=20, y=270)

        translator_btn = CTkButton(self, text='Конвертация', font=('Montserrat', 14),
                                   command=self.translator_tab)
        translator_btn.place(x=20, y=340)

        start_button = CTkButton(self, text="", width=35, height=35, image=self.image_start,
                                 command=start_program)
        start_button.place(x=40, y=430)

        start_button = CTkButton(self, text="", width=35, height=35, image=self.image_stop,
                                 )
        start_button.place(x=100, y=430)

    '''def update_canvas_colors(self, mode):
        if mode == "Dark":
            self.canvas.configure(bg="#2b2b2b")
        else:
            self.canvas.configure(bg="#dbdbdb")'''

    def general_tab(self):
        self.clean_page()
        self.create_tabview()

    def create_tabview(self):
        tabview = CTkTabview(self.main_frame)
        tabview.grid(row=0, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        tabview.add("О программе")
        tabview.add("Настройки")
        tabview.add("Помощь")

        tabview.tab("О программе").grid_columnconfigure(0, weight=1)
        tabview.tab("Настройки").grid_columnconfigure(0, weight=1)
        tabview.tab("Помощь").grid_columnconfigure(0, weight=1)

        label_tab_1 = CTkLabel(tabview.tab("О программе"),
                         text='Добро пожаловать в LanguageAssistant – интуитивный инструмент для автоматического распознавания и исправления неправильной раскладки клавиатуры. Удобно определяет сокращения, позволяя пользователям сохранить время и избежать ошибок в наборе текста. Просто начните печатать – и наша программа сделает остальное!',
                        wraplength=340)
        label_tab_1.grid(padx=20, pady=20)

        label_tab_2 = CTkLabel(tabview.tab("О программе"), text="Просто начните печатать – и программа сделает остальное!",
                               wraplength=340)
        label_tab_2.grid(padx=20, pady=20)

        label_tab_3 = CTkLabel(tabview.tab("Настройки"),
                               text="Сменить тему приложения:",
                               wraplength=340)
        label_tab_3.grid(padx=10, pady=10)

        self.appearance_mode_optionemenu = CTkComboBox(tabview.tab("Настройки"), values=["Light", "Dark"],
                                                         command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(padx=10, pady=20)

        label_tab_4 = CTkLabel(tabview.tab("Настройки"),
                               text="Сменить цвет виджетов:",
                               wraplength=340)
        label_tab_4.grid(padx=10, pady=10)

        self.appearance_mode_color = CTkComboBox(tabview.tab("Настройки"), values=["Green", "Blue"],
                                                       command=self.change_color_theme)
        self.appearance_mode_color.grid(padx=10, pady=20)

        label_tab_5 = CTkLabel(tabview.tab("Настройки"),
                               text="Сбросить пользовательские настройки:",
                               wraplength=340)
        label_tab_5.grid(padx=10, pady=10)

        self.string_input_button = CTkButton(tabview.tab("Настройки"), text="Удалить",
                                             command=self.open_reset_dialog)
        self.string_input_button.grid(padx=20, pady=(10, 10))

        '''self.save_button = customtkinter.CTkButton(tabview.tab("Настройки"), text="Сохранить", height=35,
                                              command=self.save_settings())
        self.save_button.grid(padx=20, pady=(135, 10))'''

        settings_text = """
        Как пользоваться:
        
            1. Начните печатать текст.
            2. Если заметили, что текст напечатан неправильной раскладкой, выделите нужную часть.
            3. Скопируйте текст в буфер обмена (Ctrl+C).
            4. Программа автоматически исправит раскладку и сохранит исправленный текст в буфере.
            5. Дождитесь сигнала и просто вставьте исправленный текст (Ctrl+V) – готово!
            """

        label_settings = CTkLabel(tabview.tab("Помощь"), text=settings_text,wraplength=330, justify='left')
        label_settings.grid(row=1, column=0, padx=20, pady=20, sticky="w")

        # Configure grid to expand
        #tabview.tab("Помощь").grid_rowconfigure(1, weight=1)
        tabview.tab("Помощь").grid_columnconfigure(0, weight=1)

        self.load_settings()

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode.lower())
        if len(self.settings) != 0:
            self.settings[0] = new_appearance_mode
        self.save_settings()

    def update_widget_colors(self):
        for widget in self.winfo_children():
            if isinstance(widget, CTkButton):
                if self.appearance_mode_color.get().lower() == "green":
                    widget.configure(fg_color="#2bca85")
                else:
                    widget.configure(fg_color="#258ad6")

    def change_color_theme(self, new_appearance_mode: str):
        customtkinter.set_default_color_theme(new_appearance_mode.lower())

        self.update_widget_colors()

        if len(self.settings) != 0:
            self.settings[1] = new_appearance_mode
        self.save_settings()


    def open_reset_dialog(self):
        dialog = customtkinter.CTkToplevel(self)
        dialog.geometry("470x150+560+300")
        dialog.title("Delete")

        label = customtkinter.CTkLabel(dialog, text="Вы уверены, что хотите сбросить пользовательские настройки?")
        label.pack(pady=20, padx=20)

        button_frame = customtkinter.CTkFrame(dialog, fg_color='transparent')
        button_frame.pack(pady=10)

        delete_button = customtkinter.CTkButton(button_frame, text="Удалить",
                                                command=lambda: self.reset_abbreviations(dialog))
        delete_button.pack(side="left", padx=10)

        cancel_button = customtkinter.CTkButton(button_frame, text="Отмена", command=dialog.destroy)
        cancel_button.pack(side="left", padx=10)

    def reset_abbreviations(self, dialog):
        if os.path.exists("abbreviations.txt"):
            os.remove("abbreviations.txt")
        for row in self.rows:
            row.destroy()
        self.rows = []

        self.scrollable_frame = customtkinter.CTkScrollableFrame(self.main_frame, label_text="Автозамена")

        self.create_initial_row()
        dialog.destroy()

#////////////////////////////'''
    def abbr_tab(self):
        self.clean_page()

        self.scrollable_frame = customtkinter.CTkScrollableFrame(self.main_frame, label_text="Автозамена")
        self.scrollable_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.rows = []

        self.create_abbr_tab(self.scrollable_frame)
        self.load_abbreviations()

        save_button = customtkinter.CTkButton(self.main_frame, text="Сохранить", height=35, command=self.save_abbreviations)
        save_button.pack(side="bottom", pady=35)

        '''spacer = CTkLabel(self.main_frame, text='', wraplength=340)
        spacer.pack(pady=10)'''

    def create_abbr_tab(self, tab):
        label_settings = customtkinter.CTkLabel(tab, text='Введите сокращение и горячую клавишу:', wraplength=340)
        label_settings.pack(pady=10)

    def create_row(self, abbr='', key=''):
        frame_entry = customtkinter.CTkFrame(self.scrollable_frame, fg_color='transparent') #self.scrollable_frame, fg_color='transparent'
        frame_entry.pack(fill="x", padx=10, pady=5)

        entry1 = customtkinter.CTkEntry(frame_entry, width=90)
        entry1.insert(0, abbr)
        entry1.pack(side='left', padx=10, pady=10)

        entry2 = customtkinter.CTkEntry(frame_entry, width=130)
        entry2.insert(0, key)
        entry2.pack(side='left', padx=10, pady=5)

        add_button = customtkinter.CTkButton(frame_entry, text="-", width=30, command=lambda fe=frame_entry: self.remove_row(fe))
        add_button.pack(side='left', padx=5, pady=5)

        remove_button = customtkinter.CTkButton(frame_entry, text="+", width=30, command=self.create_initial_row)
        remove_button.pack(side='left', padx=5, pady=5)

        return frame_entry

    def create_initial_row(self, abbr='', key=''):
        row = self.create_row(abbr, key)
        self.rows.append(row)

    def remove_row(self, frame_entry):
        if len(self.rows) > 1:
            self.rows.remove(frame_entry)
            frame_entry.destroy()

    def load_abbreviations(self):
        if os.path.exists("abbreviations.txt"):
            with open("abbreviations.txt", "r") as file:
                for line in file:
                    if line != '':
                        line = line.split()
                        abbr, key = line[0], ' '.join(line[1:])
                        self.create_initial_row(abbr, key)
        if not self.rows:
            self.create_initial_row()

    def save_abbreviations(self):
        abbreviations = [(row.winfo_children()[0].get(), row.winfo_children()[1].get()) for row in self.rows]
        with open("abbreviations.txt", "w") as file:
            for abbr, key in abbreviations:
                if abbr != '' and key != '':
                    file.write(f"{abbr.lower()} {key}\n")
        print("Abbreviations saved.")


    def load_settings(self):
        if os.path.exists("settings.txt"):
            with open("settings.txt", "r") as file:
                for line in file:
                    if line == "Light" or line == "Dark":
                        self.appearance_mode_optionemenu.set(line)
                        self.change_appearance_mode_event(line)
                    elif line == "Green" or line == "Blue":
                        self.appearance_mode_color.set(line)
                        self.change_color_theme(line)


    def save_settings(self):
        dictionary = []

        dictionary.append(self.settings[0])
        dictionary.append(self.settings[1])
        if hasattr(self, 'layout_switch') and self.layout_switch.winfo_exists():
            dictionary.append(self.layout_switch.get())
        else:
            dictionary.append(0)

        with open("settings.txt", "w") as file:
            for key in dictionary:
                file.write(f"{key}\n")
        print("Settings saved.")


#////////////////////////////'''

    def translator_tab(self):
        self.clean_page()
        tabview = CTkTabview(self.main_frame)
        tabview.grid(row=0, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # Configure grid of main_frame to allow tabview to expand
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        tabview.add("Конвертация")


        tabview.tab("Конвертация").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs

        label_tab_1 = CTkLabel(tabview.tab("Конвертация"),
                               text='Переключать раскладку:',
                               wraplength=340)
        label_tab_1.grid(padx=20, pady=20)

        self.layout_switch = CTkSwitch(tabview.tab("Конвертация"), text="Переключать раскладку", command=self.switch_layout)
        self.layout_switch.grid(padx=20, pady=5,)


    def switch_layout(self):
        switch = self.layout_switch.get()
        print("Switch toggled:", switch)
        self.save_settings()

    def clean_page(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

app = LanguageAssistantApp()
app.mainloop()
