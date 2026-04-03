import sqlite3
import pandas as pd

def init_db():
    conn = sqlite3.connect("triagem.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pacientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            temperatura REAL,
            freq_cardiaca INTEGER,
            pressao TEXT,
            freq_respiratoria INTEGER,
            oxigenacao REAL,
            risco TEXT
        )
    """)
    conn.commit()
    return conn

def salvar_paciente(conn, dados):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO pacientes (nome, temperatura, freq_cardiaca, pressao, freq_respiratoria, oxigenacao, risco)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, dados)
    conn.commit()

def listar_pacientes(conn):
    return pd.read_sql_query("SELECT * FROM pacientes", conn)
