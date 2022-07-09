from PySide6 import QtWidgets

import sys
from invoice.models.model_invoice_1.main_structure import main_structure
from invoice.views.form_client import FormClient
# from invoice.views.form_company import FormCompany
from invoice.views.main_window import MainWindow
from invoice.utilities import load_styles
from invoice.views.search_client import SearchClient


# def main():
#     app = QtWidgets.QApplication(sys.argv)
#     # w = FormClient()
#     load_styles(app)
#     # w = MainWindow()
#     w = SearchClient()
   
#     w.show()
#     app.exec()

def main_model():
    main_structure()


if __name__ == "__main__":
    # main()
    datas = {'path': 'invoice', 'pdf_title': 'blabla'}
    main_model()
