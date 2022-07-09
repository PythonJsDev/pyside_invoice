from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import QAction, Qt, QKeySequence
# from pySide6 import QApplication, QLabel, QMainWindow
import sys

from invoice.views.form_client import FormClient
from invoice.views.form_company import FormCompany
from invoice.models import database
from invoice.views.constants import MAIN_WIN_HEIGHT, MAIN_WIN_WIDTH


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Facture & Devis")
        self.resize(MAIN_WIN_WIDTH, MAIN_WIN_HEIGHT)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        # self.activateWindow()
        self.show()

        label = QtWidgets.QLabel("Facture & Devis")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)
        btn_company = QAction("&Enregistrer", self)
        btn_company.setStatusTip("Formulaire d'enregistrement de l'entreprise")
        btn_company.triggered.connect(self.new_company)
        btn_company.setShortcut(QKeySequence("Ctrl+E"))
        btn_update_company = QAction("&Modifier", self)
        btn_update_company.setStatusTip("Modifier les données de l'entreprise")
        btn_update_company.triggered.connect(self.update_company)
        btn_update_company.setShortcut(QKeySequence("Ctrl+M"))

        btn_client = QAction("&Nouveau", self)
        btn_client.setStatusTip("Formulaire d'enregistrement d'un client")
        btn_client.triggered.connect(self.new_client)
        btn_client.setShortcut(QKeySequence("Ctrl+N"))

        btn_update_client = QAction("&Modifier", self)
        btn_update_client.setStatusTip("Modifier les données d'un client")
        btn_update_client.triggered.connect(self.update_client)
        btn_update_client.setShortcut(QKeySequence("Ctrl+U"))

        # btn_new_company.setCheckable(True)
        # toolbar.addAction(button_action)
        # self.setStatusBar(QtWidgets.QStatusBar(self))
        # toolbar = QtWidgets.QToolBar("My main toolbar")
        # self.addToolBar(toolbar)
        # toolbar.addSeparator()
        button_action2 = QAction("&Your &button2", self)

        button_action2.setStatusTip("This is your button2")
        # button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        # toolbar.addAction(button_action2)

        # toolbar.addWidget(QLabel("Hello"))
        # toolbar.addWidget(QCheckBox())
        # self.setStatusBar(QStatusBar(self))
        menu = self.menuBar()
        company_menu = menu.addMenu("&Entreprise")
        company_menu.addAction(btn_company)
        company_menu.addSeparator()
        company_menu.addAction(btn_update_company)

        client_menu = menu.addMenu("&Client")
        client_menu.addAction(btn_client)
        client_menu.addSeparator()
        client_menu.addAction(btn_update_client)
        client_menu.addSeparator()
        # new_company_menu.addSeparator()
        # new_company_submenu = new_company_menu.addMenu("Submenu")
        # new_company_submenu.addAction(button_action2)
        # file_menu.addAction(button_action2)

    def new_company(self):
        if database.db_is_table_exist('company') and database.db_select_all('company'):
            QtWidgets.QMessageBox.warning(self, 'Erreur', "Vous ne pouvez enregistrer qu'une seule entreprise.")
        else:
            self.w = FormCompany({})
            self.w.show()

    def update_company(self):
        if not database.db_is_table_exist('company'):
            QtWidgets.QMessageBox.warning(self, 'Erreur', "Aucune entreprise n'est enregistrée.")
        else:
            datas = database.db_read_id_row('company', '1')
            self.w = FormCompany(datas)
            self.w.show()

    def new_client(self):
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)
        # print(bin(int(self.windowFlags())))
        self.show()
        # self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowStaysOnBottomHint)
        # self.show()
        self.w = FormClient()
        self.w.show()

    def update_client(self):
        if not database.db_is_table_exist('client') and not database.db_select_all('client'):
            QtWidgets.QMessageBox.warning(self, 'Erreur', "Aucun client n'est enregistré.")
        else:
            print('coucou')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
