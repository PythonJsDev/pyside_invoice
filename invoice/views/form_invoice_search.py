from PySide6 import QtWidgets, QtCore
from invoice.models.utils import find_invoice_by_number
# from invoice.models. write_invoice import modif_invoice
from invoice.views.utils import separator_hline, doc
from invoice.views.form_invoice import FormInvoice


class FormInvoiceNumber(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
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
        self.lbl_bill_number = QtWidgets.QLabel("N° de la facture:")
        self.le_bill_number = QtWidgets.QLineEdit()
        self.btn_save = QtWidgets.QPushButton("Valider", clicked=self.valid)
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
        self.main_layout.addWidget(self.lbl_bill_number, row+2, column, row_span, column_span*1)
        self.main_layout.addWidget(self.le_bill_number, row+2, column+2, row_span, column_span*1)
        # row 3
        self.main_layout.addWidget(self.hline_bottom, row+3, column, row_span, column_span*5)
        self.main_layout.addWidget(self.btn_save, row+4, column+3, row_span, column_span)
        # row 4
        self.main_layout.addWidget(self.btn_cancel, row+4, column+4, row_span, column_span)
        # row 5
        self.main_layout.addWidget(self.btn_doc, row+5, column+4, row_span, column_span)

        self.btn_cancel.setFixedWidth(128)
        self.btn_save.setFixedWidth(128)
        self.btn_doc.setFixedWidth(128)

    def valid(self):
        datas = {}
        invoice_datas = find_invoice_by_number(self.le_bill_number.text().strip())
        items = invoice_datas.get('items').split(',')
        client_address = invoice_datas.get('client_address').split('\n')
        datas['designation'] = items[0]
        datas['quantity'] = items[1]
        datas['price'] = items[2]
        datas['address'] = [e for e in client_address if e != ""]
        datas['invoice_address'] = invoice_datas.get('client_address')
        datas['bill_number'] = invoice_datas.get('bill_number')
        datas['id'] = invoice_datas.get('id')
        datas['date'] = invoice_datas.get('date')
        self.w = FormInvoice(datas)
        self.w.show()
        self.close()
