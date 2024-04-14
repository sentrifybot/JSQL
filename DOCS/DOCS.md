# JSQL Command Line Interface Documentation

The JSQL Command Line Interface (CLI) allows users to interact with the JSQL database system through a set of commands. Below is a guide on how to use these commands.

## Available Commands

- `CREATE TABLE <table_name>`: Creates a new table in the database.
- `INSERT INTO <table_name> VALUES <json_data>`: Inserts a new record into the specified table. The data must be in JSON format.
- `SELECT * FROM <table_name> WHERE <condition>`: Retrieves records from a table that meet the specified condition.
- `DELETE FROM <table_name> WHERE <condition>`: Deletes records from a table that meet the specified condition.
- `DELETE TABLE <table_name>`: Deletes an entire table from the database.
- `MODIFY <table_name> SET <json_data> WHERE <condition>`: Modifies data in a table based 
- `FLUSH`: Removes all tables and their data from the database.
- `HELP`: Displays help information about available commands.
- `QUIT`: Exits the CLI.

## How to Use Commands

1. **Starting the CLI**: Run the CLI.py script to start the interface. If you have a command to execute directly, you can pass it as an argument.
2. **Executing Commands**: Once in the CLI, type your command at the `JSQL>` prompt and press Enter. For example, to create a table named 'users', you would type: `CREATE TABLE users`.
3. **Getting Help**: If you need information on available commands, type `HELP` at the prompt.
4. **Exiting the CLI**: To exit, type `QUIT`.

This documentation provides a basic overview of interacting with the JSQL database via the CLI. For more detailed information, refer to the source code or further documentation.