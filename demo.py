from guizero import *


def main():
    def start():
        pass

    app = App()
    PushButton(app, text='Start', command=start)

    app.display()


main()
