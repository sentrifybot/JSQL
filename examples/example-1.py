from jsql import JSQL

jsql = JSQL()

print(jsql.execute_sql("CREATE TABLE users"))
print(jsql.execute_sql('INSERT INTO users VALUES {"name": "John Doe", "age": 30}'))
print(jsql.execute_sql("SELECT * FROM users WHERE name = 'John Doe'"))