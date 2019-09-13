#!/usr/bin/env python3

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Grid container")
        self.set_default_size(600, 300)

        self.main_grid = Gtk.Grid()
        self.main_grid.set_row_spacing(10)
        self.main_grid.set_column_spacing(10)
        self.add(self.main_grid)

        self.hello_button = Gtk.Button(label="Hello")
        self.hello_button.connect(
            "clicked", self.on_button_clicked, "Very nice to meet you!")
        self.main_grid.attach(self.hello_button, 0, 0, 1, 1)

        self.goodbye_button = Gtk.Button(label="Good bye")
        self.goodbye_button.connect(
            "clicked", self.on_button_clicked, "Have a great day.")
        self.main_grid.attach(self.goodbye_button, 1, 0, 1, 1)

        self.exit_button = Gtk.Button(label="Exit")
        self.exit_button.connect("clicked", Gtk.main_quit)
        self.main_grid.attach(self.exit_button, 2, 0, 1, 1)

        self.info_text = Gtk.Label(label="Welcome, use the buttons.")
        self.info_text.set_hexpand(True)
        self.info_text.set_vexpand(True)
        self.main_grid.attach(self.info_text, 0, 1, 3, 1)

    def on_button_clicked(self, widget, message):
        self.info_text.set_text(message)


win = MainWindow()
win.show_all()
win.connect("destroy", Gtk.main_quit)
Gtk.main()
