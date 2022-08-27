from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table

from invoice.models.model_invoice_1.header import header_table
from invoice.models.model_invoice_1.body import body_table
from invoice.models.model_invoice_1.footer import footer_table
from invoice.models.utils import company_identification
import os


def main_structure(datas):
    id_to_update = str(datas.get('id', None))
    path_file = os.path.join(datas.get('path'), datas.get('file_name'))
    pdf = canvas.Canvas(path_file, pagesize=A4)
    pdf.setTitle(datas.get('pdf_title'))

    width, height = A4

    height_part = {
        'header': height * 27/100,
        'body': height * 67/100,
        'footer': height * 3/100,
    }

    main_table = Table([
        [header_table(width, height_part.get('header'), id_to_update)],
        [body_table(width, height_part.get('body'), id_to_update)],
        [footer_table(width, height_part.get('footer'), company_identification())],
        ],
        colWidths=width,
        rowHeights=[height for height in height_part.values()])

    main_table.setStyle([
        ('LEFTPADDING', (0, 0), (0, 2), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ])
    main_table.wrapOn(pdf, 0, 0)
    main_table.drawOn(pdf, 0, 0)
    pdf.showPage()
    pdf.save()
