from PySide6 import QtWidgets
import sys

from invoice.views.main_window import MainWindow
from invoice.utilities import load_styles


def main():
    app = QtWidgets.QApplication(sys.argv)
    load_styles(app)
    w = MainWindow()
    w.show()
    app.exec()


if __name__ == "__main__":
    main()
