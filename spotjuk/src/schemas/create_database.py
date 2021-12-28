import os
os.remove('../database.db')

import sqlite3
conn = sqlite3.connect('../database.db')
cursor = conn.cursor()

cursor.execute("""
  CREATE TABLE categories (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    categorie VARCHAR(20) NOT NULL,
    cover VARCHAR(50) NOT NULL
  );
""")

print("Tabela criada com sucesso!")

# DESCONECTAR DO BANCO DE DADOS
conn.close()