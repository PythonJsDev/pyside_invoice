from PySide6 import QtWidgets, QtCore

from invoice.views.utils import separator_hline, doc
from invoice.views.form_client import FormClient
from invoice.views.search_client import SearchClient


class FormInvoiceClient(QtWidgets.QWidget):
    def __init__(self, datas):
        super().__init__()
        self.datas = datas
        self.setWindowTitle('Facture')
        self.resize(self.width(), self.minimumSizeHint().height())
        self.setup_ui()

    def setup_ui(self):
        self.create_widgets()
        self.create_layout()
        self.add_widgets_to_layouts()

    def create_widgets(self):
        self.lbl_title = QtWidgets.QLabel("Facture")
        self.hline_top = separator_hline(self, name='hline_top', thick=3)
        self.hline_bottom = separator_hline(self, name='hline_bottom', thick=2)
        self.lbl_already_client = QtWidgets.QLabel("Facturer un client existant:")
        self.lbl_new_client = QtWidgets.QLabel("Facturer un nouveau client:")
        self.btn_already_client = QtWidgets.QPushButton(text='Client Existant', clicked=self.already_client)
        self.btn_new_client = QtWidgets.QPushButton(text='Nouveau Client', clicked=self.new_client)
        self.btn_cancel = QtWidgets.QPushButton(text='Annuler', clicked=self.close)
        self.btn_doc = QtWidgets.QPushButton(text='Documentation',
                                             objectName='btn_doc',
                                             clicked=doc)

    def create_layout(self):
        self.main_layout = QtWidgets.QGridLayout(self)
        self.main_layout.setAlignment(QtCore.Qt.AlignTop)
        self.main_layout.setVerticalSpacing(15)

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
        self.main_layout.addWidget(self.lbl_already_client, row+2, column, row_span, column_span)
        self.main_layout.addWidget(self.lbl_new_client, row+2, column+4, row_span, column_span)        
        # row 3
        self.main_layout.addWidget(self.btn_already_client, row+3, column, row_span, column_span)
        self.main_layout.addWidget(self.btn_new_client, row+3, column+4, row_span, column_span)
        # row 4
        self.main_layout.addWidget(self.hline_bottom, row+4, column, row_span, column_span*5)
        # row 5
        self.main_layout.addWidget(self.btn_cancel, row+5, column+4, row_span, column_span)
        # row 6
        self.main_layout.addWidget(self.btn_doc, row+6, column+4, row_span, column_span)

    def already_client(self):
        self.w = SearchClient('Facture')
        self.w.show()
        self.close()

    def new_client(self):
        self.w = FormClient({})
        self.w.show()
