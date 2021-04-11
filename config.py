from tkinter import *
from tkinter import ttk

token = "9f8bfbdd4759757d4c366a7e5a37b7daba1b436861f96587c2caa082b84221ed9a60c1afc5843c189f0d2"

root = Tk()
names = ['количество лайков', 'количество репостов', 'количество комментариев', 'количество просмотров']

start_date = StringVar()
end_date = StringVar()
common_frames = []
domains = [StringVar() for i in range(10)]
walls = []
notebook = ttk.Notebook(root)
