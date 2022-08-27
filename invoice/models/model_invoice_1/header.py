from reportlab.platypus import Table, Image
from invoice.models.utils import company_address, invoice_datas


def header_table(width, height, id_to_update):
    width_part = {
        'left_column': width * 40/100,
        'center_column': width * 40/100,
        'right_column': width * 20/100,
    }

    left_padding_client_address = width_part.get('center_column')*1/3
    top_padding = 25

    logo_path = r'logo\logo_pjsdev_fb.png'
    logo_width = width_part.get('right_column')
    logo = Image(logo_path, 0.8*logo_width, 0.8*logo_width)

    company_text = company_address()
    customer_text = invoice_datas(id_to_update).get('address')
    res = Table(
        [[company_text, customer_text, logo]],
        [width for width in width_part.values()],
        height)
    res.setStyle([
        ('LEFTPADDING', (0, 0), (0, 0), 30),
        ('VALIGN', (0, 0), (0, 0), 'TOP'),
        ('TOPPADDING', (0, 0), (0, 0), top_padding),

        ('BOTTOMPADDING', (1, 0), (1, 0), 20),
        ('LEFTPADDING', (1, 0), (1, 0), left_padding_client_address),
        ('ALIGN', (0, 0), (1, 0), 'LEFT'),

        ('LEFTPADDING', (2, 0), (2, 0), 0),
        ('ALIGN', (2, 0), (2, 0), 'LEFT'),
        ('VALIGN', (2, 0), (2, 0), 'TOP'),
        ('TOPPADDING', (2, 0), (2, 0), top_padding),
        ])
    return res
