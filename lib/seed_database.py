from database_connection import DatabaseConnection

connection = DatabaseConnection()
connection.connect()
connection.seed('seeds/book_store.sql')