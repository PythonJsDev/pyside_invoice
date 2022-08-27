import os
import locale
from datetime import datetime

from .constants import ROOT_PATH

from .utils import save_invoice_datas, invoice_numero, save_invoice_update
from invoice.models.model_invoice_1.main_structure import main_structure


def make_invoice(datas: list):
    locale.setlocale(locale.LC_ALL, 'fr_FR')
    now = datetime.now()
    items = [v for v in datas[0].values()]
    invoice_datas = {'bill_number': invoice_numero(now),
                     'date': now.strftime('%d %B %Y'),
                     'items': ','.join(items),
                     'client_address': '\n'.join(datas[1])}
    save_invoice_datas(invoice_datas)
    save_pdf(invoice_datas, now)


def save_pdf(invoice_datas, now):
    path = os.path.join(ROOT_PATH, 'Factures', now.strftime('%Y'), now.strftime('%B'))
    os.makedirs(path, exist_ok=True)
    datas = {'path': path,
             'file_name': invoice_datas.get('date').replace(" ", '_')
             + "_" + invoice_datas.get('bill_number')[9:] + '.pdf',
             'pdf_title': invoice_datas.get('bill_number'),
             }
    main_structure(datas)


def modif_invoice(datas: list):
    datas_to_save = {}
    items = [datas[0].get('designation'), datas[0].get('quantity'), datas[0].get('price')]
    datas_to_save['id'] = datas[1].get('id')
    datas_to_save['bill_number'] = datas[1].get('bill_number')
    datas_to_save['date'] = datas[1].get('date')
    datas_to_save['client_address'] = datas[1].get('invoice_address')
    datas_to_save['items'] = ','.join(items)
    save_invoice_update(datas_to_save)
    save_pdf_update(datas_to_save)


def save_pdf_update(invoice_datas):
    date = invoice_datas.get('date').split()
    path = os.path.join(ROOT_PATH, 'Factures', date[-1], date[-2])
    datas = {'path': path,
             'file_name':  '_'.join(date) + "_" + invoice_datas.get('bill_number')[9:] + '.pdf',
             'pdf_title': invoice_datas.get('bill_number'),
             'id': invoice_datas.get('id')
             }
    main_structure(datas)
