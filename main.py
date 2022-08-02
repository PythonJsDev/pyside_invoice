from PySide6 import QtWidgets

import sys
from invoice.models.model_invoice_1.main_structure import main_structure
from invoice.views.form_client import FormClient
# from invoice.views.form_company import FormCompany
from invoice.views.main_window import MainWindow
from invoice.utilities import load_styles
from invoice.views.search_client import SearchClient


def main():
    app = QtWidgets.QApplication(sys.argv)
    # w = FormClient()
    load_styles(app)
    w = MainWindow()
    # w = SearchClient()

    w.show()
    app.exec()

# def main_model(datas):
#     main_structure(datas)


if __name__ == "__main__":
    main()
    # datas = {'path': 'invoice/models/model_invoice_1',
    #          'invoice_ref': 'model_1.pdf',
    #          'pdf_title': 'blabla',
    #          'phone': 'Tél : 00.00.00.00.00',
    #          'email': 'Email : mon_email@email.com',
    #          'siret': 'Siret : 00000000000000'}
    # main_model(datas)
