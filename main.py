import customtkinter as ctk
from PIL import Image 
import json
import os
from datetime import datetime
from math import ceil

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.geometry("960x500") #Установка размеров
        self.root.title("Finplace") #Надпись сверху окна, тайтл
        self.root.iconbitmap(default="icon.ico") #Установка иконки окна
        self.root.resizable(width = False, height = False) #Нельзя изменять размер окна
        ctk.set_default_color_theme("midnight.json")

        '''self.projects_file = 'projects.json'
        self.projects_all = self.load_projects()
        self.current_project = None'''


        self.create_ui()
    def create_ui(self):
        #Создание рамки(фрейма) в котором расположена кнопка настроек и кнопка проектов
        self.finplace_frame = ctk.CTkFrame(
            master=self.root,
            width = 800,
            height = 50,
            corner_radius= 20
            )
        self.finplace_frame.grid(sticky = 'nsew', row = 0, column = 0, columnspan = 5, padx = 10)

        #Текстовая метка
        self.finplace_text = ctk.CTkLabel(
            master = self.root, 
            text = 'Finplace',
            font = ("Helvetica", 24),
            fg_color="#BCC6D0"
        )
        self.finplace_text.grid(row = 0, column = 1,columnspan = 2,  sticky='n', pady = 10)

        #Создание рамки(фрейма) в котором расположены все текстовые поля
        self.textentry_frame = ctk.CTkFrame(
            master=self.root,
            width = 300,
            height = 250,
            corner_radius=20
        )
        self.textentry_frame.grid(row = 2,sticky = 'nsew', columnspan = 4, rowspan = 3, padx=10, pady = 10)

        #Все текстовые метки в главном окне
        self.text1 = ctk.CTkEntry( master = self.root, bg_color="#BCC6D0", corner_radius=10, placeholder_text='Количество товара', width=200)
        self.text1.grid(row=2, column = 0, padx = 20, pady = 20)

        self.text2 = ctk.CTkEntry( master = self.root, bg_color="#BCC6D0", corner_radius=10, placeholder_text='Цена закупки', width=200)
        self.text2.grid(row=2, column = 1, padx = 20, pady = 20)

        self.text3 = ctk.CTkEntry( master = self.root, bg_color="#BCC6D0", corner_radius=10, placeholder_text='Цена до скидки', width=200 )
        self.text3.grid(row=2, column = 2, padx = 20, pady = 20)

        self.text4 = ctk.CTkEntry( master = self.root, bg_color="#BCC6D0", corner_radius=10, placeholder_text='Скидка (в %)', width=200)
        self.text4.grid(row=2, column = 3, padx = 20, pady = 20)

        self.text5 = ctk.CTkEntry( master = self.root, bg_color="#BCC6D0", corner_radius=10, placeholder_text='Комиссия ВБ (в %)', width=200)
        self.text5.grid(row=3, column = 0, padx = 20, pady = 20)

        self.text6 = ctk.CTkEntry( master = self.root, bg_color="#BCC6D0", corner_radius=10, placeholder_text='Упаковка общая/фф', width=200)
        self.text6.grid(row=3, column = 1, padx = 20, pady = 20)

        self.text7 = ctk.CTkEntry( master = self.root, bg_color="#BCC6D0", corner_radius=10, placeholder_text='Услуги подрядчиков', width=200)
        self.text7.grid(row=3, column = 2, padx = 20, pady = 20)

        self.text8 = ctk.CTkEntry( master = self.root, bg_color="#BCC6D0", corner_radius=10, placeholder_text='Упаковка на 1 ед.', width=200)
        self.text8.grid(row=3, column = 3, padx = 20, pady = 20)

        self.text9 = ctk.CTkEntry( master = self.root,bg_color="#BCC6D0", corner_radius=10, placeholder_text="Доставка, ед. товара", width=200)
        self.text9.grid(row=4, column = 0, padx = 20, pady = 20)

        self.text10 = ctk.CTkEntry( master = self.root,bg_color="#BCC6D0", corner_radius=10, placeholder_text="% выкупа по категории", width=200 )
        self.text10.grid(row=4, column = 1, padx = 20, pady = 20)

        self.text11 = ctk.CTkEntry( master = self.root, bg_color="#BCC6D0", corner_radius=10, placeholder_text="Хранение на складе ед./сут.", width=200)
        self.text11.grid(row=4, column = 2, padx = 20, pady = 20)

        self.text12 = ctk.CTkEntry( master = self.root, bg_color="#BCC6D0", corner_radius=10, placeholder_text="УСН (Д)", width=200)
        self.text12.grid(row=4, column = 3, padx = 20, pady = 20)

        #Текст для названия проекта
        self.project_name_label = ctk.CTkLabel(
        master=self.root,
        text = "Название вашего проекта:",
        font = ("Helvetica", 20)
        )
        self.project_name_label.grid(row=1, column = 1, pady=20)

        #Текстовое поле для названия проекта
        self.project_name_entry = ctk.CTkEntry(
        master=self.root,
        width=220,
        corner_radius=0
        )
        self.project_name_entry.grid(row=1, column=2, sticky="w", padx=5)

        #Установка картинки для кнопки проектов
        img_proj = ctk.CTkImage(
        light_image=Image.open("projects.png"),  
        dark_image=Image.open("projects.png"),   
        size=(30, 30)
        )
        #Создание кнопки проектов 
        self.button_projects = ctk.CTkButton(
            master=self.root,
            image = img_proj,
            text = None, 
            command = self.projects, 
            width=20, 
            height=30, 
            fg_color="#BCC6D0", 
            bg_color="#BCC6D0", 
            corner_radius=15
            )
        self.button_projects.grid(row = 0, column = 0, sticky = 'w', padx = 15)   

        #Установка картинки для кнопки настроек
        img_opt = ctk.CTkImage(
        light_image=Image.open("options2.png"),  
        dark_image=Image.open("options2.png"),   
        size=(30, 30)
        )

        #Создание кнопки настроек
        button_options = ctk.CTkButton(
            master=self.root,
            image = img_opt, 
            text = None, 
            command=self.options, 
            width=20, 
            height=40, 
            fg_color="#BCC6D0", 
            bg_color="#BCC6D0", 
            corner_radius=15)
        button_options.grid(row = 0, column = 3, pady = 5, sticky = 'e', padx= 15)

        #Кнопка для расчетов
        self.buttoncount = ctk.CTkButton(
        master = self.root,
        text = 'Посчитать',
        font = ("Helvetica", 18),
        text_color='white',
        width = 180,
        command = self.count
        )
        self.buttoncount.grid(row = 5, column = 0, pady = 20, )

        self.errors()

    def projects(self):
        self.projectsw = ctk.CTk()
        self.projectsw.title('Проекты')
        self.projectsw.geometry('1000x500')
        self.projectsw.iconbitmap(default="icon.ico")
        self.projectsw.resizable(width = False, height = False)

        #Создание рамки в которой будут все созданные проекты
        sidebar = ctk.CTkFrame(master=self.projectsw, height=480, corner_radius=15,)
        sidebar.grid(row=0, column=0, padx=10, pady=10, sticky="nsew", rowspan = 5)

        #Надпись для рамки/название
        sidebar_label = ctk.CTkLabel(
            master= sidebar,
            text = "Ваши проекты",
            corner_radius=10,
            fg_color='#AAB0B6',
            bg_color="#BCC6D0",
            font = ('Helvetica' , 18),
            )
        sidebar_label.grid(row = 0, column = 0, sticky = 'nsew', pady = 10, padx = 10)

        #Создание рамки которую можно крутить, в ней находятся все проекты
        projects_list_frame = ctk.CTkScrollableFrame(
        master=sidebar,
        label_text=None,
        corner_radius=15,
        height = 380,
        )
        projects_list_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        #Создание рамки в которую будут выводится все полученные данные
        data_frame = ctk.CTkFrame(master=self.projectsw, corner_radius=15, height=480, width=705)
        data_frame.grid(row=0, column=2, pady=10,padx=10, sticky = 'nsew')
        self.projectsw.mainloop()

    def options(self):
        optionsw = ctk.CTk()
        optionsw.title('Настройки')
        optionsw.geometry('500x500')
        optionsw.iconbitmap(default="icon.ico")
        options_tab = ctk.CTkTabview(master=optionsw, width=460, height=300)
        options_tab.grid(padx=20, pady=20, row = 0, column = 0, sticky = 'nsew')

        themes = options_tab.add("Темы")
        theme_var = ctk.IntVar(value = 0)

        def themes_event():
            if theme_var == 1:
                ctk.set_default_color_theme("midnight.json")
            elif theme_var == 2:
                ctk.set_default_color_theme("marsh.json")

        theme_midnight = ctk.CTkRadioButton(master = themes, text='Midnight', variable=theme_var, value=1, command=themes_event)
        theme_midnight.grid(row=0, sticky='w', padx= 20, pady=20)

        theme_marsh = ctk.CTkRadioButton(master = themes, text='Marsh',  variable=theme_var, value=2, command=themes_event)
        theme_marsh.grid(row=1, sticky='w', padx= 20, pady=20)

        tab2 = options_tab.add("Настройка2")
        tab3 = options_tab.add("Настройка3")
        tab4 = options_tab.add("Настройка4")
        tab5 = options_tab.add("Настройка5")

        optionsw.mainloop()

    def errors(self):
        #Окно для ошибок в окнах ввода
        self.errorw_entry = ctk.CTk() 
        self.errorw_entry.geometry('300x100')
        self.errorw_entry.title("Ошибка")

        self.error_label_entry = ctk.CTkLabel(
        master=self.errorw_entry,
        text = 'Неверно введено значение',
        font = ("Helvetica", 20)
        )
        self.error_label_entry.grid(row= 0, column = 0, pady =20, padx = 20, sticky = 'nsew')    

        #Окно для ошибок в название проекта
        self.errorw_name = ctk.CTk()
        self.errorw_name.geometry('260x100')
        self.errorw_name.title("Ошибка")
        error_label_name = ctk.CTkLabel(
        master=self.errorw_name,
        text = 'Введите имя проекта',
        font = ("Helvetica", 20)
        )
        error_label_name.grid(row= 0, column = 0, pady =20, padx = 20, sticky = 'nsew')

    def count(self):

        '''if self.project_name_entry.get()=='':
            self.buttoncount.configure(state = 'disabled')
        else:
            self.buttoncount.configure(state = 'normal')'''

        self.resultw = ctk.CTk()
        self.resultw.geometry('700x500')
        self.resultw.title("Результаты")

        if self.project_name_entry.get()=='':
            self.errorw_name.mainloop()
        try:
            qua = float(self.text1.get())
        except ValueError:
            self.errorw_entry.mainloop()

        try:
            buy_price = float(self.text2.get())
        except ValueError:
            self.errorw_entry.mainloop()

        try:
            price_nodisc= float(self.text3.get())
        except ValueError:
            self.errorw_entry.mainloop()

        try:
            disc_per = float(self.text4.get())
        except ValueError:
            self.errorw_entry.mainloop()

        try:
            comm_per = float(self.text5.get())
        except ValueError:
            self.errorw_entry.mainloop()

        try:
            pack = float(self.text6.get())
        except ValueError:
            self.errorw_entry.mainloop()

        try:
            serv_cont = float(self.text7.get())
        except ValueError:
            self.errorw_entry.mainloop()

        try:
            pack_1 = float(self.text8.get())
        except ValueError:
            self.errorw_entry.mainloop()

        try:
            deliv_1 = float(self.text9.get())
        except ValueError:
            self.errorw_entry.mainloop()

        try:
            category = float(self.text10.get())
        except ValueError:
            self.errorw_entry.mainloop()

        try:
            store_1 = float(self.text11.get())
        except ValueError:
            self.errorw_entry.mainloop()
    
        try:
            ucn_per = float(self.text12.get())
        except ValueError:
            self.errorw_entry.mainloop()
        
        #Расчёты для вывода
        disc_rub = price_nodisc * (disc_per/100) #скидка в рублях
        price_disc = price_nodisc-disc_rub #цена со скидкой
        comm_rub = price_disc * (comm_per/100) #коммисия в рублях
        serv_design_1 = serv_cont/qua 
        store_30 = (store_1*qua)*30
        deliv_category = (deliv_1+33)/(category/100)-33
        ucn_rub = price_disc*(ucn_per/100)
        cost_price = buy_price+serv_design_1+pack_1+deliv_1

        #Выводимые данные
        self.gross_profit = price_disc-pack_1-comm_rub-deliv_category-store_1-buy_price-serv_design_1 #Валовая прибыль
        self.net_profit = self.gross_profit-ucn_rub
        self.marg = (self.net_profit/price_disc)*100
        self.roi = (self.net_profit/cost_price)*100

        #Создание переменных для удобного созранения данных
        self.gp = str(ceil(self.gross_profit))
        self.np = str(ceil(self.net_profit))
        self.mg = str(ceil(self.marg))
        self.ri = str(ceil(self.roi))

        #Создание переменной для хранения имени проекта
        self.project_name = self.project_name_entry.get()

        self.p_name_label = ctk.CTkLabel(
        master=self.resultw,
        text = self.project_name,
        font = ("Helvetica", 24),
        corner_radius=5,
        fg_color="#BCC6D0"
        )
        self.p_name_label.grid(row= 0, column = 1, columnspan=2, padx=10, pady=10, sticky='nsew')

        self.results_data1 = ctk.CTkLabel(
        master=self.resultw,
        text = 'Валовая прибыль:  '+self.gp+' руб.',
        font = ("Helvetica", 20)
        )
        self.results_data1.grid(row= 1,  column = 1, columnspan = 2, pady =20, padx = 20, sticky = 'nsew')

        self.results_data2 = ctk.CTkLabel(
        master=self.resultw,
        text = 'Чистая прибыль:  '+self.np+' руб.',
        font = ("Helvetica", 20)
        )
        self.results_data2.grid(row= 2, column = 1, columnspan = 2, pady =20, padx = 20, sticky = 'nsew') 

        self.results_data3 = ctk.CTkLabel(
        master=self.resultw,
        text = 'Маржинальность:  '+self.mg+'%',
        font = ("Helvetica", 20)
        )
        self.results_data3.grid(row= 3,  column = 1, columnspan = 2, pady =20, padx = 20, sticky = 'nsew') 

        self.results_data4 = ctk.CTkLabel(
        master=self.resultw,
        text = 'ROI:  '+self.ri+'%',
        font = ("Helvetica", 20)
        )
        self.results_data4.grid(row= 4,  column = 1, columnspan = 2, pady =20, padx = 20, sticky = 'nsew')

        self.button_save = ctk.CTkButton(
        master = self.resultw,
        text = 'Сохранить проект',
        font = ("Helvetica", 14),
        
        )
        self.button_save.grid(row=5 ,column = 0, pady =20, padx = 20, sticky = 'nsew' )

        self.resultw.mainloop()

    '''def load_projects(self):
        if os.path.exists(self.projects_file):
            try:
                with open(self.projects_file, "r") as f:
                    return json.load(f)
            except:
                return {}
        return {}

    def save_projects_to_file(self):
        with open(self.projects_file, "w") as f:
            json.dump(self.projects_all, f, indent=4)

    def update_projects_list(self):
        # Clear existing list
        for widget in self.projects_list_frame.winfo_children():
            widget.destroy()

        # Add notes to list
        if not self.projects_all:
            no_projects_label = ctk.CTkLabel(
                master=self.projects_list_frame,
                text="Проектов нет",
            )
            no_projects_label.pack(pady=10)
        else:
            for note_id, note in sorted(self.notes.items(), key=lambda x: x[1]["timestamp"], reverse=True):
                note_button = ctk.CTkButton(
                    master=self.note_list_frame,
                    text=note["title"] if note["title"] else "Untitled",
                    command=lambda id=note_id: self.load_note(id),
                    fg_color="transparent",
                    text_color=("black", "white"),
                    hover_color=("gray90", "gray20"),
                    anchor="w",
                    height=30
                )
                note_button.pack(pady=2, padx=5, fill="x")'''

if __name__ == "__main__":
    mainw = ctk.CTk()
    finplace_app = MainWindow(mainw)
    mainw.mainloop()