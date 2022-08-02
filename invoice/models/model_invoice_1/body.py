from reportlab.platypus import Table
# from reportlab.lib import colors
# from reportlab.lib.styles import ParagraphStyle

import locale
from datetime import datetime


def body_table(width, height):
    top_padding_tab = 10
    width_part = {
        'left_margin': width * 10/100,
        'center_column': width * 80/100,
        'right_margin': width * 10/100,
    }

    height_part = {
        "title": height * 10/100,
        "date": height * 5/100,
        "invoice_num": height * 5/100,
        "tab": height * 65/100,
        "paragrah_1": height * 10/100,
        "paragrah_2": height * 5/100,
    }
    # left_padding = 20
    # tables_width = width_list[1] - left_padding
    res = Table([
        ["", _title(), ""],
        ["", _date(), ""],
        ["", _bill_number(), ""],
        ["", _tab_table(width_part.get('center_column'), height_part.get('tab')), ""],
        ["", "", ""],
        ["", "", ""],
        ],
        [width for width in width_part.values()],
        [height for height in height_part.values()],
        )
    #             )
    # # res = Table([
    # #     ['', 'Offer', ''],
    # #     ['', _gen_contacts_table(tables_width, height_list[1]), ''],
    # #     ['', _gen_price_list_table(tables_width, height_list[2]), ''],
    # #     ['', _gen_description_paragraph(), ''],
    # #     ['', _gen_about_table(width_list[1], height_list[4]), '']],
    # #     width_list,
    # #     height_list)
    # color = colors.HexColor('#003363')

    res.setStyle([
        ('GRID', (0, 0), (-1, -1), 1, 'blue'),
        # titre facture
        ('ALIGN', (1, 0), (-1, 0), 'CENTER'),
        ('VALIGN', (1, 0), (-1, 0), 'MIDDLE'),
        # ('LINEBELOW', (1, 0), (1, 1), 1, color),
        # ('LINEBELOW', (1, 3), (1, 3), 1, color),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        # ('FONTSIZE', (1, 0), (1, 0), 30),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('VALIGN', (0, 3), (-1, 3), 'TOP'),
        # tab_table
        ('TOPPADDING', (1, 3), (-1, 3), top_padding_tab),
        # ('BOTTOMPADDING', (1, 1), (1, 2), 0),
        # ('BOTTOMPADDING', (1, 3), (1, 3), 40),

        # ('BOTTOMPADDING', (1, 4), (1, 4), 0),
        # ('LEFTPADDING', (1, 4), (1, 4), 0),
        ])
    return res


def _title():
    return "TITRE FACTURE"


def _date():
    locale.setlocale(locale.LC_ALL, 'fr_FR')
    now = datetime.now().strftime('%d %B %Y')
    year = datetime.now().strftime('%Y')
    month = datetime.now().strftime('%m')
    week = datetime.now().strftime('%U')
    return "Le: " + now + ' ' + year + ' ' + month + ' ' + week


def _bill_number():
    return 'num'


def _tab_table(width, height):
    width_part = {
        'left_margin': width * 10/100,
        'designation': width * 40/100,
        'quantity': width * 20/100,
        'unit_cost': width * 20/100,
        'right_margin': width * 10/100,
    }
    height_part = {
        'title': height * 5/100,
        'line_1': height * 5/100,
        'line_2': height * 5/100,
        'line_3': height * 5/100,
    }
    matrix = [
        ["", "a", "b", "c", ""],
        ["", "d", "e", "f", ""],
        ["", "g", "h", "i", ""],
        ["", "k", "l", "m", ""]]

    result = Table(matrix,
                   [width for width in width_part.values()],
                   [height for height in height_part.values()])

    result.setStyle([
        ('GRID', (0, 0), (-1, -1), 1, 'red'),
        # ('TOPPADDING', (0, 0), (-1, -1), 10),
        # title table
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'),
        # ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        # ('LEFTPADDING', (0, 0), (-1, -1), 50),
        # ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ])

    return result
