import json
import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=AgroAnalytics;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()
with open("data/processed/agro_tratado.json", encoding="utf-8") as f:
    dados = json.load(f)

sql_insert = """
INSERT INTO dbo.stg_agro_producao
(ano, estado_codigo, estado, produto_codigo, produto, valor)
VALUES (?, ?, ?, ?, ?, ?)
"""
for r in dados:
    cursor.execute(
        sql_insert,
        r["ano"],
        r["estado_codigo"],
        r["estado"],
        r["produto_codigo"],
        r["produto"],
        r["valor"]
    )

conn.commit()
cursor.close()
conn.close()

print("Carga concluída com sucesso!")






