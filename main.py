import Conn
import pathlib
import tkinter.filedialog

import pygubu
from PIL import Image, ImageTk
import cv2
PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "window.ui"


class WindowApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object("toplevel1", master)

        self.prog_lang = None
        self.if_en = None
        self.if_ger = None
        self.if_friend = None
        self.res = None
        builder.import_variables(
            self, ['prog_lang', 'if_en', 'if_ger', 'if_friend', 'res'])

        builder.connect_callbacks(self)

    def run(self):
        self.mainwindow.mainloop()

    global img
    def SendImg(self):
        canvas = self.builder.get_object("canvas1")

        f_types = [('Jpg Files', '*.jpg'), ('PNG Files', '*.png')]
        path = tkinter.filedialog.askopenfilenames(filetypes=f_types)

        my_img = cv2.imread(path[0])
        my_img = cv2.resize(my_img, (300, 300))
        my_img = cv2.cvtColor(my_img, cv2.COLOR_BGR2RGB)

        myEditedImg = Image.fromarray(my_img)

        img = ImageTk.PhotoImage(myEditedImg)

        canvas.create_image(0, 0, anchor="nw", image=img)
        canvas.image = img

    def Peek(self):
        isEn, isGer = self.if_en.get(), self.if_ger.get()
        result = self.builder.get_object("result")

        lang = ""

        if not (isEn and isGer): lang = "none"
        if isEn: lang = "English"
        if isGer: lang = "German"
        if isEn and isGer: lang = "English, German"

        self.res.set(f'Programming lang: {self.prog_lang.get()} \n'
                     f'Language: {lang} \n')
        result.configure(textvariable=self.res)

    def Quit(self):
        self.mainwindow.destroy()

    def AddContact(self):
        contact = {
            'FirstName': self.builder.get_object("FirstName").get(),
            'LastName': self.builder.get_object("LastName").get(),
            'Phone': self.builder.get_object("Phone").get(),
            'isFriend': self.if_friend.get(),
            'Email': self.builder.get_object("Email").get(),
            'Bday': self.builder.get_object("Bday").get()
        }
        print(contact['FirstName'], contact['LastName'], contact['Phone'], contact['isFriend'], contact['Email'], contact['Bday'])
        query = "INSERT INTO Contacts " \
                "(firstName, lastName, phone, isFriend, email, birthday)" \
                "VALUES " \
                "(%(FirstName)s, %(LastName)s, %(Phone)s, %(isFriend)s, %(Email)s, %(Bday)s)"
        Conn.cursor.execute(query, contact)

        Conn.Connection.commit()

if __name__ == "__main__":
    app = WindowApp()
    app.run()
