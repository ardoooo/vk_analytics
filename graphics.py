from tkinter import *
from tkinter import ttk


class StartFrame(ttk.Frame):
    def __init__(self):
        ttk.Frame.__init__(self)
        self.options_frame = ttk.Frame(self)
        self.options_frame['borderwidth'] = 2
        self.options_frame['relief'] = 'sunken'
        self.options_frame.pack(side='left', fill=Y)

        self.label_start_date = ttk.Label(self.options_frame, text='Введите начальную дату')
        self.label_start_date.pack(side='top')
        self.entry_start_date = Entry(self.options_frame, textvariable=main.start_date)
        self.entry_start_date.pack(side='top')
        self.label_end_date = ttk.Label(self.options_frame, text='Введите конечную дату')
        self.label_end_date.pack(side='top')
        self.entry_end_date = Entry(self.options_frame, textvariable=main.end_date)
        self.entry_end_date.pack(side='top')

        self.input_frame = ttk.Frame(self.options_frame)
        self.label = ttk.Label(self.input_frame, text='Введите ссылки на сообщества')
        self.label.pack(side='top')

        self.list_entries = [Entry(self.input_frame, textvariable=main.domains[i]) for i in range(10)]
        self.help_frame = ttk.Frame(self.options_frame)
        self.button_start = Button(self.options_frame, text='начать анализ', command=main.start_analytics)
        self.count_input_entry = 1
        self.button_add = Button(self.help_frame, text='+', command=main.add_entry)
        self.button_delete = Button(self.help_frame, text='-', command=main.delete_entry)

        self.help_frame.pack(side='right', fill=Y)
        self.input_frame.pack(side='top', fill=Y)
        self.button_add.pack(anchor=NE)
        self.button_delete.pack()
        self.button_start.pack(expand=1, anchor=SE)
        self.list_entries[0].pack()

        # блок с описанием функционала

        self.description_frame = ttk.Frame(self)
        self.label1 = ttk.Label(self.description_frame, text='Справка', font='18')
        self.text = Text(self.description_frame)
        self.text.insert(0.0, '1) среднее количество лайков ')
        self.text.insert(END, '2) среднее количество репостов')
        self.text.config(state=DISABLED)
        self.description_frame.pack(side='right', expand=1, fill=BOTH)
        self.label1.pack(side='top')
        self.text.pack(expand=1, fill=BOTH)


class CommonFrame(ttk.Frame):
    def __init__(self, name):
        ttk.Frame.__init__(self)
        name_frame = Entry(self, font='25', disabledforeground='Black')
        name_frame.insert(0, name)
        name_frame.configure(state=DISABLED)
        name_frame.pack(side='top', fill=X)
        nav_frame = Frame(self)
        button_prev = Button(nav_frame, text='назад', command=lambda: main.go_frame(-1))
        button_prev.pack(side='left')
        button_next = Button(nav_frame, text='вперёд', command=lambda: main.go_frame(1))
        button_next.pack(side='right')
        nav_frame.pack(side='bottom', fill=Y)
