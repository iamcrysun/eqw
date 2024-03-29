from tkinter import Frame, Label, Entry
from tkinter.ttk import Button
import requests

from desktop.materials.strings import REGISTRATION_LABEL, EMAIL_LABEL, USER_NAME_LABEL, PASSWORD_LABEL, \
    REGISTRATION_BUTTON, GO_TO_REG_LABEL
from desktop.settings import REGISTER_URL


class Registration(Frame):
    def __init__(self, master=None):
        super(Registration, self).__init__(master)
        master = master

        self.header_label = Label(self, text=REGISTRATION_LABEL, font=('Helvetica', 18, "bold"), pady=15)
        self.header_label.pack()

        self.email_label = Label(self, text=EMAIL_LABEL, font=('Helvetica', 12), pady=15)
        self.email_label.pack()

        self.email_entry = Entry(self)
        self.email_entry.pack()

        self.username_label = Label(self, text=USER_NAME_LABEL, font=('Helvetica', 12), pady=15)
        self.username_label.pack()

        self.username_entry = Entry(self)
        self.username_entry.pack()

        self.password_label = Label(self, text=PASSWORD_LABEL, font=('Helvetica', 12), pady=15)
        self.password_label.pack()

        self.password_entry = Entry(self)
        self.password_entry.pack()

        self.sign_up_button = Button(self, text=REGISTRATION_BUTTON, command=self.registration)
        self.sign_up_button.pack(pady=20)

        def auth(self):
            master.switch_frame(master.login_page)

        self.auth_label = Label(self, text="Есть аккаунт? Войти", font=('Helvetica', 12), pady=15, )
        self.auth_label.bind("<Button-1>", auth)
        self.auth_label.pack()

    def registration(self):
        reply = requests.post(REGISTER_URL, json={
            "email": self.email_entry.get(),
            "username": self.username_entry.get(),
            "password": self.password_entry.get()
        })

        if reply.status_code == requests.codes.ok:
            self.master.authorized_session = requests.session()
            self.master.authorized_session.cookies.set('session', reply.cookies["session"])
            self.master.load_current_user()
            self.master.switch_frame(self.master.menu_page)
            self.master.full_ui()
