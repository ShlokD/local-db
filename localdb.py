from table import DbTable
from json import dumps, load
from os import makedirs,path

class LocalDB:
    def __init__(self, filepath):
        self.filepath = filepath
        if not path.exists(filepath):
            makedirs(filepath)
        self.tables = {}

    def create_table(self, name, records = []):
        table = DbTable(name, records)
        self.tables[name] = table

    def table(self, name):
        if self.tables.get(name):
            return self.tables.get(name)

        db_file = open(f'{self.filepath}/{name}.json', "r")
        data = load(db_file)
        self.create_table(name, data)
        db_file.close()
        return self.tables[name]

    def write(self):
        for table in self.tables:
            db_file = open(f'{self.filepath}/{table}.json', "w")
            db_file.write(dumps(self.tables[table].get_records()))
            db_file.close()

        self.tables.clear()




