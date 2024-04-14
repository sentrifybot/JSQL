import json
from pathlib import Path
import re

class JSQL:
    def __init__(self, db_path="database.json"):
        self.db_path = Path(db_path)
        if self.db_path.exists():
            self.load_database()
        else:
            self.database = {}

    def load_database(self):
        with open(self.db_path, "r") as file:
            self.database = json.load(file)

    def save_database(self):
        with open(self.db_path, "w") as file:
            json.dump(self.database, file, indent=4)

    def execute_sql(self, command):
        create_table_pattern = r"^CREATE TABLE (\w+)$"
        insert_into_pattern = r"^INSERT INTO (\w+) VALUES (\{.*\})$"
        select_from_pattern = r"^SELECT \* FROM (\w+)( WHERE (.+))?$"
        delete_from_pattern = r"^DELETE FROM (\w+)( WHERE (.+))?$"
        delete_table_pattern = r"^DELETE TABLE (\w+)$"
        modify_pattern = r"^MODIFY (\w+) SET (\{.*\})( WHERE (.+))?$"

        if re.match(create_table_pattern, command, re.IGNORECASE):
            match = re.match(create_table_pattern, command, re.IGNORECASE)
            table_name = match.group(1)
            return self.create_table(table_name)
        elif re.match(insert_into_pattern, command, re.IGNORECASE):
            match = re.match(insert_into_pattern, command, re.IGNORECASE)
            table_name, data_str = match.groups()
            data = json.loads(data_str)
            return self.insert_data(table_name, data)
        elif re.match(select_from_pattern, command, re.IGNORECASE):
            match = re.match(select_from_pattern, command, re.IGNORECASE)
            table_name, _, search_criteria_str = match.groups()
            if search_criteria_str:
                key, value = search_criteria_str.split("=", 1)
                key = key.strip()
                value = value.strip().strip("'\"")
                search_criteria = {key: value}
            else:
                search_criteria = {}
            return self.query_table(table_name, search_criteria)
        elif re.match(delete_from_pattern, command, re.IGNORECASE):
            match = re.match(delete_from_pattern, command, re.IGNORECASE)
            table_name, _, search_criteria_str = match.groups()
            if search_criteria_str:
                key, value = search_criteria_str.split("=", 1)
                key = key.strip()
                value = value.strip().strip("'\"")
                search_criteria = {key: value}
            else:
                search_criteria = {}
            return self.delete_data(table_name, search_criteria)
        elif re.match(delete_table_pattern, command, re.IGNORECASE):
            match = re.match(delete_table_pattern, command, re.IGNORECASE)
            table_name = match.group(1)
            return self.delete_table(table_name)
        elif re.match(modify_pattern, command, re.IGNORECASE):
            match = re.match(modify_pattern, command, re.IGNORECASE)
            table_name, data_str, _, search_criteria_str = match.groups()
            data = json.loads(data_str)
            if search_criteria_str:
                key, value = search_criteria_str.split("=", 1)
                key = key.strip()
                value = value.strip().strip("'\"")
                search_criteria = {key: value}
            else:
                search_criteria = {}
            return self.modify_data(table_name, data, search_criteria)
        elif command.strip().upper() == "FLUSH":
            return self.flush_database()
        else:
            return "Invalid JSQL command syntax."

    def delete_data(self, table_name, search_criteria):
        if table_name not in self.database:
            return f"Table '{table_name}' does not exist."

        rows_to_delete = [row for row in self.database[table_name] if all(row.get(k) == v for k, v in search_criteria.items())]
        if not rows_to_delete:
            return "No matching rows found to delete."

        self.database[table_name] = [row for row in self.database[table_name] if row not in rows_to_delete]
        self.save_database()
        return f"{len(rows_to_delete)} row(s) deleted successfully."

    def create_table(self, table_name):
        if table_name in self.database:
            return f"Table '{table_name}' already exists."
        self.database[table_name] = []
        self.save_database()
        return f"Table '{table_name}' created successfully."

    def insert_data(self, table_name, data):
        if table_name not in self.database:
            return f"Table '{table_name}' does not exist."
        self.database[table_name].append(data)
        self.save_database()
        return "Data inserted successfully."

    def query_table(self, table_name, search_criteria):
        if table_name not in self.database:
            return f"Table '{table_name}' does not exist."
        results = [row for row in self.database[table_name] if all(row.get(k) == v for k, v in search_criteria.items())]
        return results

    def flush_database(self):
        self.database = {}
        self.save_database()
        return "All tables have been removed from the database."

    def delete_table(self, table_name):
        if table_name not in self.database:
            return f"Table '{table_name}' does not exist."

        del self.database[table_name]
        self.save_database()
        return f"Table '{table_name}' deleted successfully."

    def modify_data(self, table_name, data, search_criteria):
        if table_name not in self.database:
            return f"Table '{table_name}' does not exist."

        rows_to_modify = [row for row in self.database[table_name] if all(row.get(k) == v for k, v in search_criteria.items())]
        if not rows_to_modify:
            return "No matching rows found to modify."

        for row in rows_to_modify:
            row.update(data)

        self.save_database()
        return f"{len(rows_to_modify)} row(s) modified successfully."
