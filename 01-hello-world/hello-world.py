#!/usr/bin/env python3

import gi
gi.require_version("Gtk", "3.0")  # require gtk version 3.0
from gi.repository import Gtk


class MainWindow(Gtk.Window):
    '''
    The MainWindow class that inherit Gtk.Window
    '''

    def __init__(self):
        # initialize the window and set a title
        Gtk.Window.__init__(self, title="Hello world")

        # create a box container to add multiple widgets.
        self.box = Gtk.Box(spacing=10)
        self.add(self.box)

        # create a label
        self.greet_label = Gtk.Label(label="Click the button")
        self.box.pack_start(self.greet_label, True, True, 0)

        # create a button and connect it clicked to a function.
        self.greet_button = Gtk.Button(label="Greet")
        self.greet_button.connect("clicked", self.on_greet_clicked)
        self.box.pack_start(self.greet_button, True, True, 0)

    def on_greet_clicked(self, widget):
        '''
        On button clicked, greet the user in window with "Hello you!"
        '''
        self.greet_label.set_text("Hello you!")


# create an instance of the window.
win = MainWindow()
# if close (x) button clicked, close it-
win.connect("destroy", Gtk.main_quit)
# show the window.
win.show_all()
# the gtk mainloop.
Gtk.main()
