import requests
import json
import os

URL = "https://apisidra.ibge.gov.br/values/t/5457/n1/all/v/214/p/all/c782/all"

os.makedirs("data/processed", exist_ok=True)

print("Iniciando extração...")

response = requests.get(URL)
data = response.json()

records = data[1:]  

clean_data = []

for item in records:
    valor_raw = item.get("V")
    if valor_raw is None:
        valor = None
    else:
        valor_raw = valor_raw.strip()

        if valor_raw == "" or valor_raw == "-" or valor_raw == "...":
            valor = None
        else:
            try:
                valor = float(valor_raw.replace(".", "").replace(",", "."))
            except ValueError:
                valor = None

    clean_data.append({
        "ano": int(item["D3N"]),
        "estado_codigo": item["D1C"],
        "estado": item["D1N"],
        "produto_codigo": item["D4C"],
        "produto": item["D4N"],
        "valor": valor
    })

with open("data/processed/agro_tratado.json", "w", encoding="utf-8") as f:
    json.dump(clean_data, f, ensure_ascii=False, indent=2)

print("Transformação concluída com sucesso!")
