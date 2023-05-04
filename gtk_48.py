#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Apr 22 14:41:37 2023
@author: rickyd
"""

import gi
import os
import shutil
import sys
import threading
import time

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib


class ProgressBarWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="ProgressBar Demo")
        self.set_border_width(10)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.progressbar = Gtk.ProgressBar()
        vbox.pack_start(self.progressbar, True, True, 0)

        self.progressbar.set_fraction(0.0)

        self.timeout_id = GLib.timeout_add(100, self.cpprogress, 0.0)
        self.activity_mode = False

    def on_timeout(self, user_data):
        """
        Update value on the progress bar
        """
        if self.activity_mode:
            self.progressbar.pulse()
        else:
            file_name_src = "FILES/spyder.sh"
            file_name_dest = "FILES2/spyder.sh"


            """self.cpprogress(file_name_src, file_name_dest)

            if os.path.exists(file_name_dest):
                while os.path.getsize(file_name_src) != os.path.getsize(file_name_dest):
                    percentagem = int(
                        (float(os.path.getsize(file_name_dest)) / float(os.path.getsize(file_name_src))) * 100)
                    percentagem = int((float(os.path.getsize(file_name_dest)) / float(os.path.getsize(file_name_src))) * 100)
                    new_value = self.progressbar.get_fraction() + (percentagem / 100 + 0.01)
                    self.progressbar.set_fraction(new_value)"""
            new_value = self.progressbar.get_fraction() + 0.01
            self.progressbar.set_fraction(new_value)
        return True

    def getprecentprogress(self, source_path, destination_path):
        time.sleep(.24)
        if os.path.exists(destination_path):
            while os.path.getsize(source_path) != os.path.getsize(destination_path):
                percentagem = int((float(os.path.getsize(destination_path)) / float(os.path.getsize(source_path))) * 100)
                new_value = self.progressbar.get_fraction() + (percentagem / 100 + 0.01)
                # self.progressbar.set_fraction(new_value)
                # self.progressbar.pulse()
                # self.progressbar.set_text(str(new_value))
                # sys.stdout.flush()
                time.sleep(.01)

    def cpprogress(self, user_data):
        file_name_src = "FILES/spyder.sh"
        file_name_dest = "FILES2/spyder.sh"

        threading.Thread(name='progresso', target=self.getprecentprogress, args=(file_name_src, file_name_dest)).start()
        shutil.copy2(file_name_src, file_name_dest)
        time.sleep(.02)
        sys.stdout.flush()


if __name__ == '__main__':
    win = ProgressBarWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()