#!/usr/bin/env python3

from gi.repository import Gtk
import gi
gi.require_version("Gtk", "3.0")

window = Gtk.Window(title="Hello world")
window.show()
window.connect("destroy", Gtk.main_quit)
Gtk.main()
