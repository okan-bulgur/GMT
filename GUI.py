from tkinter import *
from tkinter import Canvas
from functools import partial
import objectBehaviours


class GUI:
    def __init__(self):
        self.objects = {"arrow", "rectangle"}  # list of shapes
        self.window = Tk()
        self.window.geometry("700x600+1200+80")
        self.window.title("Graphical Modeling Editor")
        self.CoordinateScreen()
        self.create_frame(self.window, self.coordinateSystem, self.objects)
        self.window.mainloop()

    def CoordinateScreen(self):  # method for right part of the existing screen.
        self.coordinateSystem = Canvas(self.window)
        self.coordinateSystem.place(relx=0.1, rely=0, relwidth=0.9, relheight=1)

    def create_label(self, obj, screen):
        self.obj = obj
        self.screen = screen
        obj_img = PhotoImage(file="images\\" + self.obj + ".png")
        _label = Label(self.screen, image=obj_img, compound=CENTER)
        _label.img = obj_img
        _label.place(relx=0, rely=0)
        objectBehaviours.Movement(_label)
        objectBehaviours.TextInput(_label, self.screen)

    def create_frame(self, screen, plotScreen, objects):  # creates left-column puts the object's buttons as well.
        j = 0
        frame_left = Frame(screen, bg="#141E27")
        frame_left.place(relx=0, rely=0, relwidth=0.1, relheight=1)

        for i in objects:
            j += 0.2
            button_obj = Button(frame_left, text=i, bg="#EEEDDE", activebackground="#203239",
                                command=partial(self.create_label, i, plotScreen))
            button_obj.place(relx=0.1, rely=j, relwidth=0.75, relheight=0.1)
