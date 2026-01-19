USE AgroAnalytics;
GO

CREATE OR ALTER VIEW dbo.vw_top_produtos_ano AS
SELECT
    ano,
    produto,
    producao_total
FROM dbo.agro_producao_anual;
