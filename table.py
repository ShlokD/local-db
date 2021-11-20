class DbTable:
    def __init__(self, name, records = []):
        self.name = name
        self.records = records.copy()

    def push(self, item):
        self.records.append(item)

    def get_records(self):
        return self.records

    def query(self, criteria = None):
        if criteria is None:
            return self.records
        else:
            result = []
            for record in self.records:
                match = True
                for key in criteria:
                    if record[key] != criteria[key]:
                        match = False
                if match:
                    result.append(record)

            return result

    def update(self, criteria, updates):
        if criteria is None:
            return
        else:
            for idx, record in enumerate(self.records):
                match = True
                for key in criteria:
                    if record[key] != criteria[key]:
                        match = False
                if match:
                    self.records[idx] = {**record, **updates}



    def delete(self, criteria):
        if criteria is None:
            self.records.clear()
        else:
            for record in self.records:
                match = True
                for key in criteria:
                    if record[key] != criteria[key]:
                        match = False
                if match:
                    self.records.remove(record)



