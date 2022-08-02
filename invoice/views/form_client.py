from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import QRegularExpressionValidator
from invoice.views.utils import separator_hline, check_len_data, doc, check_email
from invoice.views.constants import (RX_NAME,
                                     RX_EMAIL,
                                     RX_ZIP,
                                     RX_ADDRESS,
                                     RX_PHONE,
                                     FORM_WIN_HEIGHT,
                                     FORM_WIN_WIDTH)

from invoice.models import utils, database


class FormClient(QtWidgets.QWidget):
    def __init__(self, datas):
        super().__init__()
        self.datas = datas
        self.setWindowTitle('Client')
        self.resize(FORM_WIN_WIDTH, FORM_WIN_HEIGHT)
        self.setup_ui()

    def setup_ui(self):
        self.create_widgets()
        self.modify_widgets()
        self.validator_inputs()
        self.create_layout()
        self.add_widgets_to_layouts()

    def create_widgets(self):
        self.lbl_title = QtWidgets.QLabel("Client")
        self.hline_top = separator_hline(self, name='hline_top', thick=3)
        self.hline_bottom = separator_hline(self, name='hline_bottom', thick=2)
        self.lbl_company = QtWidgets.QLabel("Entreprise (raison sociale):")
        self.le_company = QtWidgets.QLineEdit()
        self.lbl_civil_title = QtWidgets.QLabel("Civilité:")
        self.cbox_civil_title = QtWidgets.QComboBox()
        self.cbox_civil_title.addItems(["", "M.", "Mme", "Monsieur", "Madame"])
        self.lbl_client_last_name = QtWidgets.QLabel("Nom:")
        self.le_client_last_name = QtWidgets.QLineEdit()
        self.lbl_client_first_name = QtWidgets.QLabel("Prénom:")
        self.le_client_first_name = QtWidgets.QLineEdit()
        self.lbl_email = QtWidgets.QLabel("Email:")
        self.le_email = QtWidgets.QLineEdit()
        self.lbl_phone = QtWidgets.QLabel("Téléphone:")
        self.le_phone = QtWidgets.QLineEdit()
        self.lbl_address = QtWidgets.QLabel("Adresse postale:")

        self.lbl_place = QtWidgets.QLabel("Voie:")
        self.le_place = QtWidgets.QLineEdit()
        self.lbl_zip = QtWidgets.QLabel("Code postal:")
        self.le_zip = QtWidgets.QLineEdit()
        self.lbl_town = QtWidgets.QLabel("Commune:")
        self.le_town = QtWidgets.QLineEdit()
        self.btn_save = QtWidgets.QPushButton("Valider", clicked=self.valid_and_save)
        # self.btn_cancel = QtWidgets.QPushButton(text='Annuler', clicked=self.close)
        cancel_button_action = self.valid_and_save if self.datas else self.close
        self.btn_cancel = QtWidgets.QPushButton(text='Annuler', clicked=cancel_button_action)

        self.btn_doc = QtWidgets.QPushButton(text='Documentation',
                                             objectName='btn_doc',
                                             clicked=doc)

    def validator_inputs(self):
        self.le_client_last_name.setValidator(QRegularExpressionValidator(RX_NAME))
        self.le_client_first_name.setValidator(QRegularExpressionValidator(RX_NAME))
        self.le_email.setValidator(QRegularExpressionValidator(RX_EMAIL))
        # self.le_email.textEdited.connect(self.text_edited)

        self.le_phone.setValidator(QRegularExpressionValidator(RX_PHONE))
        self.le_place.setValidator(QRegularExpressionValidator(RX_ADDRESS))
        self.le_zip.setValidator(QRegularExpressionValidator(RX_ZIP))
        self.le_town.setValidator(QRegularExpressionValidator(RX_NAME))

    def modify_widgets(self):
        self.lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        self.le_company.setText(self.datas.get('company_name', ""))
        self.cbox_civil_title.setCurrentText(self.datas.get('civil_title', ""))
        self.le_client_last_name.setText(self.datas.get('client_last_name', ""))
        self.le_client_first_name.setText(self.datas.get('client_first_name', ""))
        self.le_email.setText(self.datas.get('email', ""))
        self.le_phone.setText(self.datas.get('phone', ""))
        self.le_place.setText(self.datas.get('place', ""))
        self.le_zip.setText(self.datas.get('zip', ""))
        self.le_town.setText(self.datas.get('town', ''))

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
        self.main_layout.addWidget(self.lbl_company, row+2, column, row_span, column_span)
        self.main_layout.addWidget(self.le_company, row+2, column+1, row_span, column_span*4)
        # row 3
        self.main_layout.addWidget(self.lbl_civil_title, row+3, column, row_span, column_span)
        self.main_layout.addWidget(self.cbox_civil_title, row+3, column+1, row_span, column_span*4)
        # row 4
        self.main_layout.addWidget(self.lbl_client_last_name, row+4, column, row_span, column_span)
        self.main_layout.addWidget(self.le_client_last_name, row+4, column+1, row_span, column_span*4)
        # row 5
        self.main_layout.addWidget(self.lbl_client_first_name, row+5, column, row_span, column_span)
        self.main_layout.addWidget(self.le_client_first_name, row+5, column+1, row_span, column_span*4)
        # row 6
        self.main_layout.addWidget(self.lbl_email, row+6, column, row_span, column_span)
        self.main_layout.addWidget(self.le_email, row+6, column+1, row_span, column_span*4)
        # row 6
        self.main_layout.addWidget(self.lbl_phone, row+7, column, row_span, column_span)
        self.main_layout.addWidget(self.le_phone, row+7, column+1, row_span, column_span*4)
        # row 7
        self.main_layout.addWidget(self.lbl_address, row+8, column, row_span, column_span*5, QtCore.Qt.AlignCenter)
        # row 8
        self.main_layout.addWidget(self.lbl_place, row+9, column, row_span, column_span)
        self.main_layout.addWidget(self.le_place, row+9, column+1, row_span, column_span*4)
        # row 9
        self.main_layout.addWidget(self.lbl_zip, row+10, column, row_span, column_span)
        self.main_layout.addWidget(self.le_zip, row+10, column+1, row_span, column_span*4)
        # row 10
        self.main_layout.addWidget(self.lbl_town, row+11, column, row_span, column_span)
        self.main_layout.addWidget(self.le_town, row+11, column+1, row_span, column_span*4)
        # row 11
        self.main_layout.addWidget(self.hline_bottom, row+12, column, row_span, column_span*5)
        # row 13
        self.main_layout.addWidget(self.btn_save, row+13, column+3, row_span, column_span)
        self.main_layout.addWidget(self.btn_cancel, row+13, column+4, row_span, column_span)
        # row 14
        self.main_layout.addWidget(self.btn_doc, row+14, column+4, row_span, column_span)

    def valid_and_save(self):
        len_data = [(self.le_client_last_name.text(), 0, "Le nom du client est obligatoire."),
                    (self.le_place.text(), 0, "L'adresse est obligatoire."),
                    (self.le_zip.text(), 5, 'Le code postal est composé de 5 chiffres.'),
                    (self.le_town.text(), 0, "La commune est obligatoire."),
                    ]

        if check_len_data(self, len_data) and check_email(self, self.le_email.text().strip()):
            client_datas = {}
            client_datas['company_name'] = self.le_company.text().strip()
            client_datas['civil_title'] = self.cbox_civil_title.currentText()
            client_datas['client_last_name'] = self.le_client_last_name.text().strip()
            client_datas['client_first_name'] = self.le_client_first_name.text().strip()
            client_datas['email'] = self.le_email.text().strip()
            client_datas['phone'] = self.le_phone.text().strip()
            client_datas['place'] = self.le_place.text().strip()
            client_datas['zip'] = self.le_zip.text()
            client_datas['town'] = self.le_town.text().strip()
            fields = ' '.join([k + ' text,' for k in list(client_datas.keys())])[:-1]
            if not self.datas:
                if database.db_is_table_exist('client'):
                    if utils.client_already_exist(client_datas):
                        QtWidgets.QMessageBox.warning(self, 'Erreur', "Ce client est déjà enregistré")
                        self.close()
                else:
                    database.db_create('client', fields)
                    database.db_insert('client', client_datas)
                    self.close()
            else:
                database.db_update('client', client_datas, self.datas.get('id'))
                self.close()

    def event(self, event):
        """ déplace le focus vers le prochain qwidget avec la touche Enter"""
        if event.type() == QtCore.QEvent.KeyPress:
            if event.key() == QtCore.Qt.Key_Return:
                self.focusNextPrevChild(True)
        return super().event(event)

    # def text_edited(self, s):
    #     print(s)
