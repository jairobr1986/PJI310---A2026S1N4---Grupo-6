import sqlite3
import pandas as pd

def init_db():
    conn = sqlite3.connect("triagem.db", check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pacientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            idade INTEGER,
            peso REAL,
            altura REAL,
            imc REAL,
            risco TEXT,
            prioridade_nivel INTEGER,
            classificacao TEXT
        )
    """)
    conn.commit()
    return conn

def salvar_paciente(conn, dados):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO pacientes (nome, idade, peso, altura, imc, risco, prioridade_nivel, classificacao)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, dados)
    conn.commit()

def listar_pacientes(conn):
    return pd.read_sql_query("SELECT * FROM pacientes ORDER BY prioridade_nivel ASC, id ASC", conn)