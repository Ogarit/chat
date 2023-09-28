import time
from threading import Thread
from customtkinter import *
from client import Room


class App:
    def __init__(self, master):
        self.master = master
        self.master.title('Chat')
        self.master.geometry('250x150')
        self.master.minsize(width=250, height=150)
        self.master.maxsize(width=300, height=200)
        self.master.grid_columnconfigure((0, 1), weight=1)
        self.master.grid_rowconfigure((0, 1, 2), weight=1)

        CTkLabel(master, text='Insira o nome do úsuario: ')\
            .grid(row=0, column=0, pady=(10, 0), padx=15, columnspan=2, sticky='W')

        self.entry = CTkEntry(self.master, width=250)
        self.entry.grid(row=1, column=0, columnspan=2, padx=5)

        self.button = CTkButton(self.master, text='OK', command=self.ok_event, width=70, fg_color='#0000b3')
        self.button.grid(row=2, column=0, pady=20, sticky='W', padx=15)

        self.button1 = CTkButton(self.master, text='CANCELAR', command=self.cancel_event, width=70, fg_color='#b30000')
        self.button1.grid(row=2, column=1, pady=20, sticky='E', padx=15)

    def ok_event(self):
        name = self.entry.get()

        self.master.destroy()

        app1 = CTk()
        App1(app1, name.upper())
        app1.mainloop()

    def cancel_event(self):
        self.master.destroy()


class App1:
    def __init__(self, master, name):
        self.name = name

        self.master = master
        self.master.title('Chat')
        self.master.geometry('250x150')
        self.master.minsize(width=250, height=150)
        self.master.maxsize(width=300, height=200)
        self.master.grid_columnconfigure((0, 1), weight=1)
        self.master.grid_rowconfigure((0, 1, 2), weight=1)

        CTkLabel(master, text='Insira o nome da sala: ')\
            .grid(row=0, column=0, pady=(10, 0), padx=15, columnspan=2, sticky='W')

        self.entry = CTkEntry(self.master)
        self.entry.grid(row=1, column=0, columnspan=2, padx=20, sticky='WE')

        self.button = CTkButton(self.master, text='OK', command=self.ok_event, width=70, fg_color='#0000b3')
        self.button.grid(row=2, column=0, pady=20, sticky='W', padx=15)

        self.button1 = CTkButton(self.master, text='CANCELAR', command=self.cancel_event, width=70, fg_color='#b30000')
        self.button1.grid(row=2, column=1, pady=20, sticky='E', padx=15)

    def ok_event(self):
        room = self.entry.get()

        self.master.destroy()

        app2 = CTk()
        App2(app2, self.name, room.upper())
        app2.mainloop()

    def cancel_event(self):
        self.master.destroy()


class App2:
    def __init__(self, master, name, room):
        self.name = name
        self.room = room

        self.master = master
        self.master.title('Chat')

        self.outers = Room().send_msg('', self.room)
        print(self.outers)

        self.textbox = CTkTextbox(self.master, width=600, height=500, state='disable', text_color='white')
        self.textbox.grid(row=0, column=0)

        self.update_thread = Thread(target=self.update_textbox)
        self.update_thread.daemon = True
        self.update_thread.start()

        self.entry = CTkEntry(self.master, width=450)
        self.entry.grid(row=1, column=0, sticky='W', padx=10, pady=10)

        self.button = CTkButton(self.master, width=100, command=self.button_event, text='Enviar')
        self.button.grid(row=1, column=0, sticky='E', padx=10, pady=10)

    def update_textbox(self):
        while True:
            current_list = Room().send_msg('', self.room)

            current_list = list(filter(lambda x: not (x in self.outers), current_list))

            self.update_textbox_content(current_list)

            time.sleep(1)

    def update_textbox_content(self, messages):
        self.textbox.configure(state='normal')
        self.textbox.delete('1.0', 'end')

        for item in messages:
            self.textbox.insert('end', str(item) + '\n')

        self.textbox.configure(state='disable')

    def button_event(self):
        Room().send_msg(f'{self.name}: {self.entry.get()}', self.room)
        self.entry.delete(0, 'end')


if __name__ == '__main__':
    app = CTk()
    App(app)
    app.mainloop()
