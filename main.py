#!/usr/bin/python3
import pathlib
import pygubu
PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "window.ui"


class WindowApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
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

    def SendImg(self):
        pass

    def Peek(self):
        pass

    def Quit(self):
        pass

    def AddContact(self):
        pass


if __name__ == "__main__":
    app = WindowApp()
    app.run()
