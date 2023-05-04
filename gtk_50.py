#!/usr/bin/python3

import os
import sys
from PySide2.QtWidgets import QProgressBar, QApplication, QDialog, QMainWindow, QPushButton
from PySide2.QtCore import QThread, Signal, Slot


class ProgressDialog(QDialog):
    def __init__(self, parent, source, destination):
        QDialog.__init__(self, parent)

        self.resize(400, 50)

        self.parent = parent
        self.source = source
        self.destination = destination

        self.prog = QProgressBar(self)
        self.prog.setMaximum(100)
        self.prog.setMinimum(0)
        self.prog.setFormat("%p%")

    def start(self):
        self.show()
        self.copy()

    def copy(self):
        copy_thread = CopyThread(self, self.source, self.destination)
        copy_thread.procPartDone.connect(self.update_progress)
        copy_thread.procDone.connect(self.finished_copy)
        copy_thread.start()

    def update_progress(self, progress):
        self.prog.setValue(progress)

    def finished_copy(self, state):
        self.close()


class CopyThread(QThread):
    procDone = Signal(bool)
    procPartDone = Signal(int)

    def __init__(self, parent, source: str, destination: str):
        QThread.__init__(self, parent)

        self.source = source
        self.destination = destination

    def run(self):
        self.copy()
        self.procDone.emit(True)

    def copy(self):
        source_size = os.stat(self.source).st_size
        copied = 0

        with open(self.source, "rb") as source, open(self.destination, "wb") as target:
            while True:
                chunk = source.read(1024)
                if not chunk:
                    break

                target.write(chunk)
                copied += len(chunk)

                self.procPartDone.emit(copied * 100 / source_size)


class MainWindow(QMainWindow):
    def __init__(self, parent: object = None) -> None:
        super().__init__(parent)

        self.src = "FILES/spyder.sh"
        self.dest = "FILES2/spyder.sh"

        self.btn = QPushButton(self)
        self.btn.setText("Start copy")
        self.btn.clicked.connect(self.run)

        self.setCentralWidget(self.btn)

    def run(self):
        self.prog = ProgressDialog(self, self.src, self.dest)
        self.prog.start()


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()