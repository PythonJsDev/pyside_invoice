import os
DB_FILE = 'invoice/database.db'
CURRENCY = '€'
TVA_MSG = 'TVA non applicable art 261-4-4-b du CGI'
INVOICE_TITLE = "NOTE D'HONORAIRES"
INVOICE_HEADER = "Veuillez trouver le détail de nos honoraires pour les travaux suivants:"
PHRASE_1 = "Tout paiement différé de plus de 30 jours entraine l'application d'une pénalité sélevant à un 1.5 \
taux d'intérêt légal en vertu de la loi n°92-1442 du 31 décembre 1992."
PHRASE_2 = "Membre d'une association agréer par l'administration fiscale, acceptant à ce titre le réglment des \
honoraires par chèques libellès à son nom."

ROOT_PATH = os.sep.join(os.path.dirname(__file__).split(os.sep)[:-2])
