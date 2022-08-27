from reportlab.platypus import Table
from reportlab.lib import colors


def footer_table(width, height, datas):
    datas_to_display = [datas.get('siret_nb'), datas.get('code_ape')]
    text = ' - '.join(datas_to_display)
    color = colors.HexColor('#003363')

    res = Table([[text]], width, height)
    res.setStyle([
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ('BACKGROUND', (0, 0), (-1, -1), color),
        ('TEXTCOLOR', (0, 0), (-1, -1), 'white'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ])
    return res
