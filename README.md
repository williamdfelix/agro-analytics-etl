# AgroAnalytics

Projeto de estudo em **Engenharia de Dados** focado em ingestão, tratamento, carga e análise de dados de produção agrícola brasileira.

O objetivo é  construir algo coerente, reproduzível e com decisões técnicas claras.

---

##  Objetivo do Projeto

Construir um pipeline simples e funcional que:

1. Leia dados brutos em JSON
2. Realize tratamento e padronização
3. Carregue os dados em um banco relacional (SQL Server)
4. Gere tabelas analíticas para consultas
5. Permita análises reais de produção agrícola por ano, estado e produto

---

##  Arquitetura do Projeto

```
AgroAnalytics/
│
├── data/
│   ├── raw/              # Dados brutos (JSON original)
│   └── processed/        # Dados tratados (JSON pronto para carga)
│
│   ├── inspect_data.py       # Inspeção e validação dos dados tratados
│   ├── main.py   # Tratamento e normalização dos dados
│   ├── load_sqlserver.py # Carga dos dados no SQL Server
│
├── sql/
│   ├── ddl.sql           # Criação do banco e tabelas
│   └── views.sql         # Views analíticas
│
├── README.md
└── requirements.txt
```

---

##  Fluxo de Dados

1. **Entrada**

   * Arquivo JSON bruto contendo produção agrícola por estado, produto e ano

2. **Processamento (`main.py`)**

   * Padronização de campos
   * Conversão de tipos
   * Remoção de registros inválidos
   * Geração do arquivo `agro_tratado.json`

3. **Carga (`load_sqlserver.py`)**

   * Leitura do JSON tratado
   * Inserção na tabela `stg_agro_producao`

4. **Camada Analítica**

   * Views agregadas por ano, produto e estado

---

## Banco de Dados

Os scripts SQL estão na pasta `sql/`.

Ordem de execução:
1. Executar `ddl.sql` no SQL Server
2. Rodar `main.py` para gerar os dados tratados
3. Rodar `load_sqlserver.py` para carga
4. Executar `views.sql` para criar visões analíticas


### Banco

* **SQL Server 2022**
* Banco: `AgroAnalytics`

### Tabela de Staging

`dbo.stg_agro_producao`

| Campo          | Tipo    | Descrição          |
| -------------- | ------- | ------------------ |
| ano            | INT     | Ano da produção    |
| estado_codigo  | INT     | Código do estado   |
| estado         | VARCHAR | Nome do estado     |
| produto_codigo | INT     | Código do produto  |
| produto        | VARCHAR | Nome do produto    |
| valor          | DECIMAL | Produção informada |

Total carregado: **3.672 registros**

---

##  Camada Analítica

### Tabela: `agro_producao_anual`

Agrega a produção total por:

* Ano
* Produto

Exemplo de consulta:

```sql
SELECT ano, producao_total
FROM dbo.agro_producao_anual
WHERE produto = 'Abacate'
ORDER BY ano;
```

---

##  Top 10 Produções (2024)
Produção total conforme unidade informada pelo IBGE.

| Produto          | Produção    |
| ---------------- | ----------- |
| Cana-de-açúcar   | 759.662.482 |
| Soja (em grão)   | 144.473.768 |
| Milho (em grão)  | 114.953.303 |
| Mandioca         | 19.066.096  |
| Laranja          | 15.688.409  |
| Arroz (em casca) | 10.671.490  |
| Algodão herbáceo | 8.523.606   |
| Trigo (em grão)  | 7.520.178   |
| Banana (cacho)   | 7.046.345   |
| Tomate           | 4.407.502   |

---

##  Decisões Técnicas

* JSON mantido como **fonte de dados**, não como camada analítica
* SQL Server usado para:

  * Persistência
  * Integridade
  * Performance em agregações
* Separação clara entre:

  * Dados brutos
  * Dados tratados
  * Dados analíticos
  * Pipeline desenhado para fácil evolução para cargas incrementais
---

##  Próximos Passos

1. Implementar carga incremental
2. Criar dimensões de produtos e estados
3. Versionar schema (migrations)
4. Criar dashboard (Power BI ou Metabase)
5. Automatizar pipeline

---

