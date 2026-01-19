import json

with open("data/processed/agro_tratado.json", encoding="utf-8") as f:
    data = json.load(f)

print("Total de registros:", len(data))

valores_nulos = sum(1 for r in data if r["valor"] is None)
print("Registros com valor nulo:", valores_nulos)

anos = sorted({r["ano"] for r in data})
print("Anos presentes:", anos)

produtos_com_nulo = {
    r["produto"] for r in data if r["valor"] is None
}

print("Exemplo de produtos com valor nulo:")
for p in list(produtos_com_nulo)[:10]:
    print("-", p)
