from ..views.utils import dlg_ask_question
from . import database


def client_already_exist(datas: dict):
    """ retourne True si le client existe déjà dans la bdd
        même nom, prénom, adresse, zip et commune
    """
    new_client = datas.get('client_last_name') + \
        datas.get('client_first_name') + \
        datas.get('place') + \
        datas.get('zip') + \
        datas.get('town')

    registered_clients = database.db_select_by_field('client', {'client_last_name': datas.get('client_last_name')})
    if registered_clients:
        for client in registered_clients:
            client_datas = dict(zip(list(datas.keys()), client[1:]))
            old_client = client_datas.get('client_last_name') + \
                client_datas.get('client_first_name') + \
                client_datas.get('place') + \
                client_datas.get('zip') + \
                client_datas.get('town')

            if old_client.lower() == new_client.lower():
                return True
        return False
    return False


def all_clients_last_name() -> list[str]:
    """ retourne la liste des noms des clients par ordre alphabétique"""
    return sorted(database.db_select_all('client').get('client_last_name'))


def all_companies():
    """ retourne la liste des noms des entreprises clientes par ordre alphabétique"""
    companies = database.db_select_all('client').get('company_name')
    companies = [e for e in companies if e != '']
    return sorted(companies)


def all_clients_email():
    """ retourne la liste des emails des clients par ordre alphabétique"""
    emails = database.db_select_all('client').get('email')
    emails = [e for e in emails if e is not None]
    return sorted(emails)


def all_clients_phone():
    """ retourne la liste des n° de téléphone des clients"""
    phones = database.db_select_all('client').get('phone')
    phones = [e for e in phones if e != '']
    return sorted(phones)


def datas_to_display_lw(cbox_name: str, text_selected: str) -> list[str]:
    clients_fields = ["N° client: ", "Entreprise: ", "Titre: ",
                      "Nom: ", "Prénom: ", "Email: ", "Téléphone: ",
                      "Voie: ", "Code postal: ", "Commune: "]
    data_to_display = []
    data_list = database.db_select_by_field('client', {cbox_name: text_selected})
    for data in data_list:
        data_client = ""
        for i, d in enumerate(data):
            data_client += clients_fields[i] + str(d) + '\n'
        data_to_display.append(data_client)
    return data_to_display


def client_datas(id: str) -> dict[str, str]:
    """ retourne un dict contenant les données du client dont l'id est spécifié """
    return database.db_read_id_row('client', id)


def company_datas() -> dict[str, str]:
    """ retourne un dict contenant les données de l'entreprise """
    return database.db_read_id_row('company', '1')


def invoice_datas(id_to_update):
    invoice_datas = {}
    if not id_to_update:
        id = database.db_last_table_id_used('invoice')
    else:
        id = id_to_update
    invoice_datas['address'] = database.db_read_id_row('invoice', id).get('client_address')
    invoice_datas['items'] = database.db_read_id_row('invoice', id).get('items')
    invoice_datas['date'] = database.db_read_id_row('invoice', id).get('date')
    invoice_datas['bill_number'] = database.db_read_id_row('invoice', id).get('bill_number')
    return invoice_datas


def find_invoice_by_number(bill_number):
    fields = database.db_read_fields_name('invoice')
    datas = database.db_select_by_field('invoice', {'bill_number': str(bill_number)})
    return {k: v for k, v in zip(fields, datas[0])}


def datas_filtred(datas: dict) -> dict:
    """supprime les champs vide de datas """
    return {k: v for k, v in datas.items() if v != ''}


def address_list(datas: dict) -> list[str]:
    """ retourne la liste formatée par ligne des données constituant
    l'adresse postale de l'entreprise ou d'un client"""

    fields = ['company_name',
              'civil_title',
              'client_first_name',
              'client_last_name',
              'manager_first_name',
              'manager_last_name',
              'place',
              'address',
              'zip',
              'town',
              'phone',
              'email']
    address_datas = []

    line_1 = []
    line_2 = []
    line_3 = []
    line_4 = []
    line_5 = []
    line_6 = []

    for k, v in datas_filtred(datas).items():
        if k in fields[0]:
            line_1.append(str(v))
        elif k in fields[1:6]:
            line_2.append(str(v) + " ")
        elif k in fields[6:8]:
            line_3.append(str(v))
        elif k in fields[8:10]:
            line_4.append(str(v) + " ")
        elif k in fields[10:11]:
            line_5.append(str(v))
        elif k in fields[11:]:
            line_6.append(str(v))
    if line_1:
        address_datas.append(''.join(line_1).strip())
    address_datas.append(''.join(line_2).strip())
    address_datas.append(''.join(line_3).strip())
    address_datas.append(''.join(line_4).strip() + '\n')
    address_datas.append(''.join(line_5).strip())
    address_datas.append(''.join(line_6).strip())
    return address_datas


def company_address() -> str:
    """ retourne l'adresse de l'entreprise pour l'écrire sur la facture """
    return "\n".join(address_list(company_datas()))


def company_identification() -> dict:
    """ retourne le siret et le code ape pour l'écrire sur la facture """
    return {'siret_nb': 'N° siret : ' + company_datas().get('siret_nb'),
            'code_ape': 'code ape : ' + company_datas().get('code_ape')}


def delete_client(self, datas: dict):
    title_msg = 'Attention!'
    question = f"Voulez-vous supprimer le client '{datas.get('client_last_name')}'"
    if dlg_ask_question(self, title_msg, question):
        database.db_delete('client', str(datas.get('id')))
    return f"Les données du client '{datas.get('client_last_name')}' ont été effacées."


def save_client_datas(datas: dict, client_datas: dict) -> str:
    fields = ' '.join([k + ' text,' for k in list(client_datas.keys())])[:-1]
    if not datas:
        if database.db_is_table_exist('client'):
            if client_already_exist(client_datas):
                msg = f"Le client '{client_datas.get('client_last_name')}' est déjà enregistré."
            else:
                database.db_insert('client', client_datas)
                msg = f"Le client '{client_datas.get('client_last_name')}' est enregistré."
        else:
            database.db_create('client', fields)
            database.db_insert('client', client_datas)
            msg = f"Le client '{client_datas.get('client_last_name')}' est enregistré."
    else:
        database.db_update('client', client_datas, datas.get('id'))
        msg = f"Les données du client '{client_datas.get('client_last_name')}' ont été actualisées."
    return msg


def save_invoice_datas(invoice_datas: dict):
    fields = ' '.join([k + ' text,' for k in list(invoice_datas.keys())])[:-1]
    if database.db_is_table_exist('invoice'):
        database.db_insert('invoice', invoice_datas)
    else:
        database.db_create('invoice', fields)
        database.db_insert('invoice', invoice_datas)


def save_invoice_update(invoice_datas: dict):
    database.db_update('invoice', invoice_datas, invoice_datas.get('id'))


def save_company_datas(datas: dict, company_datas: dict) -> str:
    fields = ' '.join([k + ' text,' for k in list(company_datas.keys())])[:-1]
    if not datas:
        database.db_create('company', fields)
        database.db_insert('company', company_datas)
        msg = "L'entreprise est enregistrée."
    else:
        database.db_update('company', company_datas, datas.get('id'))
        msg = "Les données de l'entreprise ont été actualisées."
    return msg


def invoice_numero(date):
    year = date.strftime('%Y')
    month = date.strftime('%m')
    last_id = database.db_last_table_id_used('invoice')
    num = int(last_id) + 1
    return year+month+'000'+str(num)
