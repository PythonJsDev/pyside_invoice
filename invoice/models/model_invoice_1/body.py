from reportlab.platypus import Table
# from reportlab.lib import colors
# from reportlab.lib.styles import ParagraphStyle
from invoice.models.utils import invoice_datas
from ..constants import (CURRENCY,
                         TVA_MSG,
                         INVOICE_TITLE,
                         INVOICE_HEADER,
                         PHRASE_1,
                         PHRASE_2)
# import locale
# from datetime import datetime


def body_table(width, height, id_to_update):
    # top_padding_tab = 10
    width_part = {
        'left_margin': width * 10/100,
        'center_column': width * 80/100,
        'right_margin': width * 10/100,
    }

    height_part = {
        "title": height * 10/100,
        "sub_title": height * 3/100,
        "date": height * 5/100,
        "invoice_num": height * 5/100,
        "tab": height * 65/100,
        "paragrah_1": height * 7/100,
        "paragrah_2": height * 5/100,
    }
    
    res = Table([
        ["", INVOICE_TITLE, ""],
        ["", "", ""],
        ["", _date(id_to_update), ""],
        ["", _bill_number(id_to_update), ""],
        ["", _tab_table(width_part.get('center_column'), height_part.get('tab'), id_to_update), ""],
        ["", PHRASE_1 + "\n" + PHRASE_2, ""],
        ["", TVA_MSG, ""],
        ],
        [width for width in width_part.values()],
        [height for height in height_part.values()],
        )

    res.setStyle([
        # titre facture
        ('ALIGN', (1, 0), (-1, 0), 'CENTER'),
        ('VALIGN', (1, 0), (-1, 0), 'MIDDLE'),
        ('FONTSIZE', (1, 0), (-1, 0), 12),
        ('FONTNAME', (1, 0), (-1, 0), 'Helvetica-Bold'),

        ('ALIGN', (1, 1), (-1, 1), 'LEFT'),
        ('VALIGN', (1, 1), (-1, 1), 'MIDDLE'),

        ('ALIGN', (1, -1), (1, -1), 'CENTER'),
        ('VALIGN', (1, -1), (1, -1), 'MIDDLE'),
        ('FONTSIZE', (1, -1), (1, -1), 8),

        ('FONTSIZE', (1, -2), (1, -2), 7),
        ('ALIGN', (1, -2), (1, -2), 'CENTER'),
        ('VALIGN', (1, -2), (1, -2), 'MIDDLE'),

        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('LEFTPADDING', (1, 1), (1, 3), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ])
    return res


def _date(id_to_update):
    return "Le: " + invoice_datas(id_to_update).get('date')


def _bill_number(id_to_update):
    return 'Facture N°: ' + invoice_datas(id_to_update).get('bill_number')


def _tab_table(width, height, id_to_update):
    items = invoice_datas(id_to_update).get('items').split(',')
    width_part = {
        'left_margin': width * 10/100,
        'designation': width * 40/100,
        'quantity': width * 20/100,
        'unit_cost': width * 20/100,
        'right_margin': width * 10/100,
    }
    height_part = {
        'margin_top': height * 15/100,
        'phrase': height * 5/100,
        'title': height * 5/100,
        'line_1': height * 10/100,
        'line_2': height * 5/100,
        'line_3': height * 5/100,
        'margin_bottom': height * 55/100,
    }
    matrix = [
        [],
        ["", INVOICE_HEADER, "", "", ""],
        ["", "Désignation", "Quantité", "Tarif", ""],
        ["", items[0], items[1], items[2] + " " + CURRENCY, ""],
        [],
        ["", "", "Total:", format(float(items[1])*float(items[2]), '.2f') + " " + CURRENCY, ""],
        []]
    result = Table(matrix,
                   [width for width in width_part.values()],
                   [height for height in height_part.values()])

    result.setStyle([
        ('GRID', (1, 2), (-2, 3), 1, 'black'),
        # title table
        ('ALIGN', (0, 2), (-1, 2), 'CENTER'),
        ('VALIGN', (0, 2), (-1, 2), 'MIDDLE'),
        ('FONTNAME', (0, 2), (-1, 2), 'Helvetica-Bold'),

        ('ALIGN', (-3, 3), (-2, 3), 'CENTER'),
        ('VALIGN', (1, 3), (-2, 3), 'MIDDLE'),

        ('ALIGN', (-2, 5), (-2, 5), 'CENTER'),
        ('ALIGN', (-3, 5), (-3, 5), 'RIGHT'),

        ('FONTSIZE', (-2, 5), (-2, 5), 12),
        ('FONTNAME', (-3, 5), (-2, 5), 'Helvetica-Bold')
        ])

    return result
