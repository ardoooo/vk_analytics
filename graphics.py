from tkinter import *
from tkinter import ttk
from algorithm import *
import config


class StartFrame(ttk.Frame):

    def __init__(self):
        ttk.Frame.__init__(self)
        start_date = config.start_date

        self.options_frame = ttk.Frame(self)
        self.options_frame['borderwidth'] = 2
        self.options_frame['relief'] = 'sunken'
        self.options_frame.pack(side='left', fill=Y)

        label_start_date = ttk.Label(self.options_frame, text='Введите начальную дату')
        label_start_date.pack(side='top')
        entry_start_date = Entry(self.options_frame, textvariable=start_date)
        entry_start_date.pack(side='top')
        label_end_date = ttk.Label(self.options_frame, text='Введите конечную дату')
        label_end_date.pack(side='top')
        entry_end_date = Entry(self.options_frame, textvariable=config.end_date)
        entry_end_date.pack(side='top')

        input_frame = ttk.Frame(self.options_frame)
        label = ttk.Label(input_frame, text='Введите ссылки на сообщества')
        label.pack(side='top')

        self.list_entries = [Entry(input_frame, textvariable=config.domains[i]) for i in range(10)]
        self.help_frame = ttk.Frame(self.options_frame)
        button_start = Button(self.options_frame, text='начать анализ', command=start_analytics)
        self.count_input_entry = 1
        button_add = Button(self.help_frame, text='+', command=self.add_entry)
        button_delete = Button(self.help_frame, text='-', command=self.delete_entry)

        self.help_frame.pack(side='right', fill=Y)
        input_frame.pack(side='top', fill=Y)
        button_add.pack(anchor=NE)
        button_delete.pack()
        button_start.pack(expand=1, anchor=SE)
        self.list_entries[0].pack()

        # блок с описанием функционала

        self.description_frame = ttk.Frame(self)
        label1 = ttk.Label(self.description_frame, text='Справка', font='18')
        text = Text(self.description_frame, wrap=WORD)
        text.insert(0.0, config.info_help)
        text.config(state=DISABLED)
        self.description_frame.pack(side='right', expand=1, fill=BOTH)
        label1.pack(side='top')
        text.pack(expand=1, fill=BOTH)

    # функции для добавления(удаления) полей ввода ссылок
    def add_entry(self):
        if self.count_input_entry > 9:
            return
        self.list_entries[self.count_input_entry].pack()
        self.count_input_entry += 1

    def delete_entry(self):
        if self.count_input_entry < 2:
            return
        self.count_input_entry -= 1
        self.list_entries[self.count_input_entry].pack_forget()


class CommonFrame(ttk.Frame):
    def __init__(self, name, notebook):
        ttk.Frame.__init__(self)

        self.left_frame = ttk.Frame(self)
        left_title_entry = Entry(self.left_frame, font='18', disabledforeground='Black')
        left_title_entry.insert(0, 'среднее')
        left_title_entry.configure(state=DISABLED)
        left_title_entry.pack(anchor='nw')
        self.left_frame.pack(side='left', fill=Y)

        self.right_frame = ttk.Frame(self)
        right_title_entry = Entry(self.right_frame, font='18', disabledforeground='Black')
        right_title_entry.insert(0, 'максимальное')
        right_title_entry.configure(state=DISABLED)
        right_title_entry.pack(anchor='ne')
        self.right_frame.pack(side='right', fill=Y)

        self.mid_frame = ttk.Frame(self)
        mid_title_entry = Entry(self.mid_frame, width=37, font='20', disabledforeground='Black')
        mid_title_entry.insert(0, name)
        mid_title_entry.configure(state=DISABLED)
        mid_title_entry.pack()
        self.mid_frame.pack(side='top', fill=Y)

        nav_frame = Frame(self)
        button_prev = Button(nav_frame, text='назад', command=lambda: go_frame(-1, notebook))
        button_prev.pack(side='left')
        button_next = Button(nav_frame, text='вперёд', command=lambda: go_frame(1, notebook))
        button_next.pack(side='right')
        nav_frame.pack(side='bottom', fill=X)

    # функция, заполняющая вкладки статистикой
    def filling_frame(self, function_average, function_max):
        i = 0
        for name in config.domains:
            average_label = Label(self.left_frame)
            count = getattr(config.walls[i], function_average)
            average_label.configure(text=str(count), font='15')
            average_label.pack()

            max_label = Label(self.right_frame)
            count = getattr(config.walls[i], function_max)
            max_label.configure(text=str(count), font='15')
            max_label.pack()

            name_label = Label(self.mid_frame)
            name_label.configure(text=name.get(), font='15')
            name_label.pack()

            i += 1


# функция для навигации между вкладками
def go_frame(step, notebook):
    number = notebook.index(notebook.select())
    if number + step <= len(config.names):
        notebook.select(number + step)


# основная функция, срабатывает при нажатии кнопки "начать"
def start_analytics():
    config.domains = list(filter(lambda domain: domain.get() != '', config.domains))
    config.walls = [TableOfPosts(name.get(), config.start_date.get(), config.end_date.get()) for name in config.domains]
    i = 0
    for param in TableOfPosts.parameters:
        config.common_frames[i].filling_frame(param + '_average', param + '_max')
        i += 1

    config.notebook.select(1)
