from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import QAction, Qt, QKeySequence
import sys

from invoice.views.form_client import FormClient
from invoice.views.form_company import FormCompany
from invoice.views.form_invoice_client import FormInvoiceClient
from invoice.views.form_invoice_search import FormInvoiceNumber
from invoice.models import database
from invoice.views.search_client import SearchClient
from invoice.views.constants import MAIN_WIN_HEIGHT, MAIN_WIN_WIDTH


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Facture & Devis")
        self.resize(MAIN_WIN_WIDTH, MAIN_WIN_HEIGHT)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
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

        btn_delete_client = QAction("&Supprimer", self)
        btn_delete_client.setStatusTip("Supprimer les données d'un client")
        btn_delete_client.triggered.connect(self.delete_client)
        btn_delete_client.setShortcut(QKeySequence("Ctrl+D"))

        btn_invoice = QAction("&Nouveau", self)
        btn_invoice.setStatusTip("Formulaire de rédaction d'une facture")
        btn_invoice.triggered.connect(self.new_invoice)
        btn_invoice.setShortcut(QKeySequence("Ctrl+R"))

        btn_search_invoice = QAction("&Modifier", self)
        btn_search_invoice.setStatusTip("Modifier une facture")
        btn_search_invoice.triggered.connect(self.modif_invoice)
        btn_search_invoice.setShortcut(QKeySequence("Ctrl+F"))

        button_action2 = QAction("&Your &button2", self)
        button_action2.setStatusTip("This is your button2")
        button_action2.setCheckable(True)

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
        client_menu.addAction(btn_delete_client)
        client_menu.addSeparator()

        client_invoice = menu.addMenu("&Facture")
        client_invoice.addAction(btn_invoice)
        client_invoice.addSeparator()
        client_invoice.addAction(btn_search_invoice)
        client_invoice.addSeparator()

    def new_company(self):
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)
        self.show()
        if database.db_is_table_exist('company') and database.db_select_all('company'):
            QtWidgets.QMessageBox.warning(self, 'Erreur', "Vous ne pouvez enregistrer qu'une seule entreprise.")
        else:
            self.w = FormCompany({})
            self.w.show()

    def update_company(self):
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)
        self.show()
        if not database.db_is_table_exist('company'):
            QtWidgets.QMessageBox.warning(self, 'Erreur', "Aucune entreprise n'est enregistrée.")
        else:
            datas = database.db_read_id_row('company', '1')
            self.w = FormCompany(datas)
            self.w.show()

    def new_client(self):
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)
        self.show()
        self.w = FormClient({})
        self.w.show()

    def update_client(self):
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)
        self.show()
        if not database.db_is_table_exist('client'):
            QtWidgets.QMessageBox.warning(self, 'Erreur', "Aucun client n'est enregistré.")
        else:
            self.w = SearchClient('Modifier un client')
            self.w.show()

    def delete_client(self):
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)
        self.show()
        if not database.db_is_table_exist('client'):
            QtWidgets.QMessageBox.warning(self, 'Erreur', "Aucun client n'est enregistré.")
        else:
            self.w = SearchClient('Supprimer un client')
            self.w.show()

    def new_invoice(self):
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)
        self.show()
        self.w = FormInvoiceClient({})
        self.w.show()

    def modif_invoice(self):
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)
        self.show()
        self.w = FormInvoiceNumber()
        self.w.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
