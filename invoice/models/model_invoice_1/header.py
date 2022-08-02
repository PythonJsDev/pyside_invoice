from reportlab.platypus import Table, Image


def header_table(width, height):
    width_part = {
        'left_column': width * 40/100,
        'center_column': width * 40/100,
        'right_column': width * 20/100,
    }

    left_padding_client_adress = width_part.get('center_column')*1/3
    top_padding = 25

    logo_path = r'logo\logo_vide.png'
    logo_width = width_part.get('right_column')
    logo = Image(logo_path, 0.8*logo_width, 0.8*logo_width)

    company_text = "coucou\n25 rue du succès lol"

    customer_text = "Mme tartampion tartampion\n33 rue de ouf\n12000 Ici\ntatat"
    res = Table(
        [[company_text, customer_text, logo]],
        [width for width in width_part.values()],
        height)
    res.setStyle([
        ('GRID', (0, 0), (2, 0), 1, 'red'),
        ('LEFTPADDING', (0, 0), (0, 0), 30),
        ('VALIGN', (0, 0), (0, 0), 'TOP'),
        ('TOPPADDING', (0, 0), (0, 0), top_padding),

        ('VALIGN', (1, 0), (1, 0), 'BOTTOM'),
        ('LEFTPADDING', (1, 0), (1, 0), left_padding_client_adress),
        ('ALIGN', (0, 0), (1, 0), 'LEFT'),

        ('ALIGN', (2, 0), (2, 0), 'CENTER'),
        ('VALIGN', (2, 0), (2, 0), 'TOP'),
        ('TOPPADDING', (2, 0), (2, 0), top_padding),
        ])
    return res
