from PySide6 import QtWidgets, QtCore
from invoice.views.constants import FORM_WIN_HEIGHT, FORM_WIN_WIDTH

from invoice.views.utils import separator_hline, doc
from invoice.views.form_client import FormClient
from invoice.views.search_client import SearchClient
# from invoice.models import database, create_invoice


class FormInvoice(QtWidgets.QWidget):
    def __init__(self, datas):
        super().__init__()
        self.datas = datas
        self.setWindowTitle('Facture')
        self.resize(FORM_WIN_WIDTH, FORM_WIN_HEIGHT)
        self.setup_ui()

    def setup_ui(self):
        self.create_widgets()
        # self.modify_widgets()
        # self.validator_inputs()
        self.create_layout()
        self.add_widgets_to_layouts()

    def create_widgets(self):
        self.lbl_title = QtWidgets.QLabel("Facture")
        self.hline_top = separator_hline(self, name='hline_top', thick=3)
        self.hline_bottom = separator_hline(self, name='hline_bottom', thick=2)
        self.btn_already_client = QtWidgets.QPushButton(text='Déjà Client', clicked=self.already_client)
        self.btn_new_client = QtWidgets.QPushButton(text='Nouveau Client', clicked=self.new_client)
        self.lw = QtWidgets.QListWidget()
        self.le_company = QtWidgets.QLineEdit()
        cancel_button_action = self.valid_and_save if self.datas else self.close

        self.btn_cancel = QtWidgets.QPushButton(text='Annuler', clicked=cancel_button_action)

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
        # # row 2
        self.main_layout.addWidget(self.btn_already_client, row+2, column, row_span, column_span)
        self.main_layout.addWidget(self.btn_new_client, row+2, column+4, row_span, column_span)

        # self.main_layout.addWidget(self.le_company, row+2, column+1, row_span, column_span*4)
        # # row 3
        self.main_layout.addWidget(self.lw, row+3, column, row_span, column_span*5)
        # self.main_layout.addWidget(self.lbl_civil_title, row+3, column, row_span, column_span)
        # self.main_layout.addWidget(self.cbox_civil_title, row+3, column+1, row_span, column_span*4)
        # # row 4
        # self.main_layout.addWidget(self.lbl_client_last_name, row+4, column, row_span, column_span)
        # self.main_layout.addWidget(self.le_client_last_name, row+4, column+1, row_span, column_span*4)
        # # row 5
        # self.main_layout.addWidget(self.lbl_client_first_name, row+5, column, row_span, column_span)
        # self.main_layout.addWidget(self.le_client_first_name, row+5, column+1, row_span, column_span*4)
        # # row 6
        # self.main_layout.addWidget(self.lbl_email, row+6, column, row_span, column_span)
        # self.main_layout.addWidget(self.le_email, row+6, column+1, row_span, column_span*4)
        # # row 6
        # self.main_layout.addWidget(self.lbl_phone, row+7, column, row_span, column_span)
        # self.main_layout.addWidget(self.le_phone, row+7, column+1, row_span, column_span*4)
        # # row 7
        # self.main_layout.addWidget(self.lbl_address, row+8, column, row_span, column_span*5, QtCore.Qt.AlignCenter)
        # # row 8
        # self.main_layout.addWidget(self.lbl_place, row+9, column, row_span, column_span)
        # self.main_layout.addWidget(self.le_place, row+9, column+1, row_span, column_span*4)
        # # row 9
        # self.main_layout.addWidget(self.lbl_zip, row+10, column, row_span, column_span)
        # self.main_layout.addWidget(self.le_zip, row+10, column+1, row_span, column_span*4)
        # # row 10
        # self.main_layout.addWidget(self.lbl_town, row+11, column, row_span, column_span)
        # self.main_layout.addWidget(self.le_town, row+11, column+1, row_span, column_span*4)
        # # row 11
        # self.main_layout.addWidget(self.hline_bottom, row+12, column, row_span, column_span*5)
        # # row 13
        # self.main_layout.addWidget(self.btn_save, row+13, column+3, row_span, column_span)
        self.main_layout.addWidget(self.btn_cancel, row+13, column+4, row_span, column_span)
        # # row 14
        self.main_layout.addWidget(self.btn_doc, row+14, column+4, row_span, column_span)

    def already_client(self):
        # self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)
        # self.show()
        self.w = SearchClient('Clients')
        self.w.show()
        # print('data client', SearchClient.datas_client)
        # self.show()
        # self.client_selected()

    def new_client(self):
        # self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)
        # self.show()
        self.w = FormClient({})
        self.w.show()

    # def client_selected(self, datas):
    #     clients_fields = ["N° client: ", "Entreprise: ", "Titre: ",
    #                       "Nom: ", "Prénom: ", "Email: ", "Téléphone: ",
    #                       "Voie: ", "Code postal: ", "Commune: "]
    #     data_to_display = []
    #     print("datass", datas)
        # self.lw.clear()
        # data_list = database.db_select_by_field('client', create_invoice.invoice())
        # print('data_list', data_list)
        # for data in data_list:
        #     data_client = ""
        #     for i, d in enumerate(data):
        #         data_client += clients_fields[i] + str(d) + '\n'
        #     data_to_display.append(data_client)

        # self.lw.addItems(data_to_display)
        # self.lw.currentItemChanged.connect(self.client_selected)