from graphics import *

if __name__ == '__main__':
    # основная программа
    config.notebook = ttk.Notebook(config.root)

    start_frame = StartFrame()
    config.notebook.add(start_frame, text='начало работы')

    config.common_frames = [CommonFrame(config.names[i], config.notebook) for i in range(len(config.names))]
    for i in range(len(config.names)):
        config.notebook.add(config.common_frames[i], text=config.names[i])

    config.notebook.pack(expand=1, fill=BOTH)
    config.root.mainloop()
