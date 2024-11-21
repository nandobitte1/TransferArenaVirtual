import sqlite3

# Criar banco de dados SQLite
conn = sqlite3.connect("jogadores.db")
cursor = conn.cursor()

# Criar tabela
cursor.execute("""
CREATE TABLE jogadores (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    idade INTEGER,
    overall REAL,
    potencial REAL,
    desempenho REAL,
    preco_medio REAL,
    liquidez INTEGER
)
""")

# Inserir dados
cursor.executemany("""
INSERT INTO jogadores (nome, idade, overall, potencial, desempenho, preco_medio, liquidez)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", [
    ("Jogador A", 22, 85, 90, 8.5, 50000, 10),
    ("Jogador B", 28, 82, 85, 7.0, 30000, 5),
    ("Jogador C", 19, 78, 92, 9.0, 70000, 20),
])

conn.commit()
conn.close()
