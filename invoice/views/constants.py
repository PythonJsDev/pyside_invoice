FORM_WIN_WIDTH = 800
FORM_WIN_HEIGHT = 450

MAIN_WIN_HEIGHT, MAIN_WIN_WIDTH = 500, 800

RX_COMPANY_NAME = r"^[0-9A-Za-z-\éèêëàâîïùûüôÿçÉÈÊËÀÂÏÎÙÛÜÔŸÇ' ]{2,}$"
RX_NAME = r"^[A-Za-z-\éèêëàâîïùûüôÿçÉÈÊËÀÂÏÎÙÛÜÔŸÇ ]{2,}$"
# RX_EMAIL = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
# RX_EMAIL = r"^[a-z0-9]+[\._]?[a-z0-9]+[\._]?[a-z0-9]+[@][a-zA-Z0-9_-]+[.]\w{2,3}$"
RX_EMAIL = r"^[a-z0-9]+[\._-]?[a-z0-9]+[\._-]?[a-z0-9]+[@a-z0-9_-]+[.]\w{2,3}$"
RX_ADDRESS = r"^[0-9A-Za-z-\éèêëàâîïùûüôÿçÉÈÊËÀÂÏÎÙÛÜÔŸÇ',. ]{2,}$"
RX_ZIP = r"^[0-9]{5}$"
RX_SIRET = r"^[0-9]{14}$"
RX_PHONE = r"^[0-9 .-]{15}$"
RX_APE = r"^[0-9 ]{4}[A-Z]$"
