from invoice.models.constants import DB_FILE
import sqlite3


def db_is_table_exist(table_name: str) -> bool:
    """ retourne True si la table_name existe"""
    with sqlite3.connect(DB_FILE) as db:
        c = db.execute(f"""SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{table_name}'""")
        return True if c.fetchone()[0] == 1 else False


def db_create(table_name: str, fields: str):
    with sqlite3.connect(DB_FILE) as db:
        db.execute(f"""CREATE TABLE IF NOT EXISTS {table_name}
                   (id INTEGER NOT NULL PRIMARY KEY,{fields})""")
        db.commit()


def db_create_fk(table_name: str, related_table: str, fields: str):
    """ creation d'une table avec une foreign key"""
    related_table_id = related_table + '_ID'
    fk = f""", {related_table_id} INTEGER NOT NULL,
          FOREIGN KEY({related_table_id}) REFERENCES {related_table}(ID)"""
    with sqlite3.connect(DB_FILE) as db:
        db.execute(f"""CREATE TABLE IF NOT EXISTS {table_name}
                   (id INTEGER NOT NULL PRIMARY KEY,{fields} {fk})""")
        db.commit()


def db_insert(table_name: str, datas: dict[str, str]):
    keys = list(datas.keys())
    formated_keys = [':' + key for key in keys]
    with sqlite3.connect(DB_FILE) as db:
        db.execute(f"INSERT INTO {table_name} ({','.join(keys)}) VALUES ({','.join(formated_keys)})", datas)
        db.commit()


def db_update(table_name: str, datas: dict[str, str], id: int):
    """Mise à jour d'une ligne dans la table"""
    fields_updated = ','.join([str(k)+'=' + '"' + str(v) + '"' if v else str(k)+'=' + '""' for k, v in datas.items()])
    with sqlite3.connect(DB_FILE) as db:
        c = db.cursor()
        c.execute(f"""UPDATE {table_name} SET {fields_updated} WHERE id={id}""")
        db.commit()


def db_select_all(table_name: str) -> dict[str, list]:
    """ retourne toutes les données d'une table. 'champ': [données]"""
    all_datas = {}
    with sqlite3.connect(DB_FILE) as db:
        db.row_factory = sqlite3.Row
        c_fields = db.execute(f"SELECT * FROM {table_name}")
        c_datas = db.execute(f"SELECT * FROM {table_name}")
    fields = c_fields.fetchone().keys()
    datas = c_datas.fetchall()
    for i, field in enumerate(fields):
        data_list = [data[i] for data in datas]
        all_datas[field] = data_list
    return all_datas


def db_select_by_id(table_name: str, id: str) -> list:
    with sqlite3.connect(DB_FILE) as db:
        c = db.execute(f"SELECT * FROM {table_name} WHERE id=?", id)
    return c.fetchone()


def db_last_table_id_used(table_name: str) -> str:
    id_list = []
    if db_is_table_exist(table_name):
        id_list = db_select_all(table_name).get('id')
    else:
        id_list.append(0)
    return str(max(id_list))


def db_select_by_field(table_name: str, filter: dict[str, str]) -> list:
    """ filtrage des données sur un champ """
    key = list(filter.keys())[0]
    with sqlite3.connect(DB_FILE) as db:
        c = db.execute(f"SELECT * FROM {table_name} WHERE {key}=:{key}", filter)
    return c.fetchall()


def db_read_fields_name(table_name: str) -> list:
    """ lecture des noms des champs d'une table"""
    with sqlite3.connect(DB_FILE) as db:
        db.row_factory = sqlite3.Row
        c = db.execute(f"SELECT * FROM {table_name}")
    return c.fetchone().keys()


def db_delete(table_name: str, id: str):
    with sqlite3.connect(DB_FILE)as db:
        c = db.cursor()
        c.execute(f"DELETE FROM {table_name} WHERE id=?", id)
        db.commit()


def db_read_id_row(table_name: str, id: str) -> dict[str, str]:
    """ retourne un dict {champ: donnée} pour la ligne dont l'id est spécifié """
    datas = db_select_by_id(table_name, id)
    fields = db_read_fields_name(table_name)
    field_data = {}
    for i_data, field in enumerate(fields):
        field_data[field] = datas[i_data]
    return field_data


def convert_into_binary(file_path):
    with open(file_path, 'rb') as file:
        binary = file.read()
    return binary


if __name__ == "__main__":
    print(db_is_table_exist('client'))
