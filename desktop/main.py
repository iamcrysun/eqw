from tkinter.ttk import Notebook, Frame

import ttkbootstrap as ttkb

from desktop.materials.strings import WINDOW_NAME
from desktop.views.attackinfo import AttackInfo
from desktop.views.check import Check
from desktop.views.info import Info
from desktop.views.menu import AppMenu
from desktop.views.registration import Registration
from desktop.views.settings import Settings
from views.login import Login
from settings import ICONS_PATH, ME_URL


class MainWindow(ttkb.Window):
    def __init__(self):
        super(MainWindow, self).__init__()
        ttkb.Style().theme_use('vapor')

        self.authorized_session = None
        self.current_user = None

        self.login_page = Login(self)
        self.registration_page = Registration(self)
        self.menu_page = AppMenu(self)
        self.current_frame = self.login_page
        self.current_frame.pack()

    def load_current_user(self):
        reply = self.authorized_session.get(ME_URL)
        self.current_user = reply.json()

    def switch_frame(self, frame):
        self.current_frame.pack_forget()
        self.current_frame = frame
        self.current_frame.pack()

    def full_ui(self, tk=None):
        notebook = Notebook(self)
        notebook.pack(pady=10, expand=True)

        frame1 = Check(notebook)
        frame2 = Info(notebook)
        frame3 = AttackInfo(notebook)
        frame4 = Settings(notebook)
        frame5 = Frame(notebook, width=780, height=580)

        frame1.pack(fill='both', expand=True)
        frame2.pack(fill='both', expand=True)
        frame3.pack(fill='both', expand=True)
        frame5.pack(fill='both', expand=True)
        frame5.pack(fill='both', expand=True)

        notebook.add(frame1, text='Проверка')
        notebook.add(frame2, text='Информация о проверках')
        notebook.add(frame3, text='Опасности')
        notebook.add(frame4, text='Дополнительные возможности')
        notebook.add(frame5, text='Справка')


main_window = MainWindow()
main_window.title(WINDOW_NAME)
main_window.geometry('800x600')
main_window.iconbitmap(ICONS_PATH / 'shield.ico')
main_window.resizable(width=0, height=0)
main_window.mainloop()
