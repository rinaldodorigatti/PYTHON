#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Apr 22 14:41:37 2023
@author: rickyd
"""

import gi
import time
import threading

gi.require_version('Gtk', '3.0')
gi.require_version('Gio', '2.0')
from gi.repository import Gtk, Gio, GLib


class FileCopyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="File Copy")

        self.set_default_size(400, 100)
        self.move(300, 300)
        self.progressbar = Gtk.ProgressBar()
        self.add(self.progressbar)

        # Start the file copy operation in a separate thread
        self.source = Gio.File.new_for_path('FILES/spyder.sh')
        self.destination = Gio.File.new_for_path('FILES2/spyder.sh')
        self.copy_thread = Gio.File.copy_async(
            self.source,
            self.destination,
            flags=Gio.FileCopyFlags.NONE,
            io_priority=GLib.PRIORITY_DEFAULT,
            cancellable=None,
            callback=self.on_copy_finished)
        self.p_court = 0.0
        # self.timeout_id = GLib.timeout_add(100, self.update_progress_bar)

    def progress_callback(self, current_num_bytes, total_num_bytes, user_data):
        progress = float(current_num_bytes) / float(total_num_bytes) * 100
        # print(f"Copy progress: {progress:.0f}")
        self.p_court = float("{:.2f}".format(progress / 100))
        time.sleep(0.1)

        # print(f"Copy progress: {p_court}")


    def print_hi_three_times(self, p_court):
        self.progressbar.set_fraction(p_court)


    def update_progress_bar(self):
        flags = Gio.FileCopyFlags.OVERWRITE
        cancellable = Gio.Cancellable()

        progress = self.source.copy(self.destination, flags, cancellable, self.progress_callback, None)
        if progress:
            print("File copy progress: {0}".format(progress))
        t1 = threading.Thread(target=self.print_hi_three_times, args=(self.p_court,))
        t1.start()
            # self.progressbar.set_fraction(progress)
        # self.source.copy_async(self.destination, flags, Gio.PRIORITY_DEFAULT, cancellable, self.callback)
        """progress = self.copy_thread
        if not progress:
            self.progressbar.set_fraction(progress)"""
        return True

    def on_copy_finished(self, source, result):
        GLib.source_remove(self.timeout_id)
        success, error = source.copy_finish(result)

        if not success:
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR,
                                       Gtk.ButtonsType.OK, "File copy error")
            dialog.format_secondary_text(str(error))
            dialog.run()
            dialog.destroy()

        Gtk.main_quit()


win = FileCopyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
