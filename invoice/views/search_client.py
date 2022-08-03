from PySide6 import QtWidgets, QtCore
from functools import partial
from invoice.views.utils import separator_hline, doc
from invoice.views.form_client import FormClient

from invoice.views.constants import FORM_WIN_HEIGHT, FORM_WIN_WIDTH
from invoice.models.utils import (all_clients_last_name,
                                  all_clients_email,
                                  all_clients_phone,
                                  all_companies,
                                  datas_to_display_lw,
                                  client_datas,
                                  delete_client)


class SearchClient(QtWidgets.QWidget):
    def __init__(self, title):
        super().__init__()
        self.title = title
        self.setWindowTitle(self.title)
        self.resize(FORM_WIN_WIDTH, FORM_WIN_HEIGHT)
        self.setup_ui()

    def setup_ui(self):
        self.create_widgets()
        self.create_layout()
        self.add_widgets_to_layouts()

    def create_widgets(self):
        self.lbl_title = QtWidgets.QLabel(self.title)
        self.hline_top = separator_hline(self, name='hline_top', thick=3)
        self.hline_bottom = separator_hline(self, name='hline_bottom', thick=2)
        self.lbl_company = QtWidgets.QLabel("Entreprise:")
        self.cbox_company = QtWidgets.QComboBox()
        self.cbox_company.setPlaceholderText("Recherche par le nom de l'entreprise")
        self.cbox_company.addItems(all_companies())
        self.cbox_company.currentTextChanged.connect(partial(self.on_combobox_changed, "company_name"))
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

        self.lbl_instruction = QtWidgets.QLabel('Cliquer sur les données du client pour le selectionner:')
        self.lbl_instruction.setHidden(True)
        self.lw = QtWidgets.QListWidget()
        self.btn_cancel = QtWidgets.QPushButton(text='Annuler', clicked=self.close)
        self.btn_doc = QtWidgets.QPushButton(text='Documentation',
                                             objectName='btn_doc',
                                             clicked=doc)

    def create_layout(self):
        self.main_layout = QtWidgets.QGridLayout(self)

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
        self.main_layout.addWidget(self.lbl_company, row+2, column, row_span, column_span)
        self.main_layout.addWidget(self.cbox_company, row+2, column+1, row_span, column_span*4)

        self.main_layout.addWidget(self.lbl_client_last_name, row+3, column, row_span, column_span)
        self.main_layout.addWidget(self.cbox_client_last_name, row+3, column+1, row_span, column_span*4)
        # row 4
        self.main_layout.addWidget(self.lbl_email, row+4, column, row_span, column_span)
        self.main_layout.addWidget(self.cbox_email, row+4, column+1, row_span, column_span*4)
        # row 5
        self.main_layout.addWidget(self.lbl_phone, row+5, column, row_span, column_span)
        self.main_layout.addWidget(self.cbox_phone, row+5, column+1, row_span, column_span*4)
        # row 6
        self.main_layout.addWidget(self.hline_bottom, row+6, column, row_span, column_span*5)
        # row 7
        self.main_layout.addWidget(self.lbl_instruction, row+7, column, row_span, column_span*5)
        # row 8
        self.main_layout.addWidget(self.lw, row+8, column, row_span, column_span*5)
        # row 9
        self.main_layout.addWidget(self.btn_cancel, row+9, column+4, row_span, column_span)
        # row 10
        self.main_layout.addWidget(self.btn_doc, row+10, column+4, row_span, column_span)

    def on_combobox_changed(self, cbox_name, text_selected):
        datas_lw = datas_to_display_lw(cbox_name, text_selected)
        self.lw.clear()
        self.lbl_instruction.setHidden(False)
        self.lw.addItems(datas_lw)
        self.lw.currentItemChanged.connect(self.client_selected)

    def client_selected(self, i):
        rep = i.text()
        index = rep.find(": ")+2
        datas = client_datas(rep[index])
        if self.title == 'Supprimer un client':
            msg = delete_client(self, datas)
            QtWidgets.QMessageBox.information(self, 'Information', msg)
        if self.title == 'Modifier un client':
            self.w = FormClient(datas)
            self.w.show()
        # else:
        #     # SearchClient.datas_client = datas
        #     print('seahcg', datas)
        self.close()
