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
    companies = database.db_select_all('client').get('company_name')
    companies = [e for e in companies if e != '']
    return sorted(companies)


def all_clients_email():
    emails = database.db_select_all('client').get('email')
    emails = [e for e in emails if e is not None]
    return sorted(emails)


def all_clients_phone():
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
    return database.db_read_id_row('client', id)


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
