from flask import Flask, render_template_string
import sqlite3

app = Flask(__name__)

# Template básico em HTML
TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jogadores</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
        }
        table {
            width: 80%;
            margin: auto;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
        }
        th {
            background-color: #f4f4f4;
        }
    </style>
</head>
<body>
    <h1>Jogadores e Valores de Mercado</h1>
    <table>
        <tr>
            <th>Nome</th>
            <th>Idade</th>
            <th>Overall</th>
            <th>Potencial</th>
            <th>Desempenho</th>
            <th>Preço Médio</th>
            <th>Liquidez</th>
        </tr>
        {% for jogador in jogadores %}
        <tr>
            <td>{{ jogador[0] }}</td>
            <td>{{ jogador[1] }}</td>
            <td>{{ jogador[2] }}</td>
            <td>{{ jogador[3] }}</td>
            <td>{{ jogador[4] }}</td>
            <td>{{ jogador[5] }}</td>
            <td>{{ jogador[6] }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

# Rota principal
@app.route("/")
def home():
    # Conectar ao banco de dados SQLite
    conn = sqlite3.connect("jogadores.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nome, idade, overall, potencial, desempenho, preco_medio, liquidez FROM jogadores")
    jogadores = cursor.fetchall()
    conn.close()
    
    # Renderizar HTML
    return render_template_string(TEMPLATE, jogadores=jogadores)

if __name__ == "__main__":
    app.run(debug=True)
