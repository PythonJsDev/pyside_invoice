from PySide6 import QtWidgets, QtCore
from invoice.views.utils import separator_hline, doc
from invoice.views.constants import FORM_WIN_HEIGHT, FORM_WIN_WIDTH
from invoice.models import utils
from invoice.models. write_invoice import make_invoice, modif_invoice 


class FormInvoice(QtWidgets.QWidget):
    def __init__(self, datas):
        super().__init__()
        self.datas = datas
        self.setWindowTitle('Facture')
        self.resize(FORM_WIN_WIDTH, FORM_WIN_HEIGHT)
        self.setup_ui()
        self.datas_client = self.display_datas_client()

    def setup_ui(self):
        self.create_widgets()
        self.modify_widgets()
        self.create_layout()
        self.add_widgets_to_layouts()

    def create_widgets(self):
        self.lbl_title = QtWidgets.QLabel("Facture")
        self.hline_top = separator_hline(self, name='hline_top', thick=3)
        self.hline_bottom = separator_hline(self, name='hline_bottom', thick=2)
        self.lbl_client = QtWidgets.QLabel("Client:")
        self.lw = QtWidgets.QListWidget()
        self.lbl_designation = QtWidgets.QLabel("Désignation:")
        self.le_designation = QtWidgets.QLineEdit()
        self.lbl_quantity = QtWidgets.QLabel("Quantité:")
        self.le_quantity = QtWidgets.QLineEdit()
        self.lbl_price = QtWidgets.QLabel("Prix unitaire:")
        self.le_price = QtWidgets.QLineEdit()
        self.btn_save = QtWidgets.QPushButton("Valider", clicked=self.valid_and_save)
        self.btn_cancel = QtWidgets.QPushButton(text='Annuler', clicked=self.close)
        self.btn_doc = QtWidgets.QPushButton(text='Documentation',
                                             objectName='btn_doc',
                                             clicked=doc)

    def modify_widgets(self):
        self.lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        self.le_designation.setText(self.datas.get('designation', "")) 
        self.le_quantity.setText(self.datas.get('quantity', ""))
        self.le_price.setText(self.datas.get('price', ""))

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
        self.main_layout.addWidget(self.lbl_client, row+2, column, row_span, column_span*5)
        # row 3
        self.main_layout.addWidget(self.lw, row+3, column, row_span, column_span*5)
        self.main_layout.addWidget(self.lbl_designation, row+4, column, row_span, column_span*5)
        self.main_layout.addWidget(self.le_designation, row+5, column, row_span, column_span*5)

        self.main_layout.addWidget(self.lbl_quantity, row+6, column, row_span, column_span)
        self.main_layout.addWidget(self.le_quantity, row+7, column, row_span, column_span)
        self.main_layout.addWidget(self.lbl_price, row+6, column+4, row_span, column_span)
        self.main_layout.addWidget(self.le_price, row+7, column+4, row_span, column_span)
        # row 9
        self.main_layout.addWidget(self.hline_bottom, row+8, column, row_span, column_span*5)
        self.main_layout.addWidget(self.btn_save, row+9, column+3, row_span, column_span)
        self.main_layout.addWidget(self.btn_cancel, row+9, column+4, row_span, column_span)
        # row 10
        self.main_layout.addWidget(self.btn_doc, row+10, column+4, row_span, column_span)

        self.btn_cancel.setFixedWidth(128)
        self.btn_save.setFixedWidth(128)
        self.btn_doc.setFixedWidth(128)

    def display_datas_client(self):
        """ Affiche les coordonnées du client dans la listwidget """
        self.lw.clear()
        if self.datas.get('bill_number', None):
            self.lw.addItems(self.datas.get('address', None))
        else:
            datas_client = utils.address_list(self.datas)
            self.lw.addItems(datas_client)
            return datas_client

    def valid_and_save(self):
        invoice_datas = {}
        invoice_datas['designation'] = self.le_designation.text().strip()
        invoice_datas['quantity'] = self.le_quantity.text().strip()
        invoice_datas['price'] = self.le_price.text().strip()
        if self.datas.get('bill_number', None):
            modif_invoice([invoice_datas, self.datas])
        else:
            make_invoice([invoice_datas, self.datas_client])
        self.close()
