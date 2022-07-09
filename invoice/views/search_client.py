from PySide6 import QtWidgets, QtCore
from functools import partial
# from PySide6.QtGui import QRegularExpressionValidator
from invoice.views.utils import separator_hline, doc
from invoice.views.constants import FORM_WIN_HEIGHT, FORM_WIN_WIDTH
from invoice.models.utils import all_clients_last_name, all_clients_email, all_clients_phone
from invoice.models.database import db_select_by_field
import sys


class SearchClient(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Rechercher un client')
        self.resize(FORM_WIN_WIDTH, FORM_WIN_HEIGHT)
        self.setup_ui()

    def setup_ui(self):
        self.create_widgets()
        # self.validator_inputs()
        # self.modify_widgets()
        self.create_layout()
        self.add_widgets_to_layouts()

    def create_widgets(self):
        self.lbl_title = QtWidgets.QLabel("Rechercher un client")
        self.hline_top = separator_hline(self, name='hline_top', thick=3)
        self.hline_bottom = separator_hline(self, name='hline_bottom', thick=2)
        self.lbl_client_last_name = QtWidgets.QLabel("Nom:")
        self.cbox_client_last_name = QtWidgets.QComboBox()
        self.cbox_client_last_name.setPlaceholderText('Recherche par le nom du client')
        self.cbox_client_last_name.addItems(all_clients_last_name())
        self.cbox_client_last_name.currentTextChanged.connect(partial(self.on_combobox_changed, "client_last_name"))

        self.lbl_email = QtWidgets.QLabel("Email:")
        self.cbox_email = QtWidgets.QComboBox()
        self.cbox_email.setPlaceholderText("Recherche par l'email du client")
        self.cbox_email.addItems(all_clients_email())
        self.cbox_email.currentTextChanged.connect(partial(self.on_combobox_changed, "email"))
        self.lbl_phone = QtWidgets.QLabel("Téléphone:")
        self.cbox_phone = QtWidgets.QComboBox()
        self.cbox_phone.setPlaceholderText("Recherche par le numéro de téléphone du client")
        self.cbox_phone.addItems(all_clients_phone())
        self.cbox_phone.currentTextChanged.connect(partial(self.on_combobox_changed, "phone"))

        # self.le_phone = QtWidgets.QLineEdit()
        self.lw = QtWidgets.QListWidget()
        # widget.currentItemChanged.connect(self.index_changed)
        # widget.currentTextChanged.connect(self.text_changed)
        # self.btn_save = QtWidgets.QPushButton("Valider", clicked=self.valid_and_save)
        self.btn_cancel = QtWidgets.QPushButton(text='Annuler', clicked=self.close)
        self.btn_doc = QtWidgets.QPushButton(text='Documentation',
                                             objectName='btn_doc',
                                             clicked=doc)

    def create_layout(self):
        self.main_layout = QtWidgets.QGridLayout(self)
        # self.h_layout = QtWidgets.QHBoxLayout(self)

    def add_widgets_to_layouts(self):
        row = 0
        column = 0
        row_span = 1
        column_span = 1
        # row 0
        self.main_layout.addWidget(self.lbl_title, row, column, row_span, column_span*5, QtCore.Qt.AlignCenter)
        # row 1
        self.main_layout.addWidget(self.hline_top, row+1, column, row_span, column_span*5)
        # row 2
        self.main_layout.addWidget(self.lbl_client_last_name, row+2, column, row_span, column_span)
        self.main_layout.addWidget(self.cbox_client_last_name, row+2, column+1, row_span, column_span*4)
        # row 4
        # self.main_layout.addWidget(self.lbl_client_first_name, row+3, column, row_span, column_span)
        # self.main_layout.addWidget(self.le_client_first_name, row+3, column+1, row_span, column_span*4)
        # row 4
        self.main_layout.addWidget(self.lbl_email, row+4, column, row_span, column_span)
        self.main_layout.addWidget(self.cbox_email, row+4, column+1, row_span, column_span*4)
        # row 5
        self.main_layout.addWidget(self.lbl_phone, row+5, column, row_span, column_span)
        self.main_layout.addWidget(self.cbox_phone, row+5, column+1, row_span, column_span*4)
        # row 6
        self.main_layout.addWidget(self.hline_bottom, row+6, column, row_span, column_span*5)
        # row 7
        self.main_layout.addWidget(self.lw, row+7, column, row_span, column_span*5)
        # row 8
        self.main_layout.addWidget(self.btn_cancel, row+8, column+4, row_span, column_span)
        # row 9
        self.main_layout.addWidget(self.btn_doc, row+9, column+4, row_span, column_span)

    def on_combobox_changed(self, cbox_name, text_selected):
        clients_fields = ["id: ", "Nom: ", "Prénom: ", "Email: ", "Téléphone: ",
                          "Adresse: ", "Code postal: ", "Commune: "]
        data_to_display = []
        self.lw.clear()
        data_list = db_select_by_field('client', {cbox_name: text_selected})
        for data in data_list:
            data_client = ""
            for i, d in enumerate(data):
                if i != 0:
                    data_client += clients_fields[i] + str(d) + '\n'
            data_to_display.append(data_client)
        self.lw.addItems(data_to_display)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = SearchClient()
    win.show()
    sys.exit(app.exec())
