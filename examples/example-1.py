from jsql import JSQL

jsql = JSQL()

# Create a table named "users"
print(jsql.execute_sql("CREATE TABLE users"))

# Insert data into the "users" table
print(jsql.execute_sql('INSERT INTO users VALUES {"name": "John Doe", "age": 30}'))

# Query data from the "users" table
print(jsql.execute_sql("SELECT * FROM users WHERE name = 'John Doe'"))

# Modify data in the "users" table where name is 'John Doe'
print(jsql.execute_sql("MODIFY users SET {'age': 50} WHERE name = 'John Doe'"))

# Query data again to verify modification
print(jsql.execute_sql("SELECT * FROM users WHERE name = 'John Doe'"))

# Delete data from the "users" table where name is 'John Doe'
print(jsql.execute_sql("DELETE FROM users WHERE name = 'John Doe'"))

# Query data again to verify deletion
print(jsql.execute_sql("SELECT * FROM users WHERE name = 'John Doe'"))  # This should return an empty list

# Delete the entire "users" table
print(jsql.execute_sql("DELETE TABLE users"))

# Query data again to verify deletion of the table
print(jsql.execute_sql("SELECT * FROM users"))  # This should return an error message indicating the table doesn't exist
