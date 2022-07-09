from .database import db_select_by_field, db_select_all


def client_already_exist(datas: dict):
    """ retourne True si le client existe déjà dans la bdd
        même nom, prénom, adresse, zip et commune
    """
    new_client = datas.get('client_last_name') + \
        datas.get('client_first_name') + \
        datas.get('place') + \
        datas.get('zip') + \
        datas.get('town')

    registered_clients = db_select_by_field('client', {'client_last_name': datas.get('client_last_name')})
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


def all_clients_last_name():
    return sorted(db_select_all('client').get('client_last_name'))


def all_clients_email():
    emails = db_select_all('client').get('email')
    emails = [e for e in emails if e is not None]
    return sorted(emails)


def all_clients_phone():
    phones = db_select_all('client').get('phone')
    phones = [e for e in phones if e != '']
    return sorted(phones)


def find_a_client(data):
    pass


# def customers_name():
#     print('ici')
#     print(db_select_all('client'))
#     print(db_select_all('client').get('client_last_name'))
    